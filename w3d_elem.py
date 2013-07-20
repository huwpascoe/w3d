from xml.dom import minidom
import xml.etree.ElementTree as et
import struct
import argparse
import os
import ast

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
        'subattrib'     : [
            ['Bone0Index', 'uint16'],
            ['Bone1Index', 'uint16'],
            ['Bone0Weight', 'uint16'],
            ['Bone1Weight', 'uint16']
        ]
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
        'name'          : 'tangents',
        'code'          : 0x00000060,
        'subname'       : 'tangent',
        'subattrib'     : [['', 'vector3']]
    },
    {
        'name'          : 'binormals',
        'code'          : 0x00000061,
        'subname'       : 'binormal',
        'subattrib'     : [['', 'vector3']]
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
        'container'     : True,
    },
    {
        'name'          : 'animation_header',
        'code'          : 0x00000201,
        'attrib'        : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['HierarchyName', 'name'],
            ['NumFrames', 'uint32'],
            ['FrameRate', 'uint32']
        ]
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
        'container'     : True,
    },
    {
        'name'          : 'compressed_animation_header',
        'code'          : 0x00000281,
        'attrib'        : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['HierarchyName', 'name'],
            ['NumFrames', 'uint32'],
            ['FrameRate', 'uint16'],
            ['Flavor', 'uint16'],
        ]
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
        'attrib'        : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['HierarchyName', 'name'],
            ['FrameCount', 'uint32'],
            ['FrameRate', 'float32'],
            ['ChannelCount', 'uint32']
        ]
    },
    {
        'name'          : 'morphanim_channel',
        'code'          : 0x000002C2,
        'container'     : True
    },
    {
        'name'          : 'morphanim_posename',
        'code'          : 0x000002C3,
        'attrib'        : [['', 'string']]
    },
    {
        'name'          : 'morphanim_keydata',
        'code'          : 0x000002C4,
        'subname'       : 'key',
        'subattrib'        : [
            ['MorphFrame', 'uint32'],
            ['PoseFrame', 'uint32'],
        ]
    },
    {
        'name'          : 'morphanim_pivotchanneldata',
        'code'          : 0x000002C5,
        'subname'       : 'channel',
        'subattrib'        : [
            ['', 'uint32']
        ]
    },
    {
        'name'          : 'hmodel',
        'code'          : 0x00000300,
        'container'     : True,
    },
    {
        'name'          : 'hmodel_header',
        'code'          : 0x00000301,
        'attrib'        : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['HierarchyName', 'name'],
            ['NumConnections', 'uint16']
        ]
    },
    {
        'name'          : 'node',
        'code'          : 0x00000302,
        'attrib'        : [
            ['RenderObjName', 'name'],
            ['PivotIdx', 'uint16']
        ]
    },
    {
        'name'          : 'collision_node',
        'code'          : 0x00000303,
        'attrib'        : [
            ['RenderObjName', 'name'],
            ['PivotIdx', 'uint16']
        ]
    },
    {
        'name'          : 'skin_node',
        'code'          : 0x00000304,
        'attrib'        : [
            ['RenderObjName', 'name'],
            ['PivotIdx', 'uint16']
        ]
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
        'container'     : True,
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
        'container'     : True,
    },
    {
        'name'          : 'collection_header',
        'code'          : 0x00000421,
        'unimplemented' : True,
    },
    {
        'name'          : 'collection_obj_name',
        'code'          : 0x00000422,
        'attrib'        : [['', 'string']]
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
        'subname'       : 'point',
        'subattrib'     : [['', 'vector3']]
    },
    {
        'name'          : 'light',
        'code'          : 0x00000460,
        'container'     : True,
    },
    {
        'name'          : 'light_info',
        'code'          : 0x00000461,
        'attrib'        : [
            ['Attributes', 'uint32'],
            ['_unused', 'uint32'],
            ['Ambient', 'rgb'],
            ['Diffuse', 'rgb'],
            ['Specular', 'rgb'],
            ['Intensity', 'float32']
        ]
    },
    {
        'name'          : 'spot_light_info',
        'code'          : 0x00000462,
        'attrib'        : [
            ['SpotAngle', 'float32'],
            ['SpotExponent', 'float32']
        ]
    },
    {
        'name'          : 'near_attenuation',
        'code'          : 0x00000463,
        'attrib'        : [
            ['Start', 'float32'],
            ['End', 'float32']
        ]
    },
    {
        'name'          : 'far_attenuation',
        'code'          : 0x00000464,
        'attrib'        : [
            ['Start', 'float32'],
            ['End', 'float32']
        ]
    },
    {
        'name'          : 'emitter',
        'code'          : 0x00000500,
        'container'     : True,
    },
    {
        'name'          : 'emitter_header',
        'code'          : 0x00000501,
        'attrib'        : [
            ['Version', 'version'],
            ['Name', 'name']
        ]
    },
    {
        'name'          : 'emitter_user_data',
        'code'          : 0x00000502,
        'attrib'        : [
            ['Type', 'uint32'],
            ['SizeofStringParam', 'uint32'],
            ['StringParam', 'string']
        ]
    },
    {
        'name'          : 'emitter_info',
        'code'          : 0x00000503,
        'attrib'        : [
            ['TextureFilename', 'char', 260],
            ['StartSize', 'float32'],
            ['EndSize', 'float32'],
            ['Lifetime', 'float32'],
            ['EmissionRate', 'float32'],
            ['MaxEmissions', 'float32'],
            ['VelocityRandom', 'float32'],
            ['PositionRandom', 'float32'],
            ['FadeTime', 'float32'],
            ['Gravity', 'float32'],
            ['Elasticity', 'float32'],
            ['Velocity', 'vector3'],
            ['Acceleration', 'vector3'],
            ['StartColor', 'rgba'],
            ['EndColor', 'rgba']
        ]
    },
    {
        'name'          : 'emitter_infov2',
        'code'          : 0x00000504,
        'attrib'        : [
            ['BurstSize', 'uint32'],
            ['CreationVolume', '???'],
            ['VelRandom', '???'],
            ['OutwardVel', 'float32'],
            ['VelInherit', 'float32'],
            ['Shader', '???'],
            ['RenderMode', 'uint32'],
            ['FrameMode', 'uint32'],
            ['_reserved', 'uint32', 6],
        ]
    },
    {
        'name'          : 'emitter_props',
        'code'          : 0x00000505,
        'attrib'        : [
            ['ColorKeyframes', 'uint32'],
            ['OpacityKeyframes', 'uint32'],
            ['SizeKeyframes', 'uint32'],
            ['ColorRandom', 'rgba'],
            ['OpacityRandom', 'float32'],
            ['SizeRandom', 'float32'],
            ['_reserved', 'uint32', 4]
        ]
    },
    {
        'name'          : 'obsolete_w3d_chunk_emitter_color_keyframe',
        'code'          : 0x00000506,
        'attrib'        : [
            ['Time', 'float32'],
            ['Color', 'rgba']
        ]
    },
    {
        'name'          : 'obsolete_w3d_chunk_emitter_opacity_keyframe',
        'code'          : 0x00000507,
        'attrib'        : [
            ['Time', 'float32'],
            ['Opacity', 'float32']
        ]
    },
    {
        'name'          : 'obsolete_w3d_chunk_emitter_size_keyframe',
        'code'          : 0x00000508,
        'attrib'        : [
            ['Time', 'float32'],
            ['Size', 'float32']
        ]
    },
    {
        'name'          : 'emitter_line_properties',
        'code'          : 0x00000509,
        'attrib'        : [
            ['Flags', 'uint32'],
            ['SubdivisionLevel', 'uint32'],
            ['NoiseAmplitude', 'float32'],
            ['MergeAbortFactor', 'float32'],
            ['TextureTileFactor', 'float32'],
            ['UPerSec', 'float32'],
            ['VPerSec', 'float32'],
            ['_reserved', 'uint32', 9]
        ]
    },
    {
        'name'          : 'emitter_rotation_keyframes',
        'code'          : 0x0000050A,
        'attrib'        : [
            ['KeyframeCount', 'uint32'],
            ['Random', 'float32'],
            ['OrientationRandom', 'float32'],
            ['_reserved', 'uint32'],
        ],
        'subname'       : 'keyframe',
        'subattrib'     : [
            ['Time', 'float32'],
            ['Rotation', 'float32']
        ]
    },
    {
        'name'          : 'emitter_frame_keyframes',
        'code'          : 0x0000050B,
        'attrib'        : [
            ['KeyframeCount', 'uint32'],
            ['Random', 'float32'],
            ['_reserved', 'uint32', 2],
        ],
        'subname'       : 'keyframe',
        'subattrib'     : [
            ['Time', 'float32'],
            ['Frame', 'float32']
        ]
    },
    {
        'name'          : 'emitter_blur_time_keyframes',
        'code'          : 0x0000050C,
        'attrib'        : [
            ['KeyframeCount', 'uint32'],
            ['Random', 'float32'],
            ['_reserved', 'uint32'],
        ],
        'subname'       : 'keyframe',
        'subattrib'     : [
            ['Time', 'float32'],
            ['BlurTime', 'float32']
        ]
    },
    {
        'name'          : 'aggregate',
        'code'          : 0x00000600,
        'container'     : True
    },
    {
        'name'          : 'aggregate_header',
        'code'          : 0x00000601,
        'attrib'        : [
            ['Version', 'version'],
            ['Name', 'name']
        ],
        'container'     : True
    },
    {
        'name'          : 'aggregate_info',
        'code'          : 0x00000602,
        'attrib'        : [
            ['BaseModelName', 'name', 2],
            ['SubobjectCount', 'uint32']
        ],
        'subname'       : 'subobject',
        'subattrib'     : [
            ['SubobjectName', 'name', 2],
            ['BoneName', 'name', 2]
        ],
        
    },
    {
        'name'          : 'texture_replacer_info',
        'code'          : 0x00000603,
        'unimplemented' : True,
    },
    {
        'name'          : 'aggregate_class_info',
        'code'          : 0x00000604,
        'attrib'        : [
            ['OriginalClassID', 'uint32'],
            ['Flags', 'uint32'],
            ['_reserved', 'uint32', 3],
        ]
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
        'container'     : True,
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
    {
        'name'          : 'secondary_vertices',
        'code'          : 0x00000C00,
        'subname'       : 'vertex',
        'subattrib'     : [['', 'vector3']]
    },
    {
        'name'          : 'secondary_normals',
        'code'          : 0x00000C01,
        'subname'       : 'normal',
        'subattrib'     : [['', 'vector3']]
    },
]

struct_types = {
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
    # 'name' and 'string' are special cases
}

dint = {}
for d in descriptor:
    dint[d['code']] = d
dstr = {}
for d in descriptor:
    dstr[d['name']] = d

def elem_parse_type(file, type, count=1):
    if type == 'name':
        fmt = str(count * 16) + 's'
    else:
        fmt = struct_types[type]
        if count > 1:
            fmt *= count
    
    binary = file.read(struct.calcsize(fmt))
    if binary == b'':
        return None
    data = struct.unpack(fmt, binary)

    if type == 'rgb':
        return (data[0], data[1], data[2])
    if type == 'version':
        return str(data[1]) + '.' + str(data[0])
    if type == 'name':
        return b2s(data[0])
    
    if len(data) == 1:
        return data[0]
    
    return data
def elem_write_type(file, val, type, count=1):
    if type == 'name':
        fmt = str(count * 16) + 's'
    else:
        fmt = struct_types[type]
        if count > 1:
            fmt *= count
    
    # null values
    if val is None:
        size = struct.calcsize(fmt)
        file.write(b'\x00' * size)
        return
    
    # parse strings to types
    data = None
    if type == 'rgb':
        val = ast.literal_eval(val)
        data = struct.pack(fmt, val[0], val[1], val[2], 0)
    elif type == 'version':
        val = val.split('.')
        data = struct.pack(fmt, int(val[1]), int(val[0]))
    elif type == 'name':
        data = struct.pack(fmt, s2b(val))
    else:
        val = ast.literal_eval(val)
        if isinstance(val, tuple):
            data = struct.pack(fmt, *val)
        else:
            data = struct.pack(fmt, val)
    
    if data is not None:
        file.write(data)
    
def elem_attr_size(attrdesc):
    size = 0
    for i in attrdesc:
        if i[1] == 'name':
            if len(i) > 2:
                size += 16 * i[2]
            else:
                size += 16
            continue
        if i[1] not in struct_types:
            continue
        
        fmt = struct_types[i[1]]
        if len(i) > 2:
            fmt *= i[2]
        size += struct.calcsize(fmt)
    return size
    
def elem_parse_nodes(parent, file, size=0x7FFFFFFF):
    while size > 0:
        
        # read data in correctly
        binary = file.read(8)
        if binary == b'':
            return
        data = struct.unpack('LL', binary)
        
        # chunk type, chunk size (not including header)
        hdesc = data[0]
        hsize = data[1] & 0x7FFFFFFF
        
        # subtract header + chunk size
        size -= 8 + hsize
        
        # skip if invalid
        if hdesc not in dint:
            print("MISSINGNO : 0x%0.8X in" % hdesc, parent.tag)
            file.read(hsize)
            continue
        
        # get descriptor, but skip if unimplemented
        desc = dint[hdesc]
        if ('unimplemented' in desc and desc['unimplemented'] == True):
            print('unimplemented : ' + desc['name'])
            file.read(hsize)
            continue
        
        # create the element
        e = et.Element(desc['name'])
        parent.append(e)
        
        # attributes
        attribsize = 0
        if ('attrib' in desc and desc['attrib'] is not None):
            attribsize = elem_attr_size(desc['attrib'])
            for i in desc['attrib']:
                if i[1] == 'string': #TODO special string cases in emitter structs
                    val = b2s(file.read(hsize - attribsize))
                else:
                    if len(i) > 2:
                        val = str(elem_parse_type(file, i[1], i[2]))
                    else:
                        val = str(elem_parse_type(file, i[1]))
                if (i[0] != ''):
                    if (i[0][0] != '_'):
                        e.attrib[i[0]] = val
                else:
                    e.text = val
        
        if ('subattrib' in desc and desc['subattrib'] is not None):
            stepsize = elem_attr_size(desc['subattrib'])
            step = 0
            while step < hsize - attribsize:
                sub = et.Element(desc['subname'])
                e.append(sub)
                for i in desc['subattrib']:
                    if len(i) > 2:
                        val = str(elem_parse_type(file, i[1], i[2]))
                    else:
                        val = str(elem_parse_type(file, i[1]))
                    
                    if (i[0] != ''):
                        if (i[0][0] != '_'):
                            sub.attrib[i[0]] = val
                    else:
                        sub.text = val
                step += stepsize
        
        # containers, recursive reading
        if ('container' in desc and desc['container'] == True):
            elem_parse_nodes(e, file, hsize + attribsize)

def elem_calc_size(parent):
    
    parent.size = 0
    
    # check tag exists
    if parent.tag not in dstr:
        print("MISSINGTAG :", parent.tag)
        return 0
    
    desc = dstr[parent.tag]
    
    # attributes
    if ('attrib' in desc and desc['attrib'] is not None):
        parent.size += elem_attr_size(desc['attrib'])
        for i in desc['attrib']:
            if i[1] == 'string':
                if i[0] == '':
                    parent.size += s2bsize(parent.text)
                else:
                    parent.size += s2bsize(parent.attrib[i[0]])
    
    if ('subattrib' in desc and desc['subattrib'] is not None):
        subsize = elem_attr_size(desc['subattrib'])
        for child in parent:
            parent.size += subsize
    
    # containers, recursive
    if ('container' in desc and desc['container'] == True):
        for child in parent:
            parent.size += elem_calc_size(child)
    
    # return the size + header size
    return parent.size + 8

def elem_write_nodes(file, parent):
    
    # check tag exists
    if parent.tag not in dstr:
        print("MISSINGTAG :", parent.tag)
        return 0
    
    desc = dstr[parent.tag]
    
    # header
    data = struct.pack('LL', desc['code'], parent.size)
    file.write(data)
    
    # attributes
    if ('attrib' in desc and desc['attrib'] is not None):
        for i in desc['attrib']:
            if i[1] == 'string':
                if i[0] == '':
                    file.write(s2b(parent.text))
                else:
                    file.write(s2b(parent.attrib[i[0]]))
            else:
                if (i[0] != ''):
                    if (i[0][0] != '_'):
                        val = parent.attrib[i[0]]
                    else:
                        val = None
                else:
                    val = parent.text
                if len(i) > 2:
                    elem_write_type(file, val, i[1], i[2])
                else:
                    elem_write_type(file, val, i[1])

    
    if ('subattrib' in desc and desc['subattrib'] is not None):
        for child in parent:
            for i in desc['subattrib']:
                if (i[0] != ''):
                    if (i[0][0] != '_'):
                        val = child.attrib[i[0]]
                    else:
                        val = None
                else:
                    val = child.text
                if len(i) > 2:
                    elem_write_type(file, val, i[1], i[2])
                else:
                    elem_write_type(file, val, i[1])
    
    # containers, recursive
    if ('container' in desc and desc['container'] == True):
        for child in parent:
            elem_write_nodes(file, child)
    
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
        
# loading algorithm

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
    print('save: ' + filepath)
    
    #calculate chunk sizes
    filesize = 0
    for child in root:
        filesize += elem_calc_size(child)
    
    # write the chunks
    file = open(filepath, 'wb')
    for child in root:
        elem_write_nodes(file, child)
    file.close()
    
    print (filesize, 'bytes')

parser = argparse.ArgumentParser(description='W3D-XML')
parser.add_argument('-s', help='Source file path')
parser.add_argument('-o', help='Output file path')
args = parser.parse_args()

if args.s is not None and args.o is not None:
    srcname, srcext = os.path.splitext(args.s)
    dstname, dstext = os.path.splitext(args.o)
    
    if srcext == '.w3d' and dstext == '.xml':
        root = w3d_to_elem(args.s)
        file = open(args.o, 'w')
        file.write(minidom.parseString(et.tostring(root)).toprettyxml())
        file.close()
    
    elif srcext == '.xml' and dstext == '.w3d':
        tree = et.parse(args.s)
        root = tree.getroot()
        elem_to_w3d(root, args.o)
        
    else:
        print('NOPE. Must be either: "-s src.w3d -o dest.xml" or "-s src.xml -o dest.w3d"')
else:
    parser.print_help()