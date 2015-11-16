from mc import *		
from crtanje import *		#tu je funkcija koju zovem
from sorter_soba_2 import *	
from sorter_2 import *	
from endStorage_2 import *	
from lift import *	



def testKomplet ( orMj , orSm ,  iX=0 , iZ=0 , iY=0 ,  materijal = 98, dv = 0 , stepenice_mat = 109):

  
   
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste

   
   sorter_soba_2 ( orMj , orSm ,  iX=1 , iZ=0 , iY=-8 ,  visina = 5 ) 
   
   sorter_soba_2 ( orMj , orSm ,  iX=1 , iZ=0 , iY=0 , visina = 9 ) 

   endStorage_2 (  orMj , orSm  ,  iX=4 , iY=-8 )
   
   sorter2 (  orMj , orSm , iX=6  )
   
   crtaj_kvadar ( orMj , (1,-2 ,0)  , (1,2,2) , orSm , 0 , blok_dv = 0 )   #vrata
   crtaj_kvadar ( orMj , (11,-9,0)  , (66,9,0) , orSm , 189 , 0 ) # fence
   crtaj_kvadar ( orMj , (11,-10,-2)  , (67,10,-1) , orSm , 89 , 0 )  #lampe obrub
   crtaj_kvadar ( orMj , (12,-8,0)  , (65,8,-2) , orSm , 0 , 0 ) 
   crtaj_kvadar ( orMj , (11,-1,0)  , (11,1,0) , orSm , 0 , 0 )
   
   for br in range ( 0 , 8 ):
      crtaj_stepenice ( orMj , (11+br,-1,-1-br) , (11+br,1,-1-br)  , orSm , blok_id = 109 , rel_smjer  = "odmene" , gore_dolje = "ne"  )
      
   crtaj_hopper ( orMj , (  5 , 20 , 4 ) ,  (  5 , 20 , -2 ) , orSm , "dolje" )
   crtaj_hopper ( orMj , (  5 , 20 , -3 ) ,  (  5 , 20 , -3 ) , orSm , "desno" )
   crtaj_hopper ( orMj , (  5 , 21 , -3 ) ,  (  7 , 21 , -3 ) , orSm , "odmene" )
   crtaj_hopper ( orMj , (  8 , 21 , -3 ) ,  (  8 , 21 , -3 ) , orSm , "dolje" )
   
   crtaj_hopper ( orMj , (  2 , -20 , 4 ) ,  (  5 , -20 , 4 ) , orSm , "odmene" )
   crtaj_kutiju ( orMj , (  4 , -20 , 5 ) ,  (  5 , -20 , 5 ) , orSm , rel_smjer  = "desno" )
   for br in range ( 0 , 5 ):
      crtaj_stepenice ( orMj , ( 5 , -19 + br , 4 - br ) , (5 , -19 +br, 4 - br )  , orSm , blok_id = 109 , rel_smjer  = "desno" , gore_dolje = "ne"  )
      
   dno = nadji_dno ( orMj , ( 0 , 0, 0 ) , orSm ) + 3 # pronadji dno ovaj +2 je nekakav iskustveni korektiv
   orSmL = ortUlijevo ( orSm )
   crtaj_lift_2 ( orMj , orSmL , iX= 20 , iZ= 2 ,  iY=-7  , visina = 12 , materijal = 98 , dv = 0 )
   orSmD = ortUdesno ( orSm )
   crtaj_lift_2 ( orMj , orSmD , iX= -18 , iZ= -2 ,  iY=dno   , visina = -dno + 5 , materijal = 98 , dv = 0 )   
   
   crtaj_hopper ( orMj , (  2 , -18 , 4 ) ,  (  2 , -19 , 4 ) , orSm , "lijevo" )
   
 
if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   testKomplet ( orMj , orSm ,  iX=0 , iZ=0 , iY=0 )    