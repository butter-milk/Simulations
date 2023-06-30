**Claim** For N>2, tic tac toe will always be won by player 1.

**Proof**
We only have to proof the game for N=3, which is elaborated on below.


In order to reduce the N dimensional problem to a one of dimension 3, we take the following procedure:

1. Let $2^N$ be a cross.
2. Player 2 now must place a circle on a square in $[3]^N$ such that at least one of its components is not equal to 2. Cause pieces can not be placed on top of one another. Let this be at the ith coordinate. 
3. Then Player 1 can continue with step 2 in the methodology below using the following subspace {w$\in [3]^N$ | $w_i, w_{i-1}, w_{i+1}\in [3]$ and $w_j = 2$ for all other indices}. This choice means that the set of neighbours of the circle does not contain the entire 3d subspace. So now we can continue with step 2 of the methodology below. 




Therefore, we consider the space {(x,y,z) | x,y,z $\in${1,2,3} }. A winning tactic for player 1 is the following:

1. Let (2,2,2) be a cross.
2. Suppose that player 2 puts their circle on (x,y,z), place a cross on any of the direct orthogonal neighbours of (x,y,z). Furthermore, the placement (x',y',z') should be such that for at least two of the variables it holds that they do not equal 2. Furthermore, we require that the three in a row opportunity at (x'',y'',z'') is not a neighbour of (x,y,z) (which trivially holds due to the way we placed our cross).
3. Player 2 is forced to put a circle, on (x'',y'',z'') to prevent three in a row. This means that player 2 can not make three in a row on its next move, irrespective of player 1's move.
4. Player one should place a piece such that it is a neighbour of both (2,2,2) and (x',y',z'), whilst it does not neighbour (x,y,z) or (x'',y'',z''). Therefore making two three in a row threads and having a guaranteed win.


**A comment on step 3**
Even in higher than 3 dimensions player 2 is not able to make three in a row on its next move. Assume it was, then there would be a three in a row looking like (x,y,z,0) (x''',y''',z''',i) (x'',y'',z'',0) where i is either equal to 1 or 2, both of which would result in the three in a row not being valid. 