import bpy
from bpy.types import Panel

from . ptm_mapping_op import PTM_MappingOperator

class PTM_Panel(Panel):
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "TOOLS"
    bl_label = "Texture Mapping"
    bl_category = "PTM"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene

                                
        # Mapping operator
        row = layout.row()
        row.operator('object.ptm_mapping_op', text="Map textures", icon='MOD_BEVEL')
 