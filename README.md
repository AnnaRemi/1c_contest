# 1c_contest_2022
Код задачи: 213 "Artificial Intelligence: Bot for checkers game"

Implementation using python pygame for neat vizualization and user-friendlyness
In order to start playing download files and run in terminal:
python3 game.py

# How to play
After starting the game you'll see the board:
![alt text](https://github.com/AnnaRemi/1c_contest/blob/main/board.png)

The bot will show you all possible moves:
![alt text](https://github.com/AnnaRemi/1c_contest/blob/main/proposing%20posible%20moves.png)

You can click on free squares to make a move
The score is amount of "whites" - amount of "blacks", we want to maximize the score and out AI wants to minimize the score

When the game is over the board disappears(didn't have time to make nicer presentation)

# More on realizatoin and theoretical part of evaluation

For realization i created classes Piece for checkers pieces with methods to make a piece a king, draw it and move it,
Board for drawing a classic board with all the pieces and evaluating,
Game for updating possible moves and running the game itself. I've chosen depth=3(not very deep, but rather effective).

Basic algorithm for an AI is as it goes: look for a move where we can capture a piece, if this is possible, try to become a king; if none of that is possible, choose some random move.


More about minimax tree for games:
![alt text](https://github.com/AnnaRemi/1c_contest/blob/main/minimax_tree.png)

