# lift crta se od dna prema gore
#definicija objekta i poziv rutine za crtanje
import time 
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def crtaj_lift ( orMj , orSm , iX  , iZ ,  iY  , visina = 12 ):

   orMj   = premjesti_origin ( orMj , iX  , iZ , iY ,  orSm )

   
   
   if ( visina % 2 == 1 ) : #nesmije biti neparna visina
      mc.postToChat("NEPARNA "   )
      visina += 1
   else:
      mc.postToChat("PPPPPARNA "   )
      
   
   #sandstone glatki
   materijal = 24
   dv = 2

   # zashtita oko stupa
   crtaj_kvadar ( orMj , [ 0  , -2, -1 ]  , [ 4  , 5 , visina -7 ] , orSm , materijal , dv ) # zashtita i red ispod   pa do ispod nogu
   
   #rupa oko stupa
   crtaj_kvadar ( orMj , [ 1  , -1, 0 ]  , [ 3  , 4 , visina + 2 ] , orSm , 0 , 0 ) # zrak

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

   crtaj_kutiju ( orMj , [ 2 , 3, visina + 1  ]  , [ 2 ,  4 , visina + 1  ] , orSm , rel_smjer  = "meni" , blok_id = 54     )


def ispred_glave ():
   #pozicioniranje na soreter, ispod kutije , dva natrag, jedan lijevo
   
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   bedrock = nadji_dno ( orMj , ( 0 , 0 , 0 ) , orSm ) + 2 # maknuti crne tocke u pregledu
   crtaj_lift ( orMj ,  orSm ,  iX=0, iZ=-4 , iY=bedrock  , visina = -bedrock ) # crta se od dna prema gore

if __name__ == "__main__":    #direktan poziv
   #katakombe (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   ispred_glave () 






