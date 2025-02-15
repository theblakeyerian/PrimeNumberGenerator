#written by blake yerian, 8-1-2023
def primecounting(maxtime):
    counters = [[1, 1]]
    for t in range(2, 50):
        if not any(c[1] == 0 for c in counters):
            counters.append([t, t])
        counters = [[c[0], c[1] - 1 if c[1] != 0 else c[0]] for c in counters]
        counters[0][1] = 1
result = [c[0] for c in counters]

