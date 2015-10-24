# crta malu kucu sa puno vrata, u for petlju se stavi koliko kuca da crta

from mc import * #import api-ja
from crtaj_vrata import *
from crtaj_blok import *
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

for nr in range ( 0 , 1 , 15):
   crtaj_blok ( 1 + nr , -1 , -2 , 5+ nr , 0 , 2 , 98 )   # kameni temelji
   crtaj_blok ( 1 + nr , 1 , -2 , 5 + nr , 2 , 2 , 5 , 2)    # drveni zidovi
   crtaj_blok ( 2 + nr , 0 , -1 , 4 + nr , 1 , 1 , 0 )    # prazno unutra

   crtaj_blok ( 1+ nr , 1, -2 , 1 + nr ,2 , -2 , 5  )  # stupovi na uglovima
   crtaj_blok ( 1+ nr , 1, 2 , 1 + nr ,2 , 2 , 5  )
   crtaj_blok ( 5+ nr , 1, -2 , 5 + nr ,2 , -2 , 5  )
   crtaj_blok ( 5+ nr , 1, 2 , 5 + nr ,2 , 2 , 5  )

   crtaj_vrata ( 1 + nr , 0 , 0 , 194 , 0 )
   crtaj_vrata ( 1 + nr , 0 , -1 , 194 , 0 )
   crtaj_vrata ( 1 + nr , 0 , 1 , 194 , 0 )

   crtaj_vrata ( 5 + nr , 0 , 0 , 194 , 2 )
   crtaj_vrata ( 5 + nr , 0 , -1 , 194 , 2 )
   crtaj_vrata ( 5 + nr , 0 , 1 , 194 , 2 )

   crtaj_vrata ( 2 + nr , 0 , -2 , 194 , 1 )
   crtaj_vrata ( 3 + nr , 0 , -2 , 194 , 1 )
   crtaj_vrata ( 4 + nr , 0 , -2 , 194 , 1 )

   crtaj_vrata ( 2 + nr , 0 , 2 , 194 , 3 )
   crtaj_vrata ( 3 + nr , 0 , 2 , 194 , 3 )
   crtaj_vrata ( 4 + nr , 0 , 2 , 194 , 3 )

