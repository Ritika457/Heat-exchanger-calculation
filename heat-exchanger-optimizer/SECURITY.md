# Publication and local configuration

The public examples are synthetic. Keep local `.env` files, database exports,
spreadsheets, documents, logs, generated histories and credentials outside commits.
The `.gitignore` excludes common sensitive and generated file types; it cannot detect
credentials embedded inside otherwise valid source files.

Before future commits, inspect `git diff --cached` and `git status --short`, scan for
secrets and private records, and verify that example settings still contain invented values.
If a real secret is ever committed or published, revoke/rotate it and clean the affected
history. Removing a file from the latest commit or adding `.gitignore` is not sufficient.

Demo mode is the default and does not connect to an external database. The application
has no production authentication layer; bind it to loopback for local evaluation.
