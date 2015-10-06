# ????
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

filter ( orMj , ( 0 , 0 , 0 ) , orSm ,  visina = 6 ,   sirina = 7 , dubina = 29, baklje="da") 
