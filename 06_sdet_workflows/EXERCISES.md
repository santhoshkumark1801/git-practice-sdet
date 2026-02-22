# 🧪 Module 6: SDET Git Workflows

> **The big picture:** How do real QA/SDET teams use Git day-to-day?  
> This module connects everything you've learned to real-world scenarios.

---

## 📖 Common Branching Strategies

### Strategy 1: GitFlow (Most Structured — Enterprise teams)
```
main          ─────────────────────●──────────────────────● (production)
                                  /                       /
hotfix                           ●──●                    /
                                         \              /
release/v2.0   ──────────────────────────●─────────────●
                                        /
develop       ─────●──────●────────────● (integration)
                    \      \
feature/tests1       ●──●   \
                             ●──●──● feature/tests2
```

### Strategy 2: GitHub Flow (Simpler — Most teams use this)
```
main         ●─────────────────────────────●──────●
              \                           /        \
feature/X      ●──●──●  (PR → review → merge)      ●──●── feature/Y
```

### Strategy 3: Trunk-Based (Fast-moving CI/CD teams)
```
main   ●──●──●──●──●──●──●──● (everyone commits here via short-lived branches)
```

---

## 🏋️ EXERCISES

### Exercise 6.1 — SDET Daily Workflow Simulation (20 min)

**Simulate a full sprint day as an SDET:**

```bash
# === MORNING: Start new test feature ===

# Step 1: Sync your main with remote
git switch main
git pull origin main
# Always start your day with a pull!

# Step 2: Create test branch (JIRA ticket style naming)
git switch -c feature/QA-1234-add-user-profile-tests

# Step 3: Work on tests
# Edit 06_sdet_workflows/user_profile_tests.py — add your test cases

# Step 4: Regular small commits (don't save everything for one big commit!)
git add 06_sdet_workflows/user_profile_tests.py
git commit -m "test(QA-1234): add test for view profile"
# More work...
git commit -m "test(QA-1234): add test for update profile photo"
git commit -m "test(QA-1234): add test for delete account"

# === MIDDAY: Teammate merged to main — sync up ===

# Step 5: Pull latest main into your branch
git fetch origin
git rebase origin/main
# (or: git merge origin/main — depends on team preference)
# Resolve any conflicts if they occur

# === AFTERNOON: PR time ===

# Step 6: Push and open PR
git push -u origin feature/QA-1234-add-user-profile-tests
# Open PR on GitHub with proper description

# Step 7: Address review comments (extra commits on same branch)
git commit -m "refactor(QA-1234): use fixtures for test user data per review"
git push

# === END OF DAY ===
# Wait for approval and merge through GitHub UI
# Then clean up
git switch main
git pull
git branch -d feature/QA-1234-add-user-profile-tests
```

---

### Exercise 6.2 — Release Branch Workflow (15 min)

**Scenario:** Sprint is done. You need to cut a `release/v2.0` branch, run regression,  
then merge to main and tag it.

```bash
# Step 1: Cut the release branch from main
git switch main
git pull
git switch -c release/v2.0

# Step 2: Only BUGFIXES go here now (no new features!)
# Fix a flaky test found during regression
# Edit 06_sdet_workflows/regression_suite.py
git add .
git commit -m "fix(release): stabilize flaky order test"

# Step 3: Another small fix found during regression
# Edit 06_sdet_workflows/regression_suite.py
git commit -m "fix(release): correct expected response for mobile login"

# Step 4: Regression complete — merge to main
git switch main
git merge --no-ff release/v2.0 -m "chore: merge release/v2.0 into main"

# Step 5: Tag the release!
git tag -a v2.0.0 -m "Release v2.0.0: Sprint 42 regression complete. 127 tests passing."

# Step 6: Push everything
git push origin main
git push origin v2.0.0
git push origin --tags

# Step 7: Merge fixes back to develop (if using GitFlow)
git switch develop
git merge release/v2.0
git push origin develop
```

---

### Exercise 6.3 — Hotfix Workflow (10 min)

**Scenario:** Production is BROKEN at 2am. A critical payment test that was catching  
a bug is not running. You need to hotfix FAST.

```bash
# Step 1: Branch OFF the production tag (not develop!)
git switch main
git checkout v2.0.0           # go to production state
git switch -c hotfix/QA-9999-critical-payment-test

# Step 2: Fix it
# Edit 03_merging/payment_tests.py
git add .
git commit -m "hotfix(QA-9999): restore critical payment validation test"

# Step 3: Merge to main and tag a patch release
git switch main
git merge --no-ff hotfix/QA-9999-critical-payment-test
git tag -a v2.0.1 -m "Hotfix v2.0.1: Restore critical payment test"

# Step 4: Push
git push origin main
git push origin v2.0.1

# Step 5: Cherry-pick the fix to develop/release branch too!
git log --oneline main -1   # get the hotfix commit hash
git switch develop
git cherry-pick <hotfix-commit-hash>
git push origin develop

# Step 6: Clean up
git branch -d hotfix/QA-9999-critical-payment-test
```

---

### Exercise 6.4 — git blame (Find Who Changed What) (5 min)

**Scenario:** A test is broken. Someone changed an assertion value. WHO did it?

```bash
# Find who last edited each line of a file
git blame 03_merging/payment_tests.py

# Output format: hash | author | date | line
# e.g.:
# d4e5f6g (Santhan 2026-01-15 10:30:00) TIMEOUT = 30

# Blame with line range (only lines 10-25)
git blame -L 10,25 03_merging/payment_tests.py

# Find when a specific string was changed
git log -S "TIMEOUT" --oneline -- 03_merging/payment_tests.py
```

---

### Exercise 6.5 — Git Hooks (Automate Quality Gates) (15 min)

**Scenario:** Prevent bad test code from ever being committed — run linting/checks automatically.

```bash
# Git hooks live in .git/hooks/
ls .git/hooks/
# You'll see sample files like: pre-commit.sample, commit-msg.sample

# Step 1: Create a pre-commit hook (runs BEFORE every commit)
# Create the file:
```

**Create the file `.git/hooks/pre-commit`:**
```bash
#!/bin/sh
# Pre-commit hook: Prevent committing Python files with syntax errors

echo "🔍 Running pre-commit checks..."

# Check Python syntax on staged .py files
staged_py_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')

if [ -n "$staged_py_files" ]; then
    for file in $staged_py_files; do
        python -m py_compile "$file"
        if [ $? -ne 0 ]; then
            echo "❌ Syntax error in $file. Fix before committing!"
            exit 1
        fi
    done
    echo "✅ Python syntax OK"
fi

echo "✅ Pre-commit checks passed!"
exit 0
```

```bash
# Step 2: Make it executable (on Windows, this might not apply — use Git Bash)
chmod +x .git/hooks/pre-commit

# Step 3: Test it!
# Introduce a Python syntax error in any .py file:
# e.g., add: def broken(:    (invalid syntax)
git add .
git commit -m "this should fail"
# You should see: ❌ Syntax error in ... Fix before committing!

# Fix the syntax error and try again
git commit -m "this should pass"
# ✅ Pre-commit checks passed!
```

**More hook ideas for SDETs:**
```
pre-commit  → run pylint/flake8, check for print() statements, check for .only() in tests
commit-msg  → enforce commit message format (e.g., must start with "test/fix/feat/docs/chore")
pre-push    → run smoke tests before push
```

---

### Exercise 6.6 — Conventional Commits (Commit Message Standard) (5 min)

**Why it matters:** Consistent commit messages make release notes and git log readable.  
They also enable automated changelogs.

**Format:**
```
<type>(<scope>): <short description>
<BLANK LINE>
<optional body>
<BLANK LINE>
<optional footer>
```

**Types:**
| Type | When to use | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(login): add SSO support` |
| `fix` | Bug fix | `fix(checkout): correct tax calculation` |
| `test` | Test code | `test(api): add tests for user endpoint` |
| `refactor` | Code cleanup | `refactor(fixtures): extract common setup` |
| `docs` | Documentation | `docs(readme): update test setup instructions` |
| `chore` | Build, config | `chore(ci): add GitHub Actions workflow` |
| `perf` | Performance | `perf(search): optimize product search query` |
| `revert` | Revert commit | `revert: "feat: add SSO support"` |

**SDET-specific examples:**
```bash
git commit -m "test(QA-1234): add regression tests for user registration"
git commit -m "fix(QA-1200): update expected status code from 200 to 201"
git commit -m "chore: update pytest to 8.0.0"
git commit -m "refactor: extract API helper into base test class"
```

---

## 🗺️ SDET Git Workflow Summary

```
                    ┌─────────────────────────────────────────────────────┐
                    │                  DAILY WORKFLOW                     │
                    │                                                     │
   Sprint Start     │  git pull main → create branch → commit frequently │
       │             │  → push → PR → review → squash merge → delete      │
       ▼             └─────────────────────────────────────────────────────┘
   Feature Branch    
   (feature/QA-XXX)  ┌─────────────────────────────────────────────────────┐
       │             │              RELEASE WORKFLOW                        │
       ▼             │                                                      │
   PR + Review      │  main → cut release/vX.Y → regression → fix         │
       │             │  → merge to main → tag vX.Y.Z → push tag            │
       ▼             └─────────────────────────────────────────────────────┘
   Squash Merge      
   to main           ┌─────────────────────────────────────────────────────┐
       │             │              HOTFIX WORKFLOW                         │
       ▼             │                                                      │
   main (clean)      │  tag vX.Y.Z → hotfix branch → fix → merge main     │
                     │  → tag vX.Y.(Z+1) → cherry-pick to develop          │
                     └─────────────────────────────────────────────────────┘
```

---

## ✅ SDET Git Skills Checklist

Mark off each skill as you complete the exercises:

- [ ] Create and switch branches (`git switch -c`)
- [ ] Push branch and set upstream (`git push -u origin`)
- [ ] Undo unstaged changes (`git restore`)
- [ ] Unstage files (`git restore --staged`)
- [ ] Undo commits safely (`git reset --soft/mixed`)
- [ ] Revert pushed commits (`git revert`)
- [ ] Recover with reflog (`git reflog`)
- [ ] Merge with fast-forward
- [ ] Merge with merge commit
- [ ] Squash merge
- [ ] Resolve merge conflicts
- [ ] Rebase branch on main
- [ ] Open a PR with proper description
- [ ] Review and comment on a PR
- [ ] Protect the main branch
- [ ] Use `git stash` for interruptions
- [ ] Cherry-pick a commit
- [ ] Use `git bisect` to find a bug
- [ ] Create annotated tags
- [ ] Push tags to remote
- [ ] Use `git blame` to find author
- [ ] Set up a pre-commit hook
- [ ] Write conventional commit messages

**🎉 Congratulations!** If you've checked all of these, you have SDET-level Git skills!
