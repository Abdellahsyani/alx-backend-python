# ALX Backend Python

A collection of ALX backend Python projects covering type annotations, asyncio
coroutines, async comprehensions, and unit/integration testing patterns.

## Projects

| Directory | Focus | Highlights |
| --- | --- | --- |
| `0x00-python_variable_annotations` | Python type annotations | `add`, `concat`, `floor`, `to_str`, `sum_list`, `sum_mixed_list`, `to_kv`, `make_multiplier`, `element_length` |
| `0x01-python_async_function` | Async coroutines with `asyncio` | `wait_random`, `wait_n`, `measure_time`, `task_wait_random`, `task_wait_n` |
| `0x02-python_async_comprehension` | Async generators & comprehensions | `async_generator`, `async_comprehension`, `measure_runtime` |
| `0x03-Unittests_and_integration_tests` | Testing utilities & GitHub org client | `access_nested_map`, `get_json`, `memoize`, `GithubOrgClient`, unit/integration tests |

## Requirements

- Python 3.7+ (projects were written for Ubuntu 18.04 / Python 3.7).
- Optional test dependencies:
  - `requests`
  - `parameterized`

Install test dependencies:

```bash
python -m pip install requests parameterized
```

## Usage

Each directory contains standalone modules designed to be imported and reused.
You can run a module directly with `python <file>.py`, or import its functions
from the Python REPL or your own scripts.

## Tests

Unit and integration tests live in `0x03-Unittests_and_integration_tests`.
Run them from the repository root:

```bash
python -m unittest discover -s 0x03-Unittests_and_integration_tests -p "test_*.py"
```

## Linting

If `pycodestyle` is installed, you can run:

```bash
pycodestyle .
```

## Repository Structure

```
.
├── 0x00-python_variable_annotations
├── 0x01-python_async_function
├── 0x02-python_async_comprehension
├── 0x03-Unittests_and_integration_tests
└── README.md
```
