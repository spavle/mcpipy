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

      if dX :
         self.x += dX
      if dY :
         self.y += dY
      if dZ :
         self.z += dZ
   



if __name__ == "__main__":    #direct call for testing purpose
   # self test code
   first = Position ()
   first.x = 2
   first.y = 3
   first.z = 4
   second = Position ( first )
   print second.x
   third = Position ( second , 2 , 3 , 4 )
   print third.x