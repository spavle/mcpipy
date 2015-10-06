#Testiranje NBT atributa

import time 
import sys
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


"""
print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print '/give spavle axe'
"""

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#oakwood slab
materijal = 126
dv = 8


#spawnEntity(type,x,y,z,tags)

# ++++++++++++++++++++++++++++++++++++++++++ NAPRAVI NESTO U SVIJETU ITEM
#mc.spawnEntity('Item',2,2,2,'{Item:{id:283,Count:25}}')

# ++++++++++++++++++++++++++++++++++++++++++ NAPRAVI NESTO U SVIJETU ITEM
#mc.spawnEntity('Item',3,0,3,'{Item:{id:389,Count:25}}')

playerPos = mc.player.getPos()

#bla = rel2abs ( orMj , ( 2  , 0 ,  0  ) , orSm )

# +++++++++++++++++++++++++++++++++++++++++++++ GENERIRA KONJA
id = mc.spawnEntity('EntityHorse', int ( playerPos.x + 1 ) ,int ( playerPos.y ), int ( playerPos.z ), "{NoAI:0,Type:2,Variant:3,Tame:1}")
print id


#bla = rel2abs ( orMj , ( 5  , 0 ,  0  ) , orSm )


#bla = rel2abs ( orMj , ( 7  , 0 ,  0  ) , orSm )
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Generira zeca
#print mc.spawnEntity("Rabbit",4,1,4,"{}")

#crtaj_kvadar ( orMj , ( 1  , -1 , -1 ) , ( 3 , 1 , -1 ) , orSm , materijal , dv ) # zrak iznad stepenica

#bla = rel2abs ( orMj , ( 5  , 0 ,  0  ) , orSm )

# +++++++++++++++++++++++++++++++++++++ GENERIRA ISPISANI SIGN
#mc.setBlockWithNBT(bla,63,5,"{id:\"Sign\",Text1:\"Line1\",Text2:\"Pablo\",Text3:\"Line3\",Text4:\"Line4\"}")

# GENERIRA PUNU KUTIJU
#mc.setBlockWithNBT(bla,54,1,'{Items:[0:{Slot:0b,id:"minecraft:stone",Count:2b,Damage:4s,},1:{Slot:1b,id:"minecraft:dirt",Count:5b,Damage:0s,},2:{Slot:2b,id:"minecraft:diamond_axe",Count:55b,Damage:0s,},3:{Slot:3b,id:"minecraft:dirt",Count:5b,Damage:0s,},4:{Slot:4b,id:"minecraft:dirt",Count:5b,Damage:0s,},],id:"Hopper",Lock:"",}' )
#bla = rel2abs ( orMj , ( 1  , 0 ,  0  ) , orSm )
#print ( mc.getBlockWithNBT (bla) )
#print mc.getHeight (bla[0] , bla[1] )
#[12:09:39] [Thread-248/INFO]: [CHAT] Block(54, 2, '{Items:[0:{Slot:1b,id:"minecraft:diamond_axe",Count:1b,Damage:0s,},1:{Slot:13b,id:"minecraft:dirt",Count:22b,Damage:0s,},],id:"Chest",Lock:"",}')
#[12:32:40] [Thread-322/INFO]: [CHAT] Block(154, 0, '{TransferCooldown:0,Items:[0:{Slot:0b,id:"minecraft:dirt",Count:2b,Damage:0s,},1:{Slot:1b,id:"minecraft:dirt",Count:5b,Damage:0s,},2:{Slot:2b,id:"minecraft:dirt",Count:5b,Damage:0s,},3:{Slot:3b,id:"minecraft:dirt",Count:5b,Damage:0s,},4:{Slot:4b,id:"minecraft:dirt",Count:5b,Damage:0s,},],id:"Hopper",Lock:"",}')

"""  +++++++++++++++++++++ GENERIRA POPUNJENE HOPPERE
popis = (  
( "minecraft:cobblestone" , 0) , 
( "minecraft:dirt" , "0" ) ,
( "minecraft:stone" ,  "0" ) ,
( "minecraft:chest" , "0") ,
( "minecraft:stone" , "3" ) ,
)
#print 'jao " j o j "  pazi navodnika '
vrtilica = 1
for br in popis :
   
   sto =  '{TransferCooldown:0,Items:[0:{Slot:0b,id:"%s",Count:2b,Damage:%ss,},1:{Slot:1b,id:"%s",Count:5b,Damage:%ss,},2:{Slot:2b,id:"%s",Count:5b,Damage:%ss,},3:{Slot:3b,id:"%s",Count:5b,Damage:%ss,},4:{Slot:4b,id:"%s",Count:5b,Damage:%ss,},],id:"Hopper",Lock:"",}' % ( br [ 0 ] , br [ 1 ]  , br [ 0 ] , br [ 1 ] , br [ 0 ] , br [ 1 ] , br [ 0 ] , br [ 1 ] , br [ 0 ] , br [ 1 ] )
   bla = rel2abs ( orMj , ( 5 + vrtilica , 0 ,  0  ) , orSm )
   mc.setBlockWithNBT(bla,154,0 , sto )
   vrtilica = vrtilica + 1
   
"""
"""

[13:15:41] [Thread-61/INFO]: [CHAT] Block(54, 2, '{Items:[
0:{Slot:0b,id:"minecraft:stone",Count:64b,Damage:0s,},
1:{Slot:1b,id:"minecraft:stone",Count:64b,Damage:1s,},
2:{Slot:2b,id:"minecraft:stone",Count:64b,Damage:3s,},
],id:"Chest",Lock:"",}')

###
"""

   
   
   



"""
mc.postToChat("gdjex: %s " % ( bla ) )

#mc.setBlock (bla [ 0 ],bla [ 1 ],bla [ 2 ],63,1, "{id:\"Sign\",TTTText1:\"Line1\",Text2:\"Line2\",Text3:\"Line3\",Text4:\"Line4\"}")

mc.conn.send("world.setBlock",bla [ 0 ],bla [ 1 ],bla [ 2 ],63,1,"{id:\"Sign\",Text1:\"Line1\",Text2:\"Line2\",Text3:\"Line3\",Text4:\"Line4\"}")

mc.setBlock(-1,-1,-1,1)
mc.conn.send("world.setBlocks",1,4,0,1,0,0,63,4,"{id:\"Sign\",Text1:\"AAAAAAPablo\,Text2:\"Line2\"}")
"""

