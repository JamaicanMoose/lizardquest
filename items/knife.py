from .item import Item

class Knife(Item):
    name = 'knife'

    def __str__(self):
        return 'A Knife'
