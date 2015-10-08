# crtanje automatizirani sorter
#definicija objekta i poziv rutine za crtanje
import time 
import sys
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom



# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#oakwood slab
materijal = 126
dv = 8

djelovi = (
'{Items:' ,
'[0:{Slot:0b,id:"minecraft:diamond_pickaxe",Count:64b,Damage:0s,},',
'1:{Slot:1b,id:"minecraft:diamond_shovel",Count:64b,Damage:0s,},'
'2:{Slot:2b,id:"minecraft:diamond_axe",Count:64b,Damage:0s,},',
'3:{Slot:3b,id:"minecraft:diamond_svord",Count:64b,Damage:0s,},'
'4:{Slot:4b,id:"minecraft:diamond",Count:64b,Damage:0s,},',
'5:{Slot:5b,id:"minecraft:diamond_hoe",Count:64b,Damage:0s,},',
'6:{Slot:6b,id:"minecraft:diamond_sword",Count:64b,Damage:0s,},',
'7:{Slot:7b,id:"minecraft:diamond_helmet",Count:64b,Damage:0s,},',
'8:{Slot:8b,id:"minecraft:diamond_chestplate",Count:64b,Damage:0s,},',
'9:{Slot:9b,id:"minecraft:diamond_leggings",Count:64b,Damage:0s,},',
'10:{Slot:10b,id:"minecraft:log",Count:64b,Damage:0s,},',
'11:{Slot:11b,id:"minecraft:diamond_boots",Count:64b,Damage:0s,},'
'12:{Slot:12b,id:"minecraft:glowstone",Count:64b,Damage:0s,},'
'13:{Slot:13b,id:"minecraft:glowstone",Count:64b,Damage:0s,},'
'14:{Slot:14b,id:"minecraft:glowstone",Count:64b,Damage:0s,},'
'15:{Slot:15b,id:"minecraft:glowstone",Count:64b,Damage:0s,},'
'16:{Slot:16b,id:"minecraft:torch",Count:64b,Damage:0s,},'
'17:{Slot:17b,id:"minecraft:torch",Count:64b,Damage:0s,},'
'18:{Slot:18b,id:"minecraft:torch",Count:64b,Damage:0s,},'
'19:{Slot:19b,id:"minecraft:cooked_porkchop",Count:64b,Damage:0s,},'
'20:{Slot:20b,id:"minecraft:torch",Count:64b,Damage:0s,},],'
'id:"Hopper",Lock:"",}'
)

sadrzaj=""
for to in djelovi :  
   sadrzaj = sadrzaj + to

bla = rel2abs ( orMj , ( 2  , 0 ,  0  ) , orSm )

# GENERIRA PUNU KUTIJU
mc.setBlockWithNBT(bla,54,1, sadrzaj )


