# hello-world-app

Minimal FastAPI/Docker starter for the ML Capstone class deployment lab.

## Layout

- `hello_svc/` — the self-contained hello service:
  - `hello_svc/main.py` — FastAPI app and endpoints. Wiring only.
  - `hello_svc/greetings.py` — content + logic (the greeting dict + `get_greeting()`). Pulled out of `main.py` on purpose so you see the "split logic from wiring" pattern even at hello-world scale.
  - `hello_svc/Dockerfile` — single-stage `python:3.12-slim`, exposes `:8000`.
  - `hello_svc/requirements.txt` — Python dependencies for the service.
  - `hello_svc/requirements-dev.txt` — test and coverage dependencies.
- `tests/test_api.py` — five pytest tests hitting every endpoint in `hello_svc`.
- `.github/workflows/ci.yml` — CI workflow that runs the coverage-gated unit tests.
- `test-local.sh` — run the coverage-gated unit tests, build, run, and curl a couple endpoints, then stop the container.

## Endpoints

| Method | Path | Returns |
|---|---|---|
| GET | `/` | `{"hello": "Hello, world"}` — or `{"hello": "Hola, mundo"}` etc. with `?lang=es\|fr\|de\|ja` |
| GET | `/languages` | `{"supported": ["de", "en", "es", "fr", "ja"]}` |
| GET | `/health` | `{"ok": true, "version": "0.1.1"}` |

## Local test

```bash
./test-local.sh
```

Or run without Docker:

```bash
pip install -r hello_svc/requirements.txt
uvicorn --app-dir hello_svc main:app --reload
```

Then `curl http://127.0.0.1:8000/` and `curl http://127.0.0.1:8000/health`.

## Unit tests

```bash
pip install -r hello_svc/requirements-dev.txt
pytest tests/ -v --cov=hello_svc --cov-report=term-missing --cov-fail-under=90
```

CI requires at least 90% coverage for the `hello_svc` service.
