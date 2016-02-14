from mc import * #Minecraft api import
mc = Minecraft() #initialization
"""
Class for storing and manipulating coordintes in Minecraft 
-x
-y
-z
-direction

__init__
move
copy
rotate_left
rotate_right
real_coords
origin
"""


class Position ( object ):


   def __init__ (self, input=None , dX=None, dY=None, dZ=None ) :

      if input != None :
         self.x = input.x
         self.y = input.y
         self.z = input.z
         self.x_direction = input.x_direction
         self.z_direction = input.z_direction
      else:
         self.get_origin ()

      if dX :
         self.x += dX
      if dY :
         self.y += dY
      if dZ :
         self.z += dZ
   
   
   def get_origin ( self ):
   
      current_position = mc.player.getPos()	#coordinates
      self.x = current_position.x
      self.y = current_position.y
      self.z = current_position.z
      
      current_direction = mc.player.getDirection () #directions
      self.x_direction = 0
      self.z_direction = 0
      if abs (current_direction.x) > abs (current_direction.z): 		#nadje se dominanti smjer i spremi u vektor
         self.x_direction=round(current_direction.x)
      else:
         self.z_direction=round(current_direction.z)  
   


if __name__ == "__main__":    #direct call for testing purpose
   # self test code
   first = Position ()
   print first.x
   first.x = 2
   first.y = 3
   first.z = 4
   second = Position ( first )
   print second.x
   third = Position ( second , 2 , 3 , 4 )
   print third.x