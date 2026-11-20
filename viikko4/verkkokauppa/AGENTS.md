# Verkkokauppa

- Work from this directory; `pyproject.toml` requires Python 3.14+ and `uv.lock` is the dependency source of truth.
- Run all tests with `uv run pytest src/tests`; focus the suite with `uv run pytest src/tests/kauppa_test.py` (or a single test via `::TestKauppa::test_name`).
- `src/tests/kauppa_test.py` uses `unittest.TestCase` and pytest discovery. The app's domain code is in `src/`; `Kauppa` receives its warehouse, bank, and reference-number generator as dependencies. `src/index.py` wires default instances and runs a sample checkout.
- Code of ostos.py and tuote.py should not be changed
- Tests shouldn't be edited unless explicitly asked
- Always implement absolutely minimal code that makes the tests pass


