# podzemna citadela SA GALERIJOM OKOLO

from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

sirina = 38
dubina = 50

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#mossy coblestone tijelo
crtaj_kvadar ( orMj , (6, -sirina-6,-18)  , (1+8 + 6 + 4 + dubina,sirina + 6,3) , orSm , 98 , 1 )
crtaj_kvadar ( orMj , (11+3,-sirina,-16)  , (11+3 + dubina ,sirina,-16) , orSm , 2 )
for dX in range ( 18 , 18 + dubina , 8 ) :
   for dZ in range ( -sirina - 2  ,sirina + 8 , 8 ) :
      crtaj_kvadar ( orMj , (dX,dZ,-16)  , (dX,dZ,-16) , orSm , 89 )
      crtaj_kvadar ( orMj , (dX,dZ,1)  , (dX,dZ,1) , orSm , 89 )

crtaj_kvadar ( orMj , (11,-sirina - 3,-5)  , (11+6+dubina,sirina +3,0) , orSm , AIR.id ,  0 )   #podest okolo
crtaj_kvadar ( orMj , (13,-sirina - 1,-5)  , (11+4+dubina,sirina +1,-5) , orSm , 85 ,  0 )   #ograda okolo

crtaj_kvadar ( orMj , (11+3,-sirina ,-15)  , (11+3+dubina,sirina ,0) , orSm , AIR.id ,  0 )     #centralna rupa

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

#4 stepenice dolje
for br in range (5):
   crtaj_kvadar ( orMj , (6+br,-2,0-br)  , (6+br,2,3-br) , orSm , AIR.id , blok_dv = 0 )
   crtaj_kvadar ( orMj , (6+br,-2,-1-br)  , (6+br,2,-1-br) , orSm , 2 )
   
# podest 9 x 7 +++
crtaj_kvadar ( orMj , (11,-3,-6)  , (19,3,-16) , orSm ,98 , 1 )
crtaj_kvadar ( orMj , (11,-3,-6)  , (19,3,-6) , orSm , 2 )
crtaj_kvadar ( orMj , ( 19 , -3 , -5 )  , ( 19 , -3 , -5 ) , orSm , 89 )
crtaj_kvadar ( orMj , ( 19 , 3 , -5 )  , ( 19 , 3 , -5 ) , orSm , 89 )
crtaj_kvadar ( orMj , (11,-4,-5)  , (19,4,-5) , orSm , AIR.id ,  0 ) # prekid u ogradi
crtaj_kvadar ( orMj , (19,-4,-5)  , (19,4,-5) , orSm , 89 )       # lampe na podestu
crtaj_kvadar ( orMj , (19,-3,-5)  , (19,3,-5) , orSm , 85 ,  0 )  # OGRADA NAPRIJED

# lijeve stepenice 3 dolje
for br in range (4):
   crtaj_kvadar ( orMj , (14,-4 - br ,-7 -br)  , (19,-4 -br,-16) , orSm , 98 , 1 )
   crtaj_kvadar ( orMj , (14,-4 - br ,-6 -br)  , (19,-4 -br,-6 -br) , orSm , 2 )

# desne stepenice 3 dolje
for br in range (4):
   crtaj_kvadar ( orMj , (14,4 + br ,-7 -br)  , (19,4 +br,-16) , orSm ,  98 , 1 )
   crtaj_kvadar ( orMj , (14,4 + br ,-6 -br)  , (19,4 +br,-6 -br) , orSm , 2 )
   
#lijevi podest
crtaj_kvadar ( orMj , (14,-7,-10)  , (19,-12,-16) , orSm ,  98 , 1 )
crtaj_kvadar ( orMj , (14,-7,-9)  , (19,-12,-9) , orSm , 2 )
crtaj_kvadar ( orMj , ( 19 , -12 , -8 )  , ( 19 , -12 , -8 ) , orSm , 89 )

#desni podest
crtaj_kvadar ( orMj , (14,7,-10)  , (19,12,-16) , orSm ,  98 , 1 )
crtaj_kvadar ( orMj , (14,7,-9)  , (19,12,-9) , orSm , 2 )
crtaj_kvadar ( orMj , ( 19 , 12 , -8 )  , ( 19 , 12 , -8 ) , orSm , 89 )

#lijeve stepenice 5 dolje
for br in range (6):
   crtaj_kvadar ( orMj , (20+br,-7,-11-br)  , (20+br,-12,-16) , orSm ,  98 , 1 )
   crtaj_kvadar ( orMj , (20+br,-7,-10-br)  , (20+br,-12,-10-br) ,  orSm , 2 )
crtaj_kvadar ( orMj , ( 19 , -5 , -14 )  , ( 19 , -5 , -14 ) , orSm , 89 )
crtaj_kvadar ( orMj , ( 26 , -13 , -15 )  , ( 26 , -13 , -15 ) , orSm , 89 )


#desne stepenice 5 dolje
for br in range (6):
   crtaj_kvadar ( orMj , (20+br,7,-11-br)  , (20+br,12,-16) , orSm ,  98 , 1 )
   crtaj_kvadar ( orMj , (20+br,7,-10-br)  , (20+br,12,-10-br) , orSm , 2 )
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
crtanje_stepenastiTunel ( pomOrigin  , orSm ,  visina=4 , sirina = 13 , duzina = 3  , uspon = -1 )  #stepenasti silazak 3 stepenice
pomOrigin2 = premjesti_origin ( pomOrigin , 3 , 0 ,  -3 , orSm )
crtanje_stepenastiTunel ( pomOrigin2  , orSm ,  visina=6 , sirina = 13 , duzina = 30  , uspon = 0 )
for br in range ( 3 ) :
   crtaj_stepenice ( pomOrigin , ( br + 2 , -13, -1 -br  )  , ( br + 2 , 13, -1 -br ) , orSm , blok_id = 109 , rel_smjer  = "odmene")


