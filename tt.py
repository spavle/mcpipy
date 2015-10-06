# ??????????????????????
smjer = (1,0)
rel_smjer = 0

tablica_smjera = {}     # definira se tablica prevoda
tablica_smjera [ ( 1 , 0  ) ] = ( 0 , 2 , 1 , 3 ) # gledam north
tablica_smjera [ ( -1 , 0 ) ] = ( 2 , 0 , 3 , 1 ) # gledam south
tablica_smjera [ ( 0 , 1 ) ] = ( 1 , 3 , 2 , 0 )  # gledam east
tablica_smjera [ ( 0 , -1 ) ]= ( 3 , 1 , 0 , 2 )  # gledam weast

print tablica_smjera
   
buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]

print buff

blok_dv =  buff [ rel_smjer ]

print blok_dv


#blok_dv +=  gore_dolje  # okreni naopako ako treba