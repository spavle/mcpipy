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
def makeFarmer ( ):
# origin ispred na sredini 
   orMj = gdjeSam ()
   orSm = gdjeGledam ()
   playerPos = mc.player.getPos()
   # +++++++++++++++++++++++++++++++++++++++++++++ GENERIRA MULU
   id = mc.spawnEntity('Villager',  int( playerPos.x + 4 ) , int( playerPos.y ),  int( playerPos.z ), "{Profession:0,Career:1}")
   id = mc.spawnEntity('Villager',  int( playerPos.x + 4 ) , int( playerPos.y ),  int( playerPos.z -1 ), "{Profession:0,Career:1}")
   id = mc.spawnEntity('Villager',  int( playerPos.x + 4 ) , int( playerPos.y ),  int( playerPos.z +1), "{Profession:0,Career:1}")
   id = mc.spawnEntity('Villager',  int( playerPos.x + 4 ) , int( playerPos.y ),  int( playerPos.z +2), "{Profession:1,Career:1}")
   id = mc.spawnEntity('Villager',  int( playerPos.x + 4 ) , int( playerPos.y ),  int( playerPos.z +3), "{Profession:2,Career:1}")



makeFarmer ( )