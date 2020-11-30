# Advent of Code 2020

### Python Environment

```bash
# If you already have an environment named "aoc", and you want to remove it:
#  conda remove --name aoc --all

conda create --name aoc python=3.7
conda activate aoc
conda install -c conda-forge pypy3.7
pip install -r requirements.txt
```

### Set AoC Session ID

Find your AoC session cookie and set it so that the `aocd` package works.

```bash
export AOC_SESSION=...
```

### Solving

The standard way to set up your stuff to before solving (do this a few minutes before the puzzle releases) is like this:

```bash
mkdir day01
cd day01
cp ../t.py s.py
aocd > input
vim input s.py
```

### PyPy

Use PyPy if needed!

