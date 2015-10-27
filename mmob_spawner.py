import time 
from crtanje import *		#tu je funkcija koju zovem
from katakombe import * 
from bakljada import * 
from modul_sorter import * 
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


def modul (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0   ):
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na kocku ispod pressure plate
   #prvi red
   crtaj_kvadar ( orMj , ( 0  , 0 , 0 )  , (  2 , 0 , 0 ) , orSm ,  materijal , dv ) #tri bloka ispod kao osnova
   #drugi red
   crtaj_kvadar ( orMj , ( 0  , 0 ,1 )  , (  0 , 0 , 1 ) , orSm ,  70 , 0 ) # pressure plate
   crtaj_comparator   ( orMj  , [ 1 , 0 , 1 ]  , [ 1 , 0 , 1  ] , orSm , rel_smjer  = "odmene"    ) # iza pressure plate comparator
   crtaj_kvadar ( orMj , [ 2 , 0 , 1 ]  , [ 2 , 0 , 1  ] , orSm ,  materijal , dv ) # na kraju kocka
   #treci red 
   crtaj_kvadar ( orMj , [ 1 , 0 , 2 ]  , [ 1 , 0 , 2  ] , orSm ,  materijal , dv ) #kocka za guranje
   crtaj_sticky_piston   ( orMj  , [ 2 , 0 , 2 ]  , [2 , 0 , 2  ] , orSm , rel_smjer  = "meni"    ) #iza kocke sticky piston
   crtaj_kvadar ( orMj , [ 3 , 0 , 2 ]  , [ 3 , 0 , 2  ] , orSm ,  materijal , dv ) #estetika kocka za iza pistona
   # cetvrti red ???
   #crtaj_kvadar ( orMj , [ 2 , 0 , 3 ]  , [ 2 , 0 , 3  ] , orSm ,  materijal , dv ) #???

def tvrdja (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0 , stepenice_mat = 109 ):


   dimenzija = 26
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar 
   orginalniOrigin = orMj # spremi ??
   dubina = nadji_dno ( orMj , ( 0 , 0, 0 ) , orSm ) + 2 # pronadji dno ovaj +2 je nekakav iskustveni korektiv
   bakljadaOrigin = premjesti_origin ( orMj , 0 , 0 , dubina - 2,  orSm ) 
   
   brojalica =  0
   while brojalica < 4 :
      mc.postToChat("DUBINA: %f" % ( dubina ) )
      katOrigin = premjesti_origin ( orMj , 0 , 0 , dubina ,  orSm )
      for dX in range (-42,43,21):
         for dZ in range ( -42 , 43 , 21 ):
            # za testirenje zakomentirano
            katakombe ( katOrigin ,  orSm ,  iX = dX, iZ = dZ , iY=0 ) 
            a = 2
      dubina += 7
      brojalica += 1
      
      # za testirenje zakomentirano
      #time.sleep ( 12 )
   
   orMj = premjesti_origin ( katOrigin , 0 , 0 , 6 ,  orSm ) #mice ishodiste na centar
   mc.postToChat("Kocka"  )
   crtaj_kvadar ( orMj , (  -dimenzija  , -dimenzija ,  0  )  , (   dimenzija  ,  dimenzija ,  50  ) , orSm ,  materijal , dv  ) # kocka
   time.sleep ( 2 )
   for br in range ( 1 , 52 , 7 ):
      mc.postToChat("Kocka - rupa %f" % br )
      crtaj_kvadar ( orMj , (  - dimenzija + 1  , -dimenzija +1 , br  )  , (   dimenzija -1  ,  dimenzija-1 ,  br + 5  ) , orSm ,0 , 0  ) # rupa u kocki
      time.sleep ( 1 )
   mc.postToChat("Bakljada"  )
   bakljada ( bakljadaOrigin , orSm ,  dimenzije = 50 , visina = 110)  
   time.sleep ( 1 )
   # za testirenje zakomentirano
   bakljada ( bakljadaOrigin , orSm ,  dimenzije = 150 , visina = 110)
   time.sleep ( 10 )
   
   # 4 kata nize
   
   kata4Origin = premjesti_origin ( orMj , 0 , 0 , 0 + 1 + 21 ,  orSm )
   orSm = ortUlijevo ( orSm )
   for dummy in ( 1 , 2 , 3 ):
      for dZ in range ( -18,19 ):
         if dZ % 2 == 0:
            flag_kutija = "kutija"
         else:
            flag_kutija = "ne"
            
         if abs (dZ) > 15 :
            flag_crtaj_kutije = "ne"
         else:
            flag_crtaj_kutije = "da"
         modul_sorter (  kata4Origin ,  orSm , iX=16 , iZ=dZ , iY=0  ,  materijal = 98, dv = 0  , kutija = flag_kutija ,crtaj_kutije = flag_crtaj_kutije )
         crtaj_hopper    ( kata4Origin , [ 21   , dZ, 4-7 ]  , [ 21   ,  dZ , 4-7    ] , orSm , "meni" ) #hopper pozadi kat ispod
         if abs (dZ) < 16 :
            modul_kraj (  kata4Origin ,  orSm , iX=16 , iZ=dZ , iY=-7  ,  materijal = 98, dv = 0  , kutija = flag_kutija )  #kat ispod slijepa kutija
      crtaj_hopper    ( kata4Origin , [ 21   , -21, 4 ]  , [ 21   ,  -19 , 4  ] , orSm , "desno" ) #kutna spojnica
      crtaj_hopper    ( kata4Origin , [ 21   , 19, 4 ]  , [ 21   ,  20 , 4  ] , orSm , "desno" ) #kutna spojnica

      crtaj_hopper    ( kata4Origin , [ 21   , -20, 4-6 ]  , [ 21   ,  -19 , 4 -6 ] , orSm , "lijevo" ) #kat ispod kutna spojnica
      crtaj_hopper    ( kata4Origin , [ 21   , 19, 4-6 ]  , [ 21   ,  21 , 4  -6] , orSm , "lijevo" ) #kat ispod  kutna spojnica

      
      crtaj_hopper    ( kata4Origin , [ 20   , -18, 2 ]  , [ 20   ,  -16 , -1  ] , orSm , "dolje" ) #dolje upod
      crtaj_hopper    ( kata4Origin , [ 20   , 18, 2 ]  , [ 20   ,  16 , -1  ] , orSm , "dolje" ) #dolje upod
      crtaj_hopper    ( kata4Origin , [ 20   , -18, -2 ]  , [ 20   ,  -16 , -2  ] , orSm , "odmene" ) #dolje upod spoj na krug
      crtaj_hopper    ( kata4Origin , [ 20   , 18, -2 ]  , [ 20   ,  16 , -2  ] , orSm , "odmene" ) #dolje upod spoj na krug
      crtaj_hopper    ( kata4Origin , [ 21   , -18, 4-6 ]  , [ 21   ,  18 , 4-6    ] , orSm , "lijevo" ) #hopper pozadi kat ispod
      
      
      
      orSm = ortUdesno ( orSm )
   #red ispred vrata sa prolazom
   for dZ in (range ( -18, -4 ) + range(5,19 ) ):
      if dZ % 2 == 0:
         flag_kutija = "kutija"
      else:
         flag_kutija = "ne"
            
      if abs (dZ) > 15 :
         flag_crtaj_kutije = "ne"
      else:
         flag_crtaj_kutije = "da"
      modul_sorter (  kata4Origin ,  orSm , iX=16 , iZ=dZ , iY=0  ,  materijal = 98, dv = 0  , kutija = flag_kutija ,crtaj_kutije = flag_crtaj_kutije )
      
      if abs (dZ) < 16 :
         modul_kraj (  kata4Origin ,  orSm , iX=16 , iZ=dZ , iY=-7  ,  materijal = 98, dv = 0  , kutija = flag_kutija )  #kat ispod slijepa kutija
      crtaj_hopper    ( kata4Origin , [ 21   , dZ, 4-7 ]  , [ 21   ,  dZ , 4-7    ] , orSm , "meni" ) #hopper pozadi kat ispod
      crtaj_hopper    ( kata4Origin , [ 21   , -21, 4 ]  , [ 21   ,  -19 , 4    ] , orSm , "desno" ) #kutna spojnica
      crtaj_hopper    ( kata4Origin , [ 21   , 19, 4 ]  , [ 21   ,  20 , 4    ] , orSm , "desno" ) #kutna spojnica

      crtaj_hopper    ( kata4Origin , [ 21   , -20, 4-6 ]  , [ 21   ,  -19 , 4 -6 ] , orSm , "lijevo" ) #kat ispod kutna spojnica
      crtaj_hopper    ( kata4Origin , [ 21   , 19, 4-6 ]  , [ 21   ,  21 , 4  -6] , orSm , "lijevo" ) #kat ispod  kutna spojnica

      crtaj_hopper    ( kata4Origin , [ 20   , -18, 2 ]  , [ 20   ,  -16 , -1  ] , orSm , "dolje" ) #dolje upod
      crtaj_hopper    ( kata4Origin , [ 20   , 18, 2 ]  , [ 20   ,  16 , -1  ] , orSm , "dolje" ) #dolje upod

      crtaj_hopper    ( kata4Origin , [ 20   , -18, -2 ]  , [ 20   ,  -16 , -2  ] , orSm , "odmene" ) #dolje upod spoj na krug
      crtaj_hopper    ( kata4Origin , [ 20   , 18, -2 ]  , [ 20   ,  16 , -2  ] , orSm , "odmene" ) #dolje upod spoj na krug
   
   crtaj_hopper    ( kata4Origin , [ 21   , -4, 4 ]  , [ 21   ,  -4 , -1    ] , orSm , "dolje" ) #1 odmaknuti od kraja
   #crtaj_hopper    ( kata4Origin , [ 21   , -3, 4 ]  , [ 21   ,  -3 , -1    ] , orSm , "dolje" ) #spusti u pod
   
   
   crtaj_hopper    ( kata4Origin , [ 21   , -18, 4-6 ]  , [ 21   ,  18 , 4-6    ] , orSm , "lijevo" ) #hopper pozadi kat ispod
      
   
   # 5 katova nize
   
   kata4Origin = premjesti_origin ( orMj , 0 , 0 , -7 ,  orSm )
   
   
   
   return orMj

   

def mmob_spawner (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0 , stepenice_mat = 109 ):

   sirina = 7
   visina = 43
   razbijalica = 46
   
   time.sleep ( 5 )
   mc.postToChat("Platforma"  )
   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice ishodiste na centar 
   orginalniOrigin = orMj # spremi ??
   
   crtaj_kvadar ( orMj , (  sirina  + 5  , - sirina - 5 , - 4  )  , (   - sirina -5  ,  sirina + 5 ,  21  ) , orSm ,  0 , 0 ) # clear the deck
   time.sleep ( 1 )
   

   #orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm )
   
   
   crtaj_kvadar ( orMj , (  sirina  + 1  , - sirina - 1  , - 1  )  , (   - sirina  - 1 ,  sirina  + 1 ,    - 1 ) , orSm ,   44 , 0 ) # razbijalica okolo
   time.sleep ( 1 )
   crtaj_kvadar ( orMj , (  sirina  - 2  , - sirina + 2 , - 1  )  , (   - sirina +  2  ,  sirina - 2 ,  - 1  ) , orSm ,  89 , 0 ) # glowstone platforma u sredini
   time.sleep ( 1 )
   mc.postToChat("Staklana"  )
   orSm = ortUlijevo ( orSm )  # okret za 90
   
   # stakleni zidovi glass pane 102
   for dummy in ( 1 ,2 ,3 ,4 ): #brojalica za okretanje
      mc.postToChat("Staklana %f "  % dummy )
      crtaj_kvadar ( orMj , (  sirina  - 2  , - sirina + 2 , 0  )  , (   sirina - 2  ,  sirina - 2 ,  3 * ( visina - 1 ) + 1 + 45 ) , orSm ,  102 , 0 ) # inside glass
      crtaj_kvadar ( orMj , (  sirina  + 1  , - sirina - 1  , 0  )  , (   sirina  + 1 ,  sirina  + 1 ,   razbijalica - 1 ) , orSm ,  102 , 0 ) # outside glass
      
      #skupljaci ispod
      
      crtaj_kvadar ( orMj , (  sirina  + 1  , - sirina - 1 , -2 )  , (  sirina  - 2 , sirina  + 1 , -2 ) , orSm , 154 , smjer_hoppera ( orSm , "desno" ) ) # hopperi spod stoneslaba
      crtaj_kvadar ( orMj , (  sirina  + 1  , - sirina - 1 , -4 )  , (  sirina  - 2 , sirina  + 1 , -4 ) , orSm ,   89 , 0 ) # glowstonei ispod hoppera
      
      orSm = ortUdesno ( orSm )  # okret za 90
      time.sleep ( 1 )
   
   crtaj_hopper    ( orMj , ( sirina + 1 ,  - sirina - 1 , -2 ), (  sirina + 1 , - sirina + 2 , -2) , orSm ,  "lijevo" ) 
   crtaj_kutiju ( orMj , (  sirina + 1   , - sirina - 2, -2 ), (  sirina  , - sirina - 2 , -2) , orSm ,  rel_smjer  = "desno"  )
   crtaj_hopper    ( orMj , (  sirina + 1   , - sirina - 2, -3 ), (  sirina  , - sirina - 2 , -4) , orSm ,  "lijevo" )
   #crtaj_hopper    ( orMj , (  sirina + 1   , - sirina - 2, -4 ), (  sirina  , - sirina - 2 , -4) , orSm ,  "lijevo" )
   crtaj_kutiju ( orMj , (  sirina + 1   , - sirina - 3, -3 ), (  sirina  , - sirina - 3 , -4) , orSm ,  rel_smjer  = "desno"  )
   #crtaj_kutiju ( orMj , (  sirina + 1   , - sirina - 2, -3 ), (  sirina  , - sirina - 2 , -4) , orSm ,  rel_smjer  = "desno"  )
   crtaj_kutiju ( orMj , (  sirina + 1   , - sirina - 3, -3 ), (  sirina  , - sirina - 3 , -4) , orSm ,  rel_smjer  = "desno"  )
   crtaj_hopper    ( orMj , (  sirina + 1   , - sirina - 3, -5 ), (  sirina  , - sirina - 3 , -5) , orSm ,  "dolje" ) #hopperi ispod kutija
   crtaj_hopper    ( orMj , (  sirina + 1   , - sirina - 3, -6 ), (  sirina -1  , - sirina - 3 , -6) , orSm ,  "meni" ) #hopperi ispod kutija
   crtaj_hopper    ( orMj , (  sirina -2   , - sirina - 3, -6 ), (  sirina -2  , - sirina - 14 , -6) , orSm ,  "lijevo" ) #hopperi ispod kutija
   
   
   #return za testiranje
   #return 1
   time.sleep ( 10 )
   mc.postToChat("Gljiva"  )
   orMj = premjesti_origin ( orMj , 0  , 0 ,  razbijalica ,  orSm ) #mice ishodiste na centar i 45 iznad razbijalice
   for dummy in ( 1 ,2 ,3 ,4 ): #brojalica za okretanje
      mc.postToChat("Gljiva %f "  % dummy )
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
      time.sleep ( 20 )
   # poklopac na sredini
   #ZAKOMENTIRANO zbog testiranja
   mc.postToChat("Poklopac"  )
   crtaj_kvadar ( orMj , (  sirina   , sirina , 0 + 3 * br + 3 )  , (  - sirina  , - sirina  ,  3 * br + 3 ) , orSm ,  44 , 0 ) # poklopac na sredini stepenica half slab anti spawn
   time.sleep ( 10 )



if __name__ == "__main__":    #direktan poziv
   #polukrugTunel (   iX=2 , iZ=0 , iY=0 , radius = 8 , duzina = 70 , korekcija = 0 , uspon = 0  )
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   orMj = tvrdja (  orMj ,  orSm , iX=27 , iZ=0 , iY=0  ,  materijal = 98, dv = 0 , stepenice_mat = 109 )
   mmob_spawner (  orMj ,  orSm , iX=0 , iZ=0 , iY=33  ,  materijal = 98, dv = 0 , stepenice_mat = 109 )
   
   #tvrdja (  orMj ,  orSm , iX=14 , iZ=0 , iY=0  ,  materijal = 98, dv = 0 , stepenice_mat = 109 )
   mc.postToChat("K R A J  "  )
   
   