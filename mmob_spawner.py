import time 
from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


def modul (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0   ):
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na kocku ispod pressure plate
   #prvi red
   crtaj_kvadar ( orMj , ( 0  , 0 , 0 )  , (  2 , 0 , 0 ) , orSm ,  materijal , dv ) #tri bloka ispod
   #drugi red
   crtaj_kvadar ( orMj , ( 0  , 0 ,1 )  , (  0 , 0 , 1 ) , orSm ,  70 , 0 ) # pressure plate
   crtaj_comparator   ( orMj  , [ 1 , 0 , 1 ]  , [ 1 , 0 , 1  ] , orSm , rel_smjer  = "odmene"    ) # iza pressure plate comparator
   crtaj_kvadar ( orMj , [ 2 , 0 , 1 ]  , [ 2 , 0 , 1  ] , orSm ,  materijal , dv ) # na kraju kocka
   #treci red 
   crtaj_kvadar ( orMj , [ 1 , 0 , 2 ]  , [ 1 , 0 , 2  ] , orSm ,  materijal , dv ) #kocka za guranje
   crtaj_sticky_piston   ( orMj  , [ 2 , 0 , 2 ]  , [2 , 0 , 2  ] , orSm , rel_smjer  = "meni"    ) #iza kocke sticky piston
   crtaj_kvadar ( orMj , [ 3 , 0 , 2 ]  , [ 3 , 0 , 2  ] , orSm ,  materijal , dv ) #estetika kocka za iza pistona
   # cetvrti red ???
   #crtaj_kvadar ( orMj , [ 2 , 0 , 3 ]  , [ 2 , 0 , 3  ] , orSm ,  materijal , dv ) #kocka za guranje

def mmob_spawner (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0 , stepenice_mat = 109 ):

   sirina = 7
   visina = 25
   razbijalica = 46
   
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar 
   
   crtaj_kvadar ( orMj , (  sirina  + 1  , - sirina - 1  , - 1  )  , (   - sirina  - 1 ,  sirina  + 1 ,    - 1 ) , orSm ,   44 , 0 ) # razbijalica okolo
   crtaj_kvadar ( orMj , (  sirina  - 2  , - sirina + 2 , - 1  )  , (   - sirina +  2  ,  sirina - 2 ,  - 1  ) , orSm ,  89 , 0 ) # glowstone platforma u sredini
   
   orSm = ortUlijevo ( orSm )  # okret za 90
   
   # stakleni zidovi glass pane 102
   for dummy in ( 1 ,2 ,2 ,2 ): #brojalica za okretanje
      crtaj_kvadar ( orMj , (  sirina  - 2  , - sirina + 2 , 0  )  , (   sirina - 2  ,  sirina - 2 ,  3 * ( visina - 1 ) + 1 + 45 ) , orSm ,  102 , 0 ) # inside glass
      crtaj_kvadar ( orMj , (  sirina  + 1  , - sirina - 1  , 0  )  , (   sirina  + 1 ,  sirina  + 1 ,   razbijalica - 1 ) , orSm ,  102 , 0 ) # outside glass
      
      #skupljaci ispod
      
      crtaj_kvadar ( orMj , (  sirina  + 1  , - sirina - 1 , -2 )  , (  sirina  - 2 , sirina  + 1 , -2 ) , orSm , 154 , smjer_hoppera ( orSm , "desno" ) ) # hopperi spod stoneslaba
      crtaj_kvadar ( orMj , (  sirina  + 1  , - sirina - 1 , -4 )  , (  sirina  - 2 , sirina  + 1 , -4 ) , orSm ,   89 , 0 ) # glowstonei ispod hoppera
      
      orSm = ortUdesno ( orSm )  # okret za 90
   
   crtaj_hopper    ( orMj , ( sirina + 1 ,  - sirina - 1 , -2 ), (  sirina + 1 , - sirina + 2 , -2) , orSm ,  "lijevo" ) 
   crtaj_kutiju ( orMj , (  sirina + 1   , - sirina - 2, -2 ), (  sirina  , - sirina - 2 , -2) , orSm ,  rel_smjer  = "desno"  )
   crtaj_hopper    ( orMj , (  sirina + 1   , - sirina - 2, -3 ), (  sirina  , - sirina - 2 , -4) , orSm ,  "lijevo" )
   #crtaj_hopper    ( orMj , (  sirina + 1   , - sirina - 2, -4 ), (  sirina  , - sirina - 2 , -4) , orSm ,  "lijevo" )
   crtaj_kutiju ( orMj , (  sirina + 1   , - sirina - 3, -3 ), (  sirina  , - sirina - 3 , -4) , orSm ,  rel_smjer  = "desno"  )
   #crtaj_kutiju ( orMj , (  sirina + 1   , - sirina - 2, -3 ), (  sirina  , - sirina - 2 , -4) , orSm ,  rel_smjer  = "desno"  )
   
   
   orMj = premjesti_origin ( orMj , 0  , 0 ,  razbijalica ,  orSm ) #mice ishodiste na centar i 45 iznad razbijalice
   for dummy in ( 1 ,2 ,2 ,2 ): #brojalica za okretanje
      for br in range ( 0, visina ):
         dX = br
         dY = br * 3
         for dZ in range ( -sirina , sirina + 1   ):
            modul (  orMj ,  orSm , iX=dX + sirina + 1, iZ=dZ , iY=dY  ,  materijal = materijal, dv = dv  )
         crtaj_kvadar ( orMj , (  sirina + 1  , - sirina - 1, 0 + 3 * br )  , (  2+dX + sirina + 1 , - sirina - 1 ,  3 * br + 2 ) , orSm ,  materijal , dv ) #blokovi sastrane za zamracivanje   
         crtaj_kvadar ( orMj , (  sirina + 1  , sirina + 1, 0 + 3 * br )  , (  2+dX + sirina + 1 , sirina + 1 ,  3 * br + 2 ) , orSm ,  materijal , dv ) #blokovi sastrane za zamracivanje   
      #crtaj_kvadar ( orMj , (  sirina + 1  , sirina + 1, 0 + 3 * br + 3 )  , (  2+dX + sirina + 2 , - sirina - 1 ,  3 * br + 3 ) , orSm ,  materijal , dv ) # puni protiv svijetla
      crtaj_kvadar ( orMj , (  sirina + 1  , sirina + 1, 0 + 3 * br + 3 )  , (  2+dX + sirina + 2 , - sirina - 1 ,  3 * br + 3 ) , orSm ,  44 , 0 ) # poklopac na vrhu stepenica half slab anti spawn
      orSm = ortUlijevo ( orSm )  # okret za 90
   # poklopac na sredini
   #ZAKOMENTIRANO zbog testiranja
   crtaj_kvadar ( orMj , (  sirina   , sirina , 0 + 3 * br + 3 )  , (  - sirina  , - sirina  ,  3 * br + 3 ) , orSm ,  44 , 0 ) # poklopac na sredini stepenica half slab anti spawn



if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   mmob_spawner (  orMj ,  orSm , iX=12 , iZ=0 , iY=5  ,  materijal = 98, dv = 0 , stepenice_mat = 109 )
   