import requests
import random
import time

def get_pokemon_by_id(pokemon_id):
    # Function to retrieve Pokemon data from the PokeAPI by ID
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response and return relevant Pokemon data
        pokemon_data = response.json()
        return {
            'name': pokemon_data['name'].capitalize(),
            'id': pokemon_data['id'],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'base_experience': pokemon_data['base_experience']
        }
    else:
        # Display an error message if data retrieval fails
        print(f"Failed to get data for Pokemon with ID {pokemon_id}")
        return None

def compare_pokemon(player_pokemon, opponent_pokemon, stat):
    # Function to compare the chosen stat of player's and opponent's Pokemon
    player_stat = player_pokemon.get(stat, 0)
    opponent_stat = opponent_pokemon.get(stat, 0)

    if player_stat > opponent_stat:
        return "Player wins!"
    elif player_stat < opponent_stat:
        return "Opponent wins!"
    else:
        return "It's a tie!"


def multiple_rounds():
    # Function to execute multiple rounds of the Pokemon comparison game
    games_left = 3
    games_left = 3
    player_wins = 0
    computer_wins = 0

    while games_left > 0:
        print("New game!")

        # Get random Pokemon for the player and opponent
        player_pokemon_id = random.randint(1, 151)
        opponent_pokemon_id = random.randint(1, 151)

        player_pokemon = get_pokemon_by_id(player_pokemon_id)
        opponent_pokemon = get_pokemon_by_id(opponent_pokemon_id)

        if player_pokemon and opponent_pokemon:
            # Display player's Pokemon information
            print(
                f"\nPlayer's Pokemon: {player_pokemon['name']} (ID: {player_pokemon['id']}, Height: {player_pokemon['height']}, Weight: {player_pokemon['weight']})")
            # print(f"Opponent's Pokemon: {opponent_pokemon['name']} (ID: {opponent_pokemon['id']}, Height: {opponent_pokemon['height']}, Weight: {opponent_pokemon['weight']})")

            # Ask the user which stat to use
            chosen_stat = input("\nChoose a stat (id, height, or weight): ").lower()
            print(f"The {chosen_stat} of your opponent's pokemon is {opponent_pokemon_id}.")

            if chosen_stat in ['id', 'height', 'weight']:
                # Compare player's and opponent's Pokemon based on the chosen stat
                result = compare_pokemon(player_pokemon, opponent_pokemon, chosen_stat)
                print(f"\n{result}")

                # Update wins and decrement games left
                if result == "Player wins!":
                    player_wins += 1
                elif result == "Opponent wins!":
                    computer_wins += 1

                games_left -= 1
                time.sleep(8)
            else:
                print("Invalid stat choice. Please choose 'id', 'height', 'weight', or 'base_experience'.")
        else:
            print("Failed to retrieve Pokemon data.")

        # Display the final score after all rounds
        print(f"Computer - {computer_wins} vs Player - {player_wins}")

    # Execute the multiple_rounds function if the script is run directly
if __name__ == "__main__":
    multiple_rounds()