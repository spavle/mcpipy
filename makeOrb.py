#Testiranje NBT atributa

import time 
import sys
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

playerPos = mc.player.getPos()
# +++++++++++++++++++++++++++++++++++++++++++++ GENERIRA XP orb
id = mc.spawnEntity('XPOrb', int ( playerPos.x + 2 ) ,int ( playerPos.y + 2 ), int ( playerPos.z ), "{Value:1237}")


