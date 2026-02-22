# 🐙 Module 07: GitHub Features

> **Git ≠ GitHub.** Git is the version control tool. GitHub is the platform built around it.  
> This module covers everything GitHub offers beyond just storing code.

---

## 🏋️ EXERCISES

---

### Exercise 7.1 — GitHub Issues (Bug Tracking & Task Management) (15 min)

**Issues are where work begins.** Every test you write, every bug you file — starts as an Issue.

#### Create an Issue:
1. Go to your repo on GitHub → **Issues** tab → **New Issue**
2. Fill in:
   - **Title:** `[BUG] Login test fails when username has special characters`
   - **Labels:** `bug`, `test-automation`
   - **Assignee:** Assign to yourself
   - **Milestone:** (create one: `Sprint 42`)
3. In the body, use this template:

```markdown
## 🐛 Bug Description
The login test `test_valid_login` fails when the username contains special characters like `user+test@email.com`.

## Steps to Reproduce
1. Set username to `user+test@email.com`
2. Run: `pytest 01_branching/login_tests.py::TestLogin::test_valid_login`
3. Test fails with: `AssertionError: assert 401 == 200`

## Expected Behavior
Login should succeed (status 200)

## Actual Behavior
Returns 401 (status 401)

## Environment
- Branch: `main`
- Python: 3.12
- pytest: 8.0

## Acceptance Criteria
- [ ] Test passes for emails with `+` in username
- [ ] No regression in other login tests
```

4. Click **Submit new issue** → Note the issue number (e.g., `#3`)

---

#### Close an Issue via Commit Message:
```bash
# Any of these keywords auto-close the issue when merged to main:
# closes, fixes, resolves + #number

git commit -m "fix(QA-3): handle special chars in login test

Closes #3"

git push

# After this PR merges to main — Issue #3 is automatically CLOSED!
```

---

### Exercise 7.2 — Labels & Milestones (5 min)

**Labels** = categories for your issues/PRs  
**Milestones** = group issues by sprint/release

#### Create custom labels:
1. **Issues** → **Labels** → **New label**
2. Create these SDET-specific labels:

| Label Name | Color | Description |
|-----------|-------|-------------|
| `test-automation` | `#0075ca` | Related to test automation code |
| `flaky-test` | `#e4e669` | Flaky/unstable test |
| `regression` | `#d93f0b` | Regression test |
| `blocked` | `#b60205` | Blocked by another issue |
| `needs-review` | `#008672` | Ready for code review |

#### Create a Milestone:
1. **Issues** → **Milestones** → **New milestone**
2. Title: `Sprint 42`
3. Due date: (2 weeks from today)
4. Assign 3-4 of your issues to this milestone

---

### Exercise 7.3 — GitHub Projects (Kanban Board) (10 min)

Projects give you a Kanban board to track work visually.

1. Go to repo → **Projects** → **New project**
2. Choose template: **Board**
3. Name it: `Test Automation Sprint 42`
4. Default columns: `Todo`, `In Progress`, `Done`
5. Add custom column: `In Review`
6. Add your issues to the board by clicking **+ Add item**
7. Drag issues across columns as you work

**Workflow for SDETs:**
```
Todo → In Progress → In Review (PR open) → Done (PR merged)
```

---

### Exercise 7.4 — GitHub Actions / CI (Most Important for SDETs!) ⭐ (20 min)

**GitHub Actions** lets you run your tests automatically on every push or PR.

#### The workflow file is already created at `.github/workflows/tests.yml`
Open it and study the structure, then:

```bash
# Step 1: Push your code to GitHub (if not already done)
git push origin main

# Step 2: Go to GitHub → Actions tab
# You'll see the workflow running!

# Step 3: Click on a workflow run to see:
# - Which tests passed ✅ or failed ❌
# - Logs for each step
# - How long it took
```

#### Understanding the YAML:
```yaml
name: Run Tests          # workflow name (shown in GitHub UI)

on:                      # TRIGGER: when does this run?
  push:                  # on every push
    branches: [main]     # only to main
  pull_request:          # on every PR

jobs:                    # what to DO
  test:
    runs-on: ubuntu-latest   # the machine type

    steps:
      - uses: actions/checkout@v4     # clone the repo
      - uses: actions/setup-python@v5 # install Python
        with:
          python-version: '3.12'
      - run: pip install pytest        # install dependencies
      - run: pytest --tb=short         # run tests!
```

#### Add a status badge to README:
```markdown
![Tests](https://github.com/YOUR_USERNAME/git-practice-sdet/actions/workflows/tests.yml/badge.svg)
```

---

### Exercise 7.5 — GitHub Releases (10 min)

Releases are versioned snapshots of your project, linked to a git tag.

```bash
# Step 1: Create and push a tag
git tag -a v1.0.0 -m "Sprint 42 complete — 45 automated tests"
git push origin v1.0.0
```

#### Create the Release on GitHub:
1. Go to repo → **Releases** → **Draft a new release**
2. **Choose a tag:** Select `v1.0.0`
3. **Release title:** `v1.0.0 — Sprint 42 Automation Suite`
4. **Description** (use this template):

```markdown
## 🚀 What's New in v1.0.0

### ✅ Test Coverage Added
- Login flow: 4 tests
- API endpoints: 4 tests  
- Checkout flow: 4 tests
- Payment processing: 4 tests
- Order management: 3 tests

### 🐛 Bug Fixes
- Fixed flaky payment test (race condition resolved)
- Corrected timeout assertion values

### 📊 Stats
- **Total tests:** 45
- **Pass rate:** 100%
- **Avg execution time:** 2.3s

### 🔄 Full Changelog
See [commit history](../../commits/v1.0.0)
```

5. Click **Publish release**

---

### Exercise 7.6 — GitHub CLI (`gh`) (10 min)

The GitHub CLI lets you do GitHub operations from your terminal — no browser needed.

```bash
# Install (Windows)
winget install --id GitHub.cli
# or: choco install gh

# Authenticate
gh auth login
# Follow prompts → choose GitHub.com → HTTPS or SSH → authenticate via browser

# ─── Issues via CLI ──────────────────────────────────────────
# Create an issue
gh issue create --title "Flaky test in checkout" --body "Fails 1/10 runs" --label "flaky-test"

# List open issues
gh issue list

# View an issue
gh issue view 3

# Close an issue
gh issue close 3

# ─── PRs via CLI ──────────────────────────────────────────────
# Create a PR from your current branch
gh pr create --title "test: add checkout regression tests" --body "Closes #3"

# List open PRs
gh pr list

# Check out a PR locally (to review)
gh pr checkout 5

# View PR status (checks, reviews)
gh pr status

# Merge a PR
gh pr merge 5 --squash --delete-branch

# ─── Repos via CLI ───────────────────────────────────────────
# Create a new repo
gh repo create my-test-repo --public

# Fork a repo
gh repo fork psf/requests

# Clone a repo
gh repo clone YOUR_USERNAME/git-practice-sdet

# View repo info
gh repo view
```

---

### Exercise 7.7 — CODEOWNERS (Enforce Test Review by QA) (5 min)

`CODEOWNERS` automatically assigns reviewers to PRs based on which files changed.

**Create `.github/CODEOWNERS`:**
```
# Format: <file pattern>   <owner(s)>

# QA team must review ANY changes to test files
**/*test*.py    @qa-team-lead

# API tests — backend team + QA both review
01_branching/api_tests.py    @backend-lead @qa-team-lead

# Payment tests — very sensitive, multiple approvals
03_merging/payment_tests.py    @backend-lead @qa-team-lead @security-team

# Root config files — only repo admin can approve
*.yml    @repo-admin
.gitignore    @repo-admin
```

**How it works:**
- When someone opens a PR changing `payment_tests.py`, GitHub AUTOMATICALLY requests reviews from `@backend-lead`, `@qa-team-lead`, and `@security-team`.
- With branch protection ON, the PR cannot merge until all required reviewers approve.

---

### Exercise 7.8 — GitHub Wiki (Team Documentation) (5 min)

Wikis are great for SDET teams to document:
- Test environment setup
- How to run the test suite
- Known flaky tests list
- Test data management

1. Go to repo → **Wiki** → **Create the first page**
2. Create a page: `Test Environment Setup`
3. Add content:

```markdown
# Test Environment Setup

## Prerequisites
- Python 3.12+
- pytest 8.0+

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/git-practice-sdet.git
cd git-practice-sdet
pip install -r requirements.txt
```

## Running Tests
```bash
# Run all tests
pytest

# Run a specific module
pytest 01_branching/ -v

# Run with HTML report
pytest --html=test-results/report.html
```

## Test Environments
| Environment | URL | Credentials |
|-------------|-----|-------------|
| Dev | https://dev.example.com | test_user / stored in vault |
| Staging | https://staging.example.com | staging_user / stored in vault |
```

---

### Exercise 7.9 — Dependabot (Auto-Update Dependencies) (5 min)

**Dependabot** automatically opens PRs when your dependencies have security vulnerabilities or new versions.

**Create `.github/dependabot.yml`:**
```yaml
version: 2
updates:
  # Monitor Python packages (pip)
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"       # check every week
    labels:
      - "dependencies"
      - "automated"
    reviewers:
      - "qa-team-lead"
    commit-message:
      prefix: "chore"          # chore: bump pytest from 7.4 to 8.0

  # Monitor GitHub Actions versions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
```

1. Create this file in your repo
2. Push to GitHub
3. Go to **Security** → **Dependabot alerts** to see any current vulnerabilities

---

## 🧠 Module 07 Summary

| Feature | What it does | SDET Use |
|---------|-------------|----------|
| Issues | Track bugs & tasks | File test failures, track test coverage gaps |
| Labels | Categorize issues | `flaky-test`, `regression`, `blocked` |
| Milestones | Group by sprint | Sprint 42, Release v2.0 |
| Projects | Kanban board | Visualize test automation progress |
| Actions | CI/CD automation | Run pytest on every push/PR |
| Releases | Version snapshots | Tag test suite at each sprint |
| GitHub CLI | Terminal operations | Create PRs, check status without browser |
| CODEOWNERS | Auto-assign reviewers | QA must review all test file changes |
| Wiki | Documentation | Test setup guide, known issues |
| Dependabot | Dependency updates | Keep pytest, selenium up to date |

---

**➡️ Next:** Open `08_interactive_rebase/EXERCISES.md`
