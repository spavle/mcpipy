from mc import * #Minecraft api import
mc = Minecraft() #initialization



class Position ( object ):
    """
    Class for storing and manipulating coordintes in Minecraft 
    - x
    - y
    - z
    - x_direction
    - z_direction

    __init__
    move ?
    copy ?
    rotate_left
    rotate_right
    origin
    """

    def __init__ (self, input=None , dX=0, dY=0, dZ=0 ) :
        """ 
        Position initialization
        """
        if input != None :
            self.x = input.x
            self.y = input.y
            self.z = input.z
            self.x_direction = input.x_direction
            self.z_direction = input.z_direction
        else:
            self.get_origin ()


        print self.x
        print self.x_direction
        print dX
        self.x=self.x + self.x_direction*dX - self.z_direction*dZ    		# x translate
        self.z=self.z + self.x_direction*dZ + self.z_direction*dX			# y translate
        self.y = self.y + dY                                              # z translate

   
    def get_origin ( self ):
        """
        get current position and direction
        """
        current_position = mc.player.getPos()	#get coordinates
        self.x = current_position.x
        self.y = current_position.y
        self.z = current_position.z
      
        current_direction = mc.player.getDirection () #get direction
        self.x_direction = 0
        self.z_direction = 0
        if abs (current_direction.x) >= abs (current_direction.z): 		#find dominant direction
            self.x_direction=int(round(current_direction.x))
        else:
            self.z_direction=int(round(current_direction.z))  
   
    def rotate_left (self):
        """
        rotate direction to left
        """
        convert = {}
        convert [ ( 1 , 0  ) ] = (  0 , -1  ) # look north
        convert [ ( -1 , 0 ) ] = (  0 , 1 ) # look south
        convert [ ( 0 , 1 ) ] = (  1 , 0 )  # look east
        convert [ ( 0 , -1 ) ]= (  -1 , 0 )  # look weast
        buff = convert [ ( self.x_direction , self.z_direction )   ]
        self.x_direction=buff [0]
        self.z_direction=buff [1]
      
    def rotate_right (self):
        """
        rotate direction to right
        """
        convert = {}
        convert [ ( 1 , 0  ) ] = (  0 , 1  ) # look north
        convert [ ( -1 , 0 ) ] = (  0 , -1 ) # look south
        convert [ ( 0 , 1 ) ] = (  -1 , 0 )  # look east
        convert [ ( 0 , -1 ) ] = (  1 , 0 )  # look weast
        buff = convert [ ( self.x_direction , self.z_direction )   ]
        self.x_direction=buff [0]
        self.z_direction=buff [1]      
   
   
    @classmethod
    def origin (cls):
        """
        get toon position to object
        """
        return cls ()
      
    @classmethod
    def relative_distance (cls,dX,dY,dZ):
        """
        toon position + relative move
        """
        return cls (None,dX,dY,dZ)      


if __name__ == "__main__":    #direct call for testing purpose
    # TDD: self test code
    first = Position ()
    print first.x
    print first.x_direction
    print first.z_direction
    first.x = 2
    first.y = 3
    first.z = 4
    second = Position ( first )
    print second.x
    third = Position ( second , 2 , 3 , 4 )
    print third.x
    where_i_am = Position.origin ()
    print where_i_am.x
    where_is_house = Position.relative_distance (2,2,2)
    print where_is_house.x