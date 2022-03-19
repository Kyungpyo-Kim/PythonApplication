lscore = dict(A=4, B=3, C=2, D=1)
sscore = {
    "+": 0.3,
    "0": 0.0,
    "-": -0.3,
}
grade = input()
score = 0
if grade != "F":
    score += lscore.get(grade[0], 0)
    score += sscore.get(grade[1], 0)
print(f"{score:.1f}")