class Animal:
    def make_sound(self) -> str:
        raise NotImplementedError("Must be implemented!")


class DogOld:
    def woof(self):
        return "Au au!"


class DogAdapter(Animal):
    def __init__(self, dog_old: DogOld) -> None:
        self._dog_old = dog_old

    def make_sound(self) -> str:
        return self._dog_old.woof()


def make_sound(animal: Animal):
    return animal.make_sound()


dog_old = DogOld()
dog = DogAdapter(dog_old)

assert make_sound(dog) == "Au au!"
