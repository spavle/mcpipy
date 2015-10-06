# crtanje automatizirani sorter
#definicija objekta i poziv rutine za crtanje
import time 
import sys
from crtanje import *		#tu je funkcija koju zovem
from popis_blokova import *

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


#sandstone glatki
materijal = 24
dv = 2

orMj = gdjeSam ()
orSm = gdjeGledam ()
   
#korekcija polozaja
orMjA = gdjeSam ()

mc.postToChat("orginal: %s " %  orMj    )

def pocetak_sortera ( orMj ) :
   mc.postToChat("orginal: %s " %  orMj    )
   crtaj_hopper    ( orMj , [ 2  , 1, 4 ]  , [ 2 ,  1 , 4  ] , orSm , "odmene" ) # gornji
   crtaj_kutiju ( orMj , [ 1 , 1, 5 ]  , [ 2 ,  1 , 5  ] , orSm , rel_smjer  = "lijevo" )
   for br in range ( 0 , 4 ):
      crtaj_stepenice ( orMj , [ 2 , 5 - br , 0 + br ]  , [ 2 ,  5 - br , 0 + br  ] , orSm , blok_id = 128 , rel_smjer  = "desno" )

def crtaj_modul ( orMj , dX  ):
   """
   dX - udaljenost modula
   koja_kutija - par - obicna , nepar - traped
   """
   """
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv  )
   """
   crtaj_kvadar ( orMj , [ 3 + dX , 0, 0 ]  , [ 3 + dX , -2 , 2  ] , orSm , materijal , 2 ) # blok
   crtaj_kvadar ( orMj , [ 3 + dX , -2, 2 ]  , [ 3 + dX ,  -2 , 2  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3 + dX , -1, 1 ]  , [ 3 + dX ,  -1 , 1  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3 + dX , 0, 0 ]  , [ 3 + dX ,  0 , 0  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3 + dX , -2, 0 ]  , [ 3 + dX ,  -2 , 0  ] , orSm , 0 , 0 ) # zrak
   crtaj_redstonedust ( orMj , [ 3 + dX , -2, 2 ]  , [ 3 + dX ,  -2 , 2  ] , orSm )
   crtaj_redstonedust ( orMj , [ 3 + dX , -1, 3 ]  , [ 3 + dX ,  -1 , 3  ] , orSm )
   crtaj_redstonetorch ( orMj , [ 3 + dX , 1, 1 ]  ,  orSm  , "desno" )  
   crtaj_comparator ( orMj , [ 3 + dX , 0, 3 ]  , [ 3 + dX ,  0 , 3 ]  , orSm , rel_smjer  = "lijevo" )
   crtaj_repeater ( orMj , [ 3 + dX , -1, 1 ]  , [ 3 + dX ,  -1 , 1  ]  , orSm , rel_smjer  = "desno" )
   
   crtaj_hopper    ( orMj , [ 3 + dX , 1, 2 ]  , [ 3 + dX ,  1 , 3  ] , orSm , "desno" ) # dva doljnja
   crtaj_hopper    ( orMj , [ 3 + dX , 1, 4 ]  , [ 3 + dX ,  1 , 4  ] , orSm , "odmene" ) # gornji
   
   sto =  '{TransferCooldown:0,Items:[0:{Slot:0b,id:"%s",Count:4b,Damage:%ss,},1:{Slot:1b,id:"%s",Count:5b,Damage:%ss,},2:{Slot:2b,id:"%s",Count:5b,Damage:%ss,},3:{Slot:3b,id:"%s",Count:5b,Damage:%ss,},4:{Slot:4b,id:"%s",Count:5b,Damage:%ss,},],id:"Hopper",Lock:"",}' % ( popis [ dX ] [ 0 ] , popis [ dX ]  [ 1 ]  , popis [ dX ]  [ 0 ] , popis [ dX ]  [ 1 ] , popis [ dX ]  [ 0 ] , popis [ dX ]  [ 1 ] , popis [ dX ]  [ 0 ] , popis [ dX ]  [ 1 ] , popis [ dX ]  [ 0 ] , popis [ dX ]  [ 1 ] )
   bla = rel2abs ( orMj , ( 3 + dX , 1 ,  3  ) , orSm )
   mc.postToChat("orginal: %s %s " %  ( dX , bla )    )
   time.sleep ( 1 )
   mc.setBlockWithNBT(bla,154,smjer_hoppera ( orSm , "desno")  , sto )   #hopper gleda na istok 
   bla = rel2abs ( orMj , ( 3 + dX , 1 ,  2  ) , orSm )
   mc.postToChat("orginal: %s %s " %  ( dX , bla )    )
   time.sleep ( 1 )
   mc.setBlockWithNBT(bla,154,smjer_hoppera ( orSm , "desno")  , sto )   #hopper gleda na istok 
   #bla = rel2abs ( orMj , ( 3 + dX , 5 ,  2  ) , orSm )
   #mc.setBlock(bla,53,4  )       #oak wood stairs naopako, gledaju na istok
   crtaj_stepenice ( orMj , ( 3 + dX , 5 ,  2  ) , ( 3 + dX , 5 ,  2  ) , orSm , blok_id = 53 , rel_smjer  = "desno" , gore_dolje = "da"  )

   
   kutija = 54
   tkutija = 146
   if ( int ( dX ) % 2 == 1 ) :
      kmat = kutija
   else :
      kmat = tkutija
   crtaj_kutiju ( orMj , [ 3 + dX , 2, 2 ]  , [ 3 + dX ,  3 , 2  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     )
   crtaj_hopper    ( orMj , [ 3 + dX , 3, 1 ]  , [ 3 + dX ,  3 , 0  ] , orSm , "desno" ) # hopper ispod kutije
   crtaj_kutiju ( orMj , [ 3 + dX , 4, 1 ]  , [ 3 + dX ,  5 , 0  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     ) # dodatne kutije
   
def kraj ( orMj ,dX , duzina ) :
   dX += 1
   crtaj_hopper    ( orMj , [ 3 + dX , 1, 4 ]  , [ 3 + dX ,  1 , 4  ] , orSm , "odmene" ) # dovod i razmak od sortirke
   
   for brojalica in range ( 0 ,  duzina   ) :
      dX += 1                       # translacija "udalj"
      kutija = 54                   #materijali za kutije
      tkutija = 146
      if ( int ( dX ) % 2 == 1 ) :
         kmat = kutija
      else :
         kmat = tkutija

      crtaj_hopper    ( orMj , [ 3 + dX , 1, 4 ]  , [ 3 + dX ,  1 , 4  ] , orSm , "odmene" ) # gornji hopper
      crtaj_hopper    ( orMj , [ 3 + dX , 1, 0 ]  , [ 3 + dX ,  1 , 3  ] , orSm , "desno" ) # razvod po kutijama
      crtaj_kutiju ( orMj , [ 3 + dX , 2, 0 ]  , [ 3 + dX ,  3 , 3  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     ) #kutije
      
 

 
def sorter  ( dX , dZ , dY , duzina , rep ):

   # origin ispred na sredini 
   orMj   = rel2abs ( orMjA ,  ( dX , dZ , dY )   , orSm  ) 
   bla = orMj [ 1 ]
   orMj [ 1 ] = orMj [ 2 ]
   orMj [ 2 ] = bla
   
   mc.postToChat("orginal: %s " %  orMj    )

   

   pocetak_sortera ( orMj )
   
   for br in range (  0, duzina ):
      crtaj_modul ( orMj , br )
   
   kraj (  orMj , br , rep) 
   
   

