#!/usr/bin/python3
# -*- coding: utf8 -*-

import random

placement_item = []


def random_placement_item(lvl):
    """ set le random placement for the item """

    correct_placement = False
    while correct_placement is False:
        item_stack = False
        x = random.randint(1, 16)
        y = random.randint(1, 16)
        if len(placement_item) != 0:            # check the stack item
            for i in placement_item:
                if i[0] == x and i[1] == y:
                    item_stack = True

        if lvl[(x, y)].name == "tule_brown" and item_stack == False:
            correct_placement = True
            placement_item.append([x, y])

    return x, y


def collision_test(lvl, caractere, direction):
    """ test the collision with the environment """

    shifting = False

    x, y = caractere.get_placement()
    if direction == "left" and lvl[(x - 1, y)].collision:
        shifting = True
    if direction == "right" and lvl[(x + 1, y)].collision:
        shifting = True
    if direction == "up" and lvl[(x, y - 1)].collision:
        shifting = True
    if direction == "down" and lvl[(x, y + 1)].collision:
        shifting = True
    return shifting


