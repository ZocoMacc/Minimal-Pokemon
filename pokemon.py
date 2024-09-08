# By submitting this assignment, I agree to the following:  
# “Aggies do not lie, cheat, or steal, or tolerate those who do”  
# “I have not given or received any unauthorized aid on this assignment”  
#  
# Name: Maximus Marin  
# Section: 568
# Assignment: 14
# Date: 12/1/2023

import random
import time

def display_menu():
    '''Function to print menu of the game. It will show all possible options a player has'''
    print('''
+-----------------------------------------------+
|           WELCOME TO MINIMAL POKEMON          |
|-----------------------------------------------|
|                   Game Menu:                  |
|                                               |
| 1. Travel to other route                      |
| 2. Capture a Pokemon                          |
| 3. Battle                                     |
| 4. Save progress                              |
| 5. Exit the game                              |
+-----------------------------------------------+'''
) # TEST


def display_rules():
    '''Function to show game rules'''
    with open('pokemon_rules.txt', 'r') as rules:
        print(rules.read())


def display_poketeam(player):
    '''Function to show the player's lit of pokemon'''
    print('Team') # TEST


def get_choice(player):
    '''Function to get a valid choice of the current player'''
    try:
        choice = int(input(f'\n    > {player}, select an option (1/2/3/4/5): '))
        if choice in range(1, 6):
            return choice
        else:
            raise ValueError
    except:
        print(f'[{choice}] is not an eligible option. Please try again.')
        get_choice(player)


def travel():
    '''
    Function to ask the player for a new location and change it
    Accounts for bad inputs
    '''
    print(f'\n+--------- {curr_pl}, you are currently in {players_data[curr_pl][0]} ---------+')
    print('You can travel to:'.rjust(40))
    for route in route_names:
        print(f'- {route}')

    # Getting new location from the user
    new_loc = input('\n> Please type the number of the route (119/36/113/4/...): ')
    for route in route_names:
        if new_loc in route:
            new_loc = route
    try:
        loc_int = int(new_loc) # if loc remains an int and can be converted to int means that it is not on the list of routes
        print(f'{loc_int} is not a valid route number. Please try again.')
        time.sleep(1)
        travel()
    except:
        print(f'Traveling to {new_loc}...'.center(60))
        time.sleep(1)
        return new_loc


def capture():
    '''Function to Capture a random pokemon in the current region'''
    loc = players_data[curr_pl][0]
    poke_list = pokedex[loc]
    rand_choice = random.randint(0, 2)
    poke = poke_list[rand_choice][0]

    print(f'\n+--------- A wild {poke.upper()} appeared! ---------+')

    for i in range(3):
        time.sleep(1)
        print(f'Capturing...{i+1}')

    capt = random.randint(0, 2)
    if capt == 0:
        print(f'\n{poke.upper()} escaped, better luck next time.')
        return None, None
    else:
        print(f'A wild {poke} was captured successfully!')
        return poke, rand_choice # return the name of the pokemon and the index of the pokemon in the list of the route


def battle(pl1, pl2):
    players = [pl1, pl2]
    turn = 0
    side = '>'

    # Attacking current pokemon stats
    curr_pl = players[turn]
    curr_counter = 0
    curr_poke = players_data[curr_pl][1][curr_counter]
    curr_poke_name = curr_poke[0].upper()
    curr_poke_hp = curr_poke[1]
    curr_poke_dm = curr_poke[2]
    # curr_save_poke = [def_poke_name, def_poke_hp, def_poke_hp]

    # Defense Pokemon stats
    def_pl = players[(turn + 1) % len(players)]
    def_counter = 0
    def_poke = players_data[def_pl][1][def_counter]
    def_poke_name = def_poke[0].upper()
    def_poke_hp = def_poke[1]
    def_poke_dm = def_poke[2]
    # def_save_poke = [def_poke_name, def_poke_hp, def_poke_hp]

    while True:
        curr_pl = players[turn]
        def_pl = players[(turn + 1) % len(players)]
        print(f'''
+{'-'*48}--+
|{'BATTLE':^50}|
|----- {curr_pl:^10} ------ vs ------ {def_pl:^10} -----|
|{' '*48}  |
|      {curr_poke_name:^10}        {'>'*3}       {def_poke_name:^10}      |
|  HP: {curr_poke_hp:^10}        {'>'*3}       {def_poke_hp:^10}      |
|  Dm: {curr_poke_dm:^10}        {'>'*3}       {def_poke_dm:^10}      |
|{' '*48}  |
|{'-'*48}  |
|   1. Attack opponent's Pokemon                   |
|   2. Heal Pokemon                                |
+{'-'*48}--+
''')
        # pl1_poke = players_data[curr_pl][1][team_counter]
        print(f'It is {curr_pl} turn.')

        # Get usr input for what to do in turn
        while True:
            try:
                move = int(input(f'\n    > What do you want to do (1/2): '))
                if move not in range(1, 3):
                    raise ValueError
                break
            except:
                print('Your input is not valid. Please try again.')
        
        if move == 1:
            if turn == 0:
                def_poke_hp -= curr_poke_dm
                if def_poke_hp <= 0:
                    if def_counter < len(players_data[def_pl][1]):
                        print(f'{def_poke_name} was defeated. The next pokemon on your team will take its place')
                        def_counter += 1
                        break
                    else:
                        print(f'+--------- BATTLE IS OVER. {curr_pl} wins!!! ---------+')
                        break
            elif turn == 1:
                curr_poke_hp -= def_poke_dm
                if curr_poke_hp <= 0:
                    if curr_counter < len(players_data[curr_pl][1]):
                        print(f'{curr_poke_name} was defeated. The next pokemon on your team will take its place')
                        curr_counter += 1
                        break
                    else:
                        print(f'+--------- BATTLE IS OVER. {curr_pl} wins!!! ---------+')
                        break
        elif move == 2:
            if turn == 0:
                curr_poke_hp += 30
            elif turn == 1:
                def_poke_hp += 30
        
                # Next turn
        turn = (turn + 1) % len(players) # Can only be 0 or 1

############################## MAIN CODE ###############################

# Pokemon per route
pokedex = {
    'Kanto Route 1' : [('Charmander', 50, 20), ('Pikachu', 60, 30), ('Onix', 100, 40)],
    'Hoenn Route 119': [('Mudkip', 70, 30), ('Mawile', 90, 40), ('Ralts', 70, 10)],
    'Johto Route 36': [('Heracross', 50, 20), ('Totodile', 60, 30), ('Ho-Oh', 100, 40)],
    'Unova Route 4' : [('Victini', 70, 30), ('Tepig', 90, 40), ('Thundurus', 70, 10)],
    'Sinnoh Route 213': [('Shinx', 50, 20), ('Piplup', 60, 30), ('Garchomp', 100, 40)],
    'Alola Route 7' : [('Rowlet', 50, 20), ('Yungoos', 60, 30), ('Garchomp', 100, 40)],
    'Kalos Route 13' : [('Chespin', 70, 30), ('Froakie', 90, 40), ('Fennekin', 70, 10)],
}


display_rules()

# Initializing variables with defaults
pl1 = input('    > Please enter player 1 name: ')
pl2 = input('    > Please enter player 2 name: ')
# pl1 = 'Macc' # TEST
# pl2 = 'Milo' # TEST
players = [pl1, pl2]

location = 'Kanto Route 1'

# Save players data in a dictionary
players_data = {
    pl1 : [location, []],
    pl2 : [location, []]
}

route_names = list(pokedex.keys())
pokemon_list = list(pokedex.values())

playing = True
turn = 0

while playing:
    display_menu()
    curr_pl = players[turn]
    team = players_data[curr_pl][1]
    curr_loc = players_data[curr_pl][0]
    choice = get_choice(curr_pl)
    
    # Next turn
    turn = (turn + 1) % len(players) # Can only be 0 or 1

    if choice == 1:
        new_loc = travel()
        players_data[curr_pl][0] = new_loc
    elif choice == 2:
        wild_poke, poke_loc = capture()
        if wild_poke == None:
            continue
        else:
            add_team = input(f'\n>    Do you want to add {wild_poke} to your team? (y/n): ')
            if add_team.lower() == 'y':
                if len(team) < 6:
                    players_data[curr_pl][1].append(pokedex[curr_loc][poke_loc]) # Append new pokemon to the player's team
                else:
                    while True:
                        try:
                            add_loc = int(input(f'\n    > Which location of your team do you want to replace (1-6): '))
                            players_data[curr_pl][1][add_loc]
                            break
                        except:
                            print('Your input is not valid. Please try again.')

    elif choice == 3:
        print(f'\n+--------- {curr_pl} has started a battle! ---------+')
        battle(curr_pl, players[turn])

    elif choice == 4:
        print(f'\nSaving data for {curr_pl}...', end='    ')
        print('[', end='')
        for i in range(5):
            print('=', end='')
            time.sleep(1)
        print(']')
    elif choice == 5:
        print('\nTHANKS FOR PLAYING, Closing the game...', end='    ')
        print('[', end='')
        for i in range(5):
            print('=', end='')
            time.sleep(1)
        print(']\n')
        playing = False
