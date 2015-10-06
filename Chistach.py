#ispred lika cisti pravokutnik  3x4 i dugacak 9 i to samo blokove iz liste 

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def chistach ():
   """
   ispred lika cisti pravokutnik  3x4 i dugacak 9 i to samo blokove iz liste zaMaknuti
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
      for dZ in  range( -1 , 2 ) :    		# prodji cijeli pravokutnik
         for dY  in  range ( 0 , 9 ) : 
            for dX in  range ( 1 , 9  ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY						# pomak po y
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               if  mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknuti :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR.id)			#postavi blok
   return 1

   
   
zaMaknuti = [ SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER_STATIONARY.id]

chistach ()