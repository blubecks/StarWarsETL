from unittest.mock import MagicMock
from src.services.character_service import CharacterService
from src.models.character import Character
from src.repositories.IStarWarsRepository import IStarWarsRepository

class MockStarWarsRepository(IStarWarsRepository):
    def get_all_films(self):
        return [{'characters': ['https://swapi.dev/api/people/1/', 'https://swapi.dev/api/people/2/','https://swapi.dev/api/people/1/']}]

    def get_character_by_id(self, character_id):
        return {
            'name': 'Luke Skywalker',
            'species': ['https://swapi.dev/api/species/1/'],
            'height': '172'
        }

    def get_species_by_id(self, species_id):
        return {'name': 'Human'}

def test_get_list_of_characters_sorted_appearance():
    mock_repository = MockStarWarsRepository()
    character_service = CharacterService(mock_repository)

    characters_list = character_service.get_list_of_characters_sorted_appearance(limit=2)

    assert len(characters_list) == 2

    assert isinstance(characters_list[0], Character)
    assert characters_list[0].name == 'Luke Skywalker'
    assert characters_list[0].species == 'Human'
    assert characters_list[0].height == 172
    assert characters_list[0].appearances == 2

    # Add more assertions for the other characters in the list if needed
