from math import ceil

def alarm_min_time(speeds, N, M, L):
    fast_bikers_speed = 0
    hours_to_fast = [0] * N

    for i in range(N):
        initial_speed = speeds[i]
        hours_to_fast[i] = ceil(L / initial_speed)

    print(hours_to_fast)


alarm_min_time([20, 50, 20], 3, 400, 120)
