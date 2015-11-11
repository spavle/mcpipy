#ispred lika vrt
#ispred lika vrt

from mc import * #import api-ja
from crtanje import *	
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def vrt (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ):
   """
   funkcija za crtanje vrta oko lika
   """
   
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   crtaj_kvadar ( orMj , ( -5 , -5 , 0 )  , ( 5 , 5 , 0  ) , orSm , 98 , 0 ) #temelji od stomebricks
   crtaj_kvadar ( orMj , ( -4 , -4 , 0 )  , ( 4 , 4 , 0  ) , orSm , 60 , 0 ) #farmland

   crtaj_kvadar ( orMj , ( -4 , -4 , 1 )  , ( 4 , -2 , 1  ) , orSm , 59 , 0 ) #wheat   
   crtaj_kvadar ( orMj , ( -4 , -1 , 1 )  , ( 4 , 1 , 1  ) , orSm , 141 , 0 ) #carrot   
   crtaj_kvadar ( orMj , ( -4 , 2 , 1 )  , ( 4 , 4 , 1  ) , orSm , 142 , 0 ) #potato     
   
   crtaj_kvadar ( orMj , ( 0 , 0 , 0 )  , ( 0 , 0 , 0  ) , orSm , 9 , 0 ) #voda
   crtaj_kvadar ( orMj , ( 0 , 0 , 1 )  , ( 0 , 0 , 1  ) , orSm , 89 , 0 ) #glowstone lampa iznad vode


   return 1
   
   
   
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   vrt (  orMj ,  orSm , iX=8 , iZ=0 , iY=0 )
