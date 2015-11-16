# podzemna citadela SA GALERIJOM OKOLO

from crtanje import *		#tu je funkcija koju zovem
from mc import *		
from mmob_spawner import *	
#from sorter_soba import *	
from mining_shaht import *
#from sorter import *	
from katakombe import * 
from lift import *
from endStorage import *
from testKomplet import *

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

sirina = 38
dubina = 50

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#mossy coblestone tijelo
crtaj_kvadar ( orMj , (6, -sirina-6,-18)  , (1+8 + 6 + 4 + dubina,sirina + 6,3) , orSm , 98 , 1 )
crtaj_kvadar ( orMj , (11+3,-sirina,-16)  , (11+3 + dubina ,sirina,-16) , orSm , 2 )
for dX in range ( 18 , 18 + dubina , 8 ) :   #lampe gore i dolje
   for dZ in range ( -sirina - 2  ,sirina + 8 , 8 ) :
      crtaj_kvadar ( orMj , (dX,dZ,-16)  , (dX,dZ,-16) , orSm , 89 )
      crtaj_kvadar ( orMj , (dX,dZ,1)  , (dX,dZ,1) , orSm , 89 )

crtaj_kvadar ( orMj , (11,-sirina - 3,-5)  , (11+6+dubina,sirina +3,0) , orSm , AIR.id ,  0 )   #podest okolo
crtaj_kvadar ( orMj , (13,-sirina - 1,-5)  , (11+4+dubina,sirina +1,-5) , orSm , 85 ,  0 )   #ograda okolo

crtaj_kvadar ( orMj , (11+3,-sirina ,-15)  , (11+3+dubina,sirina ,0) , orSm , AIR.id ,  0 )     #centralna rupa

#zakomentirano za testiranje kao heavy element

mmob_spawner (  orMj ,  orSm , iX=11+3+dubina/2+4 , iZ=0 , iY=-11  ,  materijal = 98, dv = 0 , stepenice_mat = 109 , prosirenje = 0 )

#2 kocke ravno
crtaj_kvadar ( orMj , (1,-2,0)  , (2,2,1) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (1,-2,-1)  , (2,2,-1) , orSm , 2 )

#4 kocke ravno podignut strop
crtaj_kvadar ( orMj , (3,-2,0)  , (6,2,2) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (3,-2,-1)  , (6,2,-1) , orSm , 2 )
crtaj_kvadar ( orMj , ( 4 , -3 , 2 )  , ( 4 , -3 , 2 ) , orSm , 89 ) #prvi par lampi na sredini zida
crtaj_kvadar ( orMj , ( 4 , 3 , 2 )  , ( 4 , 3 , 2 ) , orSm , 89 )
crtaj_kvadar ( orMj , ( 7 , -3 , 0 )  , ( 7 , -3 , 0 ) , orSm , 89 ) #drugi par lampi iznad pocetka stepenica
crtaj_kvadar ( orMj , ( 7 , 3 , 0 )  , ( 7 , 3 , 0 ) , orSm , 89 )

# podest 9 x 7 +++
crtaj_kvadar ( orMj , (11,-3,-6)  , (19,3,-16) , orSm ,98 , 1 )
crtaj_kvadar ( orMj , (14,-3,-6)  , (18,3,-6) , orSm , 2 )
crtaj_kvadar ( orMj , ( 19 , -3 , -5 )  , ( 19 , -3 , -5 ) , orSm , 89 )
crtaj_kvadar ( orMj , ( 19 , 3 , -5 )  , ( 19 , 3 , -5 ) , orSm , 89 )
crtaj_kvadar ( orMj , (11,-4,-5)  , (19,4,-5) , orSm , AIR.id ,  0 ) # prekid u ogradi
crtaj_kvadar ( orMj , (19,-4,-5)  , (19,4,-5) , orSm , 89 )       # lampe na podestu
crtaj_kvadar ( orMj , (19,-3,-5)  , (19,3,-5) , orSm , 85 ,  0 )  # OGRADA NAPRIJED

#4 stepenice dolje
for br in range (5):
   crtaj_kvadar ( orMj , (6+br,-2,1-br)  , (6+br,2,3-br) , orSm , AIR.id , blok_dv = 0 )
   crtaj_kvadar ( orMj , (6+br,-2,-1-br)  , (6+br,2,-1-br) , orSm , 2 )
   crtaj_stepenice ( orMj , (7+br,-2,-1-br)  , (7+br,2,-1-br) , orSm , blok_id = 109 , rel_smjer  = "odmene")
   


   
#lijevi podest
crtaj_kvadar ( orMj , (14,-7,-9)  , (19,-12,-16) , orSm ,  98 , 1 )    #podloga
crtaj_kvadar ( orMj , (14,-7,-9)  , (19,-11,-9) , orSm , 2 )            #trava
crtaj_kvadar ( orMj , ( 19 , -12 , -8 )  , ( 19 , -12 , -8 ) , orSm , 89 )

#desni podest
crtaj_kvadar ( orMj , (14,7,-9)  , (19,12,-16) , orSm ,  98 , 1 )    #podloga
crtaj_kvadar ( orMj , (14,7,-9)  , (19,11,-9) , orSm , 2 )            #trava
crtaj_kvadar ( orMj , ( 19 , 12 , -8 )  , ( 19 , 12 , -8 ) , orSm , 89 )

# lijeve stepenice 3 dolje
for br in range (3):
   crtaj_kvadar ( orMj , (14,-4 - br ,-7 -br)  , (19,-4 -br,-16) , orSm , 98 , 1 )
   crtaj_kvadar ( orMj , (14,-4 - br ,-6 -br)  , (19,-4 -br,-6 -br) , orSm , 2 )
   crtaj_stepenice ( orMj , (14,-5 - br ,-6 -br)  , (19,-5 -br,-6 -br) , orSm , blok_id = 109 , rel_smjer  = "lijevo")

# desne stepenice 3 dolje
for br in range (3):
   crtaj_kvadar ( orMj , (14,4 + br ,-7 -br)  , (19,4 +br,-16) , orSm ,  98 , 1 )
   crtaj_kvadar ( orMj , (14,4 + br ,-6 -br)  , (19,4 +br,-6 -br) , orSm , 2 )
   crtaj_stepenice ( orMj , (14,5 + br ,-6 -br)  , (19,5 +br,-6 -br) , orSm , blok_id = 109 , rel_smjer  = "desno")



#lijeve stepenice 5 dolje
for br in range (7):
   crtaj_kvadar ( orMj , (20+br,-7,-10-br)  , (20+br,-12,-16) , orSm ,  98 , 1 )
   crtaj_stepenice ( orMj , (20+br,-7,-9-br)  , (20+br,-12,-9-br) , orSm , blok_id = 109 , rel_smjer  = "odmene")
crtaj_kvadar ( orMj , ( 19 , -5 , -14 )  , ( 19 , -5 , -14 ) , orSm , 89 )
crtaj_kvadar ( orMj , ( 26 , -13 , -15 )  , ( 26 , -13 , -15 ) , orSm , 89 )


#desne stepenice 5 dolje
for br in range (7):
   crtaj_kvadar ( orMj , (20+br,7,-10-br)  , (20+br,12,-16) , orSm ,  98 , 1 )
   crtaj_stepenice ( orMj , (20+br,7,-9-br)  , (20+br,12,-9-br) , orSm , blok_id = 109 , rel_smjer  = "odmene")
crtaj_kvadar ( orMj , ( 19 , 5 , -14 )  , ( 19 , 5 , -14 ) , orSm , 89 )
crtaj_kvadar ( orMj , ( 26 , 13 , -15 )  , ( 26 , 13 , -15 ) , orSm , 89 )

#lampe okolo

for br in range ( 8 , sirina + 3 + 1, 8 ) :   # lampe na podestu napred/nazad
   crtaj_kvadar ( orMj , (10,br,-2)  , (10,br,-2) , orSm , 89 )
   crtaj_kvadar ( orMj , (10,-br,-2)  , (10,-br,-2) , orSm , 89 )
   crtaj_kvadar ( orMj , (16+dubina+2,br,-2)  , (16+dubina+2,br,-2) , orSm , 89 )
   crtaj_kvadar ( orMj , (16+dubina+2,-br,-2)  , (16+dubina+2,-br,-2) , orSm , 89 )

   crtaj_kvadar ( orMj , (10,br,-4)  , (10,br,-4) , orSm , AIR.id , 0 )   # rupe ispod lampi
   crtaj_kvadar ( orMj , (10,-br,-4)  , (10,-br,-4) , orSm , AIR.id , 0 )
   crtaj_kvadar ( orMj , (16+dubina+2,br,-4)  , (16+dubina+2,br,-4) , orSm , AIR.id , 0 )
   crtaj_kvadar ( orMj , (16+dubina+2,-br,-4)  , (16+dubina+2,-br,-4) , orSm , AIR.id , 0 )

   
for br in range ( 8 , dubina + 9, 8 ) :   # lampe na podestu lijevo/desno
   crtaj_kvadar ( orMj , (10+ br,sirina + 4,-2)  , (10 + br,sirina + 4,-2) , orSm , 89 )
   crtaj_kvadar ( orMj , (10+ br,-sirina - 4,-2)  , (10 + br,-sirina - 4,-2) , orSm , 89 )

   crtaj_kvadar ( orMj , (10+ br,sirina + 4,-4)  , (10 + br,sirina + 4,-4) , orSm , AIR.id , 0 )  #rupe ispod lampi
   crtaj_kvadar ( orMj , (10+ br,-sirina - 4,-4)  , (10 + br,-sirina - 4,-4) , orSm , AIR.id , 0 )
   
for br in range ( 0 , sirina + 1, 8 ) :   # lampe na dnu napred/nazad
   #crtaj_kvadar ( orMj , (13,br,-14)  , (13,br,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13,br,-9)  , (13,br,-9) , orSm , 89 )
   #crtaj_kvadar ( orMj , (13,-br,-14)  , (13,-br,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13,-br,-9)  , (13,-br,-9) , orSm , 89 )
   #crtaj_kvadar ( orMj , (13+dubina+2,br,-14)  , (13+dubina+2,br,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+dubina+2,br,-9)  , (13+dubina+2,br,-9) , orSm , 89 )
   #crtaj_kvadar ( orMj , (13+dubina+2,-br,-14)  , (13+dubina+2,-br,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+dubina+2,-br,-9)  , (13+dubina+2,-br,-9) , orSm , 89 )
   
for br in range ( 5 , dubina + 1, 8 ) :   # lampe dnu lijevo/desno
   #crtaj_kvadar ( orMj , (13+ br,sirina+1 ,-14)  , (13 + br,sirina +1,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+ br,sirina+1 ,-9)  , (13 + br,sirina +1,-9) , orSm , 89 )
   #crtaj_kvadar ( orMj , (13+ br,-sirina-1 ,-14)  , (13 + br,-sirina-1 ,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+ br,-sirina-1 ,-9)  , (13 + br,-sirina-1 ,-9) , orSm , 89 )

#ornamenti na podestu naprijed nazad
for br in range ( 8 , sirina - 5 , 8 ) :   # lampe na podestu napred/nazad

   crtaj_kvadar ( orMj , (10,br+2,-4)  , (10,br+6,-1) , orSm , AIR.id , 0 )

   crtaj_kvadar ( orMj , (10,-br-2,-4)  , (10,-br-6,-1) , orSm , AIR.id , 0 )

   crtaj_kvadar ( orMj , (16+dubina+2,br+2,-4)  , (16+dubina+2,br+6,-1) , orSm , AIR.id , 0 )

   crtaj_kvadar ( orMj , (16+dubina+2,-br-2,-4)  , (16+dubina+2,-br-6,-1) , orSm , AIR.id , 0 )

   
#ornamenti na podestu lijevo desno
for br in range ( 8 , dubina  , 8 ) :   # lampe na podestu lijevo/desno
   if 1 == 1 : #not( br % 8 ) and not( br+1 % 8 ) and not( br-1 % 8 ) :

      crtaj_kvadar ( orMj , (2+ 10+ br,sirina + 4,-4)  , (6 + 10 + br,sirina + 4,-1) , orSm , AIR.id , 0 )

      crtaj_kvadar ( orMj , (2+ 10+ br,-sirina - 4,-4)  , (6 + 10 + br,-sirina - 4,-1) , orSm , AIR.id , 0 )



#otvor za terasu - trebalo je raditi sa pomaknutum originom

crtaj_kvadar ( orMj , ( 18 + dubina, -9 , -6 )  , (  28 + dubina  , 9 , 2 ) , orSm , 98 , 1 )     #mossy block
crtaj_kvadar ( orMj , ( 29 + dubina , -9 , -5 )  , (  41 + 6+dubina , 9 , 2 ) , orSm , 98 , 0 )   #stone block
crtaj_kvadar ( orMj , ( 18 + dubina, -6 , -5)  , ( 18 + dubina , 6 , -1 ) , orSm , AIR.id ,  0 )   #malo udubljenje
crtaj_kvadar ( orMj , ( 17 + dubina, -7 , 0)  , ( 17 + dubina , 7 , 0 ) , orSm , 98 , 1  )   #nadvoj ispred
crtaj_kvadar ( orMj , ( 14 + dubina, -7 , -6)  , ( 14 + dubina , 7 , -6 ) , orSm , 98 , 1  )   #nadvoj terse      ---------------------------
crtaj_kvadar ( orMj , ( 14 + dubina, -7 , -5)  , ( 14 + dubina , 7 , -5 ) , orSm , 85 , 1  )   #nadvoj terse ograda
crtaj_kvadar ( orMj , ( 15 + dubina, -6 , -5)  , ( 15 + dubina , 6 , -5 ) , orSm , AIR.id ,  0  )   #nadvoj terse brisanje stare ograde
crtaj_kvadar ( orMj , ( 19 + dubina, -5 , -5)  , ( 19 + dubina , 5 , -4 ) , orSm , AIR.id ,  0 )   # doljnji rub
crtaj_kvadar ( orMj , ( 19 + dubina, -5 , -3)  , ( 19 + dubina , -3 , -3 ) , orSm , AIR.id ,  0 )   # lijevi doljnji rub
crtaj_kvadar ( orMj , ( 19 + dubina, 5 , -3)  , ( 19 + dubina , 3 , -3 ) , orSm , AIR.id ,  0 )   # desni doljnji rub

crtaj_kvadar ( orMj , ( 18 + dubina, -5 , 0)  , ( 26 + dubina , 5 , -2 ) , orSm , AIR.id ,  0 )   #veliko udubljenje
crtaj_kvadar ( orMj , ( 27 + dubina, -1 , 0)  , ( 27 + dubina , 1 , -2 ) , orSm , AIR.id ,  0 )   #udubljenje oko vrata

crtaj_kvadar ( orMj , ( 27 + dubina, -3 , -1)  , ( 27 + dubina , -5 , -1 ) , orSm , 102 ,  0 )   #lijevi prozor
crtaj_kvadar ( orMj , ( 27 + dubina, 3 , -1)  , ( 27 + dubina , 5 , -1 ) , orSm , 102 ,  0 )   #desni prozor


crtaj_kvadar ( orMj , (19 + dubina,-4,1)  , (19 + dubina,-4,1) , orSm , 89 )  # lampa iznad terase prednja lijeva
crtaj_kvadar ( orMj , (19 + dubina,4,1)  , (19 + dubina,4,1) , orSm , 89 )  # lampa iznad terase prednja desna
crtaj_kvadar ( orMj , (20 + dubina,0,1)  , (20 + dubina,0,1) , orSm , 89 )  # lampa iznad terase srednja
crtaj_kvadar ( orMj , (24 + dubina,0,1)  , (24 + dubina,0,1) , orSm , 89 )  # lampa iznad terase zadnja

# ograda iznad terase
crtaj_kvadar ( orMj , (19 + dubina,-2,-2)  , (21 + dubina,2,-2) , orSm , 85 )  # ograda terasa srednja
crtaj_kvadar ( orMj , (20 + dubina,-1,-2)  , (21 + dubina,1,-2) , orSm , AIR.id , 0 )  # ograda terasa srednja

for br in range ( 4 ) :
   crtaj_stepenice ( orMj , ( br + 20 + dubina, -3 , -5 + br  )  , ( br + 20 + dubina , -5 , -5 + br ) , orSm , blok_id = 109 , rel_smjer  = "meni")
   #crtaj_kvadar ( orMj , ( br + 20 + dubina, -3 , -5 + br  )  , ( br + 20 + dubina , -5 , -5 + br ) , orSm , 109 ,  0 )   # lijevo stone brick stepenica
   crtaj_kvadar ( orMj , ( br + 20 + dubina, -3 , -4 + br  )  , ( br + 20 + dubina , -5 , -2 ) , orSm , AIR.id ,  0 )   # zrak iznad stepenica
   crtaj_stepenice ( orMj , ( br + 20 + dubina, 3 , -5 + br  )  , ( br + 20 + dubina , 5 , -5 + br ) , orSm , blok_id = 109 , rel_smjer  = "meni")
   #crtaj_kvadar ( orMj , ( br + 20 + dubina, 3 , -5 + br  )  , ( br + 20 + dubina , 5 , -5 + br ) , orSm , 109 ,  0 )   # desno stone brick stepenica
   crtaj_kvadar ( orMj , ( br + 20 + dubina, 3 , -4 + br  )  , ( br + 20 + dubina , 5 , -2 ) , orSm , AIR.id ,  0 )   # zrak iznad stepenica
   
#hodnik i sobe iza terase
crtaj_kvadar ( orMj , ( 29 + dubina, -1 , 0)  , ( 34 + dubina , 1 , -2 ) , orSm , AIR.id ,  0 )    #hodnik
crtaj_kvadar ( orMj , (31 + dubina,0,1)  , (31 + dubina,0,1) , orSm , 89 )  # lampa hodnik
crtaj_kvadar ( orMj , ( 28 + dubina, -3 , 0)  , ( 33 + dubina , -7 , -2 ) , orSm , AIR.id ,  0 )    #lijeva soba
crtaj_kvadar ( orMj , (32 + dubina,-5,1)  , (32 + dubina,-5,1) , orSm , 89 )  # lampa lijeva soba
crtaj_kvadar ( orMj , ( 28 + dubina, 3 , 0)  , ( 33 + dubina , 7 , -2 ) , orSm , AIR.id ,  0 )    #desna soba
crtaj_kvadar ( orMj , (32 + dubina,5,1)  , (32 + dubina,5,1) , orSm , 89 )  # lampa desna soba
crtaj_kvadar ( orMj , ( 36 + dubina, 7 , 0)  , ( 45 + dubina , -7 , -2 ) , orSm , AIR.id ,  0 )    #zadnja soba
crtaj_kvadar ( orMj , (40 + dubina,-4,1)  , (40 + dubina,-4,1) , orSm , 89 )  # lampa zadnja soba
crtaj_kvadar ( orMj , (40 + dubina,0,1)  , (40 + dubina,0,1) , orSm , 89 )  # lampa zadnja soba
crtaj_kvadar ( orMj , (40 + dubina,4,1)  , (40 + dubina,4,1) , orSm , 89 )  # lampa zadnja soba


crtaj_vrata ( orMj , ( 28 + dubina , 0 , -2 ) , orSm , "meni"  , blok_id = 64  , kvaka = "lijevo"  )     # prednja vrata
crtaj_vrata ( orMj , ( 30 + dubina , -2 , -2 ) , orSm , "desno"  , blok_id = 64  , kvaka = "lijevo"  )   # lijeva vrata
crtaj_vrata ( orMj , ( 30 + dubina , 2 , -2 ) , orSm , "lijevo"  , blok_id = 64  , kvaka = "lijevo"  )   # desna vrata
crtaj_vrata ( orMj , ( 35 + dubina , 0 , -2 ) , orSm , "meni"  , blok_id = 64  , kvaka = "lijevo"  )     # zadnja vrata

#stepenice lijevo i desno

#pomakni origin na ( 15 + dubina, 0 , 5) sedina - podest ispred apartmana
pomOrigin = premjesti_origin ( orMj , ( 15 + dubina ), 0 , -5 ,  orSm )

#rupe u ogradi ispred stepenica
crtaj_kvadar ( pomOrigin , ( 0 , -sirina , 0 )  , ( 0 , -sirina + 1 , 0 ) , orSm , AIR.id ,  0 )   #ispred lijevih stepenica
crtaj_kvadar ( pomOrigin , ( 0 , sirina , 0 )  , ( 0 , sirina - 1 , 0 ) , orSm , AIR.id ,  0 )   #ispred desnih stepenica

for br in  range ( -1 , -11 , -1 ):    #stepenice lijevo i desno
   crtaj_stepenice ( pomOrigin , ( br , -sirina , br   )  , ( br  , -sirina + 1 ,  br  ) , orSm , blok_id = 109 , rel_smjer  = "meni")   #stepenice lijevo
   crtaj_stepenice ( pomOrigin , ( br , sirina , br   )  , ( br  , sirina - 1 ,  br  ) , orSm , blok_id = 109 , rel_smjer  = "meni")     #stepenice desne

# lijevo dolje hala

#pomakni origin na ( 14 + dubina, sirina/2 , -15) sedina - podest ispred apartmana
pomOrigin = premjesti_origin ( orMj ,  14 + dubina, int ( - sirina / 2 ) , -15 ,  orSm )
crtaj_kvadar ( pomOrigin , (2, -14,7)  , (35,14,-5) , orSm , 98 , 1 )   # mossy coblestone tijelo
for dX in range ( 5 , 31 , 5  ) :   #lampe gore
   for dZ in range ( -10   , 11  , 5 ) :
      crtaj_kvadar ( pomOrigin , (dX,dZ,3)  , (dX,dZ,3) , orSm , 89 )

crtanje_stepenastiTunel ( pomOrigin  , orSm ,  visina=4 , sirina = 13 , duzina = 3  , uspon = -1 )  #stepenasti silazak 3 stepenice
pomOrigin2 = premjesti_origin ( pomOrigin , 3 , 0 ,  -3 , orSm )
crtanje_stepenastiTunel ( pomOrigin2  , orSm ,  visina=6 , sirina = 13 , duzina = 30  , uspon = 0 )
for br in range ( 3 ) :
   crtaj_stepenice ( pomOrigin , ( br + 2 , -13, -1 -br  )  , ( br + 2 , 13, -1 -br ) , orSm , blok_id = 109 , rel_smjer  = "odmene")
   

   
#sorter
pomOrigin =  premjesti_origin ( orMj ,  20, 0 , -15 ,  orSm )
pomSm = ortUlijevo ( ortUlijevo( orSm))

# STARI SORTER
"""
#endStorage (  pomOrigin ,  orSm , iX=-18 , iZ=19 , iY=-17  ,  materijal = 98, dv = 1 , stepenice_mat = 109 ) # iz OK
endStorage (  pomOrigin ,  orSm , iX=-28 , iZ=19 , iY=-17  ,  materijal = 98, dv = 1 , stepenice_mat = 109 ) # iz OK -iX nazad iZ lijevo
time.sleep ( 10 )
sorter_soba ( pomOrigin , pomSm ,  iX=8 , iZ=0 , iY=-7 ,  materijal = 98, dv = 1 , stepenice_mat = 109) # prvo nacrtaj sobu
time.sleep ( 10 )
crtanje_stepenastiTunel ( pomOrigin  , pomSm ,  visina=5 , sirina = 4 , duzina = 7  , uspon = -1 ) # pa tunel
for br in range ( 7 ) :
   crtaj_stepenice ( pomOrigin , ( br + 2 , -4, -1 -br  )  , ( br + 2 , 4, -1 -br ) , pomSm   , blok_id = 109 , rel_smjer  = "odmene") # pa stepenice
time.sleep ( 10 )
blok_sortera (  premjesti_origin ( pomOrigin ,  - 10 , 13 , -7 ,  orSm ) , pomSm )
"""



#katakombe

# katakombe ispod zgrade
dno = nadji_dno ( orMj , ( 0 , 0, 0 ) , orSm ) + 2 # pronadji dno ovaj +2 je nekakav iskustveni korektiv
brojalica =  0

while brojalica < 3 :
   mc.postToChat("DUBINA: %f" % ( dno ) )
   katOrigin = premjesti_origin ( orMj , 14 + dubina / 2 , 0 , dno ,  orSm )
   originBaklje = katOrigin
   for dX in range (-63,66,21):
      for dZ in range ( -63 , 66 , 21 ):
         # za testirenje zakomentirano
         katakombe ( katOrigin ,  orSm ,  iX = dX, iZ = dZ , iY=0 ) 
         a = 2
   dno += 7
   brojalica += 1
   
#put do katakombi
mining_shaht ( pomOrigin2 ,  orSm  ,  iX=10 , iZ=0 , iY=0 ,materijal = 98, dv = 1 , stepenice_mat = 109 )
#lift (  premjesti_origin ( pomOrigin ,  - 9 , 13 , -2 ,  orSm ) , pomSm )
# NOVI SORTER

crtanje_stepenastiTunel ( pomOrigin  , pomSm ,  visina=5 , sirina = 4 , duzina = 8  , uspon = -1 ) # pa tunel
for br in range ( 7 ) :
   crtaj_stepenice ( pomOrigin , ( br + 2 , -4, -1 -br  )  , ( br + 2 , 4, -1 -br ) , pomSm   , blok_id = 109 , rel_smjer  = "odmene") # pa stepenice
testKomplet ( pomOrigin , pomSm ,  iX=8 , iZ=0 , iY=-7  )    

crtaj_hopper    (   pomOrigin ,  ( -13 , 8 , -1 ) , ( -13 , 8 , -1 ) , pomSm , "lijevo" )
crtaj_hopper    (   pomOrigin ,  ( -13 , 8 , -2 ) , ( -13 , -19 , -2 ) , pomSm , "lijevo" )
crtaj_hopper    (   pomOrigin ,  (  -13 , -20 , -2 ) , (  -13 , -20 , -2 ) , pomSm , "dolje" )
crtaj_hopper    (   pomOrigin ,  ( -13 , -20 , -3 ) , ( 9 , -20 , -3 ) , pomSm , "odmene" )


#bakljada
bakljada ( originBaklje , orSm ,  dimenzije = 160 , visina = 150)



