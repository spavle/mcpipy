# crtanje automatizirani sorter
#definicija objekta i poziv rutine za crtanje
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


bla = rel2abs ( orMj , ( 2  , 0 ,  0  ) , orSm )

# GENERIRA PUNU KUTIJU
mc.setBlockWithNBT(bla,54,1,
'{Items:[0:{Slot:0b,id:"minecraft:diamond_pickaxe",Count:52b,Damage:0s,},1:{Slot:1b,id:"minecraft:diamond_shovel",Count:55b,Damage:0s,},2:{Slot:2b,id:"minecraft:diamond_axe",Count:55b,Damage:0s,},3:{Slot:3b,id:"minecraft:diamond_svord",Count:55b,Damage:0s,},4:{Slot:4b,id:"minecraft:diamond",Count:55b,Damage:0s,},5:{Slot:5b,id:"minecraft:diamond_hoe",Count:55b,Damage:0s,},6:{Slot:6b,id:"minecraft:diamond_sword",Count:55b,Damage:0s,},7:{Slot:7b,id:"minecraft:diamond_helmet",Count:55b,Damage:0s,},8:{Slot:8b,id:"minecraft:diamond_chestplate",Count:55b,Damage:0s,},9:{Slot:9b,id:"minecraft:diamond_leggings",Count:55b,Damage:0s,},10:{Slot:10b,id:"minecraft:log",Count:55b,Damage:0s,},11:{Slot:11b,id:"minecraft:torch",Count:55b,Damage:0s,},],id:"Hopper",Lock:"",}' )


