# Poker Chip Shuffling

![shuffling_demo](images/shuffling_demo.gif)

When you sit at the poker table, you see players shuffle their chips constantly. There's cool tutorial on how to do that on [youtube 🌐](https://www.youtube.com/watch?v=pwfvsa1_3Qk). When you start to learn shuffling you start with a pair of 3 chips in two colors.

You easily discover that for a pair of 3 chips, you can get the colors separated by shuffling only three times:
Start with `wwwRRR` (`w` for a white chip, and `R` for a red chip, read from top of the stack)

- The first shuffle generates: `RwRwRw`
- The second shuffle generates: `wRRwwR`
- and the last shuffle gives you: `wwwRRR` again.

![n3_shuffling](images/n3_shuffling.jpg)
> Shuffling two stack of n=3 chips, left-to-right.


## How many shuffling does it take for a pair of N chips to be separated?

Before, I address this question, we need to know if the order of shuffling matters.

> Does it mater if you put the first chip down from the left stack (as in the first gif) or right stack (as in the second figure)?

I wrote a simple piece of code in [here](src/basic_backtrack.py) which compares different shuffling for all `n`s from 1-99:

![](images/res_backtrack_shuffling_order.png)

In this experiment: 
- I do not change the shuffling for every shuffle. 
- AB shuffling always finishes with fewer number of steps as the number of the chips in each stack (green line is the identity line).
- BA shuffling somtimes finishes with fewer steps than AB shuffling.