# Security Policy

## Scope

This project is a learning capstone demonstrating secure software-engineering practices around secrets, input validation, SQL queries, dependencies, testing, and CI/CD.

## Supported Security Practices

The project includes:

- Environment-based configuration for API keys
- `.env` exclusion from Git
- Gitleaks secret scanning
- Pre-commit security checks
- Parameterized SQL queries
- Server-side input validation
- Generic client-facing error responses
- Detailed server-side error logging
- Dependency auditing with `pip-audit`
- Automated CI quality gates

## Reporting a Vulnerability

If you discover a security issue, do not publish credentials, exploit details, or sensitive information in a public issue.

For a real organizational project, report the issue through the organization's approved security reporting channel.

For this learning repository, open a GitHub issue without including any real secret or sensitive personal information, or contact the repository owner privately when appropriate.

## If a Secret Is Leaked

If a real credential is ever exposed:

1. Revoke the exposed credential immediately.
2. Rotate it and issue a replacement.
3. Check provider usage/audit logs for unauthorized activity.
4. Remove the credential from Git history if it was committed.
5. Notify the appropriate security or project owner.
6. Review how the secret bypassed existing controls and strengthen the guardrail.

Deleting the secret from the latest file is not sufficient if it remains in Git history.

## Safe Development Rules

Never commit:

- API keys
- Passwords
- Access tokens
- Private keys
- Real customer or personal data
- Production database exports
- `.env` files containing real values
- Virtual environments or generated build artifacts

Use `.env.example` or documented placeholder values when a configuration example is needed.

## Dependency Security

Dependencies should be verified before installation and audited regularly. AI-suggested packages should be checked for existence, reputation, maintenance activity, correct package naming, and actual necessity.

Run:

```powershell
pip-audit -r requirements.txt
```

before considering the dependency set ready.

## Responsible AI Use

Do not paste proprietary source code, credentials, customer data, confidential business information, or other sensitive material into an unapproved AI tool.

Any AI-generated code must be reviewed, understood, tested, and owned by the engineer who commits it.
