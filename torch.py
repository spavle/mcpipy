# from mc import *  # Minecraft api import
# from Position import *  # clas for position
# from cuboid import *
from one import *

mc = Minecraft()  # initialization


class Torch(object):
    def __init__(self, element_position_from, element_position_to, anchored_to="up"
                 ):
        # type: (Position, Position, string) -> Torch
        """
        create torch block
        :param element_position_from: torch position from
        :param element_position_to: torch position to
        :param anchored_to: relative anchor positioning
        :rtype: object
        """
        anchored_to_list = ["to_me", "from_me", "right", "left", "down"]  # on which wall
        numeric_direction = anchored_to_list.index(anchored_to)

        direction_table = dict()  # translation table verified 20.06.2016. 20:51
        direction_table[(1, 0)] = (1, 2, 4, 3, 5)  # look east
        direction_table[(-1, 0)] = (2, 1, 3, 4, 5)  # look west
        direction_table[(0, 1)] = (3, 4, 1, 2, 5)  # look south
        direction_table[(0, -1)] = (4, 3, 2, 1, 5)  # look north

        buff = direction_table[(element_position_from.x_direction, element_position_from.z_direction)]
        real_direction = buff[numeric_direction]
        Cuboid(element_position_from, element_position_to, 50, real_direction)

    @classmethod
    def one(cls, element_position, anchored_to="up"):
        # type: (Position, string) -> Torch
        """
        create one torch
        :param element_position: one torch position
        :param anchored_to: relative anchor positioning
        :return:
        :rtype: Torch
        """
        return cls(element_position, element_position, anchored_to)


if __name__ == "__main__":  # direct call for testing purpose
    # self test code

    pos = Position()

    for counter in ("from_me", "right", "to_me", "left"):
        Cuboid(Position(pos, dx=5, dz=-1), Position(pos, dx=7, dz=1), 1, 0)
        Torch.one(Position(pos, dx=6), anchored_to=counter)
        pos.rotate_left()

    Torch(Position(pos, dx=9, dz=-2), Position(pos, dx=19, dz=2), anchored_to="down")

    pos.rotate_left()
    for br in range(1, 10, 2):
        Torch.one(Position(pos, dx=6 + br, dz=br), anchored_to="down")
