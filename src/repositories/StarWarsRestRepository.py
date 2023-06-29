from src.repositories.IStarWarsRepository import IStarWarsRepository

class StarWarsRestRepository(IStarWarsRepository):

    def __init__(self, request_fn):
        self.request_fn = request_fn
    def get_species_by_id(self, species_id):
        return self.request_fn(f'http://swapi.dev/api/species/{species_id}/')

    def get_character_by_id(self, character_id):
        return self.request_fn(f'http://swapi.dev/api/people/{character_id}/')

    def get_all_films(self):
        return self.request_fn('http://swapi.dev/api/films')['results']
