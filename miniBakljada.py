#ispred lika crta more baklji po tlu

import time
from mc import * #import api-ja
from crtanje import *		#tu je funkcija koju zovem
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

zaStaviti = [ GRASS.id , SANDSTONE.id , SAND.id , STONE.id , DIRT.id , GRAVEL.id , COBBLESTONE.id , CLAY.id , FENCE.id , STONE_BRICK.id ,  17 , 162 , 5  , 78 ] # 17 , 162 wood 5 wood planks 78 snow_layer

def miniBakljada (  orMj , orSm ,  dimenzije = 30 , visina = 10 ):
   
   for dX in  range( -dimenzije , dimenzije + 1, 5 ):
      for dZ in  range( -dimenzije , dimenzije + 1, 5 ):

         increment = -2

         while increment < visina :
            gdje = rel2abs ( orMj ,  ( dX , dZ , -10 + increment )  , orSm  )
            kojiBlok = mc.getBlock ( gdje ) 
            if increment > -2 :
               if kojiBlok == AIR.id or kojiBlok == 31 or kojiBlok == 175 or kojiBlok == SNOW.id :
                  if kojiBlokIspod in zaStaviti :
                     mc.setBlock(gdje , TORCH.id , 5 )
            increment += 1
            kojiBlokIspod = kojiBlok
      mc.postToChat("dX: %f " % dX )
 
   mc.postToChat("Kraj !!!" )
   return 2
   
if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   miniBakljada ( orMj , orSm ,  dimenzije = 60 , visina = 20)   
   #bakljada (dimenzije = 200 , visina = 80)   