#kopa cilindricnu rupu do dna relativno pomaknutu u odnosu na lik

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def iskopajCilindar ( iX, iZ, iY ,radius = 6 ):
   """
   kopa cilindricnu rupu do dna relativno pomaknutu u odnosu na lik
   iX, - relativni pomak po X
   iZ, - relativni pomak po Z
   iY , - relativni pomak po Y
   radius radius rupe, default  6
   """
   #gdje sam i gdje gledam
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   #mc.postToChat("prvi origin: %s" % ( orMj ) )
    
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar cilindra
   #mc.postToChat("prvi origin: %s" % ( orMj ) )
   dubina = nadji_dno ( orMj , orMj , orSm )                #odredi dubinu do bedrocka
   #mc.postToChat("dubina: %f" % ( dubina ) )
   
   for dY in range ( 0 ,  dubina , -1 ):           #ide  sloj po sloj dolje
      #mc.postToChat("dubina: %f" % ( dY ) )
      for dX in range( - radius, radius + 1):
         for dZ in range( - radius, radius + 1):
            if dX**2 + dZ**2  < radius**2:  #kopati ili ne kopati
               gdje = rel2abs ( orMj ,  ( dX , dZ , dY )  , orSm  )  #relativne koordinate u apsolutne worlda
               mc.setBlock(gdje , AIR.id , 2 )                       # sve ide van
   return 1         
            
            
 
if __name__ == "__main__":    #direktan poziv
   iskopajCilindar ( 15, 0, 0 ,radius = 12 )

