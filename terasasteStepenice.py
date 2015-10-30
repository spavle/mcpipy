# Test novih funkcija iz modula CRTANJE.PY
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

crtaj_terase ( gdjeSam () , ( -1 , 0 , 0 ) ,  gdjeGledam () , korak = 1 , visina = 35 , sirina = 1, baklje="ne")