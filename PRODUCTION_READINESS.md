# Production Readiness Checklist

This checklist records the final review of the Software Engineering Best Practices Capstone.

## 1. Working Discipline

- [x] Work is pushed to the remote repository.
- [x] Changes are kept in small, reviewable commits.
- [x] Work is not intentionally kept only on a local machine.
- [x] Repository work is stored in the sanctioned project remote.

## 2. Responsible AI and Data Handling

- [x] AI-generated code is reviewed before being committed.
- [x] AI-generated code is tested and understood by the author.
- [x] Secrets are not pasted into unapproved AI tools.
- [x] Customer, personal, proprietary, or confidential data should not be supplied to unapproved AI tools.
- [x] AI-suggested dependencies are verified before installation.

## 3. Secrets Management

- [x] API keys are read from environment configuration.
- [x] `.env` is excluded from version control.
- [x] Placeholder configuration can be documented without exposing real credentials.
- [x] Gitleaks is configured.
- [x] Pre-commit runs the secret scan.
- [x] CI runs secret scanning.
- [x] A leaked real credential would be revoked and rotated immediately.

## 4. Git Hygiene

- [x] Virtual environments are excluded.
- [x] Generated/cache files are excluded.
- [x] Secrets and environment files are excluded.
- [x] Pre-commit hooks enforce repository checks.
- [x] Dependabot is configured for dependency updates.

## 5. Secure Coding

- [x] Server-side validation is applied to the username query parameter.
- [x] Username length is constrained.
- [x] SQL uses parameterized statements.
- [x] SQL-injection-style input is tested.
- [x] Database errors are caught.
- [x] Client-facing errors do not expose internal database details.
- [x] Detailed errors are logged internally.

## 6. Dependencies

- [x] Dependencies are declared in `requirements.txt`.
- [x] Dependency vulnerabilities are checked with `pip-audit`.
- [x] Current audit completed without known vulnerabilities.
- [x] Dependabot is configured for automated dependency update proposals.
- [x] Dependencies should be reviewed before installation, including AI-suggested packages.

## 7. Testing

- [x] pytest is configured.
- [x] Normal API behavior is tested.
- [x] Validation edge cases are tested.
- [x] SQL injection safety is tested.
- [x] Database behavior is mocked in a unit-style test.
- [x] Database failure handling is tested.
- [x] Test suite passes locally.
- [x] Coverage was measured during development.

## 8. Code Quality

- [x] Ruff linting is configured and passing.
- [x] Ruff formatting is configured and passing.
- [x] Pre-commit checks pass.
- [x] Code review notes are documented.

## 9. CI/CD

- [x] GitHub Actions workflow is present.
- [x] CI runs on pull requests.
- [x] CI runs on pushes to `main`.
- [x] Ruff linting runs in CI.
- [x] Ruff format checking runs in CI.
- [x] Gitleaks runs in CI.
- [x] `pip-audit` runs in CI.
- [x] pytest runs in CI.
- [x] CI failures block successful workflow completion.
- [ ] GitHub branch protection/ruleset requiring the CI check before merge — verify in repository settings.

## 10. Documentation

- [x] README.md exists.
- [x] SECURITY.md exists.
- [x] CONTRIBUTING.md exists.
- [x] Production readiness checklist exists.
- [x] CI status badge is included in README.

## Final Assessment

The capstone demonstrates the requested engineering guardrails across secure coding, secrets management, dependency security, testing, repository hygiene, and CI/CD.

The remaining repository-level verification is to confirm that GitHub branch protection/rulesets require the CI quality check before merging pull requests.
