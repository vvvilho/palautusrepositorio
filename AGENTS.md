# Login exercise (`viikko3/login`)

- Work from `viikko3/login`; this project has its own `pyproject.toml` and `uv.lock` and requires Python 3.14+.
- Start the Flask app with `uv run python src/index.py` (port 5001). In another terminal, run browser tests with `uv run robot src/tests`; focus a suite with `uv run robot src/tests/login.robot`.
- Robot Browser tests use Chromium at `http://localhost:5001` and default to a visible browser. Install its Playwright browser if needed with `uv run rfbrowser install`; use `uv run robot --variable HEADLESS:true src/tests` in headless environments.
- `src/index.py` starts the app; `src/app.py` connects routes to `services/user_service.py` and `repositories/user_repository.py`. User storage is in-memory; `/tests/reset` clears it for test setup.
- Username and password validation happens in `services/user_service.py` (`UserService.validate`), called when registering a user; login credential checks are in `UserService.check_credentials`.
