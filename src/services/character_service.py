from typing import List, Dict
from collections import Counter
from src.utils import make_a_request, get_id_by_url
import itertools

from src.repositories.IStarWarsRepository import IStarWarsRepository
from src.models.character import Character


class CharacterService:

    def __init__(self, repository: IStarWarsRepository):
        self.sw_repository = repository
        return

    def get_list_of_characters_sorted_appearance(self, limit=5):
        characters_list = []
        all_films = self.sw_repository.get_all_films()
        characters_urls = [film['characters'] for film in all_films]
        flatted_list_of_charactes_url = itertools.chain(*characters_urls)
        counter_characters = Counter(flatted_list_of_charactes_url)
        # [{"url": "people/1", "appearance": n}]
        characters_urls_counter = [{'url': key, 'appearances': count} for key, count in
                                   counter_characters.items()]
        characters_urls_counter_sorted = sorted(characters_urls_counter, key=lambda x: x['appearances'], reverse=True)

        for row_url_appearence in characters_urls_counter_sorted[:limit]:
            character_info = self.sw_repository.get_character_by_id(
                get_id_by_url(row_url_appearence['url'])
            )

            if len(character_info['species']) == 1:
                species_name = self.sw_repository.get_species_by_id(
                    get_id_by_url(character_info['species'][0])
                )['name']
            else:
                species_name = ''

            c = Character(
                character_info['name'],
                species_name,
                int(character_info['height']),
                int(row_url_appearence['appearances'])
            )
            characters_list.append(c)

        return characters_list
