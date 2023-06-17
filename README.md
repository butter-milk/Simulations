# Silly math problems
## Discrete problems
### MultiDimensionalTicTacToe
Claim: For N>2, tic tac toe will always be won by player 1.

Proof:
We only have to proof the game for N=3, since for any N>3, we can choose any three dimensions and win using this subspace. E.g. when playing on $[3]^8$ use the subspace {(x,y,z,1) | x,y,z $\in${1,2,3} }.

Note that, if you were to play a game in more than 3 dimensions, where player 2 would place a circle on a square which was not in the subspace of your choice, you have a free win anyway. Since player 1 just moves their cross next to the one of player 2, if it is possible in their chosen set of dimensions, Then you can skip to step 3) in the method below. So we do not have to consider this case.

Therefore, we consider the space {(x,y,z) | x,y,z $\in${1,2,3} }. A winning tactic for player 1 is the following:

1. Let (2,2,2) be a cross.
2. Suppose that player 2 puts their circle on (x,y,z), place a cross on any of the direct orthogonal neighbours of (x,y,z). Furthermore, the placement (x',y',z') should be such that for at least two of the variables it holds that they do not equal 1. 
3. Player 2 is forced to put a circle, on lets say (x'',y'',z'') to prevent three in a row. Furthermore, due to 2) we have that x'' $\neq$ x, y'' $\neq$ y and z'' $\neq$ z, which means that player 2 can not make three in a row on its next move, irrespective of player 1's move.
4. Player one should place a piece such that it is a neighbour of both (2,2,2) and (x',y',z'), whilst it does not neighbour (x,y,z) or (x'',y'',z''). Therefore making two three in a row threads and having a guaranteed win. 


## Simulations 
This repository contains different simulations of (mathematical) problems. You can find a description of these problems below:


### Seats.py
The problem is defined as follows: Suppose we have a plane which is fully booked. The first person to enter is blind and therefore takes a random seat, if one of the passengers seats is already taken, they will take a random seat as well. 

**What is the probability that the last person to enter the plane will be able to sit in their assigned seat?**

Exact answer: 0.5, this can be easily proven using induction.

### candleColouring.py
Given a NxN grid, where the edges of each unit square are coloured either red or black (with p=0.5), what is the probability that none of the unit squares have all sides coloured the same:

Exact answer: [WILL BE ADDED ONCE SUBMISSIONS CLOSE]

### ClustersEmpirical.py
This file is a study on how well it works if we take a sample of a dataset, after which we use this to create an empirical distribution and try to find the outliers of the data based on this. Which means that we do not have to iterate over the entire dataset. However, the results are quite poor, as can be seen in the result. Furthermore, we can not know for sure that the result of doing this multiple times converges.

### Pi.py
An estimate of Pi by sampling points in the second quadrant of the unit square (using the fact that the estimated ratio of points in the second quadrant and in the unit circle wrt the previous one will be pi) uniformly.



 



