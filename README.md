# python-fun

A small Python playground with a colorful terminal **Hello, World!** script.

## Requirements

- Python 3.9+ (stdlib only — no extra packages)

## Run it

From the project folder:

```bash
cd python-fun
```

### Examples

**Default** — animated rainbow greeting to “World”:

```bash
python3 hello.py
```

**Greet someone by name:**

```bash
python3 hello.py -n Zizi
python3 hello.py --name Rob
```

**Skip the typewriter** (instant output):

```bash
python3 hello.py --fast
python3 hello.py -n Zizi --fast
```

**Plain text** (no ANSI colors):

```bash
python3 hello.py --no-color
python3 hello.py -n World --no-color --fast
```

**Show help:**

```bash
python3 hello.py --help
```

**Save output to a file** (colors are turned off automatically when not writing to a terminal):

```bash
python3 hello.py --fast > greeting.txt
cat greeting.txt
```

**Run as an executable** (after making it executable once with `chmod +x hello.py`):

```bash
chmod +x hello.py
./hello.py -n Zizi
```

### Options

| Flag | Description |
|------|-------------|
| `-n`, `--name NAME` | Who to greet (default: `World`) |
| `--fast` | Skip the typewriter animation |
| `--no-color` | Plain text output |

## What it does

`hello.py` prints an ASCII **HELLO** banner, animates a rainbow greeting in the terminal, and picks a random tagline and sparkle each run. Colors are disabled automatically when output is not a TTY (for example, when piping to a file).

## Files

- `hello.py` — fancy Hello, World! script
