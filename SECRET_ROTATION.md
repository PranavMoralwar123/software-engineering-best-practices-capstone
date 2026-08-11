# Secret Leak Response & Rotation

## Simulated Incident

The fake API key `sk-fake-12345` was accidentally exposed in a public repository.

This is a simulated exercise using a fake credential. No real credential was exposed.

## First Five Minutes

1. **Revoke** — Immediately invalidate the exposed credential at the provider.
2. **Rotate** — Generate a new credential and update the secret manager or environment configuration.
3. **Audit** — Check provider usage logs for unauthorized activity during the exposure window.
4. **Purge history** — Remove the exposed secret from Git history rather than only deleting it in a later commit.
5. **Notify** — Inform the appropriate team or security lead so the impact can be assessed.

## Rotation Principle

The old credential must be revoked. Simply replacing the value locally does not make the exposed credential safe.

The application should obtain the credential from environment-based configuration so that rotating the credential does not require changing application source code.