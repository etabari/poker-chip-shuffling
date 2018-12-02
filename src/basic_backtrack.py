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


if __name__ == '__main__':

	shuffling = []
	shuffling_rev = []
	for x in range(1, 100):
		shuffling += [basic_backtrack(x, shuffleAB)]
		shuffling_rev += [basic_backtrack(x, shuffleBA)]

	plt.plot(range(1, 100), shuffling, label='AB Shuffling')
	plt.plot(range(1, 100), shuffling_rev, label='BA Shuffling')
	plt.legend()
	plt.plot(range(1, 100), range(1, 100), linestyle='--')
	plt.xlabel('Number of chips in each stack')
	plt.ylabel('Number of shuffling')
	plt.suptitle('Basic Backtracking: Shuffling Order')
	plt.show()
