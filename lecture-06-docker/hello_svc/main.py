from fastapi import FastAPI
from pydantic import BaseModel

# Support both package execution (`hello_svc.main`) and running this service
# with `uvicorn --app-dir hello_svc main:app`.
if __package__:
    from .greetings import APP_VERSION, GREETINGS, get_greeting
else:
    from greetings import APP_VERSION, GREETINGS, get_greeting

app = FastAPI(title="Hello World Demo", version=APP_VERSION)


class HealthResponse(BaseModel):
    ok: bool
    version: str


@app.get("/")
def hello(lang: str = "en"):
    return {"hello": get_greeting(lang)}


@app.get("/languages")
def languages():
    return {"supported": sorted(GREETINGS.keys())}


@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(ok=True, version=APP_VERSION)
