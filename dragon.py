from cow import Cow


# created a dragon class that inherits its methods from the cow class, it also uses the super function to take the name
class Dragon(Cow):
    def __init__(self, name, image):
        super().__init__(name)
        self.image = image

    def can_breathe_fire(self):
        return True
