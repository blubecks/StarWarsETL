from dataclasses import dataclass, field


@dataclass(order=True)
class Character:
    name: str
    species: str
    height: int
    appearances: int

    def __str__(self):
        return f'{self.name}, {self.species}, {self.height}, {self.appearances}'
