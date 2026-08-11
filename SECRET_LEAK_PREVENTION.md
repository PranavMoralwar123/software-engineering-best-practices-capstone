\# Secret Leak Prevention Notes



\## Lessons From the Recovery Exercise



1\. Never store real credentials in source files or tracked configuration.

2\. Keep `.env` files and other secret-bearing files in `.gitignore`.

3\. Use pre-commit secret scanning so accidental secrets are caught before commit.

4\. Review staged changes before committing.

5\. Use approved environment variables or a secret manager for credentials.

6\. If a secret is exposed, revoke and rotate it immediately rather than only deleting the file.

7\. Scan repository history when investigating a suspected leak.

8\. Keep secret-scanning allowlists narrow and limited to reviewed harmless fixtures.



\## Key Lesson



Deleting a secret from the latest version of a repository does not remove it from Git history. If a real credential is committed, it must be revoked/rotated and removed from the repository history using an appropriate history-rewriting process.



\## Prevention Going Forward



The main project uses `.gitignore`, Gitleaks, and a pre-commit hook to reduce the chance of credentials entering Git in the first place.

