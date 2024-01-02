# file_cow.py

from cow import Cow  # Make sure to import the Cow class from the correct location


class FileCow(Cow):
    def __init__(self, name, filename):
        try:
            with open(filename, 'r') as file:
                image = file.read()
        except FileNotFoundError:
            raise RuntimeError("MOOOOO!!!!!!")

        super().__init__(name, image)

    def set_image(self, image):
        raise RuntimeError("Cannot reset FileCow Image")