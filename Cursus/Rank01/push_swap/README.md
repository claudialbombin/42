*This project has been created as part of the 42 curriculum by clopez-b, pvivas-f.*

# push_swap

## Description

`push_swap` is a 42 School algorithmic project. Given a random list of integers,
the goal is to sort them in ascending order using two stacks (`a` and `b`) and a
small, fixed set of operations (`sa`, `sb`, `ss`, `pa`, `pb`, `ra`, `rb`, `rr`,
`rra`, `rrb`, `rrr`), while using as few operations as possible.

The project extends the standard push_swap subject with a **disorder index**
(a value between 0 and 1 describing how far the input is from being sorted)
and requires implementing four distinct sorting strategies, each targeting a
different complexity class, plus an adaptive mode that picks between them
based on the disorder index:

| Flag         | Strategy                         | Complexity class |
|--------------|-----------------------------------|-------------------|
| `--simple`   | Selection-based sort               | O(n²)             |
| `--medium`   | Chunk-based sort                   | O(n√n)            |
| `--complex`  | LSD radix sort                     | O(n log n)        |
| `--adaptive` | Picks one of the above (default)   | depends on input  |

Complexity here is always measured as **the number of push_swap operations
generated**, not the theoretical complexity of a classic array-sorting
algorithm (per the subject's model, VI.3.1).

## Instructions

### Build

```
make            # builds push_swap
make bonus      # builds the checker (bonus)
make clean      # removes object files
make fclean     # removes object files and binaries
make re         # fclean + all
```

The Makefile compiles with `-Wall -Wextra -Werror`, uses `cc`, and never
relinks unnecessarily.

### Run

```
./push_swap 2 1 3 6 5 8
```

Prints the shortest sequence of operations found, one per line, to `stdout`.
With no arguments, the program prints nothing and returns control immediately.

### Strategy selector (optional flag)

```
./push_swap --simple 5 4 3 2 1
./push_swap --medium 5 4 3 2 1
./push_swap --complex 5 4 3 2 1
./push_swap --adaptive 5 4 3 2 1   # same as no flag at all
```

### Benchmark mode (optional flag)

```
./push_swap --bench 2 1 3 6 5 8 2> bench.txt
cat bench.txt
```

Prints, to `stderr` only:
- the disorder index (as a percentage, two decimals),
- the strategy used and its theoretical complexity class,
- the total number of operations,
- a breakdown of operations by type.

`stdout` keeps showing only the operation sequence, so it can still be piped
straight into a checker.

### Error handling

Invalid input (non-integer arguments, values outside `int` range, duplicate
values) makes the program print `Error` followed by `\n` to `stderr` and exit,
without printing any operations.

## Project structure

```
push_swap/
├── Makefile
├── README.md
├── includes/
│   ├── push_swap.h
│   └── checker_bonus.h
├── src/
│   ├── main.c
│   ├── parsing/
│   │   ├── build_stack.c
│   │   ├── parser_flags.c
│   │   ├── parser_numbers.c
│   │   ├── nodes.c
│   │   ├── split.c
│   │   ├── ft_atol.c
│   │   ├── utils_parser_num.c
│   │   ├── utils.c
│   │   ├── libft_utils.c
│   │   └── errors_stack.c
│   ├── stack_ops/
│   │   ├── ops_swap.c
│   │   ├── ops_push.c
│   │   ├── ops_rotate.c
│   │   └── ops_reverse.c
│   ├── algorithms/
│   │   ├── disorder_index.c
│   │   ├── simple_sort.c
│   │   ├── linear_sort.c
│   │   ├── medium_sort.c
│   │   ├── medium_sort_extract.c
│   │   ├── medium_sort_chunk_sort.c
│   │   ├── medium_sort_utils.c
│   │   ├── complex_sort.c
│   │   ├── adaptative_sort.c
│   │   ├── small_sort*.c        (exhaustive-search optimal sort, n <= 5)
│   │   └── sort_utils.c
│   ├── bench/
│   │   ├── bench.c
│   │   └── bench_utils.c
│   └── checker_bonus/           (bonus, see "Checker (bonus)" below)
│       ├── checker_bonus.c
│       ├── read_stdin_bonus.c
│       └── exec_instr_bonus.c
└── checker_Mac                  (reference binary supplied by the subject)
```

## Algorithms

### Disorder index

Computed once, before any operation is applied, by counting inversions:
pairs `(i, j)` with `i` before `j` where the value at `i` is greater than the
value at `j`. The result is `mistakes / total_pairs`, where `total_pairs =
n * (n - 1) / 2`. This counting itself never generates any push_swap
operation — it is plain C bookkeeping and is not part of the operation-count
complexity the subject asks us to optimize.

### Simple sort — O(n²)

Repeatedly finds the current minimum of stack `a`, rotates it to the top in
whichever direction is shorter, and pushes it to `b`. The last element left in
`a` is always the maximum, so it is never moved. Finally, `b` is drained back
into `a`, restoring ascending order.

- **Space:** O(1) extra (in-place on the existing nodes).
- **Time (operations):** each of the n iterations costs up to O(n) for the
  minimum search and up to O(n) for the rotation, giving O(n²) operations in
  the worst case.

### Linear sort — O(n)

Used only by the adaptive strategy's low-disorder branch, not exposed as its
own flag. A stack this close to sorted is, in practice, either already sorted
or the sorted sequence rotated by some offset (eg. the last k values moved in
front of the rest) — and that specific shape can be fixed in true O(n):
find the minimum and rotate it to the top in whichever direction is shorter.
A fully general O(n) comparison sort cannot exist for every permutation in
this disorder band (the disorder index only bounds the number of inversions,
not the stack's shape), so as a correctness safety net, the rare low-disorder
stack that turns out not to be a pure rotation falls back to the complex sort
below instead — that path is no longer O(n), but the result is always
correct.

- **Space:** O(1) extra.
- **Time (operations):** O(n) to find the minimum, O(n) to rotate it to the
  top; O(n) overall whenever the input is in fact a rotated sorted sequence.

### Medium sort — O(n√n)

Each value is mapped to its rank (0 to n-1), and ranks are split into chunks
(see the chunk size note below). Chunks are processed from highest to lowest
rank; for each one:

1. **Extract** the chunk in a single bounded pass over `a` (`extract_chunk`,
   the same technique `complex_sort`'s bit passes use, applied to a rank
   range instead of a bit): every element currently in `a` is looked at
   exactly once — `pb` if its rank falls in the chunk, `ra` otherwise — so
   this always costs exactly the current size of `a`, never more, no matter
   how many elements match.
2. **Sort that isolated chunk** entirely within `b` (`drain_chunk_sorted`):
   repeatedly find the current max among the chunk's (at most √n-ish)
   elements, rotate it to the top of `b`, and `pa` it onto `a`. Because the
   picks happen highest-to-lowest, each chunk's own values end up ascending
   from the top once its turn is done.

Processing chunks highest rank first means each finished chunk sits directly
on top of `a`, and the next (lower) chunk's extraction pass simply rotates
straight past that already-sorted portion — so by the time the lowest chunk
is placed, `a` is fully sorted with nothing left to unload from `b`.

- **Space:** O(1) extra.
- **Time (operations):** each of the `n / chunk` extraction passes costs the
  current size of `a` (it does not shrink between chunks — see the chunk
  size note), and each isolated chunk costs O(chunk²) to sort internally;
  summed over every chunk this is `O(n² / chunk + n·chunk)`, which is
  `O(n√n)` for any `chunk = Θ(√n)`.

**Chunk size note:** a plain `chunk = √n` minimizes the two terms above
*in theory*, but not in practice, because they don't carry equal real
weight — the `n² / chunk` extraction term dominates (it never shrinks
between chunks), while the `n·chunk` internal-sort term is comparatively
cheap. Minimizing `D·n²/chunk + C·n·chunk` for the true measured constants
(`D ≈ 1`, `C ≈ 0.13`, fit against actual `--bench` output) gives an optimum
around `chunk ≈ 3√n`, not `√n`. Empirically this cuts the worst-case
operation count for 500 random numbers from ~13 000 down to ~9 000 — the
difference between failing and comfortably clearing the subject's
12 000-operation minimum (see VI.6). `chunk_length()` implements this tuned
formula (`chunk² ≥ 9n`), not the naive one.

### Complex sort — O(n√n)

A chunked selection sort adapted to stacks. Each value is mapped to its rank
(0 to n-1) via `assign_indexes`. Elements are then distributed from `a` into
`b` in bands of width `k = √(1.4n)`: a running `counter` tracks the current
band's lower bound, and each element is pushed to `b` (with an extra `rb` if
it falls into the *next* band) once its rank falls within reach; elements
outside the current band are rotated to the bottom of `a` with `ra` until
their band comes around. This leaves `b` holding groups of already
loosely-ordered elements instead of one arbitrary jumble.

`ksort_back` then repeatedly extracts the current maximum from `b`: the
node's position relative to the top is compared to `b`'s midpoint, and `b` is
rotated with `rb` or `rrb` — whichever is cheaper — until the target node
surfaces, then it's pushed to `a` with `pa` (a following `sa` fixes the
top pair if needed). The second-highest rank is pushed directly without
searching, since it's already known to sit just behind the max. Repeating
this until `b` is empty leaves `a` fully sorted.

- **Space:** O(1) extra.
- **Time (operations):** the banding phase is O(n); `ksort_back` performs up
  to n extractions, each costing O(√n) on average thanks to the band width
  chosen in `ft_complex_sort`, giving roughly O(n√n) operations overall.

### Adaptive sort

Picks one of the three strategies above based on the disorder index computed
at the start:

| Disorder range   | Strategy used | Complexity |
|-------------------|--------------|------------|
| `< 0.2`            | Linear sort   | O(n)      |
| `0.2` to `< 0.5`   | Medium sort   | O(n√n)     |
| `>= 0.5`           | Complex sort  | O(n log n) |

> **Erratum note:** the written subject states that low disorder (`< 0.2`)
> should use O(n). This was confirmed by staff during a live correction
> session to be a typo in the subject text: the intended mapping is low
> disorder → O(n), medium disorder → O(n√n), high disorder → O(n log n),
> which is the mapping implemented and described above.

**Threshold justification:**

- **`0.5` (high disorder cutoff):** for a uniformly random permutation of n
  distinct values, the expected number of inversions is `n(n-1)/4`, i.e. the
  expected disorder index is exactly `0.5`. Using `0.5` as the cutoff for the
  most general-purpose strategy (radix sort, which makes no assumption about
  the input's structure) means: anything at or above "average shuffle"
  randomness gets the strategy with the strongest worst-case guarantee.
- **`0.2` (low disorder cutoff):** below this point, fewer than one in five
  possible pairs are inverted, which in practice corresponds to inputs that
  are already nearly sorted or the sorted sequence rotated by some offset —
  exactly the shape linear sort fixes in true O(n). Above this point the
  input is more likely to contain a structure linear sort can't guarantee to
  fix in one pass, so it hands off to a strategy with a general worst-case
  guarantee instead.
- **`[0.2, 0.5)` (medium band):** the remaining range is handled by the
  chunk-based sort, giving a middle-ground operation count that fits inputs
  that are partially, but not extremely, shuffled.

## Bonus: checker

`checker` verifies that a sequence of push_swap operations actually sorts a
given stack, per the subject's bonus specification (VIII.1). It is not built
by `make`/`make all` — build it separately with `make bonus`.

### Usage

```
./push_swap 2 1 3 6 5 8 | ./checker 2 1 3 6 5 8
```

- Takes stack `a` as a list of integers, same argument format (and the same
  parsing/validation) as `push_swap` — the first argument is the top of the
  stack.
- Reads a sequence of instructions from `stdin`, one per line, until EOF.
- Applies each instruction to the stack, then prints to `stdout`:
  - **`OK`** if `a` ends up sorted ascending and `b` is empty;
  - **`KO`** otherwise.
- On error (non-integer or out-of-range arguments, duplicate values, or an
  instruction that isn't one of the 11 valid ones / is malformed) it prints
  `Error` to `stderr` instead, matching `push_swap`'s own error contract.
  With no arguments at all, it prints nothing and exits immediately.

### Implementation

`checker` deliberately shares almost all of its code with `push_swap` rather
than reimplementing stack parsing or the 11 operations from scratch:
`ft_build_stack` builds the stack from `argv` exactly as `push_swap` does,
and each instruction line is dispatched straight to the real `ft_sa`, `ft_pa`,
`ft_ra`, ... entry points that actually mutate the stacks — with printing and
bench-counting turned off (`print = 0`, `bench = NULL`), both parameters
those functions already take for every caller, so no change to the mandatory
code was needed to reuse them here. Only three pieces are checker-specific:
reading the whole of `stdin` into a buffer (`checker_read_stdin`, since
`realloc` isn't in the subject's authorized function list, so the buffer is
grown by allocating a new block and copying, not resizing in place),
splitting it into instruction lines, and matching each line against the 11
valid instruction names (`checker_apply_line`).

### Verification

Checked against the reference `checker_Mac` binary supplied with the subject:
piping real `push_swap` output for randomized stacks (sizes 0–500) through
both always agrees; deliberately shuffled (incorrect) instruction sequences
agree on `KO`; every error case (non-integer/out-of-range/duplicate
arguments, unknown or malformed instructions) agrees on `Error`.

## Resources

- Donald Knuth, *The Art of Computer Programming, Vol. 3: Sorting and
  Searching* — background on sorting algorithms and Big-O notation.
- Wikipedia: [Radix sort](https://en.wikipedia.org/wiki/Radix_sort),
  [Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort),
  [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation).
- 42 Norm v4.1 — coding style requirements applied throughout this project.
- 42 push_swap subject (this repository's `en_norm.pdf` / project subject
  files) for the operation definitions and evaluation criteria.

### AI usage disclosure

AI assistance was minimaly used in the early design stages to design the
project architecture and to understand the initial logic of the stack
operations (`sa`/`sb`/`ss`/`pa`/`pb`/`ra`/`rb`/`rr`/`rra`/`rrb`/`rrr`), the
disorder index calculation, to help choose the four sorting strategies and to understand the benchmark mode.
