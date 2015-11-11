#ispred lika cisti pravokutnik  3x4 i dugacak 9 i to samo blokove iz liste 

import time
from mc import * #import api-ja
from crtanje import *		#tu je funkcija koju zovem
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def bigBager ( orMj , orSm ,  dimenzije = 50 , visina = 20) :

   for dX in  range( -dimenzije , dimenzije + 1 ):
      for dZ in  range( -dimenzije , dimenzije + 1 ):
 
         gdje = rel2abs ( orMj ,  ( dX , dZ ,  0 )  , orSm  )
         gdje2 = rel2abs ( orMj ,  ( dX , dZ , - visina )  , orSm  )
         mc.setBlocks(gdje , gdje2 , AIR.id , 0 )
 
      mc.postToChat("dX: %f " % dX )
 
   mc.postToChat("Kraj !!!" )
   return 1

   
 
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   bigBager ( orMj , orSm ,  dimenzije = 280 , visina = 70)   
