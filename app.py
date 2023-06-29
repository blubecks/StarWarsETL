from src.output import generate_output
from src.services.character_service import CharacterService
from src.repositories.StarWarsRestRepository import StarWarsRestRepository
from src.utils import send_data_to_bucket, make_a_request


def main():
    sw_repository = StarWarsRestRepository(make_a_request)
    character_service = CharacterService(sw_repository)

    characters = character_service.get_list_of_characters_sorted_appearance(limit=10)
    filename = generate_output(
        sorted(characters, key=lambda c: c.height, reverse=True),
        ['name', 'species', 'height', 'appearances']
    )
    send_data_to_bucket(filename)


if __name__ == "__main__":
    main()
