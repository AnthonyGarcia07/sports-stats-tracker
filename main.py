import requests             # brings in the library that lets you make web requests

# while loop so that the program can ask user for another search
while True:
    print("=== Sports Stats Tracker CLI ===")

    search_input = input("Do you want to enter a player or a team?: ").lower()
    name = input("Enter a name: ")

    print(f"You selected: {search_input}" )
    print(f"You entered: {name}")



    # if conditional to check for a player or team
    if search_input == "player":
    
        # just a string, the address we're calling, f string so that you can look up any player name
        url_players = f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p={name}"
        # this allows us to make a call to the api
        player_response = requests.get(url_players)

        # response.json puts it into a python dictionary, making it easier to work with
        data = player_response.json()
        # indexing into a dictionary, it basically gives me the value stored at the key 
        players = data["player"]


        # nested if conditon, if player is not in the api key, print player doesn't exist, else print the player's name, team, sport, and nationality 
        if players is None:
            print("That player doesn't exist in this api")
        else:
            # added f strings and more print statements to make it look more presentable
            print("=== Player Found ===")
            print(f"Name:        {players[0]["strPlayer"]}")
            print(f"Team:        {players[0]["strTeam"]}")
            print(f"Sport:       {players[0]["strSport"]}")
            print(f"Nationality: {players[0]["strNationality"]}")

    # elif conditonal checking for a team
    elif search_input == "team":
    
        # a string, the address we're calling, f string so that you can look up any team name
        url_teams = f"https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t={name}"
        # calls the actual api key so that we can use it
        team_response = requests.get(url_teams)

        # converts the messy response into a python dictionary, allowing us to work with it
        team_data = team_response.json()
        # indexing into a dictionary, it basically gives me the value stored at the key 
        teams = team_data["teams"]


        # nested if condition, if team is not in the api key, print team doesn't exist, else print the team name, sport, league, and stadium
        if teams is None:
            print("That team doesn't exist in this api")
        else:
            # added f strings and more print statements to make it look more presentable
            print("=== Team Found ===")
            print(f"Team Name:       {teams[0]["strTeam"]}")
            print(f"Sport:           {teams[0]["strSport"]}")
            print(f"League:          {teams[0]["strLeague"]}")
            print(f"Stadium:         {teams[0]["strStadium"]}")

    # prints invalid search input if search input is not "player" or "team"
    else:
        print("Invalid Search Input")
    # asks user at the end if user wants to search again, if "No", then breaks
    keep_going = input("Search again? (yes/no): ").lower()
    if keep_going == "yes":
        continue
    elif keep_going == "no":
        break
    else:
        print("Invalid input (Must be Yes or No.)")
        break