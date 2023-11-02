class Car:
    def __init__(self, name, model, patch_number):
        self.name = name
        self.model = model
        self._patch_number = patch_number

    @property
    def get_patch(self):
        return self._patch_number

    @get_patch.setter
    def get_patch(self, value):
        self._patch_number = value


bmw = Car("BMW", "5 series", "#123")

print(bmw.get_patch)

bmw.get_patch = '#990'

print(bmw.get_patch)
