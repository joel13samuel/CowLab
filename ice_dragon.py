from dragon import Dragon

# created a dragon class that inherits its methods from the dragon class, it also uses the super function to take the
# name of the dragon

class IceDragon(Dragon):
    def __init__(self, name, image):
        super().__init__(name, image)

    def can_breathe_fire(self):
        return False
