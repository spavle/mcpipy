#ispred lika crta more baklji po tlu

import time
from mc import * #import api-ja
from crtanje import *		#tu je funkcija koju zovem
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


def bakljada ():
   """
   ispred lika cisti pravokutnik  3x4 i dugacak 9 i to samo blokove iz liste zaMaknuti
   """
   #dimenzije = 150     #za jake PC-e
   dimenzije = 100   # za slabe PC-e
   #gdje sam
   orMj = gdjeSam ()
   orSm = gdjeGledam ()

   
   for dX in  range( -dimenzije , dimenzije , 5 ):
      for dZ in  range( -dimenzije , dimenzije , 5 ):
         increment = 0
         while increment < 40 :
            gdje = rel2abs ( orMj ,  ( dX , dZ , 0 + increment )  , orSm  )
            kojiBlok = mc.getBlock ( gdje ) 
            if kojiBlok == AIR.id or kojiBlok == GRASS_TALL.id:
               mc.setBlock(gdje , TORCH.id , 5 )
               break
            increment += 1
 
   mc.postToChat("Kraj !!!" )
   return 1

   

bakljada ()