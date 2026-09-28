# learnpy

My 3-week path from C#/Go/Java backend engineer to productive **Python + FastAPI** developer.

**Goal:** write clean, typed, tested Python; build production-style REST APIs with FastAPI; finish with a portfolio-ready mock SaaS connector (`slack-mock-api`, separate repo).

**Pace:** ~1.5 hrs on weekdays, 3–4 hrs on weekend days (~15 hrs/week).

---

## Plan at a glance

| Week | Focus | Deliverable |
|---|---|---|
| 0 | Setup | Python 3.12+, VS Code + Pylance, uv, Git, Docker, AI assistant |
| 1 | Python essentials | Typed, tested Python; LeetCode Medium in 30 min |
| 2 | FastAPI core | `week2-task-tracker/` – mini-Jira REST API with DB, auth, 80%+ coverage |
| 3 | Capstone | [`slack-mock-api`](#) – mock Slack Web API with Docker + CI (separate public repo) |

### Week 1 – Python for a C#/Java/Go engineer

| Day | Topic | Maps to | Practice |
|---|---|---|---|
| 1 | Syntax, control flow, f-strings | C# basics | 3 LeetCode Easy |
| 2 | list / dict / set / tuple, slicing, comprehensions | `List<T>`, `Dictionary`, LINQ | Rewrite 3 LINQ queries as comprehensions |
| 3 | Functions, `*args` / `**kwargs`, lambdas | Methods, `params` | 3 LeetCode Easy (arrays, hash maps) |
| 4 | Classes, `@dataclass`, dunder methods | Classes, records | Model Slack `Message` and `Channel` |
| 5 | Type hints, `Optional`, `Protocol`, `Enum` | Static typing, interfaces | Type-hint Day 4 code; Pylance strict |
| 6 | Modules, packages, `uv add`, exceptions, `with` | Namespaces, NuGet, `using` | Split into a package; custom exceptions |
| 7 | `async`/`await`, `httpx`, pytest basics | `async Task`, `HttpClient`, xUnit | Async API call + 5 pytest tests |

### Week 2 – FastAPI core (Task Tracker API)

| Day | Topic | Maps to (ASP.NET Core) | Build |
|---|---|---|---|
| 1 | First app, path/query params, uvicorn, `/docs` | Controllers, routing | `GET /health`, `GET /issues/{id}` |
| 2 | Pydantic request/response models | DTOs + data annotations | `POST /issues` with validation |
| 3 | Status codes, `HTTPException`, `APIRouter` | `IActionResult`, middleware | Full CRUD, 404s, split routers |
| 4 | Dependency injection with `Depends` | `IServiceCollection` | Inject repository + settings |
| 5 | SQLModel + SQLite | Entity Framework | Persist issues, projects, comments |
| 6 | Auth: API keys, OAuth2, JWT | Auth handlers | Protect write endpoints |
| 7 | `TestClient` + pytest, fixtures, coverage | `WebApplicationFactory` | 80%+ coverage (`pytest --cov`) |

---

## Repo structure

```
learnpy/
├── README.md
├── week1-python/
│   ├── day1_basics.py ... day7_async.py
│   ├── leetcode/            # one file per problem
│   └── tests/
├── week2-task-tracker/
│   ├── app/                 # main.py, routers/, models/, db.py, deps.py
│   ├── tests/
│   └── pyproject.toml
└── .gitignore               # GitHub Python template (.venv, __pycache__, .env)
```

## Getting started

```bash
# once
pip install uv

# week 1
cd week1-python
uv run python day1_basics.py
uv run pytest

# week 2
cd week2-task-tracker
uv sync
uv run uvicorn app.main:app --reload   # open http://127.0.0.1:8000/docs
uv run pytest --cov=app
```

**Secrets:** never commit tokens. Use a local `.env` and commit `.env.example` with placeholders.

---

## Progress log

| Date | Day | What I did | What I learned / stuck on |
|---|---|---|---|
|  | W1 D1 |  |  |

## Checklist

- [ ] Week 0 – tools installed, `uv run python --version` works
- [ ] Week 1 – LeetCode Medium in Python in 30 min; comfortable with type hints, async, pytest
- [ ] Week 2 – Task Tracker API with DB, auth, 80%+ test coverage
- [ ] Week 3 – `slack-mock-api` public with Docker, CI and README
- [ ] 3–4 notes on how I used AI coding assistants
- [ ] CV + Turing profile updated with Python / FastAPI

## AI assistant usage notes

<!-- Record concrete examples, e.g. "Copilot drafted pytest fixtures; I fixed 3 wrong assertions." -->

-

## Resources

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [FastAPI Tutorial – User Guide](https://fastapi.tiangolo.com/tutorial/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [pytest](https://docs.pytest.org/)
- [Slack Web API methods](https://api.slack.com/methods) (Week 3 spec)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [GitHub Actions for Python](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python)
