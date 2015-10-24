import mcpi.minecraft as minecraft
import mcpi.block as block
import server
import sys
mc = minecraft.Minecraft.create(server.address)
mc.postToChat("Hello world!")
playerPos = mc.player.getPos()
mc.setBlock(playerPos.x,playerPos.y-1,playerPos.z,block.DIAMOND_ORE)

ispis="X: %d " % (playerPos.x)
mc.postToChat(ispis)
ispis="Y: %d " % (playerPos.y)
mc.postToChat(ispis)
ispis="Z: %d " % (playerPos.z)
mc.postToChat(ispis)


# idemo po x-u

mc.setBlock(playerPos.x-1,playerPos.y-1,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-2,playerPos.y-1,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-3,playerPos.y-1,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-4,playerPos.y-1,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-5,playerPos.y-1,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-6,playerPos.y-1,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-7,playerPos.y-1,playerPos.z,block.AIR)

# drugi red dublje

mc.setBlock(playerPos.x-2,playerPos.y-2,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-3,playerPos.y-2,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-4,playerPos.y-2,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-5,playerPos.y-2,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-6,playerPos.y-2,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-7,playerPos.y-2,playerPos.z,block.AIR)

# drugi i jos dublje

mc.setBlock(playerPos.x-3,playerPos.y-3,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-4,playerPos.y-3,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-5,playerPos.y-3,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-6,playerPos.y-3,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-7,playerPos.y-3,playerPos.z,block.AIR)

# drugi i jos dublje


mc.setBlock(playerPos.x-4,playerPos.y-4,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-5,playerPos.y-4,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-6,playerPos.y-4,playerPos.z,block.AIR)
mc.setBlock(playerPos.x-7,playerPos.y-4,playerPos.z,block.AIR)
