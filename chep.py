#ispred lika radi chep 3x3 i dugacak 9

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def chep ():
   """
   funkcija za crtanje chepa od pjeska dimenzija 9x3x3 neposredno ispred lika
   crta chep samo gdje je zrak
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
      for dZ in  range( -1 , 2 ) :    		# prodji chep
         for dY  in ( 0 , 1 , 2 ) : 
            for dX in ( 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               if mc.getBlock ( gdjeX , gdjeY , gdjeZ ) == AIR.id :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , SAND)			#postavi blok
               #mc.postToChat("gdjeX: %f gdjeY: %f gdjeZ: %f " % ( gdjeX , gdjeY , gdjeZ  ) )
   #mc.postToChat("X: %f Y: %f Z: %f " % ( radnaPozicija.x , radnaPozicija.y , radnaPozicija.z  ) )
   return 1
   
chep ()