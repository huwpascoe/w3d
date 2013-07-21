from xml.dom import minidom
import xml.etree.ElementTree as et
import os, argparse, ast
import w3d_chunk, w3d_format

def str2val(str):
    if str == 'nan':
        return float('nan')
    if str == 'inf':
        return float('inf')
    return ast.literal_eval(str)
    
dstr = {}
for d in w3d_format.format:
    dstr[d['tag']] = d

def chunk_to_xml(chunk):
    e = et.Element(chunk.format['tag'])
    for k, v in chunk.attr.items():
        if k != '':
            e.attrib[k] = str(v)
        else:
            e.text = str(v)
    for sub in chunk.subattr:
        se = et.Element(chunk.format['subtag'])
        e.append(se)
        for k, v in sub.items():
            if k != '':
                se.attrib[k] = str(v)
            else:
                se.text = str(v)
    for child in chunk.children:
        e.append(chunk_to_xml(child))
    return e

def xml_to_chunk(e):
    # check tag exists
    if e.tag not in dstr:
        print("MISSINGTAG :", e.tag)
        return None
    
    chunk = w3d_chunk.Chunk(dstr[e.tag])
    
    if ('attr' in chunk.format and chunk.format['attr'] is not None):
        for i in chunk.format['attr']:
            if i[0] != '':
                if i[0] in e.attrib:
                    val = e.attrib[i[0]]
                else:
                    chunk.attr[i[0]] = None
                    continue
            else:
                val = e.text
            if i[1] == 'string' or i[1] == 'name' or i[1] == 'version':
                chunk.attr[i[0]] = val
            else:
                chunk.attr[i[0]] = str2val(val)
    
    if ('subattr' in chunk.format and chunk.format['subattr'] is not None):
        for se in e:
            sub = {}
            chunk.subattr.append(sub)
            
            for i in chunk.format['subattr']:
                if i[0] != '':
                    if i[0] in se.attrib:
                        val = se.attrib[i[0]]
                    else:
                        sub[i[0]] = None
                        continue
                else:
                    val = se.text
                if i[1] == 'string' or i[1] == 'name' or i[1] == 'version':
                    sub[i[0]] = val
                else:
                    sub[i[0]] = str2val(val)
    
    if ('container' in chunk.format and chunk.format['container'] == True):
        for child in e:
            chunk.children.append(xml_to_chunk(child))
    
    return chunk


# interface
parser = argparse.ArgumentParser(description='W3D-XML')
parser.add_argument('-s', help='Source file path')
parser.add_argument('-o', help='Output file path')
args = parser.parse_args()

if args.s is not None and args.o is not None:
    srcname, srcext = os.path.splitext(args.s)
    dstname, dstext = os.path.splitext(args.o)
    
    if srcext == '.w3d' and dstext == '.xml':
        # load w3d
        print('open:', args.s)
        file = open(args.s, 'rb')
        try:
            root = w3d_chunk.read(file)
        finally:
            file.close()
        
        # save xml
        print('save:', args.o)
        eroot = et.Element('w3d')
        for chunk in root.children:
            eroot.append(chunk_to_xml(chunk))
        file = open(args.o, 'w')
        file.write(minidom.parseString(et.tostring(eroot)).toprettyxml())
        file.close()
    
    elif srcext == '.xml' and dstext == '.w3d':
        # load xml
        print('open:', args.s)
        tree = et.parse(args.s)
        eroot = tree.getroot()
        
        # save w3d
        print('save:', args.o)
        root = w3d_chunk.Chunk(None)
        for e in eroot:
            root.children.append(xml_to_chunk(e))
        file = open(args.o, 'wb')
        size = w3d_chunk.write(root, file)
        file.close()
        
        print (size, 'bytes')
        
    else:
        print('NOPE. Must be either: "-s src.w3d -o dest.xml" or "-s src.xml -o dest.w3d"')
else:
    parser.print_help()
