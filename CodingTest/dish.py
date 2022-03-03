dishes = input()

d_prev = dishes[0]
height = 10
for i in range(1, len(dishes)):
    d = dishes[i]
    height += 5 if d == d_prev else 10
    d_prev = d
print(height)