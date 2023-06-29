from abc import ABC, abstractmethod


class IStarWarsRepository(ABC):
    @abstractmethod
    def get_all_films(self):
        pass

    @abstractmethod
    def get_character_by_id(self, character_id):
        pass

    @abstractmethod
    def get_species_by_id(self, species_id):
        pass
