#OKOLO lika crta tor sa travom unutar ograde

from mc import * #import api-ja
from crtanje import *	
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def tor (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 ):
   """
   funkcija za crtanje vrta oko lika
   """
   
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   crtaj_kvadar ( orMj , ( -10 , -10 , -1 )  , ( 10 , 10 , -1  ) , orSm , 2 , 0 ) #temelji od grasslanda
   crtaj_kvadar ( orMj , ( -10 , -10 , 0 )  , ( 10 , 10 , 0  ) , orSm , 189 , 0 ) #fence   
   crtaj_kvadar ( orMj , ( -9 , -9 , 0 )  , ( 9 , 9 , 0  ) , orSm , 0 , 0 ) #air   



   return 1
   
   
   
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   tor (  orMj ,  orSm , iX=0 , iZ=0 , iY=0 )
