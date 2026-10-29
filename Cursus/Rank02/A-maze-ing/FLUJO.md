# A-Maze-ing: cómo funciona por dentro

Guía para entender el flujo completo del programa: qué pasa desde que
escribes `python3 a_maze_ing.py config.txt` hasta que sale el laberinto,
qué archivo hace cada cosa y dónde tocar si en la defensa te piden un
cambio.

---

## 1. Vista general

```
config.txt
    │
    ▼
┌──────────────┐   MazeConfig    ┌──────────────┐
│   parsing/   │ ──────────────► │    app/      │
│ lee y valida │                 │  session.py  │
└──────────────┘                 └──────┬───────┘
                                        │ crea MazeGenerator(...)
                                        ▼
                                 ┌──────────────┐
                                 │   mazegen/   │  ← paquete reutilizable
                                 │ genera, crea │
                                 │ bucles, BFS  │
                                 └──────┬───────┘
                       laberinto ya     │
                       generado         │
                 ┌──────────────────────┴───────────────┐
                 ▼                                      ▼
          ┌──────────────┐                       ┌──────────────┐
          │   output/    │                       │   display/   │
          │ escribe el   │                       │ lo dibuja en │
          │ maze.txt     │                       │ la terminal  │
          └──────────────┘                       └──────────────┘
                                        ▲
                                        │ redibuja
                                 ┌──────┴───────┐
                                 │ app/menu.py  │  ← bucle del menú
                                 └──────────────┘
```

Regla importante: **`mazegen/` no importa nada del resto del proyecto**.
Las flechas solo van hacia `mazegen`, nunca salen de él. Por eso se puede
empaquetar solo en el `.whl` y reutilizar en otro proyecto.

| Carpeta    | Responsabilidad                                   | Se reutiliza |
|------------|---------------------------------------------------|--------------|
| `parsing/` | Leer el `config.txt` y convertir los valores      | No           |
| `mazegen/` | Generar el laberinto, el "42", los bucles y el camino | **Sí**   |
| `output/`  | Escribir el fichero de salida                     | No           |
| `display/` | Dibujar en la terminal con colores                | No           |
| `app/`     | Pegar todo: sesión + menú                         | No           |

---

## 2. El flujo paso a paso

### Paso 0: arranque (`a_maze_ing.py` → `main()`)

```python
if len(sys.argv) != 2:          # sin argumento o con demasiados
    print(USAGE); return 1
try:
    config = read_config(sys.argv[1])        # Paso 1
    session = MazeSession(config)            # Paso 2
    if not session.maze.has_pattern:
        print(NO_PATTERN)                    # el "42" no cabe
    session.new_maze(session.maze.seed)      # Pasos 3, 4 y 5
    run_menu(session)                        # Paso 6
except ConfigError / ValueError / OutputError / KeyboardInterrupt
```

`main()` no hace ningún trabajo: solo llama a las piezas en orden y
**captura todas las excepciones**, así que el programa nunca acaba con un
traceback. Devuelve 0 si todo va bien y 1 si hay algún error, y
`sys.exit(main())` lo convierte en el código de salida del programa.

---

### Paso 1: leer el config (`parsing/`)

```
parser.read_config(path)
   │
   ├── reader.read_pairs(path)
   │      ├── _read_lines(path)     abre el fichero con "with"
   │      │                         FileNotFound / IsADirectory /
   │      │                         Permission / UnicodeDecode → ConfigError
   │      └── por cada línea:
   │            - vacía o empieza por '#' → se ignora
   │            - _split_line()       ¿tiene '='? ¿la clave existe?
   │                                  ¿el valor está vacío?
   │            - ¿clave repetida?   → ConfigError
   │      devuelve {"WIDTH": "20", "ENTRY": "0,0", ...}  (todo texto)
   │
   ├── ¿están las 6 claves obligatorias?  → si no, ConfigError
   │
   ├── converters.py convierte cada valor:
   │      to_int("WIDTH", "20")        → 20
   │      to_coords("ENTRY", "0,0")    → (0, 0)
   │      to_bool("PERFECT", "False")  → False
   │
   ├── claves opcionales (SEED, ALGORITHM, ANIMATION): si no están,
   │   se quedan con su valor por defecto de MazeConfig
   │
   └── ¿OUTPUT_FILE es el propio config?  → ConfigError
       (si no se comprobara, el programa borraría tu config.txt)

devuelve MazeConfig(width=20, height=15, entry=(0,0), exit=(19,14),
                    output_file="maze.txt", perfect=False, seed=42,
                    algorithm="backtracker", animation=False)
```

**¿Por qué está dividido así?**
- `reader.py` solo comprueba la **sintaxis** (KEY=VALUE).
- `converters.py` solo comprueba los **tipos** (¿es un int? ¿es x,y?).
- `parser.py` junta las dos cosas y comprueba que **no falte nada**.
- En `parsing/` no se mira si los valores tienen sentido (por ejemplo, si
  la entrada cae dentro del laberinto). Eso lo comprueba `mazegen/checks.py`,
  porque es una regla del laberinto y no del fichero.

---

### Paso 2: crear la sesión y el generador (`app/session.py`)

```python
MazeSession(config)
   ├── self.maze = MazeGenerator(width, height, entry, exit,
   │                             perfect, seed, algorithm)
   └── self.display = TerminalDisplay()
```

Al **crear** el `MazeGenerator` (su `__init__`) todavía no se genera
nada; solo se comprueba que con esos parámetros se puede hacer un
laberinto válido:

```
MazeGenerator.__init__
   ├── checks.check_size(w, h)        2 ≤ w, h ≤ 200         → ValueError
   ├── checks.check_algorithm(alg)    "backtracker" o "prim" → ValueError
   ├── exit por defecto = esquina de abajo a la derecha (si no se pasa)
   ├── seed por defecto = random.randint(0, 999999) (si no se pasa)
   ├── pattern.pattern_cells(w, h)    → set con las celdas del "42"
   │                                    (vacío si no cabe)
   ├── MazeGrid(w, h, pattern)        grid temporal para las comprobaciones
   ├── checks.check_cells(...)        entrada/salida dentro, que no caigan
   │                                  en el "42" y que sean distintas → ValueError
   └── si PERFECT=False:
         checks.check_loops_possible  ¿cabe un mínimo de 2 bucles? → ValueError
```

Así, un config imposible falla **antes** de dibujar nada.

---

### Paso 3: generar el laberinto (`mazegen/generator.py` → `generate()`)

```python
session.new_maze(seed)
   ├── si ANIMATION=True → display.animate(...)   (llama a generate con on_step)
   │   si no             → maze.generate(seed)
   └── write_maze(maze, output_file)              (Paso 4)
```

Dentro de `generate()`:

```
1. rng = random.Random(seed)       ← generador aleatorio PROPIO
2. grid = MazeGrid(...)            ← todas las celdas a 15 (4 muros cerrados)
3. carve_backtracker() o carve_prim()   → laberinto perfecto
4. si PERFECT=False:
      braid()      → quita los callejones sin salida
      add_loops()  → asegura un mínimo de 2 bucles
5. path = find_path(entry, exit)   → BFS, camino más corto
```

**Reproducibilidad (la semilla):** se usa `random.Random(seed)` y no el
`random` global. Con la misma semilla las llamadas a `choice`, `shuffle`
y `randrange` dan siempre los mismos números, en el mismo orden, así que
sale exactamente el mismo laberinto. Por eso se muestra la semilla debajo
del laberinto.

Cada parte se explica en detalle en la sección 3.

---

### Paso 4: escribir el fichero (`output/`)

```
writer.write_maze(maze, path)
   ├── formatter.maze_to_text(maze)    construye TODO el texto primero
   │      "D53D5551...\n"   ← una línea por fila (maze.to_hex_lines())
   │      ...
   │      "\n"              ← línea vacía
   │      "0,0\n"           ← entrada x,y
   │      "19,14\n"         ← salida x,y
   │      "EESSWS...\n"     ← camino (maze.get_solution())
   └── open(path, "w") con "with" y escribe   → si falla: OutputError
```

Se construye el texto antes de abrir el fichero para que, si algo falla,
no quede un fichero escrito a medias.

---

### Paso 5: dibujar (`display/`)

```
TerminalDisplay.draw(maze, info)
   ├── Palette(color_muro_actual, color_42_actual)
   ├── path_cells = set(maze.path) si show_path, si no vacío
   ├── para cada píxel (px, py) de la rejilla (2·W+1) x (2·H+1):
   │      pixels.pixel_colour(...)  → número de color o None
   │      colours.block(color)      → "  " con fondo de color ANSI
   └── CLEAR + todas las líneas + info, en UN SOLO print
```

Se imprime todo de golpe para que la pantalla no parpadee, sobre todo en
la animación. Ver la sección 3.7 para el truco de los píxeles.

---

### Paso 6: el menú (`app/menu.py`)

```
run_menu(session)
   bucle:
     ├── draw(maze, info_text + MENU)
     ├── input("Choice? (1-5): ")
     │      Ctrl-D (EOFError) o Ctrl-C (KeyboardInterrupt) → salir
     ├── "5" → return (salir)
     └── _do_choice:
           "1" → session.new_maze(random.randint(...))   nueva semilla
                 (vuelve a hacer los pasos 3 y 4, también se reescribe maze.txt)
           "2" → display.show_path = not show_path
           "3" → display.next_wall_colour()
           "4" → display.next_pattern_colour()
           otra cosa → no hace nada, se vuelve a pintar el menú
```

---

## 3. Las piezas por dentro

### 3.1 Cómo se guardan los muros (`constants.py` + `grid.py`)

Cada celda es **un int de 4 bits**, un bit por muro (1 = cerrado):

```
bit:     3     2     1     0
muro:    W     S     E     N
valor:   8     4     2     1
```

| Valor | Binario | Muros cerrados   |
|-------|---------|------------------|
| `F` (15) | 1111 | los 4 (celda del "42" o celda sin abrir) |
| `A` (10) | 1010 | E y W (pasillo vertical) |
| `5` (5)  | 0101 | N y S (pasillo horizontal) |
| `3` (3)  | 0011 | N y E |

Operaciones de bits que se usan:
- **¿está abierto?** `not (celda & EAST)` → si el bit vale 0, está abierto.
- **abrir:** `celda &= ~EAST` → pone ese bit a 0.
- **cerrar:** `celda |= EAST` → pone ese bit a 1.

`grid.cells[y][x]`: primero la fila (y) y luego la columna (x).
Las coordenadas siempre se pasan como `(x, y)`, igual que en el subject.

**Coherencia:** `set_wall()` siempre cambia **las dos celdas**. Si abres el
muro E de (3,2), también abre el muro W de (4,2). Por eso el analizador
nunca encuentra muros incoherentes. `MOVES` dice hacia dónde está el
vecino y `OPPOSITE` qué muro es desde el otro lado.

---

### 3.2 El "42" (`pattern.py`)

```
PATTERN_42 = "#.#.###"     # = celda cerrada
             "#.#...#"     . = celda normal
             "###.###"
             "..#.#.."
             "..#.###"
               ↑
           columna central vacía
```

- Mide 7x5 y necesita 1 celda libre alrededor, así que el laberinto tiene
  que ser como mínimo **9x7**. Si no cabe, se devuelve un set vacío,
  `has_pattern = False` y se muestra el mensaje de error que pide el subject.
- Se centra con `left = (W - 7) // 2` y `top = (H - 5) // 2`.
- La **columna central del patrón está vacía** y siempre cae en el centro
  del laberinto. Así el centro es un pasillo, que es justo lo que pide el
  modo Pac-Man (el jugador empieza ahí).
- Las celdas del "42" **nunca se visitan**: los algoritmos las saltan
  porque `is_free()` devuelve False. Por eso se quedan a 15 (`F`).

---

### 3.3 Laberinto perfecto: backtracker (`algorithms/backtracker.py`)

Es un DFS aleatorio con una **pila** en vez de recursión, porque con un
laberinto de 200x200 Python llegaría al límite de recursión.

```
pila = [entrada], visitadas = {entrada}
mientras haya pila:
    celda = cima de la pila
    vecinos libres y no visitados
    si no hay ninguno → pop (retrocede)
    si hay → elige uno al azar, abre el muro, lo marca y hace push
```

Recorre todas las celdas libres y abre exactamente N-1 muros para N
celdas, así que forma un **árbol de expansión**: hay un único camino entre
dos celdas cualesquiera y por tanto es perfecto. Da pasillos largos y con
pocas ramas.

### 3.4 Laberinto perfecto: Prim (`algorithms/prim.py`), bonus

```
frontera = muros alrededor de la entrada
mientras haya frontera:
    saca un muro AL AZAR
    si la celda de detrás ya está visitada → lo ignora
    si no → abre el muro, la marca y añade sus muros a la frontera
```

También da un árbol, pero con pasillos cortos y muchas ramas. El
`swap + pop()` sirve para sacar un elemento al azar en O(1) en vez de
`pop(index)`, que es O(n).

---

### 3.5 Modo Pac-Man: braid + bucles (`braid.py` + `open_area.py`)

Solo se ejecuta con `PERFECT=False`. Parte del laberinto perfecto:

**`braid()`**: para cada callejón sin salida (celda con 1 sola abertura):
1. Busca sus muros cerrados hacia celdas libres.
2. Prefiere un vecino que **también sea callejón**, porque así se quitan
   dos callejones de una vez.
3. Intenta abrirlo con `try_open()`.

**`try_open()`**: abre el muro y comprueba con `makes_big_area()` si se ha
formado un bloque 3x3 sin muros. Si se ha formado, lo vuelve a cerrar y
devuelve False. Es la regla del subject de que los pasillos no pueden
tener más de 2 celdas de ancho.

**`is_open_block()`**: un bloque 3x3 tiene 12 muros interiores (6 E y 6 S).
Si están los 12 abiertos, es un área abierta prohibida.

**`add_loops()`**: comprueba que quedan **≥ 2 bucles**. Casi siempre ya se
cumple después de braid; si no, abre muros al azar hasta conseguirlo.

**Fórmula de los bucles** (`grid.count_loops()`):
```
bucles = aristas - celdas + 1
```
Un árbol tiene aristas = celdas - 1, así que 0 bucles (laberinto perfecto).
Cada muro que abres de más añade un bucle.

Los únicos callejones que quedan son los que **encierra el propio "42"**
(por ejemplo, el hueco de dentro del 4), porque esos muros dan a celdas del
patrón y no se pueden abrir. El analizador los cuenta aparte como
"enclosed" y los permite, así que da el bonus igualmente.

---

### 3.6 Camino más corto: BFS (`solver.py`)

```
came_from = {entrada: None}, cola = [entrada]
mientras haya cola:
    celda = popleft()
    si es la salida → para
    por cada dirección con el muro ABIERTO y vecino no visto:
        came_from[vecino] = celda; lo mete en la cola
reconstrucción: desde la salida sigue came_from hasta la entrada y le da la vuelta
```

BFS explora por distancias (primero las celdas a 1 paso, luego a 2, etc.),
así que **la primera vez que llega a la salida es por el camino más
corto**. En modo perfecto solo existe un camino; en modo Pac-Man hay
varios y BFS encuentra el más corto. `path_to_letters()` convierte la
lista de celdas en `"EESSWN..."`.

---

### 3.7 Dibujo: la rejilla de píxeles (`pixels.py`)

Un laberinto de W x H se dibuja como una rejilla de **(2W+1) x (2H+1)**
"píxeles":

```
px:  0 1 2 3 4
py 0 █ █ █ █ █     par, par     → esquina (siempre muro)
   1 █ · ? · █     impar, impar → celda (x = px//2, y = py//2)
   2 █ ? █ ? █     par, impar   → muro vertical (E de la celda de la izquierda)
   3 █ · ? · █     impar, par   → muro horizontal (S de la celda de arriba)
   4 █ █ █ █ █
```

Prioridad de colores en una celda: **entrada > salida > "42" > camino >
vacía**. Así la entrada y la salida se ven aunque el camino pase por
encima.

El hueco entre dos celdas del camino también se pinta del color del
camino para que se vea una línea continua. Funciona porque en un camino
más corto, dos celdas vecinas y conectadas siempre son consecutivas.

Cada píxel son **2 espacios** con color de fondo ANSI (`\033[48;5;Nm`),
porque un carácter es el doble de alto que de ancho y así el laberinto
se ve cuadrado.

### 3.8 Animación (`animation.py`), bonus

`generate()` acepta una función `on_step`. `MazeGrid.carve()` y
`try_open()` la llaman cada vez que abren un muro. `animate()` le pasa
una función que redibuja **cada N pasos** (máximo unos 300 frames) con
una pausa de 0,01 s. Así el generador no sabe nada de la terminal: solo
avisa de que ha abierto un muro.

---

## 4. ¿Qué error sale de dónde?

| Situación | Dónde se detecta | Excepción | Mensaje (resumido) |
|-----------|------------------|-----------|--------------------|
| Sin argumento / 2 argumentos | `main()` | (ninguna) | `Usage: ...` |
| El config no existe | `reader._read_lines` | ConfigError | `config file 'x' not found` |
| El config es una carpeta | `reader._read_lines` | ConfigError | `is a directory` |
| Línea sin `=` | `reader._split_line` | ConfigError | `expected KEY=VALUE` |
| Clave desconocida | `reader._split_line` | ConfigError | `unknown key` |
| Valor vacío | `reader._split_line` | ConfigError | `has no value` |
| Clave repetida | `reader.read_pairs` | ConfigError | `is repeated` |
| Falta una clave obligatoria | `parser.read_config` | ConfigError | `missing mandatory key` |
| `WIDTH=abc` | `converters.to_int` | ConfigError | `must be an integer` |
| `ENTRY=1` | `converters.to_coords` | ConfigError | `must look like x,y` |
| `PERFECT=maybe` | `converters.to_bool` | ConfigError | `must be True or False` |
| OUTPUT_FILE = el propio config | `parser.read_config` | ConfigError | `can't be the config file` |
| Tamaño fuera de 2..200 | `checks.check_size` | ValueError | `must be between 2 and 200` |
| Algoritmo desconocido | `checks.check_algorithm` | ValueError | `unknown algorithm` |
| Entrada/salida fuera del laberinto | `checks.check_cells` | ValueError | `is outside the maze` |
| Entrada/salida sobre el "42" | `checks.check_cells` | ValueError | `is on the '42' pattern` |
| Entrada == salida | `checks.check_cells` | ValueError | `must be different` |
| Modo Pac-Man demasiado pequeño (2x2) | `checks.check_loops_possible` | ValueError | `too small for a non perfect board` |
| Laberinto < 9x7 | `pattern` + `main` | (ninguna, solo aviso) | `too small to draw the '42'` |
| No se puede escribir el output | `writer.write_maze` | OutputError | `no permission` / `is a directory` |
| Ctrl-C / Ctrl-D | `menu` / `main` | se captura | sale limpio |

Comprobación rápida en la defensa:

```bash
python3 a_maze_ing.py                 # usage
python3 a_maze_ing.py noexiste.txt    # not found
python3 a_maze_ing.py /tmp            # is a directory
```

---

## 5. Mapa subject → código

| Lo que pide el subject | Dónde está |
|------------------------|------------|
| `python3 a_maze_ing.py config.txt` | `a_maze_ing.py` |
| KEY=VALUE, comentarios con `#` | `parsing/reader.py` |
| Claves obligatorias | `parsing/maze_config.py` (`MANDATORY_KEYS`) |
| Claves extra (SEED, ALGORITHM, ANIMATION) | `parsing/maze_config.py` (`OPTIONAL_KEYS`) |
| Aleatorio pero reproducible con semilla | `generator.generate()` → `random.Random(seed)` |
| Muros coherentes entre vecinos | `grid.set_wall()` (cambia las dos celdas) |
| Bordes exteriores cerrados | nunca se abre hacia fuera (`free_neighbours` / `is_free`) |
| Conectividad total, sin celdas aisladas | los algoritmos visitan todas las celdas libres |
| "42" con celdas cerradas | `pattern.py` |
| Error si el "42" no cabe | `pattern_fits()` + `NO_PATTERN` en `app/messages.py` |
| Sin áreas abiertas de 3x3 | `open_area.py` |
| PERFECT=True → un solo camino | `algorithms/` (árbol de expansión) |
| PERFECT=False → esquinas y centro abiertos | todo es pasillo salvo el "42", y su columna central cae en el centro |
| PERFECT=False → ≥ 2 bucles | `braid.add_loops()` + `MIN_LOOPS` |
| PERFECT=False → pocos callejones | `braid.braid()` (en realidad 0, que es el bonus) |
| Fichero hex + línea vacía + entrada/salida/camino | `output/formatter.py` |
| Camino más corto en N/E/S/W | `solver.py` |
| Mostrar muros, entrada, salida y camino | `display/pixels.py` |
| Regenerar / mostrar camino / colores / color del 42 | `app/menu.py` |
| Clase única reutilizable | `mazegen/generator.py` → `MazeGenerator` |
| Paquete `mazegen-*.whl` en la raíz | `pyproject.toml` + `make build` |
| LICENSE.md | MIT |
| Makefile (install, run, debug, clean, lint) | `Makefile` |
| flake8 + mypy + type hints + docstrings | todo el código |
| **Bonus**: 0 callejones | `braid.py` |
| **Bonus**: varios algoritmos | `algorithms/prim.py` |
| **Bonus**: animación | `display/animation.py` + `on_step` |

---

## 6. Modificaciones típicas en la defensa: dónde tocar

| Te piden... | Archivo | Qué cambias |
|-------------|---------|-------------|
| Una opción nueva en el config (p. ej. `DELAY`) | `parsing/maze_config.py` + `parsing/parser.py` | añadir la clave a `OPTIONAL_KEYS`, un campo a `MazeConfig` y convertirla en `read_config` |
| Cambiar los colores | `display/colours.py` | las listas `WALL_COLOURS` / `PATTERN_COLOURS` |
| Una opción nueva en el menú | `app/messages.py` (texto) + `app/menu.py` (`_do_choice`) | otro `elif` |
| Escribir el hex en minúsculas | `generator.to_hex_lines()` | `format(cell, "x")` |
| Otro dibujo en vez del "42" | `mazegen/constants.py` | `PATTERN_42` (y revisar que el centro quede libre) |
| Un tercer algoritmo | `mazegen/algorithms/` nuevo archivo + `ALGORITHMS` + `generator.generate()` | |
| Exigir 3 bucles en vez de 2 | `mazegen/constants.py` | `MIN_LOOPS = 3` |
| Cambiar el tamaño máximo | `mazegen/constants.py` | `MAX_SIZE` |
| Que el modo Pac-Man deje algunos callejones | `braid.py` | no llamar a `braid()`, o solo braidear una parte |
| Mostrar el nº de bucles debajo del laberinto | `app/messages.py` → `info_text()` | añadir `maze.count_loops()` |

---

## 7. Preguntas que te pueden hacer

- **¿Por qué una pila y no recursión?** Por el límite de recursión de
  Python (1000 por defecto). Un laberinto de 200x200 tiene 40.000 celdas.
- **¿Cómo garantizas que es perfecto?** El DFS y Prim forman un árbol de
  expansión: N celdas y N-1 aberturas, conectado y sin ciclos. Se ve con
  `count_loops() == 0` y con el analizador.
- **¿Cómo garantizas la coherencia?** `set_wall()` siempre modifica las dos
  celdas a la vez.
- **¿Por qué BFS y no DFS para el camino?** DFS encuentra *un* camino, BFS
  encuentra el *más corto* porque explora por distancias.
- **¿Por qué `random.Random(seed)` y no `random.seed()`?** Para no tocar el
  generador global; el menú usa el global para elegir semillas nuevas sin
  afectar al laberinto.
- **¿Qué hay en el `.whl`?** Solo `mazegen/` (con su README y la licencia).
  Se comprueba con `unzip -l mazegen-1.0.0-py3-none-any.whl`.
- **¿Cómo se usa desde otro proyecto?**
  ```python
  from mazegen import MazeGenerator
  m = MazeGenerator(20, 15, seed=42, perfect=False)
  m.generate()
  m.grid, m.path, m.get_solution()
  ```
- **¿Por qué la licencia MIT?** Permite reutilizar, modificar y distribuir
  el código (lo pide el subject para los proyectos siguientes) y solo
  exige mantener el aviso de copyright.
