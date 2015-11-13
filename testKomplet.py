from mc import *		
from crtanje import *		#tu je funkcija koju zovem
from sorter_soba_2 import *	
from sorter_2 import *	
from endStorage_2 import *	
from lift import *	


if 1 == 1:
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   sorter_soba_2 ( orMj , orSm ,  iX=5 , iZ=0 , iY=-8 ,  visina = 5 ) 
   
   sorter_soba_2 ( orMj , orSm ,  iX=5 , iZ=0 , iY=0 , visina = 9 ) 

   endStorage_2 (  orMj , orSm  ,  iX=8 , iY=-8 )
   
   sorter2 (  orMj , orSm , iX=10  )
   
   crtaj_kvadar ( orMj , (15,-9,0)  , (46,9,0) , orSm , 189 , 0 ) # fence
   crtaj_kvadar ( orMj , (14,-10,-2)  , (47,10,-1) , orSm , 89 , 0 ) 
   crtaj_kvadar ( orMj , (16,-8,0)  , (45,8,-2) , orSm , 0 , 0 ) 
   crtaj_kvadar ( orMj , (15,-1,0)  , (15,1,0) , orSm , 0 , 0 )
   
   for br in range ( 0 , 8 ):
      crtaj_stepenice ( orMj , (15+br,-1,-1-br) , (15+br,1,-1-br)  , orSm , blok_id = 109 , rel_smjer  = "odmene" , gore_dolje = "ne"  )
      
   orSmL = ortUlijevo ( orSm )
   crtaj_lift_2 ( orMj , orSmL , iX= 20 , iZ= 7 ,  iY=-7  , visina = 12 , materijal = 24 , dv = 2 )