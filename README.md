# Ping Pong Game

## Overview

This is a simple Ping Pong game developed using Processing.py. The game allows you to play against a computer-controlled paddle. The objective is to score points by making the ball pass the opponent's paddle while preventing the ball from passing your paddle.

## Features

- **Single Player Mode:** Play against a computer-controlled opponent.
- **Score Tracking:** Keeps track of the scores for both the player and the computer.
- **Customizable Game Settings:** Modify the game speed, paddle size, and other settings.

## Requirements

- [Processing.py](https://processing.org/download) installed on your system.
- Python (version 2.7 or higher).

## How to Play

1. Download and install Processing.py from the official website.
2. Clone or download this repository to your local machine.
3. Open the `ping_pong_game.pyde` file in the Processing IDE.
4. Click the `Run` button in the Processing IDE to start the game.

### Controls

- Use the `W` and `S` keys to move your paddle up and down.

## Game Settings

You can customize the game settings by modifying the variables in the `setup()` function of the `ping_pong_game.pyde` file:

- `ball.speedX`: Speed of the ball along the X-axis.
- `ball.speedY`: Speed of the ball along the Y-axis.
- `pad1.speedY`: Speed of the player's paddle.
- `pad2.speedY`: Speed of the computer-controlled paddle.

## Code Structure

- `setup()`: Initializes the game window and sets up initial game parameters.
- `draw()`: Main game loop that updates the game state and renders the game objects.
- `Ball` class:
  - `__init__()`: Initializes the ball's position, size, speed, color, and scores.
  - `move()`: Handles the movement of the ball and checks for collisions with the top and bottom walls.
  - `checkCollision()`: Checks for collisions between the ball and paddles.
  - `scores()`: Updates and displays the scores, and resets the ball when a point is scored.
  - `display()`: Renders the ball on the screen.
  - Helper methods: `left()`, `right()`, `top()`, `bottom()`, `reset()`.
- `Paddle` class:
  - `__init__()`: Initializes the paddle's position, size, and speed.
  - `move()`: Handles the movement of the player and computer-controlled paddles.
  - `display()`: Renders the paddle on the screen.
  - Helper methods: `left()`, `right()`, `top()`, `bottom()`.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgements

- Thanks to the Processing Foundation for providing an excellent platform for creating visual and interactive programs.
- Inspired by the classic arcade game Pong.

Enjoy the game!
