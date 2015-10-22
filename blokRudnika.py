#oko lika cisti pravokutnik  optimizirano za chunkUpdate i to samo blokove iz liste 

import time
from mc import * #import api-ja
from crtanje import *		#tu je funkcija koju zovem
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def blokRudnika ():
   """
   ispred lika cisti pravokutnik  3x4 i dugacak 9 i to samo blokove iz liste zaMaknuti
   """
   dimenzije = 150
   #gdje sam
   orMj = gdjeSam ()
   orSm = gdjeGledam ()

   #crtanje
   for dZ in  range( -dimenzije , dimenzije + 1 ) :    		# prodji cijeli pravokutnik
      for dX  in  range ( -dimenzije , dimenzije + 1 ) : 
         for dY in  range ( 7 , -1 , -1  ) :
            gdje = rel2abs ( orMj ,  ( dX , dZ , dY )  , orSm  ) # hodalica
            kojiBlok = mc.getBlock ( gdje ) # koji blok je tu
            if dY == 7 :
               if kojiBlok in zaMaknutiOpasno :
                  mc.setBlock(gdje , STONE.id , 2 )	               
            else:
               if kojiBlok in zaMaknuti :
                  mc.setBlock(gdje , AIR.id)			#postavi blok
               if dY == 0 and (int ( dX ) % 7  == 0)  and ( int ( dZ ) % 7 ) == 0 :
                  gdje = rel2abs ( orMj ,  ( dX , dZ , dY )  , orSm  ) # hodalica
                  kojiBlok = mc.getBlock ( gdje )
                  if kojiBlok == AIR.id :
                     mc.setBlock( gdje , TORCH.id , 5 )
      mc.postToChat("dZ: %f" % ( dZ ) )
      time.sleep ( 1 )
   """
   for dX in ( -dimenzije , dimenzije , 7 ):
      for dZ in ( -dimenzije , dimenzije , 7 ):
         gdje = rel2abs ( orMj ,  ( dX , dZ , 0 )  , orSm  )
         kojiBlok = mc.getBlock ( gdje ) 
         if kojiBlok == AIR.id :
            mc.setBlock(gdje , TORCH.id , 5 )
   """
   mc.postToChat("Kraj !!!" )
   return 1

   
   
zaMaknuti = [ SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id ,  WATER_FLOWING.id, WATER_STATIONARY.id , LAVA_STATIONARY.id, LAVA_FLOWING.id ]
zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , SAND.id , GRAVEL.id ] # Dodani shljunak i pjesak jer padanja sve poremete

blokRudnika ()