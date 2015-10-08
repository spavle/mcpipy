# mob spawner - simple
#definicija objekta i poziv rutine za crtanje

from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#sandstone glatki
materijal = 1
dv = 1
uZraku = 34 # because of witchs
nivoa=11
visinaNivoa = 5


#crtaj_kvadar ( orMj , [ 8 , 8, uZraku -6 ]  , [ 11 , 11 , uZraku - 1   ] , orSm , STONE.id , 2 ) # lijevak ispod netreba
crtaj_kvadar ( orMj , [ 0 , 0, uZraku ]  , [ 18 , 18 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , STONE.id , 2 ) # main body
crtaj_kvadar ( orMj , [ 9 , 9, uZraku - 6 ]  , [ 9 , 9 , uZraku + nivoa*visinaNivoa    ] , orSm , AIR.id , 2 ) # sredisnja rupa
# estetika
crtaj_kvadar ( orMj , [ 0 , 0, uZraku - 6 ]  , [ 4 , 4 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # lijeva dolje rupa
crtaj_kvadar ( orMj , [ 0 , 14, uZraku - 6 ]  , [ 4 , 18 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # desna dolje rupa
crtaj_kvadar ( orMj , [ 14 , 0, uZraku - 6 ]  , [ 18 , 4 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # lijeva dolje rupa
crtaj_kvadar ( orMj , [ 14 , 14, uZraku - 6 ]  , [ 18 , 18 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # desna dolje rupa


for br in range ( nivoa ) :
   crtaj_kvadar ( orMj , [ 2 , 6, uZraku + 3 + br * visinaNivoa ]  , [ 16 , 12 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # main hole uzduzna
   crtaj_kvadar ( orMj , [ 6 , 2, uZraku + 3 + br * visinaNivoa ]  , [ 12 , 16 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # main hole popprecna
   crtaj_kvadar ( orMj , [ 1 , 9, uZraku + 1 + br * visinaNivoa ]  , [ 17 , 9 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # uzduzna voda duga
   crtaj_kvadar ( orMj , [ 5 , 5, uZraku + 1 + br * visinaNivoa ]  , [ 13 , 5 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # uzduzna voda lijeva
   crtaj_kvadar ( orMj , [ 5 , 13, uZraku + 1 + br * visinaNivoa ]  , [ 13 , 13 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # uzduzna voda desna
   crtaj_kvadar ( orMj , [ 9 , 1, uZraku + 1 + br * visinaNivoa ]  , [ 9 , 17 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # poprecna voda duga
   crtaj_kvadar ( orMj , [ 5 , 5, uZraku + 1 + br * visinaNivoa ]  , [ 5 , 13 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # poprecna voda bliza
   crtaj_kvadar ( orMj , [ 13 , 5, uZraku + 1 + br * visinaNivoa ]  , [ 13 , 13 , uZraku +  4 + br * visinaNivoa  ] , orSm , AIR.id , 0 ) # poprecna voda dalja
   
   crtaj_kvadar ( orMj , [ 9 , 1, uZraku + 1 + br * visinaNivoa ]  , [ 9 , 1 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water uzduzno blizi
   crtaj_kvadar ( orMj , [ 9 , 17, uZraku + 1 + br * visinaNivoa ]  , [ 9 , 17 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water uzduzno dalji
   crtaj_kvadar ( orMj , [ 1 , 9, uZraku + 1 + br * visinaNivoa ]  , [ 1 , 9 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water poprecno blizi
   crtaj_kvadar ( orMj , [ 17 , 9, uZraku + 1 + br * visinaNivoa ]  , [ 17 , 9 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water poprecno dalji

   crtaj_kvadar ( orMj , [ 9 , 1, uZraku + 2 + br * visinaNivoa ]  , [ 9 , 1 , uZraku +  4 + br * visinaNivoa  ] , orSm ,  materijal , dv ) #kamen iznad water water uzduzno blizi
   crtaj_kvadar ( orMj , [ 9 , 17, uZraku + 2 + br * visinaNivoa ]  , [ 9 , 17 , uZraku +  4 + br * visinaNivoa  ] , orSm , materijal , dv ) #kamen iznad water water uzduzno dalji
   crtaj_kvadar ( orMj , [ 1 , 9, uZraku + 2 + br * visinaNivoa ]  , [ 1 , 9 , uZraku +  4 + br * visinaNivoa  ] , orSm , materijal , dv ) #kamen iznad water water poprecno blizi
   crtaj_kvadar ( orMj , [ 17 , 9, uZraku + 2 + br * visinaNivoa ]  , [ 17 , 9 , uZraku +  4 + br * visinaNivoa  ] , orSm , materijal , dv ) #kamen iznad water water poprecno dalji

   
   crtaj_kvadar ( orMj , [ 5 , 5, uZraku + 1 + br * visinaNivoa ]  , [ 5 , 5 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water dolje lijevo
   crtaj_kvadar ( orMj , [ 5 , 13, uZraku + 1 + br * visinaNivoa ]  , [ 5 , 13 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water dolje desno
   crtaj_kvadar ( orMj , [ 13 , 5, uZraku + 1 + br * visinaNivoa ]  , [ 13 , 5 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water gore lijevo
   crtaj_kvadar ( orMj , [ 13 , 13, uZraku + 1 + br * visinaNivoa ]  , [ 13 , 13 , uZraku +  1 + br * visinaNivoa  ] , orSm , 9 , 0 ) # water gore desno

   crtaj_kvadar ( orMj , [ 5 , 5, uZraku + 2 + br * visinaNivoa ]  , [ 5 , 5 , uZraku +  4 + br * visinaNivoa  ] , orSm , materijal , dv ) #kamen iznad water dolje lijevo
   crtaj_kvadar ( orMj , [ 5 , 13, uZraku + 2 + br * visinaNivoa ]  , [ 5 , 13 , uZraku + 4 + br * visinaNivoa  ] , orSm ,  materijal , dv ) #kamen iznad  water dolje desno
   crtaj_kvadar ( orMj , [ 13 , 5, uZraku + 2 + br * visinaNivoa ]  , [ 13 , 5 , uZraku +  4 + br * visinaNivoa  ] , orSm ,  materijal , dv ) #kamen iznad  water gore lijevo
   crtaj_kvadar ( orMj , [ 13 , 13, uZraku + 2 + br * visinaNivoa ]  , [ 13 , 13 , uZraku +  4 + br * visinaNivoa  ] , orSm ,  materijal , dv ) #kamen iznad  water gore desno
   
   
   #slabstoni   
   for dX in range ( 3 , 16 , 4 ) :
      for dY in range ( 3 , 16 , 4 ) :
         crtaj_kvadar ( orMj , [ dX , dY, uZraku + 3 + br * visinaNivoa ]  , [ dX , dY , uZraku +  3 + br * visinaNivoa  ] , orSm , 44 , 5 ) # stoneslabi protiv pauka
   
   
# lampe na vrhu

for dX in range ( 1 , 19 , 5 ) :
   for dY in range ( 1 , 19 , 5 ) :
      crtaj_kvadar ( orMj , [ dX , dY , uZraku + nivoa*visinaNivoa + 2 ]  , [ dX , dY , uZraku + nivoa*visinaNivoa + 2   ] , orSm , 89 , 0 ) # on top

# estetika
crtaj_kvadar ( orMj , [ 0 , 0, uZraku - 6 ]  , [ 4 , 4 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # lijeva dolje rupa
crtaj_kvadar ( orMj , [ 0 , 14, uZraku - 6 ]  , [ 4 , 18 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # desna dolje rupa
crtaj_kvadar ( orMj , [ 14 , 0, uZraku - 6 ]  , [ 18 , 4 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # lijeva dolje rupa
crtaj_kvadar ( orMj , [ 14 , 14, uZraku - 6 ]  , [ 18 , 18 , uZraku + nivoa*visinaNivoa + 1   ] , orSm , AIR.id , 2 ) # desna dolje rupa

# razbijalica
crtaj_kvadar ( orMj , ( 6  , 6 , 1 )  , (  13 , 13 , 1 ) , orSm ,  89 , 0 ) # glowstone okolo
crtaj_kvadar ( orMj , ( 7  , 7 , 1 )  , (  12 , 12 , 1 ) , orSm , 44 , 5 ) # stonebrick slab kocka


crtaj_kvadar ( orMj , ( 8  , 7 , 0 )  , (  12 , 12 , 0 ) , orSm , 154 , smjer_hoppera ( orSm , "meni" ) ) # hopperi spod stoneslaba
crtaj_kvadar ( orMj , ( 7  , 6 , 0 )  , (  7 , 12 , 0 ) , orSm , 154 , smjer_hoppera ( orSm , "lijevo" ) ) # hopperi spod stoneslaba za skupljanje
crtaj_kutiju ( orMj , ( 7  , 4 , 0 )  , (  7 ,5 , 0 ) , orSm , rel_smjer  = "meni" , blok_id = 54     )  #kutija je malo pomaknuta da stanu glowestoni

crtaj_kvadar ( orMj , ( -2  , -2 , -1 )  , (  10 , 10 , -1 ) , orSm ,  89 , 0 ) # glowstone podloga

   




