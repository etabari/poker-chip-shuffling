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


def basic_backtrack(n, shuffler):
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


def _so_backtrack(chips, shuffler, depth=0):
    n = len(chips) // 2

    if depth > n:
        return n

    bottom_chips = chips[:n]
    top_chips = chips[n:]

    chips = shuffler(top_chips, bottom_chips)

    if sum(chips[:n]) * sum(chips[n:]) == 0:
        return 1
    else:
        return min(_so_backtrack(chips, shuffleAB, depth+1), _so_backtrack(chips, shuffleBA, depth + 1)) + 1


def so_backtrack(n):
    # label chips 0 and 1.
    # it makes it easier to see if all 0s are together.
    chips = [0] * n + [1] * n

    return min(_so_backtrack(chips, shuffleAB), _so_backtrack(chips, shuffleBA))


if __name__ == '__main__':

    shuffling = []
    shuffling_rev = []
    shuffling_opt = []
    x_range = range(3, 30)
    for x in x_range:
        shuffling += [basic_backtrack(x, shuffleAB)]
        shuffling_rev += [basic_backtrack(x, shuffleBA)]
        shuffling_opt += [so_backtrack(x)]
        if x % 5 == 0:
            print(x)

    with open('data/backtracking.csv', 'w', newline='') as csvfile:
        fieldnames = ['chips', 'ABshufflings', 'BAshufflings', 'OptimalShufflings']
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fieldnames)
        for i in range(len(x_range)):
            csvwriter.writerow([x_range[i], shuffling[i], shuffling_rev[i], shuffling_opt[i]])


    plt.plot(x_range, shuffling, label='AB Shuffling')
    plt.plot(x_range, shuffling_rev, label='BA Shuffling')
    plt.plot(x_range, shuffling_opt, label='Optimum Shuffling')
    plt.legend()
    plt.plot(x_range, x_range, linestyle='--')
    plt.xlabel('Number of chips in each stack')
    plt.ylabel('Number of shufflings')
    plt.suptitle('Basic Backtracking: Shuffling Order')
    plt.show()
