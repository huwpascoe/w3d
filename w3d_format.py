format = [
    {
        'tag'           : 'mesh',
        'id'            : 0x00000000,
        'container'     : True
    },
    {
        'tag'           : 'vertices',
        'id'            : 0x00000002,
        'subtag'        : 'vertex',
        'subattr'       : [['', 'vector3']]
    },
    {
        'tag'           : 'vertex_normals',
        'id'            : 0x00000003,
        'subtag'        : 'normal',
        'subattr'       : [['', 'vector3']]
    },
    {
        'tag'           : 'mesh_user_text',
        'id'            : 0x0000000C,
        'attr'          : [['', 'string']]
    },
    {
        'tag'           : 'vertex_influences',
        'id'            : 0x0000000E,
        'subtag'        : 'id',
        'subattr'       : [
            ['Bone0Index', 'uint16'],
            ['Bone1Index', 'uint16'],
            ['Bone0Weight', 'uint16'],
            ['Bone1Weight', 'uint16']
        ]
    },
    {
        'tag'           : 'mesh_header3',
        'id'            : 0x0000001F,
        'attr'          : [
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
        'tag'           : 'triangles',
        'id'            : 0x00000020,
        'subtag'        : 'triangle',
        'subattr'       : [
            ['Vindex', 'uint32', 3],
            ['Attributes', 'uint32'],
            ['Normal', 'vector3'],
            ['Dist', 'float32']
        ]
    },
    {
        'tag'           : 'vertex_shade_indices',
        'id'            : 0x00000022,
        'subtag'        : 'id',
        'subattr'       : [['', 'uint32']]
    },
    {
        'tag'           : 'prelit_unlit',
        'id'            : 0x00000023,
        'container'     : True
    },
    {
        'tag'           : 'prelit_vertex',
        'id'            : 0x00000024,
        'container'     : True
    },
    {
        'tag'           : 'prelit_lightmap_multi_pass',
        'id'            : 0x00000025,
        'container'     : True
    },
    {
        'tag'           : 'prelit_lightmap_multi_texture',
        'id'            : 0x00000026,
        'container'     : True
    },
    {
        'tag'           : 'material_info',
        'id'            : 0x00000028,
        'attr'          : [
            ['PassCount', 'uint32'],
            ['VertexMaterialCount', 'uint32'],
            ['ShaderCount', 'uint32'],
            ['TextureCount', 'uint32']
        ]
    },
    {
        'tag'           : 'shaders',
        'id'            : 0x00000029,
        'subtag'        : 'shader',
        'subattr'       : [
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
        'tag'           : 'vertex_materials',
        'id'            : 0x0000002A,
        'container'     : True
    },
    {
        'tag'           : 'vertex_material',
        'id'            : 0x0000002B,
        'container'     : True
    },
    {
        'tag'           : 'vertex_material_name',
        'id'            : 0x0000002C,
        'attr'          : [['', 'string']]
    },
    {
        'tag'           : 'vertex_material_info',
        'id'            : 0x0000002D,
        'attr'          : [
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
        'tag'           : 'vertex_mapper_args0',
        'id'            : 0x0000002E,
        'attr'          : [['', 'string']]
    },
    {
        'tag'           : 'vertex_mapper_args1',
        'id'            : 0x0000002F,
        'attr'          : [['', 'string']]
    },
    {
        'tag'           : 'textures',
        'id'            : 0x00000030,
        'container'     : True
    },
    {
        'tag'           : 'texture',
        'id'            : 0x00000031,
        'container'     : True
    },
    {
        'tag'           : 'texture_name',
        'id'            : 0x00000032,
        'attr'          : [['', 'string']]
    },
    {
        'tag'           : 'texture_info',
        'id'            : 0x00000033,
        'attr'          : [
            ['Attributes', 'uint16'],
            ['AnimType', 'uint16'],
            ['FrameCount', 'uint32'],
            ['FrameRate', 'float32']
        ]
    },
    {
        'tag'           : 'material_pass',
        'id'            : 0x00000038,
        'container'     : True
    },
    {
        'tag'           : 'vertex_material_ids',
        'id'            : 0x00000039,
        'subtag'        : 'id',
        'subattr'       : [['', 'uint32']]
    },
    {
        'tag'           : 'shader_ids',
        'id'            : 0x0000003A,
        'subtag'        : 'id',
        'subattr'       : [['', 'uint32']]
    },
    {
        'tag'           : 'dcg',
        'id'            : 0x0000003B,
        'subtag'        : 'rgba',
        'subattr'       : [['', 'rgba']]
    },
    {
        'tag'           : 'dig',
        'id'            : 0x0000003C,
        'subtag'        : 'rgb',
        'subattr'       : [['', 'rgb']]
    },
    {
        'tag'           : 'scg',
        'id'            : 0x0000003E,
        'subtag'        : 'rgb',
        'subattr'       : [['', 'rgb']]
    },
    {
        'tag'           : 'texture_stage',
        'id'            : 0x00000048,
        'container'     : True
    },
    {
        'tag'           : 'texture_ids',
        'id'            : 0x00000049,
        'subtag'        : 'id',
        'subattr'       : [['', 'uint32']]
    },
    {
        'tag'           : 'stage_texcoords',
        'id'            : 0x0000004A,
        'subtag'        : 'uv',
        'subattr'       : [['', 'uv']]
    },
    {
        'tag'           : 'per_face_texcoord_ids',
        'id'            : 0x0000004B,
        'subtag'        : 'id',
        'subattr'       : [['', 'uint32', 3]]
    },
    {
        'tag'           : 'deform',
        'id'            : 0x00000058,
        'attr'          : [
            ['SetCount', 'uint32'],
            ['AlphaPasses', 'uint32'],
            ['_reserved', 'uint32', 3]
        ],
        'container'     : True
    },
    {
        'tag'           : 'deform_set',
        'id'            : 0x00000059,
        'attr'          : [
            ['KeyframeCount', 'uint32'],
            ['flags', 'uint32'],
            ['_reserved', 'uint32']
        ],
        'container'     : True
    },
    {
        'tag'           : 'deform_keyframe',
        'id'            : 0x0000005A,
        'attr'          : [
            ['DeformPercent', 'float32'],
            ['DataCount', 'uint32'],
            ['_reserved', 'uint32', 2]
        ],
        'container'     : True
    },
    {
        'tag'           : 'deform_data',
        'id'            : 0x0000005B,
        'attr'          : [
            ['VertexIndex', 'uint32'],
            ['Position', 'vector3'],
            ['Color', 'rgba'],
            ['_reserved', 'uint32', 2]
        ]
    },
    {
        'tag'           : 'tangents',
        'id'            : 0x00000060,
        'subtag'        : 'tangent',
        'subattr'       : [['', 'vector3']]
    },
    {
        'tag'           : 'binormals',
        'id'            : 0x00000061,
        'subtag'        : 'binormal',
        'subattr'       : [['', 'vector3']]
    },
    {
        'tag'           : 'ps2_shaders',
        'id'            : 0x00000080,
        'subtag'        : 'shader',
        'subattr'       : [
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
        'tag'           : 'aabtree',
        'id'            : 0x00000090,
        'container'     : True
    },
    {
        'tag'           : 'aabtree_header',
        'id'            : 0x00000091,
        'attr'          : [
            ['NodeCount', 'uint32'],
            ['PolyCount', 'uint32'],
            ['_padding', 'uint32', 6]
        ]
    },
    {
        'tag'           : 'aabtree_polyindices',
        'id'            : 0x00000092,
        'subtag'        : 'id',
        'subattr'       : [['', 'uint32']]
    },
    {
        'tag'           : 'aabtree_nodes',
        'id'            : 0x00000093,
        'subtag'        : 'node',
        'subattr'       : [
            ['Min', 'vector3'],
            ['Max', 'vector3'],
            ['FrontOrPoly0', 'uint32'],
            ['BackOrPolyCount', 'uint32']
        ]
    },
    {
        'tag'           : 'hierarchy',
        'id'            : 0x00000100,
        'container'     : True
    },
    {
        'tag'           : 'hierarchy_header',
        'id'            : 0x00000101,
        'attr'          : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['NumPivots', 'uint32'],
            ['Center', 'vector3']
        ]
    },
    {
        'tag'           : 'pivots',
        'id'            : 0x00000102,
        'subtag'        : 'pivot',
        'subattr'       : [
            ['Name', 'name'],
            ['ParentIdx', 'uint32'],
            ['Translation', 'vector3'],
            ['EulerAngles', 'vector3'],
            ['Rotation', 'quaternion']
        ]
    },
    {
        'tag'           : 'pivot_fixups',
        'id'            : 0x00000103,
        'subtag'        : 'matrix3x4',
        'subattr'       : [
            ['', 'float32', 12]
        ]
    },
    {
        'tag'           : 'animation',
        'id'            : 0x00000200,
        'container'     : True,
    },
    {
        'tag'           : 'animation_header',
        'id'            : 0x00000201,
        'attr'          : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['HierarchyName', 'name'],
            ['NumFrames', 'uint32'],
            ['FrameRate', 'uint32']
        ]
    },
    {
        'tag'           : 'animation_channel',
        'id'            : 0x00000202,
        'attr'          : [
            ['FirstFrame', 'uint16'],
            ['LastFrame', 'uint16'],
            ['VectorLen', 'uint16'],
            ['Flags', 'uint16'],
            ['Pivot', 'uint16'],
            ['_padding', 'uint16']
        ],
        'subtag'        : 'data',
        'subattr'       : [
            ['', 'float32'],
        ]
    },
    {
        'tag'           : 'bit_channel',
        'id'            : 0x00000203,
        'attr'          : [
            ['FirstFrame', 'uint16'],
            ['LastFrame', 'uint16'],
            ['Flags', 'uint16'],
            ['Pivot', 'uint16'],
            ['DefaultVal', 'uint8']
        ],
        'subtag'        : 'data',
        'subattr'       : [
            ['', 'uint8'],
        ]
    },
    {
        'tag'           : 'compressed_animation',
        'id'            : 0x00000280,
        'container'     : True,
    },
    {
        'tag'           : 'compressed_animation_header',
        'id'            : 0x00000281,
        'attr'          : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['HierarchyName', 'name'],
            ['NumFrames', 'uint32'],
            ['FrameRate', 'uint16'],
            ['Flavor', 'uint16'],
        ]
    },
    {
        'tag'           : 'compressed_animation_channel',
        'id'            : 0x00000282,
        'unimplemented' : True,
    },
    {
        'tag'           : 'compressed_bit_channel',
        'id'            : 0x00000283,
        'unimplemented' : True,
    },
    {
        'tag'           : 'morph_animation',
        'id'            : 0x000002C0,
        'container'     : True
    },
    {
        'tag'           : 'morphanim_header',
        'id'            : 0x000002C1,
        'attr'          : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['HierarchyName', 'name'],
            ['FrameCount', 'uint32'],
            ['FrameRate', 'float32'],
            ['ChannelCount', 'uint32']
        ]
    },
    {
        'tag'           : 'morphanim_channel',
        'id'            : 0x000002C2,
        'container'     : True
    },
    {
        'tag'           : 'morphanim_posename',
        'id'            : 0x000002C3,
        'attr'          : [['', 'string']]
    },
    {
        'tag'           : 'morphanim_keydata',
        'id'            : 0x000002C4,
        'subtag'        : 'key',
        'subattr'       : [
            ['MorphFrame', 'uint32'],
            ['PoseFrame', 'uint32'],
        ]
    },
    {
        'tag'           : 'morphanim_pivotchanneldata',
        'id'            : 0x000002C5,
        'subtag'        : 'channel',
        'subattr'       : [
            ['', 'uint32']
        ]
    },
    {
        'tag'           : 'hmodel',
        'id'            : 0x00000300,
        'container'     : True,
    },
    {
        'tag'           : 'hmodel_header',
        'id'            : 0x00000301,
        'attr'          : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['HierarchyName', 'name'],
            ['NumConnections', 'uint16']
        ]
    },
    {
        'tag'           : 'node',
        'id'            : 0x00000302,
        'attr'          : [
            ['RenderObjName', 'name'],
            ['PivotIdx', 'uint16']
        ]
    },
    {
        'tag'           : 'collision_node',
        'id'            : 0x00000303,
        'attr'          : [
            ['RenderObjName', 'name'],
            ['PivotIdx', 'uint16']
        ]
    },
    {
        'tag'           : 'skin_node',
        'id'            : 0x00000304,
        'attr'          : [
            ['RenderObjName', 'name'],
            ['PivotIdx', 'uint16']
        ]
    },
    {
        'tag'           : 'obsolete_w3d_chunk_hmodel_aux_data',
        'id'            : 0x00000305,
        'unimplemented' : True,
    },
    {
        'tag'           : 'obsolete_w3d_chunk_shadow_node',
        'id'            : 0x00000306,
        'unimplemented' : True,
    },
    {
        'tag'           : 'lodmodel',
        'id'            : 0x00000400,
        'container'     : True,
    },
    {
        'tag'           : 'lodmodel_header',
        'id'            : 0x00000401,
        'unimplemented' : True,
    },
    {
        'tag'           : 'lod',
        'id'            : 0x00000402,
        'unimplemented' : True,
    },
    {
        'tag'           : 'collection',
        'id'            : 0x00000420,
        'container'     : True,
    },
    {
        'tag'           : 'collection_header',
        'id'            : 0x00000421,
        'unimplemented' : True,
    },
    {
        'tag'           : 'collection_obj_name',
        'id'            : 0x00000422,
        'attr'          : [['', 'string']]
    },
    {
        'tag'           : 'placeholder',
        'id'            : 0x00000423,
        'unimplemented' : True,
    },
    {
        'tag'           : 'transform_node',
        'id'            : 0x00000424,
        'unimplemented' : True,
    },
    {
        'tag'           : 'points',
        'id'            : 0x00000440,
        'subtag'        : 'point',
        'subattr'       : [['', 'vector3']]
    },
    {
        'tag'           : 'light',
        'id'            : 0x00000460,
        'container'     : True,
    },
    {
        'tag'           : 'light_info',
        'id'            : 0x00000461,
        'attr'          : [
            ['Attributes', 'uint32'],
            ['_unused', 'uint32'],
            ['Ambient', 'rgb'],
            ['Diffuse', 'rgb'],
            ['Specular', 'rgb'],
            ['Intensity', 'float32']
        ]
    },
    {
        'tag'           : 'spot_light_info',
        'id'            : 0x00000462,
        'attr'          : [
            ['SpotAngle', 'float32'],
            ['SpotExponent', 'float32']
        ]
    },
    {
        'tag'           : 'near_attenuation',
        'id'            : 0x00000463,
        'attr'          : [
            ['Start', 'float32'],
            ['End', 'float32']
        ]
    },
    {
        'tag'           : 'far_attenuation',
        'id'            : 0x00000464,
        'attr'          : [
            ['Start', 'float32'],
            ['End', 'float32']
        ]
    },
    {
        'tag'           : 'emitter',
        'id'            : 0x00000500,
        'container'     : True,
    },
    {
        'tag'           : 'emitter_header',
        'id'            : 0x00000501,
        'attr'          : [
            ['Version', 'version'],
            ['Name', 'name']
        ]
    },
    {
        'tag'           : 'emitter_user_data',
        'id'            : 0x00000502,
        'attr'          : [
            ['Type', 'uint32'],
            ['SizeofStringParam', 'uint32'],
            ['StringParam', 'string']
        ]
    },
    {
        'tag'           : 'emitter_info',
        'id'            : 0x00000503,
        'attr'          : [
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
        'tag'           : 'emitter_infov2',
        'id'            : 0x00000504,
        'attr'          : [
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
        'tag'           : 'emitter_props',
        'id'            : 0x00000505,
        'attr'          : [
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
        'tag'           : 'obsolete_w3d_chunk_emitter_color_keyframe',
        'id'            : 0x00000506,
        'attr'          : [
            ['Time', 'float32'],
            ['Color', 'rgba']
        ]
    },
    {
        'tag'           : 'obsolete_w3d_chunk_emitter_opacity_keyframe',
        'id'            : 0x00000507,
        'attr'          : [
            ['Time', 'float32'],
            ['Opacity', 'float32']
        ]
    },
    {
        'tag'           : 'obsolete_w3d_chunk_emitter_size_keyframe',
        'id'            : 0x00000508,
        'attr'          : [
            ['Time', 'float32'],
            ['Size', 'float32']
        ]
    },
    {
        'tag'           : 'emitter_line_properties',
        'id'            : 0x00000509,
        'attr'          : [
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
        'tag'           : 'emitter_rotation_keyframes',
        'id'            : 0x0000050A,
        'attr'          : [
            ['KeyframeCount', 'uint32'],
            ['Random', 'float32'],
            ['OrientationRandom', 'float32'],
            ['_reserved', 'uint32'],
        ],
        'subtag'        : 'keyframe',
        'subattr'       : [
            ['Time', 'float32'],
            ['Rotation', 'float32']
        ]
    },
    {
        'tag'           : 'emitter_frame_keyframes',
        'id'            : 0x0000050B,
        'attr'          : [
            ['KeyframeCount', 'uint32'],
            ['Random', 'float32'],
            ['_reserved', 'uint32', 2],
        ],
        'subtag'        : 'keyframe',
        'subattr'       : [
            ['Time', 'float32'],
            ['Frame', 'float32']
        ]
    },
    {
        'tag'           : 'emitter_blur_time_keyframes',
        'id'            : 0x0000050C,
        'attr'          : [
            ['KeyframeCount', 'uint32'],
            ['Random', 'float32'],
            ['_reserved', 'uint32'],
        ],
        'subtag'        : 'keyframe',
        'subattr'       : [
            ['Time', 'float32'],
            ['BlurTime', 'float32']
        ]
    },
    {
        'tag'           : 'aggregate',
        'id'            : 0x00000600,
        'container'     : True
    },
    {
        'tag'           : 'aggregate_header',
        'id'            : 0x00000601,
        'attr'          : [
            ['Version', 'version'],
            ['Name', 'name']
        ],
        'container'     : True
    },
    {
        'tag'           : 'aggregate_info',
        'id'            : 0x00000602,
        'attr'          : [
            ['BaseModelName', 'name', 2],
            ['SubobjectCount', 'uint32']
        ],
        'subtag'        : 'subobject',
        'subattr'       : [
            ['SubobjectName', 'name', 2],
            ['BoneName', 'name', 2]
        ],
        
    },
    {
        'tag'           : 'texture_replacer_info',
        'id'            : 0x00000603,
        'unimplemented' : True,
    },
    {
        'tag'           : 'aggregate_class_info',
        'id'            : 0x00000604,
        'attr'          : [
            ['OriginalClassID', 'uint32'],
            ['Flags', 'uint32'],
            ['_reserved', 'uint32', 3],
        ]
    },
    {
        'tag'           : 'hlod',
        'id'            : 0x00000700,
        'container'     : True
    },
    {
        'tag'           : 'hlod_header',
        'id'            : 0x00000701,
        'attr'          : [
            ['Version', 'version'],
            ['LodCount', 'uint32'],
            ['Name', 'name'],
            ['HierarchyName', 'name']
        ]
    },
    {
        'tag'           : 'hlod_lod_array',
        'id'            : 0x00000702,
        'container'     : True
    },
    {
        'tag'           : 'hlod_sub_object_array_header',
        'id'            : 0x00000703,
        'attr'          : [
            ['ModelCount', 'uint32'],
            ['MaxScreenSize', 'float32']
        ]
    },
    {
        'tag'           : 'hlod_sub_object',
        'id'            : 0x00000704,
        'attr'          : [
            ['BoneIndex', 'uint32'],
            ['Name', 'name', 2]
        ]
    },
    {
        'tag'           : 'hlod_aggregate_array',
        'id'            : 0x00000705,
        'container'     : True
    },
    {
        'tag'           : 'hlod_proxy_array',
        'id'            : 0x00000706,
        'container'     : True
    },
    {
        'tag'           : 'box',
        'id'            : 0x00000740,
        'attr'          : [
            ['Version', 'version'],
            ['Attributes', 'uint32'],
            ['Name', 'name', 2],
            ['Color', 'rgb'],
            ['Center', 'vector3'],
            ['Extent', 'vector3']
        ]
    },
    {
        'tag'           : 'sphere',
        'id'            : 0x00000741,
        'attr'          : [
            ['Version', 'version'],
            ['Attributes', 'uint32'],
            ['Name', 'name', 2],
            ['Color', 'rgb'],
            ['Center', 'vector3'],
            ['Extent', 'vector3']
        ]
    },
    {
        'tag'           : 'ring',
        'id'            : 0x00000742,
        'attr'          : [
            ['Version', 'version'],
            ['Attributes', 'uint32'],
            ['Name', 'name', 2],
            ['Color', 'rgb'],
            ['Center', 'vector3'],
            ['Extent', 'vector3']
        ]
    },
    {
        'tag'           : 'null_object',
        'id'            : 0x00000750,
        'attr'          : [
            ['Version', 'version'],
            ['Attributes', 'uint32'],
            ['_padding', 'uint32', 2],
            ['Name', 'name', 2]
        ]
    },
    {
        'tag'           : 'lightscape',
        'id'            : 0x00000800,
        'container'     : True
    },
    {
        'tag'           : 'lightscape_light',
        'id'            : 0x00000801,
        'container'     : True,
    },
    {
        'tag'           : 'light_transform',
        'id'            : 0x00000802,
        'attr'          : [['matrix4x3', 'float32', 12]]
    },
    {
        'tag'           : 'dazzle',
        'id'            : 0x00000900,
        'container'     : True
    },
    {
        'tag'           : 'dazzle_name',
        'id'            : 0x00000901,
        'attr'          : [['', 'string']]
    },
    {
        'tag'           : 'dazzle_typename',
        'id'            : 0x00000902,
        'attr'          : [['', 'string']]
    },
    {
        'tag'           : 'soundrobj',
        'id'            : 0x00000A00,
        'container'     : True
    },
    {
        'tag'           : 'soundrobj_header',
        'id'            : 0x00000A01,
        'attr'          : [
            ['Version', 'version'],
            ['Name', 'name'],
            ['Flags', 'uint32'],
            ['_padding', 'uint32', 8]
        ]
    },
    {
        'tag'           : 'soundrobj_definition',
        'id'            : 0x00000A02,
        'unimplemented' : True,
    },
    {
        'tag'           : 'secondary_vertices',
        'id'            : 0x00000C00,
        'subtag'        : 'vertex',
        'subattr'       : [['', 'vector3']]
    },
    {
        'tag'           : 'secondary_normals',
        'id'            : 0x00000C01,
        'subtag'        : 'normal',
        'subattr'       : [['', 'vector3']]
    },
]