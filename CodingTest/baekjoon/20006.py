"""

1. idea
- make matching system
- level: -10 ~ +10
- if there is available room, wait until it fulls
- p, n, l

2. complexity

3. data structure
- list, set

4. category
- implementation


"""

import sys

input = sys.stdin.readline

p, m = map(int, input().split())

games = []

for _ in range(p):
    l, n = input().strip().split()
    l = int(l)

    make = True
    # check exist games
    for i, game in enumerate(games):
        if len(game) < m and game[0][1] - 10 <= l <= game[0][1] + 10:
            game.append((n, l))
            make = False
            break

    # else make new game
    if make:
        games.append([(n, l)])

for game in games:
    if len(game) == m:
        print("Started!")
    else:
        print("Waiting!")

    game = sorted(game)
    for g in game:
        print(g[1], g[0])
