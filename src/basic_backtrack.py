import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def shuffleAB(a, b):
    tuppled = [[a[i], b[i]] for i in range(len(a))]
    return [x for ab in tuppled for x in ab]


def shuffleBA(b, a):
    tuppled = [[a[i], b[i]] for i in range(len(a))]
    return [x for ab in tuppled for x in ab]


def count_shuffles(n, shuffler):
    # label chips 0 and 1.
    # it makes it easier to see if all 0s are together.
    chips = [0] * n + [1] * n
    count = 0
    while True:
        # split the stack
        bottom_chips = chips[:n]
        top_chips = chips[n:]
        # shuffle
        chips = shuffler(top_chips, bottom_chips)
        count += 1
        # if any set adds up to 0, all 0 chips are together
        if sum(chips[:n]) * sum(chips[n:]) == 0:
            break
    return count

########################################################################
########################################################################
########################################################################
# Pick the best shuffling order every time:


memory = {}
memory_access = 0
nodes = 0

def _backtrack_shuffles(chips, shuffler, best_case, depth=0):
    global memory, memory_access, nodes
    
    n = len(chips) // 2

    if depth >= best_case:
        return best_case

    bottom_chips = chips[:n]
    top_chips = chips[n:]

    chips = shuffler(top_chips, bottom_chips)

    chips_str = ''.join([str(c) for c in chips])
    if chips_str in memory:
        memory_access += 1
        return best_case
    else:
        memory[chips_str] = 1

    nodes += 1
    if sum(chips[:n]) * sum(chips[n:]) == 0:
        return 1
    else:
        ab = _backtrack_shuffles(chips, shuffleAB, best_case, depth + 1)
        ba = _backtrack_shuffles(chips, shuffleBA, best_case, depth + 1)
        return min(ab, ba) + 1


def backtrack_shuffles(n, best_case):
    global memory, memory_access

    memory = {}
    memory_access = 0
    nodes = 0
    # label chips 0 and 1.
    # it makes it easier to see if all 0s are together.
    chips = [0] * n + [1] * n

    return min(_backtrack_shuffles(chips, shuffleAB, best_case), _backtrack_shuffles(chips, shuffleBA, best_case))


def main():
    with open('data/backtracking.csv', 'a', newline='') as csvfile:
        fieldnames = ['chips', 'ABshufflings', 'BAshufflings', 'OptimalShufflings']
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fieldnames)

    shuffling = []
    shuffling_rev = []
    shuffling_opt = []
    x_range = range(30, 100)
    for x in x_range:
        shuffling += [count_shuffles(x, shuffleAB)]
        shuffling_rev += [count_shuffles(x, shuffleBA)]
        best_case = min(shuffling[-1], shuffling_rev[-1])
        shuffling_opt += [backtrack_shuffles(x, best_case)]

        print(x, len(memory), memory_access, nodes)

        with open('data/backtracking.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([x, shuffling[-1], shuffling_rev[-1], shuffling_opt[-1]])

    plt.plot(x_range, shuffling, label='AB Shuffling')
    plt.plot(x_range, shuffling_rev, label='BA Shuffling')
    plt.plot(x_range, shuffling_opt, label='Optimum Shuffling')
    plt.legend()
    plt.plot(x_range, x_range, linestyle='--')
    plt.xlabel('Number of chips in each stack')
    plt.ylabel('Number of shufflings')
    plt.suptitle('Basic Backtracking: Shuffling Order')
    plt.show()


if __name__ == '__main__':
    main()