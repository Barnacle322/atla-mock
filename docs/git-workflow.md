# Simple Git Workflow

This document explains the basic steps to contribute to this repository.

## 1. Create a Branch

Never make changes directly to the `main` branch. Always create a new branch.

```bash
# Update your local main branch
git checkout main
git pull origin main

# Create a new branch for your feature
git checkout -b my-new-feature
```

## 2. Make Changes

Edit the files you need to change.

## 3. Commit Changes

Save your changes to git history.

```bash
git add .
git commit -m "Add a clear message explaining what you did"
```

## 4. Push to GitHub

Send your branch to the server.

```bash
git push origin my-new-feature
```

## 5. Open a Pull Request

1. Go to the repository page on GitHub.
2. You will see a button to "Compare & pull request".
3. Click it and fill out the template.
4. Wait for review!
