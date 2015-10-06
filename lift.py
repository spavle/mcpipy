# lift
#definicija objekta i poziv rutine za crtanje
import time 
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def crtaj_lift ( dX , dZ , dY , visina ):
   # origin ispred na sredini 
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   
   #korekcija polozaja
   orMjA = gdjeSam ()
   orMj   = rel2abs ( orMjA ,  ( dX , dZ , dY )   , orSm  ) 
   bla = orMj [ 1 ]
   orMj [ 1 ] = orMj [ 2 ]
   orMj [ 2 ] = bla
   
   """
   #mc.postToChat("orginal: %f %f %f " %  orMj [ 0 ]  , orMj [ 1 ] , orMj [ 2 ] )
   mc.postToChat("orginal: %s " %  orMj    )
   #mc.postToChat("pretvoreno: %f %f %f " %  orMjA [ 0 ]   , orMjA [ 1 ]  , orMjA [ 2 ] )
   mc.postToChat("pretvoreno: %s" %  orMjA     )
   """
   
   if ( visina % 2 == 1 ) : #nesmije biti neparna visina
      mc.postToChat("NEPARNA "   )
      visina += 1
   else:
      mc.postToChat("PPPPPARNA "   )
      
   
   #sandstone glatki
   materijal = 1
   dv = 1



   #prvi red
   crtaj_kvadar ( orMj , [ 2  , 0, 0 ]  , [ 2  , 4 , 0  ] , orSm , materijal , dv ) # temeljniblok
   crtaj_redstonedust ( orMj , [ 2 , 0, 1 ]  , [ 2 ,  0 , 1  ] , orSm )
   crtaj_repeater ( orMj , [ 2 , 1, 1 ]  , [ 2 ,  1 , 1  ] , orSm , rel_smjer  = "desno" )
   crtaj_kvadar ( orMj , [ 2  , 2, 1 ]  , [ 2  , 2 , 1  ] , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , [ 2  , 3, 1 ]   ,  orSm  , "desno" ) 
   

   #drugi red
   crtaj_kvadar ( orMj , [ 2  , 1, 2 ]  , [ 2  , 1 , 2  ] , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , [ 2  , 0, 2 ]   ,  orSm  , "lijevo" )  
   crtaj_comparator ( orMj , [ 2  , 2, 2 ]  , [ 2  , 2 , 2  ]  , orSm , rel_smjer  = "lijevo" )
   crtaj_dropper    ( orMj , [ 2  , 3, 2 ]  , [ 2  , 3 , 2  ]  , orSm , rel_smjer  = "gore" )
   crtaj_hopper    ( orMj , [ 2  , 4, 2 ]  , [ 2  , 4 , 2  ] , orSm , "lijevo" )
  

   #treci red
   crtaj_kvadar ( orMj , [ 2  , 0, 3 ]  , [ 2  , 0 , 3  ] , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , [ 2  , 1, 3 ]   ,  orSm  , "desno" )
   crtaj_dropper    ( orMj , [ 2  , 3, 3 ]  , [ 2  , 3 , 3  ]  , orSm , rel_smjer  = "gore" )
   crtaj_kutiju ( orMj , [ 2 , 4, 3 ]  , [ 1 ,  4 , 3  ] , orSm , rel_smjer  = "desno" , blok_id = 54     )
   

   korigirana_visina = int ( ( visina -3  )  )
   for br in range ( 0 , korigirana_visina , 2 ):
      #cetvrti red

      crtaj_kvadar ( orMj , [ 2  , 1, 4 + br  ]  , [ 2  , 1 , 4  + br ] , orSm , materijal , dv )
      crtaj_redstonetorch ( orMj , [ 2  , 0, 4 + br ]   ,  orSm  , "lijevo" )  
      crtaj_redstonetorch ( orMj , [ 2  , 2, 4 + br ]   ,  orSm  , "desno" )
      crtaj_dropper    ( orMj , [ 2  , 3, 4 + br ]  , [ 2  , 3 , 4 + br  ]  , orSm , rel_smjer  = "gore" )
      #time.sleep ( 1 )

      # peti red

      crtaj_kvadar ( orMj , [ 2  , 0, 5 + br ]  , [ 2  , 0 , 5  + br ] , orSm , materijal , dv )
      crtaj_redstonetorch ( orMj , [ 2  , 1, 5  + br]   ,  orSm  , "desno" )
      crtaj_dropper    ( orMj , [ 2  , 3, 5 + br ]  , [ 2  , 3 , 5  + br ]  , orSm , rel_smjer  = "gore" )
      #time.sleep ( 1 )
   
   
   crtaj_kvadar ( orMj , [ 2  , 1, visina  ]  , [ 2  , 1 , visina ] , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , [ 2  , 0, visina ]   ,  orSm  , "lijevo" )  
   crtaj_redstonetorch ( orMj , [ 2  , 2, visina ],  orSm  , "desno" )
   crtaj_dropper    ( orMj , [ 2  , 3, visina ]  , [ 2  , 3 , visina  ]  , orSm , rel_smjer  = "gore" )
   
   #kutija na vrhu

   crtaj_kutiju ( orMj , [ 2 , 3, visina +1  ]  , [ 2 ,  4 , visina +1  ] , orSm , rel_smjer  = "meni" , blok_id = 54     )










