import pytest
from unittest.mock import patch
from src.repositories.StarWarsRestRepository import StarWarsRestRepository

@pytest.fixture
def mock_make_a_request():
    with patch('src.utils.make_a_request') as mock:
        yield mock

@pytest.fixture
def star_wars_repository(mock_make_a_request):
    return StarWarsRestRepository(mock_make_a_request)

def test_get_species_by_id(mock_make_a_request, star_wars_repository):
    species_id = 10

    expected_url = f'http://swapi.dev/api/species/{species_id}/'
    mock_make_a_request.return_value = {'name': 'Human'}

    result = star_wars_repository.get_species_by_id(species_id)

    mock_make_a_request.assert_called_once_with(expected_url)
    assert result == {'name': 'Human'}

def test_get_character_by_id(mock_make_a_request, star_wars_repository):
    character_id = 5

    expected_url = f'http://swapi.dev/api/people/{character_id}/'
    mock_make_a_request.return_value = {'name': 'Luke Skywalker'}

    result = star_wars_repository.get_character_by_id(character_id)

    mock_make_a_request.assert_called_once_with(expected_url)
    assert result == {'name': 'Luke Skywalker'}

def test_get_all_films(mock_make_a_request, star_wars_repository):
    expected_url = 'http://swapi.dev/api/films'
    mock_make_a_request.return_value = {'results': ['A New Hope', 'The Empire Strikes Back']}

    result = star_wars_repository.get_all_films()

    mock_make_a_request.assert_called_once_with(expected_url)
    assert result == ['A New Hope', 'The Empire Strikes Back']
