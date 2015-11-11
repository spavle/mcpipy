#ispred lika radi dirt samo na mjestima gdje je stone i gravel 3 sirine i dugacak 9

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def travnjak ():
   """
   ispred lika radi dirt samo na mjestima gdje je stone i gravel 3 sirine i dugacak 9
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
      for dZ in  range ( -44 , 44 ) :    		# prodji shirinu
         for dY  in  range( -2 ,0 ) : 			#samo jedan level ispod
            for dX in  range ( -44 , 44 ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY						# pomak po y
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               mc.setBlock(gdjeX , gdjeY , gdjeZ , GRASS )					#postavi zemlju 
               mc.postToChat("gdjeX: %f gdjeY: %f gdjeZ: %f " % ( gdjeX , gdjeY , gdjeZ  ) )
   #mc.postToChat("X: %f Y: %f Z: %f " % ( radnaPozicija.x , radnaPozicija.y , radnaPozicija.z  ) )
   return 1
   
travnjak ()
