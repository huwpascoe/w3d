from xml.dom import minidom
import xml.etree.ElementTree as et
import struct
import argparse

descriptor = [
    {
        'name'          : 'mesh',
        'code'          : 0x00000000,
        'container'     : True
    },
    {
        'name'          : 'vertices',
        'code'          : 0x00000002,
        'subname'       : 'vertex',
        'subattrib'     : [['', 'vector3']]
    },
    {
        'name'          : 'vertex_normals',
        'code'          : 0x00000003,
        'subname'       : 'normal',
        'subattrib'     : [['', 'vector3']]
    },
    {
        'name'          : 'mesh_user_text',
        'code'          : 0x0000000C,
        'attrib'        : [['', 'string']]
    },
    {
        'name'          : 'vertex_influences',
        'code'          : 0x0000000E,
        'subname'       : 'id',
        'subattrib'     : [['', 'uint16'], ['_padding', 'uint8', 6]]
    },
    {
        'name'          : 'mesh_header3',
        'code'          : 0x0000001F,
        'attrib'        : [
            ['Version', 'version'],
            ['Attributes', 'uint32'],
            ['MeshName', 'name'],
            ['ContainerName', 'name'],
            ['NumTris', 'uint32'],
            ['NumVertices', 'uint32'],
            ['NumMaterials', 'uint32'],
            ['NumDamageStages', 'uint32'],
            ['SortLevel', 'sint32'],
            ['PrelitVersion', 'version'],
            ['FutureCounts', 'uint32'],
            ['VertexChannels', 'uint32'],
            ['FaceChannels', 'uint32'],
            ['Min', 'vector3'],
            ['Max', 'vector3'],
            ['SphCenter', 'vector3'],
            ['SphRadius', 'float32']
        ]
    },
    {
        'name'          : 'triangles',
        'code'          : 0x00000020,
        'subname'       : 'triangle',
        'subattrib'     : [
            ['Vindex', 'uint32', 3],
            ['Attributes', 'uint32'],
            ['Normal', 'vector3'],
            ['Dist', 'float32']
        ]
    },
    {
        'name'          : 'vertex_shade_indices',
        'code'          : 0x00000022,
        'subname'       : 'id',
        'subattrib'     : [['', 'uint32']]
    },
    {
        'name'          : 'prelit_unlit',
        'code'          : 0x00000023,
        'container'     : True
    },
    {
        'name'          : 'prelit_vertex',
        'code'          : 0x00000024,
        'container'     : True
    },
    {
        'name'          : 'prelit_lightmap_multi_pass',
        'code'          : 0x00000025,
        'container'     : True
    },
    {
        'name'          : 'prelit_lightmap_multi_texture',
        'code'          : 0x00000026,
        'container'     : True
    },
    {
        'name'          : 'material_info',
        'code'          : 0x00000028,
        'attrib'        : [
            ['PassCount', 'uint32'],
            ['VertexMaterialCount', 'uint32'],
            ['ShaderCount', 'uint32'],
            ['TextureCount', 'uint32']
        ]
    },
    {
        'name'          : 'shaders',
        'code'          : 0x00000029,
        'subname'       : 'shader',
        'subattrib'        : [
            ['DepthCompare', 'uint8'],
            ['DepthMask', 'uint8'],
            ['ColorMask', 'uint8'],
            ['DestBlend', 'uint8'],
            ['FogFunc', 'uint8'],
            ['PriGradient', 'uint8'],
            ['SecGradient', 'uint8'],
            ['SrcBlend', 'uint8'],
            ['Texturing', 'uint8'],
            ['DetailColorFunc', 'uint8'],
            ['DetailAlphaFunc', 'uint8'],
            ['ShaderPreset', 'uint8'],
            ['AlphaTest', 'uint8'],
            ['PostDetailColorFunc', 'uint8'],
            ['PostDetailAlphaFunc', 'uint8'],
            ['_padding', 'uint8']
        ]
    },
    {
        'name'          : 'vertex_materials',
        'code'          : 0x0000002A,
        'container'     : True
    },
    {
        'name'          : 'vertex_material',
        'code'          : 0x0000002B,
        'container'     : True
    },
    {
        'name'          : 'vertex_material_name',
        'code'          : 0x0000002C,
        'attrib'        : [['', 'string']]
    },
    {
        'name'          : 'vertex_material_info',
        'code'          : 0x0000002D,
        'attrib'        : [
            ['Attributes', 'uint32'],
            ['Ambient', 'rgb'],
            ['Diffuse', 'rgb'],
            ['Specular', 'rgb'],
            ['Emissive', 'rgb'],
            ['Shininess', 'float32'],
            ['Opacity', 'float32'],
            ['Translucency', 'float32']
        ]
    },
    {
        'name'          : 'vertex_mapper_args0',
        'code'          : 0x0000002E,
        'attrib'        : [['', 'string']]
    },
    {
        'name'          : 'vertex_mapper_args1',
        'code'          : 0x0000002F,
        'attrib'        : [['', 'string']]
    },
    {
        'name'          : 'textures',
        'code'          : 0x00000030,
        'container'     : True
    },
    {
        'name'          : 'texture',
        'code'          : 0x00000031,
        'container'     : True
    },
    {
        'name'          : 'texture_name',
        'code'          : 0x00000032,
        'attrib'        : [['', 'string']]
    },
    {
        'name'          : 'texture_info',
        'code'          : 0x00000033,
        'attrib'        : [
            ['Attributes', 'uint16'],
            ['AnimType', 'uint16'],
            ['FrameCount', 'uint32'],
            ['FrameRate', 'float32']
        ]
    },
    {
        'name'          : 'material_pass',
        'code'          : 0x00000038,
        'container'     : True
    },
    {
        'name'          : 'vertex_material_ids',
        'code'          : 0x00000039,
        'subname'       : 'id',
        'subattrib'     : [['', 'uint32']]
    },
    {
        'name'          : 'shader_ids',
        'code'          : 0x0000003A,
        'subname'       : 'id',
        'subattrib'     : [['', 'uint32']]
    },
    {
        'name'          : 'dcg',
        'code'          : 0x0000003B,
        'subname'       : 'rgba',
        'subattrib'     : [['', 'rgba']]
    },
    {
        'name'          : 'dig',
        'code'          : 0x0000003C,
        'subname'       : 'rgb',
        'subattrib'     : [['', 'rgb']]
    },
    {
        'name'          : 'scg',
        'code'          : 0x0000003E,
        'subname'       : 'rgb',
        'subattrib'     : [['', 'rgb']]
    },
    {
        'name'          : 'texture_stage',
        'code'          : 0x00000048,
        'container'     : True
    },
    {
        'name'          : 'texture_ids',
        'code'          : 0x00000049,
        'subname'       : 'id',
        'subattrib'     : [['', 'uint32']]
    },
    {
        'name'          : 'stage_texcoords',
        'code'          : 0x0000004A,
        'subname'       : 'uv',
        'subattrib'     : [['', 'uv']]
    },
    {
        'name'          : 'per_face_texcoord_ids',
        'code'          : 0x0000004B,
        'subname'       : 'id',
        'subattrib'     : [['', 'uint32', 3]]
    },
    {
        'name'          : 'deform',
        'code'          : 0x00000058,
        'attrib'        : [
            ['SetCount', 'uint32'],
            ['AlphaPasses', 'uint32'],
            ['_reserved', 'uint32', 3]
        ],
        'container'     : True
    },
    {
        'name'          : 'deform_set',
        'code'          : 0x00000059,
        'attrib'        : [
            ['KeyframeCount', 'uint32'],
            ['flags', 'uint32'],
            ['_reserved', 'uint32']
        ],
        'container'     : True
    },
    {
        'name'          : 'deform_keyframe',
        'code'          : 0x0000005A,
        'attrib'        : [
            ['DeformPercent', 'float32'],
            ['DataCount', 'uint32'],
            ['_reserved', 'uint32', 2]
        ],
        'container'     : True
    },
    {
        'name'          : 'deform_data',
        'code'          : 0x0000005B,
        'attrib'        : [
            ['VertexIndex', 'uint32'],
            ['Position', 'vector3'],
            ['Color', 'rgba'],
            ['_reserved', 'uint32', 2]
        ]
    },
    {
        'name'          : 'ps2_shaders',
        'code'          : 0x00000080,
        'subname'       : 'shader',
        'subattrib'        : [
            ['DepthCompare', 'uint8'],
            ['DepthMask', 'uint8'],
            ['ColorMask', 'uint8'],
            ['DestBlend', 'uint8'],
            ['FogFunc', 'uint8'],
            ['PriGradient', 'uint8'],
            ['SecGradient', 'uint8'],
            ['SrcBlend', 'uint8'],
            ['Texturing', 'uint8'],
            ['DetailColorFunc', 'uint8'],
            ['DetailAlphaFunc', 'uint8'],
            ['ShaderPreset', 'uint8'],
            ['AlphaTest', 'uint8'],
            ['PostDetailColorFunc', 'uint8'],
            ['PostDetailAlphaFunc', 'uint8'],
            ['_padding', 'uint8']
        ]
    },
    {
        'name'          : 'aabtree',
        'code'          : 0x00000090,
        'container'     : True
    },
    {
        'name'          : 'aabtree_header',
        'code'          : 0x00000091,
        'attrib'        : [
            ['NodeCount', 'uint32'],
            ['PolyCount', 'uint32'],
            ['_padding', 'uint32', 6]
        ]
    },
    {
        'name'          : 'aabtree_polyindices',
        'code'          : 0x00000092,
        'subname'       : 'id',
        'subattrib'     : [['', 'uint32']]
    },
    {
        'name'          : 'aabtree_nodes',
        'code'          : 0x00000093,
        'subname'       : 'node',
        'subattrib'     : [
            ['Min', 'vector3'],
            ['Max', 'vector3'],
            ['FrontOrPoly0', 'uint32'],
            ['BackOrPolyCount', 'uint32']
        ]
    },
    {
        'name'          : 'hierarchy',
        'code'          : 0x00000100,
        'container'     : True
    },
    {
        'name'          : 'hierarchy_header',
        'code'          : 0x00000101,
        'attrib'     : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['NumPivots', 'uint32'],
            ['Center', 'vector3']
        ]
    },
    {
        'name'          : 'pivots',
        'code'          : 0x00000102,
        'subname'       : 'pivot',
        'subattrib'     : [
            ['Name', 'name'],
            ['ParentIdx', 'uint32'],
            ['Translation', 'vector3'],
            ['EulerAngles', 'vector3'],
            ['Rotation', 'quaternion']
        ]
    },
    {
        'name'          : 'pivot_fixups',
        'code'          : 0x00000103,
        'subname'       : 'matrix3x4',
        'subattrib'     : [
            ['', 'float32', 12]
        ]
    },
    {
        'name'          : 'animation',
        'code'          : 0x00000200,
        'unimplemented' : True,
    },
    {
        'name'          : 'animation_header',
        'code'          : 0x00000201,
        'unimplemented' : True,
    },
    {
        'name'          : 'animation_channel',
        'code'          : 0x00000202,
        'unimplemented' : True,
    },
    {
        'name'          : 'bit_channel',
        'code'          : 0x00000203,
        'unimplemented' : True,
    },
    {
        'name'          : 'compressed_animation',
        'code'          : 0x00000280,
        'unimplemented' : True,
    },
    {
        'name'          : 'compressed_animation_header',
        'code'          : 0x00000281,
        'unimplemented' : True,
    },
    {
        'name'          : 'compressed_animation_channel',
        'code'          : 0x00000282,
        'unimplemented' : True,
    },
    {
        'name'          : 'compressed_bit_channel',
        'code'          : 0x00000283,
        'unimplemented' : True,
    },
    {
        'name'          : 'morph_animation',
        'code'          : 0x000002C0,
        'container'     : True
    },
    {
        'name'          : 'morphanim_header',
        'code'          : 0x000002C1,
        'unimplemented' : True,
    },
    {
        'name'          : 'morphanim_channel',
        'code'          : 0x000002C2,
        'container'     : True
    },
    {
        'name'          : 'morphanim_posename',
        'code'          : 0x000002C3,
        'unimplemented' : True,
    },
    {
        'name'          : 'morphanim_keydata',
        'code'          : 0x000002C4,
        'unimplemented' : True,
    },
    {
        'name'          : 'morphanim_pivotchanneldata',
        'code'          : 0x000002C5,
        'unimplemented' : True,
    },
    {
        'name'          : 'hmodel',
        'code'          : 0x00000300,
        'unimplemented' : True,
    },
    {
        'name'          : 'hmodel_header',
        'code'          : 0x00000301,
        'unimplemented' : True,
    },
    {
        'name'          : 'node',
        'code'          : 0x00000302,
        'unimplemented' : True,
    },
    {
        'name'          : 'collision_node',
        'code'          : 0x00000303,
        'unimplemented' : True,
    },
    {
        'name'          : 'skin_node',
        'code'          : 0x00000304,
        'unimplemented' : True,
    },
    {
        'name'          : 'obsolete_w3d_chunk_hmodel_aux_data',
        'code'          : 0x00000305,
        'unimplemented' : True,
    },
    {
        'name'          : 'obsolete_w3d_chunk_shadow_node',
        'code'          : 0x00000306,
        'unimplemented' : True,
    },
    {
        'name'          : 'lodmodel',
        'code'          : 0x00000400,
        'unimplemented' : True,
    },
    {
        'name'          : 'lodmodel_header',
        'code'          : 0x00000401,
        'unimplemented' : True,
    },
    {
        'name'          : 'lod',
        'code'          : 0x00000402,
        'unimplemented' : True,
    },
    {
        'name'          : 'collection',
        'code'          : 0x00000420,
        'unimplemented' : True,
    },
    {
        'name'          : 'collection_header',
        'code'          : 0x00000421,
        'unimplemented' : True,
    },
    {
        'name'          : 'collection_obj_name',
        'code'          : 0x00000422,
        'unimplemented' : True,
    },
    {
        'name'          : 'placeholder',
        'code'          : 0x00000423,
        'unimplemented' : True,
    },
    {
        'name'          : 'transform_node',
        'code'          : 0x00000424,
        'unimplemented' : True,
    },
    {
        'name'          : 'points',
        'code'          : 0x00000440,
        'unimplemented' : True,
    },
    {
        'name'          : 'light',
        'code'          : 0x00000460,
        'unimplemented' : True,
    },
    {
        'name'          : 'light_info',
        'code'          : 0x00000461,
        'unimplemented' : True,
    },
    {
        'name'          : 'spot_light_info',
        'code'          : 0x00000462,
        'unimplemented' : True,
    },
    {
        'name'          : 'near_attenuation',
        'code'          : 0x00000463,
        'unimplemented' : True,
    },
    {
        'name'          : 'far_attenuation',
        'code'          : 0x00000464,
        'unimplemented' : True,
    },
    {
        'name'          : 'emitter',
        'code'          : 0x00000500,
        'unimplemented' : True,
    },
    {
        'name'          : 'emitter_header',
        'code'          : 0x00000501,
        'unimplemented' : True,
    },
    {
        'name'          : 'emitter_user_data',
        'code'          : 0x00000502,
        'unimplemented' : True,
    },
    {
        'name'          : 'emitter_info',
        'code'          : 0x00000503,
        'unimplemented' : True,
    },
    {
        'name'          : 'emitter_infov2',
        'code'          : 0x00000504,
        'unimplemented' : True,
    },
    {
        'name'          : 'emitter_props',
        'code'          : 0x00000505,
        'unimplemented' : True,
    },
    {
        'name'          : 'obsolete_w3d_chunk_emitter_color_keyframe',
        'code'          : 0x00000506,
        'unimplemented' : True,
    },
    {
        'name'          : 'obsolete_w3d_chunk_emitter_opacity_keyframe',
        'code'          : 0x00000507,
        'unimplemented' : True,
    },
    {
        'name'          : 'obsolete_w3d_chunk_emitter_size_keyframe',
        'code'          : 0x00000508,
        'unimplemented' : True,
    },
    {
        'name'          : 'emitter_line_properties',
        'code'          : 0x00000509,
        'unimplemented' : True,
    },
    {
        'name'          : 'emitter_rotation_keyframes',
        'code'          : 0x0000050A,
        'unimplemented' : True,
    },
    {
        'name'          : 'emitter_frame_keyframes',
        'code'          : 0x0000050B,
        'unimplemented' : True,
    },
    {
        'name'          : 'emitter_blur_time_keyframes',
        'code'          : 0x0000050C,
        'unimplemented' : True,
    },
    {
        'name'          : 'aggregate',
        'code'          : 0x00000600,
        'container'     : True
    },
    {
        'name'          : 'aggregate_header',
        'code'          : 0x00000601,
        'unimplemented' : True,
    },
    {
        'name'          : 'aggregate_info',
        'code'          : 0x00000602,
        'unimplemented' : True,
    },
    {
        'name'          : 'texture_replacer_info',
        'code'          : 0x00000603,
        'unimplemented' : True,
    },
    {
        'name'          : 'aggregate_class_info',
        'code'          : 0x00000604,
        'unimplemented' : True,
    },
    {
        'name'          : 'hlod',
        'code'          : 0x00000700,
        'container'     : True
    },
    {
        'name'          : 'hlod_header',
        'code'          : 0x00000701,
        'attrib'        : [
            ['Version', 'version'],
            ['LodCount', 'uint32'],
            ['Name', 'name'],
            ['HierarchyName', 'name']
        ]
    },
    {
        'name'          : 'hlod_lod_array',
        'code'          : 0x00000702,
        'container'     : True
    },
    {
        'name'          : 'hlod_sub_object_array_header',
        'code'          : 0x00000703,
        'attrib'        : [
            ['ModelCount', 'uint32'],
            ['MaxScreenSize', 'float32']
        ]
    },
    {
        'name'          : 'hlod_sub_object',
        'code'          : 0x00000704,
        'attrib'        : [
            ['BoneIndex', 'uint32'],
            ['Name', 'name', 2]
        ]
    },
    {
        'name'          : 'hlod_aggregate_array',
        'code'          : 0x00000705,
        'container'     : True
    },
    {
        'name'          : 'hlod_proxy_array',
        'code'          : 0x00000706,
        'container'     : True
    },
    {
        'name'          : 'box',
        'code'          : 0x00000740,
        'attrib'        : [
            ['Version', 'version'],
            ['Attributes', 'uint32'],
            ['Name', 'name', 2],
            ['Color', 'rgb'],
            ['Center', 'vector3'],
            ['Extent', 'vector3']
        ]
    },
    {
        'name'          : 'sphere',
        'code'          : 0x00000741,
        'attrib'        : [
            ['Version', 'version'],
            ['Attributes', 'uint32'],
            ['Name', 'name', 2],
            ['Color', 'rgb'],
            ['Center', 'vector3'],
            ['Extent', 'vector3']
        ]
    },
    {
        'name'          : 'ring',
        'code'          : 0x00000742,
        'attrib'        : [
            ['Version', 'version'],
            ['Attributes', 'uint32'],
            ['Name', 'name', 2],
            ['Color', 'rgb'],
            ['Center', 'vector3'],
            ['Extent', 'vector3']
        ]
    },
    {
        'name'          : 'null_object',
        'code'          : 0x00000750,
        'attrib'        : [
            ['Version', 'version'],
            ['Attributes', 'uint32'],
            ['_padding', 'uint32', 2],
            ['Name', 'name', 2]
        ]
    },
    {
        'name'          : 'lightscape',
        'code'          : 0x00000800,
        'container'     : True
    },
    {
        'name'          : 'lightscape_light',
        'code'          : 0x00000801,
        'unimplemented' : True,
    },
    {
        'name'          : 'light_transform',
        'code'          : 0x00000802,
        'attrib'        : [['matrix4x3', 'float32', 12]]
    },
    {
        'name'          : 'dazzle',
        'code'          : 0x00000900,
        'container'     : True
    },
    {
        'name'          : 'dazzle_name',
        'code'          : 0x00000901,
        'attrib'        : [['', 'string']]
    },
    {
        'name'          : 'dazzle_typename',
        'code'          : 0x00000902,
        'attrib'        : [['', 'string']]
    },
    {
        'name'          : 'soundrobj',
        'code'          : 0x00000A00,
        'container'     : True
    },
    {
        'name'          : 'soundrobj_header',
        'code'          : 0x00000A01,
        'attrib'        : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['Flags', 'uint32'],
            ['_padding', 'uint32', 8]
        ]
    },
    {
        'name'          : 'soundrobj_definition',
        'code'          : 0x00000A02,
        'unimplemented' : True,
    },
]

struct_types = {
    'uint8': 'B',
    'uint16': 'H',
    'uint32': 'L',
    'sint32': 'l',
    'version': '2H',
    'rgb': '4B',
    'rgba': '4B',
    
    'float32': 'f',
    'uv': '2f',
    'vector3': '3f',
    'quaternion': '4f',
    
    'name': '16s',
    # 'string' is a special case
}

dint = {}
for d in descriptor:
    dint[d['code']] = d
dstr = {}
for d in descriptor:
    dstr[d['name']] = d

def elem_init(desc):
    e = et.Element(desc['name'])
    e.desc = desc
    return e

def elem_parse_type(file, type, count=1):
    fmt = struct_types[type]
    if count > 1:
        fmt *= count
    
    binary = file.read(struct.calcsize(fmt))
    if binary == b'':
        return None
    data = struct.unpack(fmt, binary)
    
    if type == 'name':
        return b2s(data[0])
    if type == 'version':
        return str(data[1]) + '.' + str(data[0])
    
    if len(data) == 1:
        return data[0]
    
    return data
def elem_attr_size(attrdesc):
    size = 0
    for i in attrdesc:
        if i[1] == 'string':
            continue
        
        fmt = struct_types[i[1]]
        if len(i) > 2:
            fmt *= i[2]
        size += struct.calcsize(fmt)
    return size
    
def elem_parse_nodes(parent, file, size=0x7FFFFFFF):
    while size > 0:
        
        # read data in correctly
        data = read_struct(file, 'LL')
        if data == None:
            return
        
        hdesc = data[0]
        hsize = data[1] & 0x7FFFFFFF
        
        # header size + chunk size
        size -= 8 + hsize
        
        # check header exists
        if hdesc not in dint:
            print('MISSINGNO : ' + "0x%0.8X" % hdesc)
            file.read(hsize)
            continue
        
        # create the element
        e = elem_init(dint[hdesc])
        parent.append(e)
        
        if ('unimplemented' in e.desc and e.desc['unimplemented'] == True):
            print('unimplemented : ' + e.desc['name'])
            file.read(hsize)
            continue
        
        # attributes
        attribsize = 0
        if ('attrib' in e.desc and e.desc['attrib'] is not None):
            attribsize = elem_attr_size(e.desc['attrib'])
            for i in e.desc['attrib']:
                if i[1] == 'string':
                    val = b2s(file.read(hsize))
                else:
                    if len(i) > 2:
                        val = str(elem_parse_type(file, i[1], i[2]))
                    else:
                        val = str(elem_parse_type(file, i[1]))
                if (i[0] != ''):
                    if (i[0][1] != '_'):
                        e.attrib[i[0]] = val
                    else:
                        e.text = val
        
        if ('subattrib' in e.desc and e.desc['subattrib'] is not None):
            stepsize = elem_attr_size(e.desc['subattrib'])
            step = 0
            while step < hsize:
                sub = et.Element(e.desc['subname'])
                e.append(sub)
                for i in e.desc['subattrib']:
                    if i[1] == 'string':
                        val = b2s(file.read(hsize))
                    else:
                        if len(i) > 2:
                            val = str(elem_parse_type(file, i[1], i[2]))
                        else:
                            val = str(elem_parse_type(file, i[1]))
                    if (i[0] != ''):
                        if (i[0][1] != '_'):
                            sub.attrib[i[0]] = val
                        else:
                            sub.text = val
                step += stepsize
        
        # containers, recursive reading
        if ('container' in e.desc and e.desc['container'] == True):
            elem_parse_nodes(e, file, hsize + attribsize)

def b2s(str):
    return str.split(b'\0')[0].decode('utf-8')
def s2b(str, s=None):
    str = str.encode('utf-8')
    if s is not None and len(str) >= s:
        str = str[:s - 1]
    return str + b'\0'
        
# loading algorithm

def read_struct(file, fmt):
    binary = file.read(struct.calcsize(fmt))
    
    if binary == b'':
        return None
    
    data = struct.unpack(fmt, binary)
    return data

def read_header(file):
    data = read_struct(file, 'LL')
    
    if data == None:
        return None
    
    try:
        type = w3d_def_load[data[0]]
    except KeyError:
        type = 'error'
    
    size = data[1] & 0x7FFFFFFF
    
    return (type, size)

def parse_nodes(parent, file, size=0x7FFFFFFF):
    while size > 0:
        ci = read_header(file)
        if ci == None:
            break
        
        try:
            child = globals()['node_' + ci[0]]()
            child.read(file, ci[1])
            parent.append(child)
        except KeyError:
            file.read(ci[1])
            print('Error! Not implemented: ' + ci[0])
        
        # limit size for nested chunks
        size -= 8 + ci[1] # header size + chunk size
    
def w3d_to_elem(filepath):
    file = open(filepath, 'rb')
    print('load: ' + filepath)
    try:
        root = et.Element('w3d')
        elem_parse_nodes(root, file)
    finally:
        file.close()
    return root
    
def elem_to_w3d(root, filepath):
    file = open(filepath, 'wb')
    print('save: ' + filepath)
    for child in root:
        child.pack()
        child.write(file)
    file.close()

parser = argparse.ArgumentParser(description='Westwood3D to XML')
parser.add_argument('-s', help='Source file path e.g. kane.w3d')
parser.add_argument('-o', help='Output file path e.g. kane.xml')
args = parser.parse_args()

if args.s is not None and args.o is not None:

    #tree = et.parse('test.xml')
    #root = tree.getroot()
    #elem_to_w3d('myfile.w3d')

    root = w3d_to_elem(args.s)
    file = open(args.o, 'w')
    file.write(minidom.parseString(et.tostring(root)).toprettyxml())
    file.close()
else:
    parser.print_help()