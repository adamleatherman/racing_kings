# racing_kings
Racing Kings chess variant built in Python.

As in standard chess, white moves first. The first player to move their king onto row 8 is the winner, unless black finishes the next move after white does, in which case it's a tie. Pieces move and capture the same as in standard chess. As in standard chess, a player is not allowed to expose their own king to check (including moving a piece that was blocking a check such that it no longer does). **Unlike** standard chess, a player is not allowed to put the opponent's king in check (including moving a piece that was blocking a check such that it no longer does).

![image](https://github.com/adamleatherman/racing_kings/assets/16127160/8b4789b5-878b-4aad-b0ec-663fd50b6717)

Locations on the board will be specified using "algebraic notation", with columns labeled a-h and rows labeled 1-8, with row 1 being the start side and row 8 the finish side, as shown in the diagram above.
