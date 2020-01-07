# Lights Out Puzzle Solver

The Lights Out puzzle consists of an m×n grid of lights, each of which has two states: on and off. The goal of the puzzle is to turn all the lights off, with the caveat that whenever a light is toggled, its neighbors above, below, to the left, and to the right will be toggled as well. If a light along the edge of the board is toggled, then fewer than four other lights will be affected, as the missing neighbors will be ignored.

This was made as an exercise to implement a breadth-first graph search algorithm in order to solve a puzzle. So please take in account that this code was written in a few days without any professional review/standard .

## Getting Started

The file ["lights_out_puzzle.py"](lights_out_puzzle.py) contains all the code and breadth-first algorithm to solve our puzzle.

The file ["lights_out_puzzle_gui.py"](lights_out_puzzle_gui.py) contains a gui in order to interface with the breadth-first algorithm and our puzzle.

### Prerequisites

- [tkinter](https://docs.python.org/3/library/tkinter.html)

## Running the gui

You can run the gui with the following:

```[python]
python3 lights_out_gui.py rows cols
```

The arguments rows and cols are positive integers designating the size of the puzzle.

## Authors

- **Raphael Van Hoffelen** - [github](https://github.com/dskart) - [website](https://www.raphaelvanhoffelen.com/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
