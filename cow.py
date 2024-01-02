class Cow:
    # initializes the name, and sets the image to be none
    def __init__(self, name):
        self.name = name
        self.image = None

    # returns the name
    def get_name(self):
        return self.name

    # returns the image
    def get_image(self):
        return self.image

    # sets the image to image being plugged in as the parameter
    def set_image(self, image):
        self.image = image
