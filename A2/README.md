# Comp472 Assignment 2 README

Team Members:
Irina Patrocinio-Frazao 40024714
Emilie Mines 40045370
Zach Eichler 40018021

Git Hub link: https://github.com/irinafrazao/Comp472

TO ADD DETAILS



Info that could be useful for the analysis:

- Since the search space of this problem is huge (each node has 12 childrens, 12 possible moves at each state), the uninformed search algorithm do very poorly.
There is not enough time to visit every node (brute forcing)
- The depth first search finds no solution at all, even for the puzzles with just 1 move to the solution. This is because it has to go far into the tree until it finds a duplicate node
before it can come back up. So it can fully explore the wrong path before getting to the move it needs
- The iterative deepening does better than DFS but only for small puzzles, less or equal to 5 moves. Since it has a depth limit, it wont get lost in the wrong path forever like DFS.
It has no choice but to come back up when it reaches the depth. This will lead to smaller trees and we can find the solution faster.
However it is still brute forcing so bigger puzzles cannot be solve by this with our time limit.

- the manhattan heuristic takes less computational time but is less precise in the h(n) values that it generates.
- the sum of permutations heuristic takes more computation time to run but is more precise in the h(n) values that it generates
- since we have a 60secs timer, computational time is very important for this context and the manhattan heuristic ends up with better results even if it is less precise (20/20 vs 13/20)

ADMISSIBILITY (guarantee lowest solution path)

- the manhattan distance is an admissible heuristic because it never over estimates the h(n) value of a node.  
This heuristic counts how many moves each tile needs to be placed correctly but does not consider the effect moving one tile has on the others.
We have relaxed the puzzle constraints to form this heuristic so for sure in real life the actual cost of the node are higher.

- although more difficult to prove, the sum of permutations heuristic is also admissible. 
This can be proven because the h() value of the goal node is zero. that is one of the characteristics of admissibility.
This also might not take in account the movement on other tiles?? (not too sure how to prove admissibility on this one)

MONOTONICITY (guarantees lowest solution and search path)

- I dont think any of our heuristics are monotonic??? dont know how to prove this.

INFORMEDNESS

- the sum of permutations is more informed than the manhattan distance because the values of h are higher for the same node.
- it might expand fewer search nodes (idk to check in results) but the computational power needed is higher and so it takes more time to run.