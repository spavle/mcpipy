#ispred lika cisti pravokutnik  3x4 i dugacak 9 i to samo blokove iz liste 

import time
from mc import * #import api-ja
from crtanje import *		#tu je funkcija koju zovem
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def bigBager ( orMj , orSm ,  dimenzije = 50 , visina = 20) :

   for dX in  range( -dimenzije , dimenzije + 1 ):
      for dZ in  range( -dimenzije , dimenzije + 1 ):
         increment = 0
         while increment < visina :
            gdje = rel2abs ( orMj ,  ( dX , dZ ,  increment )  , orSm  )
            mc.setBlock(gdje , AIR.id , 0 )
            increment += 1
      mc.postToChat("dX: %f " % dX )
 
   mc.postToChat("Kraj !!!" )
   return 1

   
 
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   bigBager ( orMj , orSm ,  dimenzije = 120 , visina = 50)   
