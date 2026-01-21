Asteroids (Pygame)

A simple Asteroids-style arcade game built with Python and Pygame. Fly your ship, shoot asteroids, and avoid collisions.

Features
	•	Player movement and rotation (W/A/S/D)
	•	Shooting with cooldown (Spacebar)
	•	Asteroid spawning from screen edges
	•	Asteroid movement with velocity
	•	Asteroid splitting into smaller asteroids when shot
	•	Collision detection (player vs asteroid, shot vs asteroid)
	•	Basic event logging (game_events.jsonl)

Controls

W     Move forward
S     Move backward
A     Rotate left
D     Rotate right
Space Shoot

Requirements
	•	Python 3.x
	•	Pygame

Install dependencies:
pip install pygame

How to Run

From the project folder:
python main.py

Notes
	•	If the player collides with an asteroid, the game prints “Game over!” and exits.
	•	Shooting asteroids logs events and removes objects from the game using sprite .kill().

Project Structure

main.py          Game loop, sprite groups, collision handling
player.py        Player movement and shooting
shot.py          Bullet behaviour
asteroid.py      Asteroid behaviour and splitting
asteroidfield.py Asteroid spawn logic
circleshape.py   Shared circle-based movement and collision logic
constants.py     Game constants
logger.py        Event/state logging
