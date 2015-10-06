# crtanje automatizirane topionice
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from crtanje2 import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

crtaj_kutiju   ( gdjeSam () , [ 2 , 0 , 0 ]  , [ 2 , 1 , 0  ] , gdjeGledam (), rel_smjer  = "meni"    ) # prednje kutije

crtaj_kutiju   ( gdjeSam () , [ 3 , -1 , 2 ]  , [ 3 , 2 , 2  ] , gdjeGledam (), rel_smjer  = "meni"    ) # srednje kutije
crtaj_pec   ( gdjeSam () , [ 3 , 0 , 1 ]  , [ 3 , 1 , 1  ] , gdjeGledam (), rel_smjer  = "meni"    ) # peci
crtaj_kutiju   ( gdjeSam () , [ 3 , 0 , 3 ]  , [ 3 , 1 , 3  ] , gdjeGledam (), rel_smjer  = "meni"    ) #gornje kutije
crtaj_hopper   ( gdjeSam () , [ 3 , 0 , 0 ]  , [ 3 , 1 , 0  ] , gdjeGledam (), rel_smjer  = "meni"    ) #doljnji hopperi
#
crtaj_hopper   ( gdjeSam () , [ 3 , 0 , 2 ]  , [ 3 , 1 , 2  ] , gdjeGledam (), rel_smjer  = "dolje"    ) #gornji hopperi
crtaj_hopper   ( gdjeSam () , [ 3 , -1 , 1 ]  , [ 3 , -1 , 1  ] , gdjeGledam (), rel_smjer  = "desno"    ) #lijevi hopper
crtaj_hopper   ( gdjeSam () , [ 3 , 2 , 1 ]  , [ 3 , 2 , 1  ] , gdjeGledam (), rel_smjer  = "lijevo"    ) #desni hopper
