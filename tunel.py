#ispred lika cisti pravokutnik  i to samo blokove iz liste pod i strop QUARTZ & QUARTZ - HARDCODED & LOSHE

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def tunel ():
   """
   ispred lika cisti pravokutnik  i to samo blokove iz liste pod i strop QUARTZ & QUARTZ
   """
   #gdje sam
   radnaPozicija = mc.player.getPos()		
   #kamo gledam
   smjerRada = mc.player.getDirection ()			#uzmem kamo gledam
   #smjer gledanja radi preglednosti spremimo u "vektor""
   Vx=0												#pocetne vrijednosti su nule
   Vz=0
   if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
      Vx=round(smjerRada.x)
   else:
      Vz=round(smjerRada.z)
   #mc.postToChat("vX: %f vZ: %f " % ( Vx , Vz  ) )

   #crtanje
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dZ in  range( -13 , 14 ) :    		# prodji cijeli pravokutnik
         for dY  in  range ( -3 , 9 ) : 
            for dX in  range ( -1 , 183  ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               if mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknutiOpasno :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , STONE.id , 2 )			#postavi blok      

   for dZ in  range( -11 , 12 ) :    		# prodji cijeli pravokutnik
         for dY  in  range ( -1 , 8 ) : 
            for dX in  range ( 1 , 181  ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               if  ( dY != 7 ) and ( dY != -1 ) and ( mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknuti ) :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR)			#postavi blok
               
               if  ( dY == -1 ) or ( dY == 7) :
                  if (abs (dX) % 3) == 0  and ( abs (dZ) % 3 ) == 0 :
                     mc.setBlock( gdjeX , gdjeY , gdjeZ , 89 )		#u podlogu obavezno stavi glowstone
                     #mc.setBlock(gdjeX , gdjeY , gdjeZ , 155 , 0)			#postavi blok
                  else :
                     mc.setBlock(gdjeX , gdjeY , gdjeZ , 155 , 1)			#postavi blok
               
   return 1

   
   
zaMaknuti = [ SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER.id , LAVA_FLOWING.id , LAVA.id ]
zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id , SAND.id , GRAVEL.id ] # Dodani shljunak i pjesak jer padanje sve poremete
 
tunel ()