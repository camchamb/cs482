#!/usr/bin/env bash
# Quick local check: run unit tests, build, run detached, curl a couple
# endpoints, and stop the container.
set -euo pipefail
cd "$(dirname "$0")"

IMAGE=hello-world-app:local
CONTAINER=hello-world-local

echo "=== unit tests (90% coverage required) ==="
pytest tests/ -v --cov=hello_svc --cov-report=term-missing --cov-fail-under=90

echo "=== building ==="
docker build -t "$IMAGE" ./hello_svc

echo
echo "=== running (detached, --rm) ==="
docker rm -f "$CONTAINER" >/dev/null 2>&1 || true
docker run -d --rm --name "$CONTAINER" -p 8000:8000 "$IMAGE" >/dev/null

cleanup() {
    docker stop "$CONTAINER" >/dev/null 2>&1 || true
}
trap cleanup EXIT

# Wait for /health to come up
for _ in $(seq 1 15); do
    if curl -sSf http://127.0.0.1:8000/health >/dev/null 2>&1; then
        break
    fi
    sleep 1
done

echo
echo "=== GET / ==="
curl -sS http://127.0.0.1:8000/
echo
echo "=== GET /health ==="
curl -sS http://127.0.0.1:8000/health
echo
echo
echo "Stopping container '$CONTAINER'."
