import requests             # brings in the library that lets you make web requests

print("=== Sports Stats Tracker CLI ===")

search_input = input("Do you want to enter a player or a team?: ")
name = input("Enter a name: ")

print(f"You selected: {search_input}" )
print(f"You entered: {name}")


# just a string, the address we're calling, f string so that you can look up any name
url_players = f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p={name}"       

url_teams = f"https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t={name}"




if search_input == "player":
    url_players = f"https://www.thesportsdb.com/api/v1/json/123/searchplayers.php?p={name}"
    response = requests.get(url_players)

    data = response.json()
    players = data["player"]
    
    if players is None:
        print("That player doesn't exist in this api")
    else:
        print(players[0]["strPlayer"])
        print(players[0]["strTeam"])
        print(players[0]["strSport"])
        print(players[0]["strNationality"])

elif search_input == "team":
    url_teams = f"https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t={name}"
    response1 = requests.get(url_teams)

    team_data = response1.json()
    teams = team_data["teams"]

    if teams is None:
        print("That team doesn't exist in this api")
    else:
        print(teams[0]["strTeam"])