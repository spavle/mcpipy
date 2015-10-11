#ispred lika soba 11 x 11

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def katakombe ( orMjL ,  orSm ,iX=0 , iZ=0 , iY=0 ,  materijal = 98, dv = 0 , stepenice_mat = 109):
   #ishodiste je u sredini
   orMjL = premjesti_origin ( orMjL , iX  , iZ , iY ,  orSm ) #centar , stup u sredini 
   filter ( orMjL , ( -6 , 0 , 0 ) , orSm ,  visina = 8 ,   sirina = 5 , dubina = 11, baklje="ne") 
   #strop
   crtaj_kvadar ( orMjL , (-5,-5,6)  , (5,5,6) , orSm , materijal , dv ) 
   #podesti
   crtaj_kvadar ( orMjL , (-1,-1,0)  , (1,1,0) , orSm , 44 , 0 ) 
   #stup
   crtaj_kvadar ( orMjL , (0,0,1)  , (0,0,3) , orSm , materijal , dv ) 
   #doljnja lampa
   crtaj_kvadar ( orMjL , (0,0,0)  , (0,0,0) , orSm , 89 , 0 ) 
   #gornja lampa
   crtaj_kvadar ( orMjL , (0,0,4)  , (0,0,4) , orSm , 89 , 0 ) 
   #vijenci
   crtaj_stepenice ( orMjL , (1,-1,5) , (1,1,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "odmene" , gore_dolje = "da"  )
   crtaj_stepenice ( orMjL , (-1,-1,5) , (-1,1,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "meni" , gore_dolje = "da"  )
   crtaj_stepenice ( orMjL , (0,-1,5) , (0,-1,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "lijevo" , gore_dolje = "da"  )       
   crtaj_stepenice ( orMjL , (0,1,5) , (0,1,5) , orSm , blok_id = stepenice_mat , rel_smjer  = "desno" , gore_dolje = "da"  ) 
   
   #stropne lampe
   crtaj_kvadar ( orMjL , (-5,0,6)  , (-5,0,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (5,0,6)  , (5,0,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (-5,0,6)  , (-5,0,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (0,5,6)  , (0,5,6) , orSm , 89 , 0 )
   
 
if __name__ == "__main__":    #direktan poziv
   #katakombe (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   for dX in range (0,50,11):
      for dZ in range ( -44 , 46 , 11 ):
         katakombe ( orMj ,  orSm ,  iX=6 + dX, iZ=dZ , iY=0 ) 