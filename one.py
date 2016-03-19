from mc import * #Minecraft api import
from Position import * # clas for position
from cuboid import *
mc = Minecraft() #initialization

class Block (Cuboid):
    """
    class for creating one block
    """
    def __init__ ( self , block_position , material , material_modification = 0 ):
        """
        Block class initialization
        """
        self.draw ( block_position.x , block_position.y , block_position.z  , material , material_modification )
      
    def draw ( self , block_position_x , block_position_y , block_position_z  , material , material_modification ) :
        """
        create one  block
        """
        Cuboid.draw ( self , block_position_x , block_position_y , block_position_z , block_position_x , block_position_y , block_position_z , material , material_modification )
        
      
      

      
      
      
if __name__ == "__main__":    #direct call for testing purpose
    # TDD: self test code

      
    Block ( Position.relative_distance  ( 2 , 1 , -1 )   , 1 , 0 )
    
    pos = Position ()
    
    pos.rotate_left ()
    Block ( Position ( pos , 4 , 1 , -1 )   , 1 , 0 )
    pos.rotate_right ()
    pos.rotate_right ()
    Block ( Position ( pos , 4 , 2 , -1 )   , 1 , 0 )
    pos.rotate_right ()
    Block ( Position ( pos , 4 , 3 , -1 )   , 1 , 0 )
   