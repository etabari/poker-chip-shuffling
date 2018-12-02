import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def shuffle(a, b):
	tuppled = [[a[i], b[i]] for i in range(len(a))]
	return [x for ab in tuppled for x in ab]


def basic_backtrack(n):
	# label chips 0 and 1.
	# it makes it easier to see if all 0s are together.
	chips = [0] * n + [1] * n
	count = 0
	while True:
		# split the stack
		bottom_chips = chips[:n]
		top_chips = chips[n:]
		# shuffle 
		chips = shuffle(top_chips, bottom_chips)
		count += 1
		# if any set adds up to 0, all 0 chips are together
		if sum(chips[:n]) * sum(chips[n:]) == 0:
			break
	return count


if __name__ == '__main__':

	shuffling = []
	for x in range(1, 100):
		shuffling += [basic_backtrack(x)]
	
	plt.plot(range(1, 100), shuffling)
	plt.xlabel('Number of chips in each set')
	plt.ylabel('Number of shuffling')
	plt.suptitle('Basic Shuffling: Backtracking')
	plt.show()
