# CVRPTW Solver (HOM Project)

A solver for the **Capacitated Vehicle Routing Problem with Time Windows (CVRPTW)**, written for the **Heuristic Optimization Methods (HOM)** course at FER, University of Zagreb.

Given a depot, a fleet of vehicles and a set of customers with demands and time windows, the program constructs routes that:

- start and end at the depot
- respect vehicle capacity
- respect customer ready times and due dates
- visit every customer

The objective is to minimize total travel distance.

## Approach

The solver combines several heuristics:

1. **Greedy construction** (`algorithms/greedy.py`)
2. **Local search** (`algorithms/local.py`)
3. **Custom heuristic** with configurable neighbourhood ordering (`algorithms/heuristic.py`)
4. **Simulated annealing** (`algorithms/SA.py`)

It also includes a validator for checking solution feasibility and reported distance.

## Requirements

- Python 3.8 or newer
- `numpy`
- `click` (only required by the validator)

Install the dependencies with:

```bash
pip install numpy click
```

## Run

From this directory:

```bash
python3 main.py
```

At the top of `main.py`:

```python
INSTANCE_INDEX = 7   # selects resources/instances/i7.txt
TIME_LIMIT = 1       # time limit in minutes for each heuristic
```

Change `INSTANCE_INDEX` to use another instance (`i1`–`i7`).

Solutions are written to `resources/solutions/i<index>/` using a filename that records the time limit and iteration count.

## Validator

The validator from the assignment is included in `resources/validator/`:

```bash
python3 resources/validator/validator.py \
  -i resources/instances/i1.txt \
  -o resources/solutions/i1/1.txt
```

It checks that all customers are visited, capacities and time windows are respected, routes start and end at the depot, and the reported distance matches the routes.

## Project structure

```text
main.py
algorithms/
├── greedy.py
├── local.py
├── heuristic.py
├── SA.py
└── new_heuristic_test.py
models/customers.py
instanceio/
├── input.py
└── output.py
resources/
├── instances/   # CVRPTW instances i1-i7
├── solutions/   # generated solutions
└── validator/   # assignment validator and its instructions
HOM_project_2021.pdf   # original assignment description
```

## Notes

- Input and output paths are relative to the project root, so run `main.py` from this directory.
- The instance file format is the standard Solomon-style CVRPTW text format; parser details are in `instanceio/input.py`.
