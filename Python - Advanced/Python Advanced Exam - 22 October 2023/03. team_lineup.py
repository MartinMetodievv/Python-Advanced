from collections import defaultdict


def team_lineup(*args):
    players = defaultdict(list)
    for player, country in args:
        players[country].append(player)
    sorted_players = dict(sorted(players.items(), key=lambda kvp: (-len(kvp[1]), (kvp[0]))))
    result = []
    for c, p in sorted_players.items():
        result.append(f'{c}:')
        for x in p:
            result.append(f"  -{x}")
    return '\n'.join(result).strip()


print(team_lineup(("Harry Kane", "England"), ("Manuel Neuer", "Germany"), ("Raheem Sterling", "England"),
                  ("Toni Kroos", "Germany"), ("Cristiano Ronaldo", "Portugal"), ("Thomas Muller", "Germany")))
