# mazegen

Small maze generator made for the A-Maze-ing project (42 curriculum).
It generates random mazes, perfect or not, with a "42" drawn in the
middle, and it can give you the shortest path from the entry to the exit.

## Install

```
pip install mazegen-1.0.0-py3-none-any.whl
```

## Basic example

```python
from mazegen import MazeGenerator

maze = MazeGenerator(20, 15)      # 20 columns, 15 rows
maze.generate()

print(maze.to_hex_lines())        # the maze, one hex digit per cell
print(maze.get_solution())        # shortest path, e.g. "EESSWS..."
```

## Custom parameters

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

If the parameters are wrong (size out of 2..200, entry or exit outside
the maze or on the "42", entry == exit, non perfect maze too small...)
the constructor raises a `ValueError` with a message.

If the maze is smaller than 9x7 there is no room for the "42": the maze
is generated without it and `maze.has_pattern` is `False`.

## Access the maze

- `maze.grid[y][x]`: an int with the closed walls of the cell
  (`NORTH = 1`, `EAST = 2`, `SOUTH = 4`, `WEST = 8`, all of them
  can be imported from `mazegen`).
- `maze.is_open(x, y, EAST)`: True if you can go east from (x, y).
- `maze.pattern`: set of the (x, y) cells used by the "42".
- `maze.path`: list of the (x, y) cells of the shortest path.
- `maze.get_solution()`: the same path as a string of `N`, `E`, `S`, `W`.
- `maze.count_loops()`: number of independent loops (0 = perfect maze).
- `maze.seed`: seed used, to generate the same maze again.

## Animation

`generate()` accepts an `on_step` function, called every time a wall is
opened. You can use it to draw the maze while it is being generated:

```python
maze.generate(on_step=my_draw_function)
```
