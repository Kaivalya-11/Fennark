# Tic-Tac-Toe AI

A console-based **Tic-Tac-Toe game built with Python**, where the player competes against an AI powered by the **Minimax algorithm**.

## Features

* Player plays as `X`
* AI plays as `O`
* AI uses the **Minimax algorithm** to select optimal moves
* AI can block the player's winning moves
* AI can identify winning opportunities
* Win and draw detection
* Input validation
* Prevents moves on occupied positions
* Simple interactive console interface

## How It Works

The AI uses the **Minimax algorithm**, a decision-making algorithm used for two-player games.

The AI evaluates possible future game states and assigns scores:

```text
AI Win     → +10
Player Win → -10
Draw       → 0
```

The search depth is also considered so the AI prefers winning sooner and delaying a loss when possible.

### Minimax Process

```text
Current Board
     ↓
Generate Possible Moves
     ↓
Simulate AI Move
     ↓
Simulate Player Response
     ↓
Evaluate Game State
     ↓
Choose Best Move
```

Because Tic-Tac-Toe has a relatively small game state, the AI can search the possible moves without needing complex optimization.

## Technologies Used

* **Python 3**
* Minimax Algorithm
* Conditional Statements
* Functions
* Loops
* Console Input/Output

## How to Run

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project folder:

```bash
cd tic-tac-toe-ai
```

Run the game:

```bash
python tic_tac_toe.py
```

## Example

```text
====================================
        TIC-TAC-TOE AI GAME
====================================

Player [X] ---- AI [O]

The AI uses the Minimax Algorithm.
You cannot defeat the AI if it plays optimally.

  X   |       |
______|_______|______
      |   O   |
______|_______|______
      |       |

Player's chance
Enter the position between [1-9] where you want to mark: 3

AI is thinking...
```

## Board Positions

The available positions are:

```text
  1 | 2 | 3
 ---+---+---
  4 | 5 | 6
 ---+---+---
  7 | 8 | 9
```

Enter the corresponding number to place your `X`.

## Project Structure

```text
tic-tac-toe-ai/
│
├── tic_tac_toe.py
└── README.md
```

## Algorithm

The **Minimax algorithm** recursively explores possible moves and chooses the move that gives the AI the best possible outcome.

The AI acts as the **maximizing player**, while the human player is treated as the **minimizing player**.

This allows the AI to:

* Find winning moves
* Block potential losses
* Force a draw when winning is not possible
* Make optimal decisions

## Learning Objective

This project demonstrates the practical implementation of:

* Game logic
* Recursion
* Decision-making algorithms
* Minimax
* Basic artificial intelligence
* Python programming fundamentals

## Author

**Kaivalya**