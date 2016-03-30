# from mc import *  # Minecraft api import
# from Position import *  # clas for position
# from cuboid import *
from one import *

mc = Minecraft()  # initialization


class Torch(object):
    def __init__(self, element_position, direction="up"):
        # type: (Position, string) -> object
        """
        create torch
        :param element_position: torch position
        :param direction: relative direction
        :rtype: object
        """
        direction_list = ["to_me", "from_me", "right", "left", "up"]  # on which wall
        numeric_direction = direction_list.index(direction)

        direction_table = dict()  # translation table verified 20.06.2016. 20:51
        direction_table[(1, 0)] = (1, 2, 4, 3, 5)  # look east
        direction_table[(-1, 0)] = (2, 1, 3, 4, 5)  # look west
        direction_table[(0, 1)] = (3, 4, 1, 2, 5)  # look south
        direction_table[(0, -1)] = (4, 3, 2, 1, 5)  # look north

        buff = direction_table[(element_position.x_direction, element_position.z_direction)]
        real_direction = buff[numeric_direction]
        Block(element_position, 50, real_direction)


if __name__ == "__main__":  # direct call for testing purpose
    # self test code

    pos = Position()

    for counter in ("from_me", "right", "to_me", "left"):
        Cuboid(Position(pos, dx=5, dz=-1), Position(pos, dx=7, dz=1), 1, 0)
        Torch(Position(pos, dx=6), direction=counter)
        pos.rotate_left()

