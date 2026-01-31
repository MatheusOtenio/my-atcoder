
import sys

def solve():
    data = sys.stdin.read().split()
    
    if not data:
        return

    iterator = iter(data)
    N = int(next(iterator))
    T = int(next(iterator))

    next_open_time = 0
    total_duration = 0

    for _ in range(N):
        A_i = int(next(iterator))
        
        if A_i > next_open_time:
            total_duration += (A_i - next_open_time)
            next_open_time = A_i + 100
    
    if T > next_open_time:
        total_duration += (T - next_open_time)

    print(total_duration)

if __name__ == '__main__':
    solve()
