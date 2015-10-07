# BUGOVITO NERADI

import time 
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

  
def ubij_ispod (pos) :
   mc.setBlock(pos.x  , pos.y - 1 , pos.z , AIR.id  )
   return
  
def go_south ( koliko , pomak ) :
   for brojalica in range ( 0 , koliko + 1 ):
      mc.postToChat("brojalica : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.setBlock(pos.x - pomak , 109 , pos.z  , STONE.id)
      time.sleep ( 3 )
      ubij_ispod ( pos )
      mc.player.setPos(pos.x - pomak , 110 , pos.z)
      time.sleep ( 3 )
      
      
def go_west ( koliko , pomak ) :
   for brojalica in range ( 0 , koliko + 1 ):
      mc.postToChat("brojalica : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.setBlock(pos.x  , 109 , pos.z - pomak , STONE.id )
      time.sleep ( 3 )
      ubij_ispod ( pos )
      mc.player.setPos(pos.x  , 110 , pos.z - pomak)
      time.sleep ( 3 )
      
      
def go_north ( koliko , pomak ) :
   for brojalica in range ( 0 , koliko + 1 ):
      mc.postToChat("brojalica : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.setBlock(pos.x + pomak , 109 , pos.z , STONE.id )
      time.sleep ( 3 )
      ubij_ispod ( pos )
      mc.player.setPos(pos.x + pomak , 110 , pos.z)
      time.sleep ( 3 )
      
def go_east ( koliko , pomak ) :
   for brojalica in range (  0 , koliko + 1  ):
      mc.postToChat("brojalica : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.setBlock(pos.x  , 109 , pos.z + pomak , STONE.id )
      time.sleep ( 3 )
      ubij_ispod ( pos )
      mc.player.setPos(pos.x  , 110 , pos.z + pomak)
      time.sleep ( 3 )
      
korak = 50
pocetak =  mc.player.getTilePos()
for krug in range ( 2 , 250 , 2) :
   mc.postToChat("krug : %f " % ( krug  ) )
   go_south ( 1 , korak )
   go_west ((int ( krug / 2 ) + 1 ) , korak )
   go_north ( krug + 1 , korak )
   go_east ( (int ( krug / 2 ) + 1 ) , korak )
   go_east ( (int ( krug / 2 ) + 1 ) , korak )
   go_south ( krug +1 , korak )
   go_west (( int ( krug / 2 + 1 ) ) , korak )
   
mc.player.setPos( pocetak.x ,  pocetak.y ,  pocetak.z )

