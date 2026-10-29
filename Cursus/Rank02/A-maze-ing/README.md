*This project has been created as part of the 42 curriculum by clopez-b and javiesan.*

# A-Maze-ing

## Description

A-Maze-ing is a maze generator written in Python. It reads a small
configuration file, generates a random maze (always the same one for the
same seed), writes it in a file using one hexadecimal digit per cell and
shows it in the terminal with colours.

Every maze has a "42" drawn in the middle with fully closed cells. There
are two modes:

- **PERFECT=True**: a perfect maze, there is exactly one path between the
  entry and the exit (no loops at all).
- **PERFECT=False**: a board for a Pac-Man like game: every cell can be
  reached, the corners and the centre are corridors, there are a lot of
  loops and there are no dead-ends (only the ones closed by the "42"
  itself, which can't be opened).

The generation part is a separate package (`mazegen`) so it can be reused
in a later project.

## Instructions

Python 3.10 or later is needed. Nothing has to be installed to run the
program, the extra tools are only for lint and for building the package.

```
python3 -m venv .venv
source .venv/bin/activate
make install        # flake8, mypy and build
```

Run the program:

```
python3 a_maze_ing.py config.txt
make run            # same thing with the default config.txt
make debug          # run it inside pdb
make lint           # flake8 + mypy with the flags of the subject
make lint-strict    # flake8 + mypy --strict
make build          # build mazegen and copy the .whl to the root
make clean          # remove caches and build folders
```

Once the maze is shown, the menu under it lets you:

1. Re-generate a new maze (with a new random seed, printed under the maze)
2. Show / Hide the shortest path
3. Rotate the wall colours
4. Rotate the "42" colours
5. Quit

Each new maze is also written again in the output file, so the file
always matches what is on the screen. The output file can be checked with
the script given with the subject:

```
python3 maze_analyzer.py maze.txt                     # PERFECT=True
python3 maze_analyzer.py maze.txt --max-dead-ends 0   # PERFECT=False
```

## Configuration file

One `KEY=VALUE` per line. Empty lines and lines starting with `#` are
ignored. Spaces around the key and the value are ignored too.

| Key           | Mandatory | Description                          | Example            |
|---------------|-----------|--------------------------------------|--------------------|
| `WIDTH`       | yes       | Number of columns (2 to 200)         | `WIDTH=20`         |
| `HEIGHT`      | yes       | Number of rows (2 to 200)            | `HEIGHT=15`        |
| `ENTRY`       | yes       | Entry cell `x,y`                     | `ENTRY=0,0`        |
| `EXIT`        | yes       | Exit cell `x,y`                      | `EXIT=19,14`       |
| `OUTPUT_FILE` | yes       | File where the maze is written       | `OUTPUT_FILE=maze.txt` |
| `PERFECT`     | yes       | `True` or `False`                    | `PERFECT=True`     |
| `SEED`        | no        | Seed (random if not given)           | `SEED=42`          |
| `ALGORITHM`   | no        | `backtracker` (default) or `prim`    | `ALGORITHM=prim`   |
| `ANIMATION`   | no        | Show the generation step by step     | `ANIMATION=True`   |

`x` is the column and `y` is the row, `0,0` is the top left corner.

The program stops with a clear message (and never with a traceback) if:
the file does not exist or can't be read, a line has no `=`, a key is
unknown or repeated, a mandatory key is missing, a value has a wrong type,
the size is out of range, the entry or the exit is outside the maze, on the
"42" or both are the same cell, or a non perfect maze is too small to have
loops. If the maze is smaller than 9x7, the "42" does not fit: an error
message is printed and the maze is generated without it.

## Output file

```
<one line per row, one hex digit per cell>

<entry x,y>
<exit x,y>
<shortest path with N, E, S, W>
```

Each digit says which walls are closed: bit 0 = North, bit 1 = East,
bit 2 = South, bit 3 = West (`F` = the 4 walls closed).

## Maze generation algorithm

The default algorithm is the **recursive backtracker** (a random depth
first search):

1. Start at the entry and mark it as visited.
2. Look at the neighbours not visited yet (the "42" cells are skipped).
3. If there is one, pick one at random, open the wall between both cells
   and move to it.
4. If there is none, go back to the previous cell.
5. Stop when we are back at the start.

It gives a spanning tree of all the cells, so the maze is perfect. I wrote
it with a list used as a stack instead of real recursion, because with big
mazes Python reaches the recursion limit.

For `PERFECT=False` I start from the same perfect maze and then **braid**
it: for every dead-end I open one more wall (if possible towards another
dead-end, so two of them disappear at once). Before opening a wall I check
that it does not create a 3x3 open area, because corridors can't be wider
than 2 cells. At the end I check that the maze has at least 2 independent
loops (`loops = edges - cells + 1`).

The shortest path is found with a BFS from the entry.

### Why this algorithm

- It is the easiest one to understand and to explain: it is just a DFS.
- The mazes have long corridors with few branches, they look nice and they
  are hard to solve.
- Working with the "42" is easy: its cells are simply never visited.

## Project structure

Each folder does only one thing, and `a_maze_ing.py` just calls them:

```
A-maze-ing/
├── a_maze_ing.py          main: read config -> session -> menu
├── config.txt             default configuration
├── parsing/               the configuration file
│   ├── errors.py          ConfigError
│   ├── maze_config.py     MazeConfig (the options) + list of keys
│   ├── reader.py          read the file, split KEY=VALUE, check syntax
│   ├── converters.py      text -> int / (x, y) / bool
│   └── parser.py          read_config(): uses reader + converters
├── mazegen/               the generator (reusable package)
│   ├── constants.py       wall bits, moves, "42" pattern, limits
│   ├── grid.py            MazeGrid: walls and basic operations
│   ├── checks.py          check the parameters before generating
│   ├── pattern.py         place the "42" in the middle
│   ├── algorithms/
│   │   ├── backtracker.py recursive backtracker (DFS)
│   │   └── prim.py        randomized Prim (bonus)
│   ├── open_area.py       the "no 3x3 open area" rule
│   ├── braid.py           perfect maze -> Pac-Man board
│   ├── solver.py          shortest path (BFS) and N/E/S/W letters
│   └── generator.py       MazeGenerator: calls all the files above
├── output/                the output file
│   ├── errors.py          OutputError
│   ├── formatter.py       build the text of the file
│   └── writer.py          write it on disk
├── display/               drawing in the terminal
│   ├── colours.py         ANSI codes and colour lists
│   ├── pixels.py          colour of every pixel of the drawing
│   ├── terminal.py        TerminalDisplay: options + draw()
│   └── animation.py       animated generation (bonus)
└── app/                   the program itself
    ├── messages.py        texts shown to the user
    ├── session.py         MazeSession: config + maze + display
    └── menu.py            the interactive menu
```

The dependencies only go in one direction: `app` uses `parsing`,
`mazegen`, `output` and `display`, but `mazegen` never imports anything
from the rest of the project.

## Reusable part

Only the `mazegen/` folder is reusable (and it is the only thing that
goes in the package): the `MazeGenerator` class does not print anything
and does not touch files. The other folders are only for this project.

The package is already built at the root of the repository:
`mazegen-1.0.0-py3-none-any.whl`. To build it again from the sources:

```
python3 -m venv .venv
source .venv/bin/activate
pip install build
python3 -m build            # creates dist/mazegen-1.0.0-py3-none-any.whl
```

(or just `make build`). Then, in any other project:

```
pip install mazegen-1.0.0-py3-none-any.whl
```

### Basic example

```python
from mazegen import MazeGenerator

maze = MazeGenerator(20, 15)      # 20 columns, 15 rows
maze.generate()

print(maze.to_hex_lines())        # the maze, one hex digit per cell
print(maze.get_solution())        # shortest path, e.g. "EESSWS..."
```

### Custom parameters

```python
maze = MazeGenerator(
    width=30,
    height=20,
    entry_pos=(0, 0),        # (x, y)
    exit_pos=(29, 19),       # (x, y)
    perfect=False,           # False = board with loops, no dead-ends
    seed=1234,               # same seed = same maze
    algorithm="prim",        # "backtracker" (default) or "prim"
)
maze.generate()
maze.generate(seed=99)       # new maze with another seed
```

Wrong parameters raise a `ValueError` with a message.

### Access the structure and the solution

- `maze.grid[y][x]`: int with the closed walls of the cell (`NORTH = 1`,
  `EAST = 2`, `SOUTH = 4`, `WEST = 8`, they can be imported from `mazegen`).
- `maze.is_open(x, y, EAST)`: True if you can go east from (x, y).
- `maze.pattern`: set of the (x, y) cells of the "42".
- `maze.has_pattern`: False if the maze was too small for the "42".
- `maze.path`: list of the (x, y) cells of the shortest path.
- `maze.get_solution()`: the same path as a string of `N`, `E`, `S`, `W`.
- `maze.count_loops()`: number of independent loops (0 = perfect maze).
- `maze.seed`: the seed used, to get the same maze again.

## Bonus

- **No dead-end at all** in the default (non perfect) mode: the braiding
  removes all of them, `maze_analyzer.py --max-dead-ends 0` says
  "bonus-grade (perfectly braided)".
- **Two generation algorithms**: `ALGORITHM=backtracker` (DFS) and
  `ALGORITHM=prim` (randomized Prim: the maze grows from the entry by
  opening a random wall of the "frontier" each time, it gives shorter
  corridors and more branches).
- **Animation**: with `ANIMATION=True` the maze is drawn while it is being
  generated (the generator calls a function each time it opens a wall).

## Notes about the subject

Things I found while reading the subject (v2.2) and how I understood them:

- `PERFECT` is in the table of mandatory keys, but the text also talks
  about "the default" when it is not activated. I made it mandatory, as
  the table says.
- "Corridors can't be wider than 2 cells" + "2x3 is ok, 3x3 is not": I
  understood that no 3x3 block can be fully open.
- Nothing is said about an entry or exit placed on the "42": I show an
  error because those cells must be fully closed.
- For an even width or height there is no single centre cell. The "42"
  is placed so its empty middle column is always in the centre, so the
  centre is always a corridor.
- The example output file has `# entry (x,y)` next to the coordinates. I
  think it is only an explanation in the picture, so I don't write it
  (`maze_analyzer.py` would not read the coordinates with it).
- Page 8 tolerates "a couple" of dead-ends in the default mode, page 10
  says no dead-ends besides the "42". Mine has none, so both are fine.

## Resources

- [Maze generation algorithm - Wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Jamis Buck - Maze Generation: Recursive Backtracking](https://weblog.jamisbuck.com/2010/12/27/maze-generation-recursive-backtracking)
- [Jamis Buck - Maze Generation: Prim's Algorithm](https://weblog.jamisbuck.com/2011/1/10/maze-generation-prim-s-algorithm)
- [Think Labyrinth - Maze Algorithms (braid mazes)](https://www.astrolog.org/labyrnth/algrithm.htm)
- [Python docs - random, collections.deque, dataclasses](https://docs.python.org/3/library/)
- [Python Packaging User Guide - pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [PEP 257 - Docstring conventions](https://peps.python.org/pep-0257/)
- [ANSI escape codes (256 colours)](https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit)
- [choosealicense.com - MIT License](https://choosealicense.com/licenses/mit/)

### Use of AI

AI (Claude) was used as a support tool during the project: to go through
the subject and list its ambiguities, to explain and compare the
generation algorithms, to help write and review parts of the code (mainly
the braiding and the 3x3 check) and the documentation, and to find edge
cases for the config file. Every part was reviewed, tested with
`maze_analyzer.py`, flake8 and mypy, and I can explain all of it.

## Team and project management

- **clopez-b**: everything (generation, config parsing, output file,
  terminal display, package, documentation).

**Planning.** The first plan was: config parser and output file first,
then a perfect maze with the backtracker, then the display and the menu,
and the package at the end. It changed a bit: the "42" pattern had to be
placed before generating (the entry and the exit must be checked against
it) and the non perfect mode took longer than expected because of the 3x3
rule and the corners / centre requirements. The bonus (Prim and the
animation) came at the end.

**What worked well.** Keeping the generator in its own class without any
print from the start made the package part very easy. The analyzer given
with the subject was really useful to test hundreds of seeds.

**What could be improved.** A MiniLibX display would look better than the
terminal, and more algorithms (Kruskal, Wilson) could be added.

**Tools.** Python 3.10, flake8, mypy, pdb, `build`, venv, git and
`maze_analyzer.py`.
