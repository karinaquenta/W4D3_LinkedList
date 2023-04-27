from requests import get
from Node import Node
class Pokemon():
    
    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.types = []
        self.weight = None
        self.image = None
        self.call_poke_api()
        self.pokes = []
        self.evolve_chain = []       
            
    def get_evolution_chain(self):
        response = get(self.species_url)
        if response.status_code == 200:
            data = response.json()
        evolution_chain_url = data['evolution_chain']['url']
        evolution_chain = get(evolution_chain_url)
        if evolution_chain.status_code == 200:
            return evolution_chain.json()['chain']
            
    def evolve_pokemon(self, evolution_chain):
        if not evolution_chain['evolves_to']:
            print(f'This is the final from')
            return
        current_pokemon_in_chain = evolution_chain['species']['name']
        next_pokemon_in_chain = evolution_chain['evolves_to'][0]['species']['name']
        if current_pokemon_in_chain == self.name:
            self.name = next_pokemon_in_chain
            self.add_evolve_chain()
            return
        else:
            return self.evolve_pokemon(evolution_chain['evolves_to'][0])
        
        
    def add_evolve_chain(self, evolution_chain):
            pokemon = Pokemon(evolution_chain)
            if not self.name:
                self.name = pokemon
            else:
                current_pokemon_in_chain = self.name
            while current_pokemon_in_chain.right:
              next_pokemon_in_chain = current_pokemon_in_chain.right
              current_pokemon_in_chain.left = next_pokemon_in_chain
            current_pokemon_in_chain.right = pokemon


