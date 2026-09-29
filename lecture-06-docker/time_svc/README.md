# Add the `time` service to the `hello` demo

This folder already contains a small FastAPI service with a `/now` endpoint.
The steps below connect it to the `hello` service over the internal Docker
Compose network.

## 1. Update `hello_svc/main.py`

Add these standard-library imports near the top of the file:

```python
import json
from urllib.request import urlopen
```

Add this service URL after the `app = FastAPI(...)` line:

```python
TIME_SERVICE_URL = "http://time:8001"
```

Add this endpoint to the file:

```python
@app.get("/time")
def current_time():
    with urlopen(f"{TIME_SERVICE_URL}/now", timeout=5) as response:
        return json.load(response)
```

The hostname `time` is the Compose service name. Do not use `localhost` here:
inside the `hello` container, `localhost` refers to the `hello` container
itself.
This endpoint is intended to be called while the services are running through
Compose.

## 2. Update `docker-compose.yaml`

Add this dependency under the existing `hello` service. It makes Compose wait
until the `time` service's Compose health check passes before starting
`hello`:

```yaml
    depends_on:
      time:
        condition: service_healthy
```

Then add this service at the same indentation level as `hello`:

```yaml
  time:
    build: ./time_svc
    expose:
      - "8001"
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8001/health').read()"]
      interval: 30s
      timeout: 5s
      retries: 3
      start_period: 10s
    restart: unless-stopped
```

The health check belongs in Compose so it can be used by `depends_on`. Port
8001 is only exposed to the internal Compose network; the time service does
not need its own public route.

## 3. Build and run both services

From the repository root:

```bash
docker compose up --build
```

Once the services are running, request `/time` through the `hello` service. The
hello service will call `http://time:8001/now` over the internal network and
return the `time` service's JSON response.
