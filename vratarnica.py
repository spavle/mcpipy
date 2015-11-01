# crta malu kucu sa puno vrata, u for petlju se stavi koliko kuca da crta

from mc import * #import api-ja
from crtanje import *	
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def vratarnica (  orMj ,  orSm , iX=8 , iZ=0 , iY=0 ):
   
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar
   
   crtaj_kvadar ( orMj , ( -2 , -2 , -1 )  , ( 2 , 2 , 0  ) , orSm , 98 , 0 ) #temelji od stomebricks
   crtaj_kvadar ( orMj , ( -2 , -2 , 1 )  , ( 2 , 2 , 2  ) , orSm , 5 , 2 ) #drveni zidovi
   crtaj_kvadar ( orMj , ( -1 , -1 , 0 )  , ( 1 , 1 , 1  ) , orSm , 0 , 0 ) #prazno unutra
   for dX in ( -2 , 2 ):
      for dZ in  ( -2 , 2 ):
         crtaj_kvadar ( orMj , ( dX , dZ , -1 )  , ( dX , dZ , 1  ) , orSm , 89 , 0 ) # svjetleci, glowstone, stupovi na uglovima
   crtaj_kvadar ( orMj , ( 0 , 0 , 2 )  , ( 0 , 0 , 2  ) , orSm , 89 , 0 ) # svjetleci, glowstone, lampa u sredini
   
   for br in ( -1 , 0 , 1 ):
      crtaj_vrata ( orMj , [ 2 , 0 + br , 0 ]   , orSm, "odmene"   , kvaka = "lijevo" , blok_id = 194 ) #vrata naprijed
      crtaj_vrata ( orMj , [ -2 , 0 + br , 0 ]   , orSm, "meni"   , kvaka = "lijevo" , blok_id = 194 ) #vrata pozadi
      crtaj_vrata ( orMj , [ 0 + br , -2 , 0 ]   , orSm, "lijevo"   , kvaka = "lijevo" , blok_id = 194 ) #vrata lijevo
      crtaj_vrata ( orMj , [ 0 + br , 2 , 0 ]   , orSm, "desno"   , kvaka = "lijevo" , blok_id = 194 ) #vrata desno
      
   
   return 1

  
if __name__ == "__main__":    #direktan poziv
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   vratarnica (  orMj ,  orSm , iX=8 , iZ=0 , iY=0 )
