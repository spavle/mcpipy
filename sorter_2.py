
import time 
from crtanje import *		#tu je funkcija koju zovem
from mc import *		


def modul_sorter2 (  orMj ,  orSm , iX=0 , iZ=0 , iY=0  ,  materijal = 98, dv = 0  , kutija = "kutija" , crtaj_kutije = "da" ):

   orMj = premjesti_origin ( orMj , iX , iZ , iY ,  orSm ) #mice gdje treba, crta ispred kutija
   if crtaj_kutije == "da" :
      if ( kutija == "kutija" ) :
         kmat = 54
      else :
         kmat = 146
      crtaj_kutiju ( orMj , [ 3   , 0, 2 ]  , [ 4   ,  0 , 2  ] , orSm , rel_smjer  = "desno" , blok_id = kmat     )
      crtaj_hopper    ( orMj , [ 3   , 0, 1 ]  , [ 3   ,  0 , 0  ] , orSm , "meni" ) # hopper ispod kutije
      crtaj_kutiju ( orMj , [ 1   , 0, 0 ]  , [ 2   ,  0 , 1  ] , orSm , rel_smjer  = "desno" , blok_id = kmat     )
      crtaj_stepenice ( orMj , ( 1   , 0 ,  2  ) , ( 1   , 0 ,  2  ) , orSm , blok_id = 53 , rel_smjer  = "odmene" , gore_dolje = "ne"  )
      crtaj_comparator ( orMj , [ 0   , 0, 0 ]  , [ 0   ,  0 , 0 ]  , orSm , rel_smjer  = "meni" ) #ima li stvari u kutiji
   crtaj_kvadar ( orMj , [ 8   , 0, 0 ]  , [ 8   , 0 , 0  ] , orSm , materijal , 2 ) # doljnji blok
   crtaj_kvadar ( orMj , [ 7   , 0, 1 ]  , [ 9   , 0 , 1  ] , orSm , materijal , 2 ) # srednji blokovi
   crtaj_kvadar ( orMj , [ 6   , 0, 2 ]  , [ 8   , 0 , 2  ] , orSm , materijal , 2 ) # gornji blokovi
   
   crtaj_repeater ( orMj , [ 8   , 0, 1 ]  , [ 8   ,  0 , 1  ]  , orSm , rel_smjer  = "meni" )
   crtaj_redstonetorch ( orMj , [ 6   , 0, 1 ]  ,  orSm  , "meni" )
   
   crtaj_redstonedust ( orMj , [ 9   , 0, 2 ]  , [ 9   ,  0 , 2  ] , orSm )
   
   crtaj_redstonedust ( orMj , [ 8   , 0, 3 ]  , [ 7   ,  0 , 3  ] , orSm )
   crtaj_comparator ( orMj , [ 6   , 0, 3 ]  , [ 6   ,  0 , 3 ]  , orSm , rel_smjer  = "odmene" )
   
   crtaj_hopper    ( orMj , [ 5   , 0, 4 ]  , [ 5   ,  0 , 4  ] , orSm , "desno" ) # gornji
   
   sto =  '{TransferCooldown:0,Items:[0:{Slot:0b,id:"item_frame",Count:1b,Damage:0s,},1:{Slot:1b,id:"flower_pot",Count:1b,Damage:0s,},2:{Slot:2b,id:"flower_pot",Count:1b,Damage:0s,},3:{Slot:3b,id:"flower_pot",Count:1b,Damage:0s,},4:{Slot:4b,id:"flower_pot",Count:1b,Damage:0s,},],id:"Hopper",Lock:"",}' 
   bla = rel2abs ( orMj , ( 5 , 0 , 3  ) , orSm )
   time.sleep ( 0.1 )
   mc.setBlockWithNBT(bla,154,smjer_hoppera ( orSm , "meni")  , sto )   #hopper gleda meni
   
   crtaj_hopper    ( orMj , [ 5   , 0, 2 ]  , [ 5   ,  0 , 2  ] , orSm , "meni" ) # doljnji
   
   
   

def sorter2 (  orMj , orSm   ) :
   for br in range (  0, 21 ):
      if br % 2 == 1 :
         koja_kutija = "kutija"
      else:
         koja_kutija = "druga_kutija"
            
      modul_sorter2 (  orMj ,  orSm , iX=3 , iZ=br , iY=0  ,  materijal = 98, dv = 0  , kutija = koja_kutija , crtaj_kutije = "da" )
   orSm = ortUlijevo ( ortUlijevo ( orSm ))
   
   for br in range (  0, - 21 , -1 ):
      if br % 2 == 1 :
         koja_kutija = "kutija"
      else:
         koja_kutija = "druga_kutija"
            
      modul_sorter2 (  orMj ,  orSm , iX=3 , iZ=br , iY=0  ,  materijal = 98, dv = 0  , kutija = koja_kutija , crtaj_kutije = "da" )


if __name__ == "__main__":    #direktan poziv
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   sorter2 (  orMj , orSm   )