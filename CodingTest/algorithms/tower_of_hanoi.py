def move_tower(n, start, middle, end, move: list):
    if n == 1:
        move.append(f"{start} {end}")
        return move
    if n > 1:
        move = move_tower(n-1, start, end, middle, move)
        move.append(f"{start} {end}")
        move = move_tower(n-1, middle, start, end, move)
        return move

move = move_tower(int(input()), 1, 2, 3, list())
print(len(move))
[print(m) for m in move]