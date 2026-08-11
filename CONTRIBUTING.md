# Contributing Guide

## Before You Start

Make sure your local environment is configured and dependencies are installed:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Install development tooling if needed:

```powershell
pip install pre-commit ruff pip-audit
pre-commit install
```

## Branching

Use short-lived branches for focused changes.

Examples:

```text
feat/add-user-search
fix/database-error-handling
test/add-api-tests
docs/add-security-policy
chore/update-dependencies
```

Keep branches reasonably small and up to date with `main`.

## Commit Messages

Use clear Conventional Commit-style messages:

- `feat:` new functionality
- `fix:` bug fixes
- `test:` tests
- `docs:` documentation
- `refactor:` code restructuring
- `chore:` tooling or dependency changes

Examples:

```text
feat: add user search validation
test: cover database error handling
docs: add production readiness checklist
chore: configure GitHub Actions CI
```

## Pull Requests

A pull request should:

1. Explain what changed.
2. Explain why the change was needed.
3. Include tests for changed behavior.
4. Avoid unrelated changes.
5. Confirm that secrets are not included.
6. Confirm dependencies are verified.
7. Pass all automated CI checks.

## Local Quality Checks

Run:

```powershell
ruff check .
ruff format --check .
pre-commit run --all-files
pytest -v
pip-audit -r requirements.txt
```

Do not bypass pre-commit hooks with `--no-verify` during normal development.

## Testing Expectations

Tests should cover:

- Normal behavior
- Validation failures
- Security-sensitive inputs
- Error paths
- Important integration behavior

Mocks may be used for isolated unit tests, but integration tests should also exercise important interactions with real components where practical.

## Code Review

Reviewers should focus on:

- Correctness
- Security
- Tests
- Dependency changes
- Readability
- Scope
- Whether the author understands the code, including AI-generated code

Blocking feedback should identify a concrete issue that must be fixed. Style preferences that are already enforced by tooling should generally not become manual review blockers.

## Secrets

Never commit real secrets.

Use environment variables locally and approved secret-management facilities in CI/production. If a secret is accidentally exposed, revoke and rotate it immediately and follow the project's security process.
