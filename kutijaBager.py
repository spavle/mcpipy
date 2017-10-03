import time

from crtanje import *  # tu je funkcija koju zovem
from mc import *  # import api-ja

zaObradu = [STONE.id, DIRT.id, GRASS.id, SANDSTONE.id, SAND.id, GRAVEL.id, COBBLESTONE.id, CLAY.id, GOLD_ORE.id,
            IRON_ORE.id, COAL_ORE.id, DIAMOND_ORE.id, OBSIDIAN.id, REDSTONE_ORE.id, LAPIS_LAZULI_ORE.id,
            129]  # 129 emerald


def puniKutije(orMj, orSm, dimenzije=55, visina=5):
    # Ovo kupi rude i kopa definirani oblik
    popis = dict()
    jednaKutija = ''
    brojKutija = 0
    a = 1
    for dY in range(visina, -1, -1):
        mc.postToChat("Level: %s " % dY)
        time.sleep(1)
        for dZ in range(-3 - dY, 4 + dY):
            for dX in range(0, dimenzije  + dY):
                a += 1
                gdje = rel2abs((int(orMj[0]), int(orMj[1]), int(orMj[2])), (dX, dZ, dY), orSm)
                myBlock = mc.getBlockWithData(int(gdje[0]), int(gdje[1]), int(gdje[2]))
                if myBlock.id in (8, 9, 10, 11):  # makni lavu
                    mc.setBlock(int(gdje[0]), int(gdje[1]), int(gdje[2]), AIR.id, 0)
                if myBlock.id in zaObradu:
                    a = a + 1
                    mc.setBlock(int(gdje[0]), int(gdje[1]), int(gdje[2]), AIR.id, 0)  # stavlja rupu     
                    if ((myBlock.id, myBlock.data)) in popis:  # puni popis
                        popis[(myBlock.id, myBlock.data)] += 1
                    else:
                        popis[(myBlock.id, myBlock.data)] = 1
    slozi_NBT_za_kutije ( orMj, orSm , popis )

    # kopa ispred V iskop visine 'visina' dubine 'dimenzije'

if __name__ == "__main__":  # direktan poziv
    orMj = gdjeSam()
    orSm = gdjeGledam()
    puniKutije(orMj, orSm, dimenzije=221, visina=5)
