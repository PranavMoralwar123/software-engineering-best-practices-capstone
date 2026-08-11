# Software Engineering Best Practices Capstone

A FastAPI security and software-engineering practices project demonstrating secure coding, dependency security, automated testing, repository hygiene, pre-commit guardrails, and CI/CD quality gates.

## What this project demonstrates

- Environment-based API-key configuration with `python-dotenv`
- `.env` protection through Git hygiene
- Server-side input validation with FastAPI `Query`
- Parameterized SQLite queries to prevent SQL injection
- Generic client-facing error responses with detailed server-side logging
- Automated tests with `pytest`
- Mocked database testing with `unittest.mock`
- Test coverage reporting with `pytest-cov`
- Ruff linting and formatting
- Gitleaks secret scanning
- Pre-commit enforcement
- Dependency vulnerability auditing with `pip-audit`
- Dependabot dependency update configuration
- GitHub Actions CI for pull requests and pushes to `main`

## Project structure

```text
.
├── app.py
├── users.db
├── requirements.txt
├── pytest.ini
├── .gitignore
├── .gitleaks.toml
├── .pre-commit-config.yaml
├── CODE_REVIEW.md
├── SECURITY.md
├── CONTRIBUTING.md
├── PRODUCTION_READINESS.md
├── tests/
│   ├── test_app.py
│   └── secret_fixture.txt
└── .github/
    ├── dependabot.yml
    └── workflows/
        └── ci.yml
```

## Local setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pre-commit ruff pip-audit
```

Create a local `.env` file:

```text
API_KEY=your_local_test_key
```

The `.env` file is for local development only and must never be committed.

## Run the API

```powershell
uvicorn app:app --reload
```

The API exposes:

```text
GET /users?username=<username>
```

The username is validated server-side with a minimum length of 1 and maximum length of 50 characters.

## Run tests

```powershell
pytest -v
```

Coverage:

```powershell
pytest --cov=app --cov-report=term-missing -v
```

The project test suite covers:

- Existing-user lookup
- Empty username rejection
- Maximum-length validation
- SQL-injection-style input
- Database mocking
- Database error handling and safe error messages

## Quality and security checks

Run all pre-commit hooks:

```powershell
pre-commit run --all-files
```

Run Ruff:

```powershell
ruff check .
ruff format --check .
```

Run the dependency audit:

```powershell
pip-audit -r requirements.txt
```

## CI/CD

GitHub Actions runs the quality pipeline on pull requests and pushes to `main`.

The pipeline checks:

1. Ruff lint
2. Ruff formatting
3. Gitleaks secret scanning
4. Dependency vulnerabilities with `pip-audit`
5. The full pytest suite

A failing quality gate should prevent the change from being considered production-ready.

## Security design

The `/users` endpoint uses a parameterized SQL statement:

```sql
SELECT id, username, email
FROM users
WHERE username = ?
```

User input is passed separately as a SQL parameter rather than concatenated into the query.

Database exceptions are logged internally while the API returns a generic message:

```json
{
  "detail": "Unable to process the request."
}
```

This prevents internal database details from being exposed to API clients.

## Development principles

This capstone follows the practices defined in the training material:

- Push work frequently.
- Keep commits small and reviewable.
- Never commit secrets, virtual environments, generated artifacts, or private data.
- Verify AI-generated code and dependencies before using them.
- Validate external input on the server.
- Use parameterized queries.
- Keep sensitive implementation details out of client-facing errors.
- Run automated quality and security checks before merging.

## CI status

![CI](https://github.com/PranavMoralwar123/software-engineering-best-practices-capstone/actions/workflows/ci.yml/badge.svg)

## Capstone documentation

- [Security Policy](SECURITY.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Production Readiness Checklist](PRODUCTION_READINESS.md)
- [Code Review Notes](CODE_REVIEW.md)
