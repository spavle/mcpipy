# LAME TOOL

#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


"""
crtaj_stepenice ( gdjeSam () , ( 5 , -2 , 0) , ( 5 , 2 , 0) , gdjeGledam () , rel_smjer = 3 )
crtaj_stepenice ( gdjeSam () , ( 6 , 3 , 0) , ( 11 , 3 , 0) , gdjeGledam () , rel_smjer = 1 )
crtaj_stepenice ( gdjeSam () , ( 12 , -2 , 0) , ( 12 , 2 , 0) , gdjeGledam () , rel_smjer = 2 )
crtaj_stepenice ( gdjeSam () , ( 6 , -3 , 0) , ( 11 , -3 , 0) , gdjeGledam () , rel_smjer = 0 )
crtaj_stepenice ( gdjeSam () , ( 5 , 3 , 0) , ( 5 , 3 , 0) , gdjeGledam () , rel_smjer = 3 )
crtaj_stepenice ( gdjeSam () , ( 12 , 3 , 0) , ( 12 , 3 , 0) , gdjeGledam () , rel_smjer = 1 )
crtaj_stepenice ( gdjeSam () , ( 12 , -3 , 0) , ( 12 , -3 , 0) , gdjeGledam () , rel_smjer = 2 )
crtaj_stepenice ( gdjeSam () , ( 5 , -3 , 0) , ( 5 , -3 , 0) , gdjeGledam () , rel_smjer = 0 )


#crtaj_deblo ( origin , poc , kraj , smjer , blok_id = 53 , podtip = 0 , rel_smjer = 0   ) 

# lijevo/desno
crtaj_deblo ( gdjeSam () , ( 3 , -1 , 0 ) , (3 ,1 , 0 ) , gdjeGledam () , 17, 0 , 1 )

# naprijed nazad

crtaj_deblo ( gdjeSam () , ( 3 , -3 , 0 ) , (7, -3 , 0 ) , gdjeGledam () , 17, 0 , 2 )

# gore/ dolje
crtaj_deblo ( gdjeSam () , ( 3 , 3 , 0 ) , (3 ,3 , 5 ) , gdjeGledam () , 17, 0 , 0 )
"""

""""
crtaj_deblo ( gdjeSam () , ( 3 , 0 , 0 ) , (3 ,0 , 7 ) , gdjeGledam () , 17, 0 , 0 )

crtaj_baklju ( gdjeSam () , ( 2 , 0 , 1 ) ,  gdjeGledam () ,  rel_smjer = 2   )
crtaj_baklju ( gdjeSam () , ( 3 , 1 , 2 ) ,  gdjeGledam () ,  rel_smjer = 0   )
crtaj_baklju ( gdjeSam () , ( 4 , 0 , 3 ) ,  gdjeGledam () ,  rel_smjer = 3   )
crtaj_baklju ( gdjeSam () , ( 3 , -1 , 4 ) ,  gdjeGledam () ,  rel_smjer = 1   )
crtaj_baklju ( gdjeSam () , ( 3 , 0 , 8 ) ,  gdjeGledam () ,  rel_smjer = 4   )
"""

# ograda

crtaj_kvadar ( gdjeSam () , [ 4 , -5 , 0 ]  , [ 4 , 5 , 0  ] , gdjeGledam () , 85 , 0 ) #prednja ograda
#crtaj_vrataograde ( origin , poc ,  smjer , blok_id = 107 ,  rel_smjer = 0   )
crtaj_vrataograde ( gdjeSam () , [ 4 , -1 , 0 ]   , gdjeGledam () , 107 , 0 ) #prednja ograda

crtaj_kvadar ( gdjeSam () , [ 1 , -4 , 0 ]  , [ 3 , -4 , 0  ] , gdjeGledam () , 85 , 0 ) #prednja ograda
#crtaj_vrataograde ( origin , poc ,  smjer , blok_id = 107 ,  rel_smjer = 0   )
crtaj_vrataograde ( gdjeSam () , [ 2 , -4 , 0 ]   , gdjeGledam () , 107 , 1 ) #prednja ograda

""""
for br in range (0,4) :

   crtaj_stepenice ( gdjeSam () , ( 4 + 2 * br , -1 , 0 )  , ( 3 + 2 * br  , 1 , 0 ) , gdjeGledam ()  ,  br  )
#crtaj_stepenice ( origin , poc  , smjer , blok_id = 53 , rel_smjer = 0  , gore_dolje = 0  )
"""

   
"""


crtaj_kvadar ( gdjeSam () , ( 1 , 0 , 0 )  , ( 3 , 0 , 2 ) , gdjeGledam () , 1 ) 
#crtaj_kvadar ( gdjeSam () , ( 2 , 0 , 0 )  , ( 2 ,0 , 1 ) , gdjeGledam () , 0 ) 
crtaj_vrata ( gdjeSam () , ( 2 , 0 , 0 )  , gdjeGledam () , 3 )

"""