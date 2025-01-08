"""

demolish 할 때

해당 공간에 빌딩이 있으면,
그 빌딩을 지우고, 왼쪽, 오른쪽 빈 공간에 따라 빈 공간의 정보가 업데이트 되어야 함

빌딩, 빈공간이 유효한지 체크하는 리스트 사용
빈공간 체크 리스트
빌딩 체크 리스트
빈공간 힙


"""

import heapq


class Solver:
    def __init__(self, N):
        # print(">> init")
        self.N = N
        self.buildings = {}  # addr: length
        self.empty = {0: N}  # addr: length
        self.empty_q = []  # -length, addr
        self.empty_index = {}
        self.empty_index[0] = 0
        self.empty_index[N - 1] = 0
        heapq.heappush(self.empty_q, (-N, 0))

    def build(self, mLength: int) -> int:
        empty = self.empty
        empty_index = self.empty_index

        while self.empty_q:
            length, addr = self.empty_q[0]
            length = -length
            if addr in empty and empty[addr] == length:
                break
            heapq.heappop(self.empty_q)
        else:
            return -1

        if mLength > length:
            return -1

        heapq.heappop(self.empty_q)
        del empty[addr]
        del empty_index[addr]
        del empty_index[addr + length - 1]

        addr_new = (length - mLength) // 2 + addr
        self.buildings[addr_new] = mLength

        length_left = (length - mLength) // 2
        if length_left:
            empty[addr] = length_left
            heapq.heappush(self.empty_q, (-length_left, addr))
            empty_index[addr] = addr
            empty_index[addr + length_left - 1] = addr

        length_right = length - length_left - mLength
        if length_right:
            addr = addr + length_left + mLength
            empty[addr] = length_right
            heapq.heappush(self.empty_q, (-length_right, addr))
            empty_index[addr] = addr
            empty_index[addr + length_right - 1] = addr

        return addr_new

    def demolish(self, mAddr: int) -> int:
        blds = self.buildings
        empty = self.empty
        empty_index = self.empty_index
        if mAddr not in blds:
            return -1

        ret = length = blds[mAddr]
        addr = mAddr
        del blds[mAddr]

        # left
        if mAddr > 0 and (mAddr - 1) in empty_index:
            addr = empty_index[mAddr - 1]
            length += empty[addr]
            del empty[addr]

        # right
        if addr + length < self.N and (addr + length) in empty_index:
            tmp_addr = addr + length
            length += empty[tmp_addr]
            del empty[tmp_addr]

        # update new empty
        empty[addr] = length
        empty_index[addr] = addr
        empty_index[addr + length - 1] = addr

        heapq.heappush(self.empty_q, (-length, addr))
        return ret


global solver


def init(N: int) -> None:
    global solver
    solver = Solver(N)


def build(mLength: int) -> int:
    global solver
    return solver.build(mLength)


def demolish(mAddr: int) -> int:
    global solver
    return solver.demolish(mAddr)


# import sys
# from solution import build, demolish, init

CMD_INIT = 1
CMD_BUILD = 2
CMD_DEMOLISH = 3


def run():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            init(N)
            okay = True
        elif cmd == CMD_BUILD:
            mLength = int(next(input_iter))
            ret = build(mLength)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_DEMOLISH:
            mAddr = int(next(input_iter))
            ret = demolish(mAddr)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        else:
            okay = False
    return okay


import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()


if __name__ == "__main__":
    T, MARK = map(int, input().split())
    # T = 17
    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)

profiler.disable()
stats = pstats.Stats(profiler).strip_dirs().sort_stats(pstats.SortKey.TIME)
stats.print_stats()
