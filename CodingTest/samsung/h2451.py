from typing import List


class Runner:
    def __init__(self, hp):
        self.hp = hp
        self.pos = -1

    def start(self):
        self.pos = 0


class Tower:
    def __init__(self, mRow, mCol, mInterval):
        self.r = mRow
        self.c = mCol
        self.interval = mInterval
        self.time = 0
        self.target = -1
        self.range = None

    def update(self, runners, runners_idx):
        self.time = max(0, self.time - 1)

        if self.time != 0:
            return

        if self.target != -1 and (
            (self.target in runners_idx) and (runners[self.target].pos in self.range)
        ):
            # Keep the same target
            return
        else:
            # Update target
            self.target, hp = -1, 201
            for i in runners_idx:
                runner = runners[i]
                if hp > runner.hp > 0:
                    if runner.pos in self.range:
                        self.target, hp = i, runner.hp

    def attack(self, runner):
        if self.time == 0 and self.target != -1:
            runner.hp = max(0, runner.hp - 1)
            self.time = self.interval

    def check_target(self, runner: Runner):
        return runner.pos in self.range


class Solver:
    def __init__(self, N, mMap):
        self.N = N
        self.start = None
        self.end = None

        # Identify start and end positions
        for r in range(N):
            for c in range(N):
                if mMap[r][c] == 2:
                    self.start = (r, c)
                elif mMap[r][c] == 3:
                    self.end = (r, c)

        # Build the path (store coords as tuples)
        self.path = [self.start]
        while True:
            r, c = self.path[-1]
            mMap[r][c] = 0
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < N) and (0 <= nc < N) and (mMap[nr][nc] in (1, 3)):
                    self.path.append((nr, nc))
                    break

            if self.path[-1] == self.end:
                break

        self.path_len = len(self.path) - 1
        self.towers = []
        self.num_towers = 0

    def add_tower(self, mRow, mCol, mInterval):
        tower = Tower(mRow, mCol, mInterval)
        t_range = set()
        for i, p in enumerate(self.path):
            r, c = p
            if abs(mRow - r) + abs(mCol - c) <= 3:
                t_range.add(i)
        tower.range = t_range
        self.towers.append(tower)
        self.num_towers += 1

    def run_sim(
        self, M: int, mInterval: int, mHP: int, mRetTs: List[int], mRetHP: List[int]
    ):
        runners = [Runner(mHP) for _ in range(M)]
        # runners_idx = set(range(M))
        runners_idx = list(range(M))

        for i in range(self.num_towers):
            self.towers[i].target = -1
            self.towers[i].time = 0

        T = 1
        m_cnt = 0

        while runners_idx:
            towers = self.towers
            for i in range(self.num_towers):
                towers[i].update(runners, runners_idx)

            for i in range(self.num_towers):
                towers[i].attack(runners[towers[i].target])

            # Update dead runners
            dead_idx = []
            for i in runners_idx:
                if runners[i].hp == 0:
                    mRetHP[i] = 0
                    mRetTs[i] = T
                    dead_idx.append(i)

            for i in dead_idx:
                runners_idx.remove(i)

            # Move runners
            if T % mInterval == 0:
                for i in runners_idx:
                    if runners[i].pos >= 0:
                        runners[i].pos += 1

                # Check if anyone reached the goal
                goal_idx = []
                for i in runners_idx:
                    if runners[i].pos == self.path_len:
                        mRetHP[i] = runners[i].hp
                        mRetTs[i] = T
                        goal_idx.append(i)
                for i in goal_idx:
                    runners_idx.remove(i)

                # Onboard a new runner
                if m_cnt < M:
                    runners[m_cnt].start()
                    m_cnt += 1

            T += 1


global solver


def init(N: int, mMap: List[List[int]]) -> None:
    global solver
    solver = Solver(N, mMap)


def addTower(mRow: int, mCol: int, mInterval: int) -> None:
    global solver
    solver.add_tower(mRow, mCol, mInterval)


def runSimulation(
    M: int, mInterval: int, mHP: int, mRetTs: List[int], mRetHP: List[int]
) -> None:
    global solver
    solver.run_sim(M, mInterval, mHP, mRetTs, mRetHP)


# import sys
# from solution import addTower, init, runSimulation

CMD_ADD = 200
CMD_RUN = 300


def run():
    okay = False
    N = int(input())
    mMap = [[0] * N for _ in range(N)]

    for y in range(N):
        input_iter = iter(input().split())
        for x in range(N):
            mMap[y][x] = int(next(input_iter))

    init(N, mMap)

    okay = True
    Q = int(input())

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))

        if cmd == CMD_ADD:
            mRow = int(next(input_iter))
            mCol = int(next(input_iter))
            mInterval = int(next(input_iter))
            addTower(mRow, mCol, mInterval)

        elif cmd == CMD_RUN:
            M = int(next(input_iter))
            mInterval = int(next(input_iter))
            mHP = int(next(input_iter))
            mRetTs = [0 for _ in range(M)]
            mRetHP = [0 for _ in range(M)]

            runSimulation(M, mInterval, mHP, mRetTs, mRetHP)

            for i in range(M):
                x = int(next(input_iter))
                if mRetTs[i] != x:
                    okay = False

            for i in range(M):
                x = int(next(input_iter))
                if mRetHP[i] != x:
                    okay = False
        else:
            okay = False

    return okay


## sys.stdin = open('sample_input.txt', 'r')

T, MARK = map(int, input().split())


import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

for tc in range(1, T + 1):
    score = MARK if run() else 0
    print("#%d %d" % (tc, score))

profiler.disable()
stats = pstats.Stats(profiler).strip_dirs().sort_stats(pstats.SortKey.TIME)
stats.print_stats()
