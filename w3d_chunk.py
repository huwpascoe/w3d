import struct
import w3d_format

class Chunk:
    def __init__(self, format):
        self.format = format
        self.attr = {}
        self.subattr = []
        self.children = []

format_int = {}
for i in w3d_format.format:
    format_int[i['id']] = i

attr_types = {
    'uint8': 'B',
    'uint16': 'H',
    'uint32': 'L',
    'sint32': 'l',
    'rgb': '4B',
    'rgba': '4B',
    
    'float32': 'f',
    'uv': '2f',
    'vector3': '3f',
    'quaternion': '4f',
    
    'char': 'B',
    'version': '2H',
    
    # 'string' is 0 terminated and not packed
    # 'name' is also a special case; '16s', '32s', etc.
}

def b2s(str):
    return str.split(b'\0')[0].decode('utf-8')

def s2b(str, s=None):
    str = str.encode('utf-8')
    if s is not None and len(str) >= s:
        str = str[:s - 1]
    return str + b'\0'

def s2bsize(str, s=None):
    str = str.encode('utf-8')
    if s is not None and len(str) >= s:
        str = str[:s - 1]
    return len(str + b'\0')

def read(file):
    root = Chunk(None)
    chunk_read(root, file)
    return root
    
def write(root, file):
    filesize = 0
    for child in root.children:
        filesize += chunk_size(child)
    
    for child in root.children:
        chunk_write(file, child)
    
    return filesize

def attr_read(file, type, count=1):
    if type == 'name':
        fmt = str(count * 16) + 's'
    else:
        fmt = attr_types[type]
        fmt *= count
    
    binary = file.read(struct.calcsize(fmt))
    if binary == b'':
        return None
    data = struct.unpack(fmt, binary)

    if type == 'rgb':  # Same as RGBA but with an unused byte
        return (data[0], data[1], data[2])
    if type == 'version':
        return str(data[1]) + '.' + str(data[0])
    if type == 'name':
        return b2s(data[0])
    
    if len(data) == 1:
        return data[0]
    
    return data
    
def attr_write(file, val, type, count=1):
    if type == 'name':
        fmt = str(count * 16) + 's'
    else:
        fmt = attr_types[type]
        fmt *= count
    
    # zero fill
    if val is None:
        size = struct.calcsize(fmt)
        file.write(b'\x00' * size)
        return
    
    if type == 'rgb':  # Same as RGBA but with an unused byte
        data = struct.pack(fmt, val[0], val[1], val[2], 0) 
        
    elif type == 'version':
        val = val.split('.')
        data = struct.pack(fmt, int(val[1]), int(val[0]))
        
    elif type == 'name':
        data = struct.pack(fmt, s2b(val))
        
    else:
        if isinstance(val, tuple):
            data = struct.pack(fmt, *val)
        else:
            data = struct.pack(fmt, val)
    
    file.write(data)
    
def attr_size(attrdesc):
    size = 0
    for i in attrdesc:
        if i[1] == 'name':
            if len(i) > 2:
                size += 16 * i[2]
            else:
                size += 16
            continue
        
        if i[1] in attr_types:
            fmt = attr_types[i[1]]
            if len(i) > 2:
                fmt *= i[2]
            size += struct.calcsize(fmt)
    
    return size
    
def chunk_read(parent, file, size=0x7FFFFFFF):
    while size > 0:
        
        # read data in correctly
        binary = file.read(8)
        if binary == b'':
            return
        data = struct.unpack('LL', binary)
        
        # chunk type, chunk size (not including header)
        hdesc = data[0]
        hsize = data[1] & 0x7FFFFFFF # remove container flag
        
        # subtract header + chunk size
        size -= 8 + hsize
        
        # skip if invalid
        if hdesc not in format_int:
            print("MISSINGNO : 0x%0.8X in" % hdesc, parent.format['tag'])
            file.read(hsize)
            continue
        
        # get descriptor, but skip if unimplemented
        desc = format_int[hdesc]
        if ('unimplemented' in desc and desc['unimplemented'] == True):
            print('unimplemented : ' + desc['tag'])
            file.read(hsize)
            continue
        
        # create the element
        chunk = Chunk(desc)
        parent.children.append(chunk)
        
        # attributes
        attrsize = 0
        if ('attr' in chunk.format and chunk.format['attr'] is not None):
            attrsize = attr_size(chunk.format['attr'])
            for i in chunk.format['attr']:
                if i[1] == 'string': #TODO special string cases in emitter structs
                    val = b2s(file.read(hsize - attrsize))
                else:
                    if len(i) > 2:
                        val = str(attr_read(file, i[1], i[2]))
                    else:
                        val = str(attr_read(file, i[1]))
                if (i[0] != ''):
                    if (i[0][0] != '_'):
                        chunk.attr[i[0]] = val
                else:
                    chunk.attr[''] = val
        
        if ('subattr' in chunk.format and chunk.format['subattr'] is not None):
            stepsize = attr_size(chunk.format['subattr'])
            step = 0
            while step < hsize - attrsize:
                sub = {}
                chunk.subattr.append(sub)
                
                for i in chunk.format['subattr']:
                    if len(i) > 2:
                        val = str(attr_read(file, i[1], i[2]))
                    else:
                        val = str(attr_read(file, i[1]))
                    
                    if (i[0] != ''):
                        if (i[0][0] != '_'):
                            sub[i[0]] = val
                    else:
                        sub[''] = val
                step += stepsize
        
        # containers, recursive reading
        if ('container' in chunk.format and chunk.format['container'] == True):
            chunk_read(chunk, file, hsize + attrsize)

def chunk_write(file, chunk):
    iscont = ('container' in chunk.format and chunk.format['container'] == True)
    
    # header
    if iscont:
        data = struct.pack('LL', chunk.format['id'], chunk.size | 0x80000000) # container flag
    else:
        data = struct.pack('LL', chunk.format['id'], chunk.size)
    
    file.write(data)
    
    # attributes
    if ('attr' in chunk.format and chunk.format['attr'] is not None):
        for i in chunk.format['attr']:
            if i[1] == 'string':
                if i[0] == '':
                    file.write(s2b(chunk.attr['']))
                else:
                    file.write(s2b(chunk.attr[i[0]]))
            else:
                if (i[0] != ''):
                    if (i[0][0] != '_'):
                        val = chunk.attr[i[0]]
                    else:
                        val = None
                else:
                    val = chunk.attr['']
                if len(i) > 2:
                    attr_write(file, val, i[1], i[2])
                else:
                    attr_write(file, val, i[1])

    
    if ('subattr' in chunk.format and chunk.format['subattr'] is not None):
        for sub in chunk.subattr:
            for i in chunk.format['subattr']:
                if (i[0] != ''):
                    if (i[0][0] != '_'):
                        val = sub[i[0]]
                    else:
                        val = None
                else:
                    val = sub['']
                if len(i) > 2:
                    attr_write(file, val, i[1], i[2])
                else:
                    attr_write(file, val, i[1])
    
    # containers, recursive
    if iscont:
        for child in chunk.children:
            chunk_write(file, child)

def chunk_size(chunk):
    chunk.size = 0
    
    # attributes
    if ('attr' in chunk.format and chunk.format['attr'] is not None):
        chunk.size += attr_size(chunk.format['attr'])
        for i in chunk.format['attr']:
            if i[1] == 'string':
                if i[0] == '':
                    chunk.size += s2bsize(chunk.attr[''])
                else:
                    chunk.size += s2bsize(chunk.attr[i[0]])
    
    if ('subattr' in chunk.format and chunk.format['subattr'] is not None):
        subsize = attr_size(chunk.format['subattr'])
        chunk.size += len(chunk.subattr) * subsize
    
    # containers, recursive
    if ('container' in chunk.format and chunk.format['container'] == True):
        for child in chunk.children:
            chunk.size += chunk_size(child)
    
    # return the size + header size
    return chunk.size + 8
