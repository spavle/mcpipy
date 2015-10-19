#ispred lika soba 11 x 11

from crtanje import *		#tu je funkcija koju zovem
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def katakombe ( orMjL ,  orSm ,iX=0 , iZ=0 , iY=0 ,  materijal = 98, dv = 0 , stepenice_mat = 109):
   #ishodiste je u sredini
   orMjL = premjesti_origin ( orMjL , iX  , iZ , iY ,  orSm ) #centar , stup u sredini 
   filter ( orMjL , ( -11 , 0 , 0 ) , orSm ,  visina = 8 ,   sirina = 10 , dubina = 21, baklje="ne") 
   #strop
   crtaj_kvadar ( orMjL , (-10,-10,6)  , (10,10,6) , orSm , materijal , dv ) 
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
   crtaj_kvadar ( orMjL , (-9,0,6)  , (-9,0,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (9,0,6)  , (9,0,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (0,-9,6)  , (0,-9,6) , orSm , 89 , 0 )
   crtaj_kvadar ( orMjL , (0,9,6)  , (0,9,6) , orSm , 89 , 0 )
   
   #baklje na podu
   for dX in ( 5 , 10 , 15 ):
      for dZ in ( -5 , 0 , 5):
         gdje = rel2abs ( orMjL ,  ( dX , dZ , 0 )  , orSm  )
         kojiBlok = mc.getBlock ( gdje ) 
         if kojiBlok == AIR.id :
            mc.setBlock(gdje , TORCH.id , 5 )
   
 
if __name__ == "__main__":    #direktan poziv
   #katakombe (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   for dX in range (0,66,21):
      for dZ in range ( -64 , 66 , 21 ):
         katakombe ( orMj ,  orSm ,  iX=11 + dX, iZ=dZ , iY=0 ) 