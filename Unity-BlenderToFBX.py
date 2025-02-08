import sys
argv = sys.argv
outfile = ' '.join(argv[argv.index("--") + 1:])

print("Starting blender to FBX conversion " + outfile)

import bpy.ops
bpy.ops.export_scene.fbx(
    filepath=outfile,
    check_existing=False,
    use_selection=False,
    use_active_collection=False,
    object_types={'ARMATURE','CAMERA','LIGHT','MESH','OTHER','EMPTY'},
    use_mesh_modifiers=True,
    mesh_smooth_type='OFF',
    use_custom_props=True,
    bake_anim_use_nla_strips=False,
    bake_anim_use_all_actions=False,
    apply_scale_options='FBX_SCALE_ALL',
    bake_space_transform=True
)

print("Finished blender to FBX conversion " + outfile)
