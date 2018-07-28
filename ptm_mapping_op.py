import bpy
from bpy.types import Operator
 
class PTM_MappingOperator(Operator):
    bl_idname = "object.ptm_mapping_op"
    bl_label = "Map textures"
    bl_description = "Connect PBR textures to the Principled shader" 
    bl_options = {'REGISTER', 'UNDO'} 
    
    def add_link(self, tree, node, node2, output_name, input_name, non_color_data = False):
        
        tree.links.new(node.outputs[output_name], node2.inputs[input_name])
        
        if(hasattr(node, "color_space")):
            if(non_color_data):
                node.color_space = "NONE"
            else:
                node.color_space = "COLOR"
    
    def create_normal_map(self, tree):
        return tree.nodes.new('ShaderNodeNormalMap')
             
    def execute(self, context):
        
        tree = context.space_data.node_tree
        
        shader_nodes  = [n for n in tree.nodes if n.type == "BSDF_PRINCIPLED"]
        
        texture_nodes = [n for n in tree.nodes if n.type == "TEX_IMAGE"]
        
        if(len(shader_nodes) == 0 or len(texture_nodes) == 0):
            return {'CANCELLED'} 
        
        shader_node = shader_nodes[0] 
            
        for node in texture_nodes:
            
            lower_name = node.image.name.lower()
            
            if any(name in lower_name for name in ["diffuse", "albedo"]):            
                self.add_link(tree, node, shader_node, "Color", "Base Color")
                
            elif("metallic" in lower_name):
                self.add_link(tree, node, shader_node, "Color", "Metallic", True)
                
            elif("roughness" in lower_name):
                self.add_link(tree, node, shader_node, "Color", "Roughness", True)
                   
            elif("normal" in lower_name):
                
                if(len(node.outputs["Color"].links) == 0):
                    
                    normal_node = self.create_normal_map(tree)
                    
                    self.add_link(tree, node, normal_node, "Color", "Color", True)
                    self.add_link(tree, normal_node, shader_node, "Normal", "Normal")
                
        return {'FINISHED'}