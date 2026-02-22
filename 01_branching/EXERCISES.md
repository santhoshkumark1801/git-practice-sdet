# 🌿 Module 1: Branching

> **Why branching matters for SDETs:**  
> You never write test code directly on `main`. Branches let you work on test features  
> in isolation — so broken test code never affects the team's CI/CD pipeline.

---

## 📖 Core Concepts

| Concept | What it means |
|---------|--------------|
| `main` / `master` | The "source of truth" — always stable |
| Feature branch | A branch for one piece of work |
| `HEAD` | A pointer to your current position in git history |
| Upstream | The remote branch your local branch tracks |

### 🌳 Branch Naming Convention (SDET Style)
```
feature/add-login-tests
bugfix/fix-flaky-checkout-test  
test/api-regression-suite
release/v2.1.0-tests
hotfix/critical-payment-test
```

---

## 🏋️ EXERCISES

### Exercise 1.1 — Your First Branch (10 min)

**Goal:** Create a feature branch and make a commit on it.

```bash
# Step 1: Make sure you're in the project folder
cd "c:\Users\santh\Documents\Projects\Git Practice Project"

# Step 2: Check your current branch (should be 'main' or 'master')
git branch

# Step 3: Create and switch to a new branch
git switch -c feature/add-login-tests

# Step 4: Verify you're on the new branch
git branch
# You should see: * feature/add-login-tests

# Step 5: Open the file 01_branching/login_tests.py
# Make a small change — add a comment at the top like:
# # Author: YourName | Date: 2026-02-22

# Step 6: Stage and commit your change
git add 01_branching/login_tests.py
git commit -m "test: add author info to login tests"

# Step 7: See your commit
git log --oneline
```

**✅ Check:** Run `git log --oneline`. You should see your new commit only on this branch.

---

### Exercise 1.2 — Switching Between Branches (5 min)

**Goal:** Understand that branches are isolated.

```bash
# Step 1: Look at your commit on the feature branch
git log --oneline
# Note the commit hash (first 7 chars)

# Step 2: Switch back to main
git switch main

# Step 3: Look at the log on main
git log --oneline
# Notice: your commit from feature/add-login-tests is NOT here!

# Step 4: Check the file - your change is gone from this branch
# (Don't worry, it's safe on the feature branch)

# Step 5: Switch back to your feature branch
git switch feature/add-login-tests
# Your change is back!
```

**✅ Key Insight:** Branches are completely isolated. Changes on one branch don't affect others until you MERGE.

---

### Exercise 1.3 — Multiple Branches (10 min)

**Goal:** Simulate real-world parallel work (two SDETs working simultaneously).

```bash
# Step 1: Create a second branch from main
git switch main
git switch -c feature/add-api-tests

# Step 2: Modify 01_branching/api_tests.py
# Add a comment: # API Tests - Sprint 42

# Step 3: Commit
git add 01_branching/api_tests.py
git commit -m "test: create api test skeleton for sprint 42"

# Step 4: Now create a THIRD branch
git switch main
git switch -c bugfix/fix-flaky-search-test

# Step 5: Modify 01_branching/search_tests.py
# Change the search term from "laptop" to "smartphone"

# Step 6: Commit
git add 01_branching/search_tests.py
git commit -m "fix: update search test to use stable test data"

# Step 7: See ALL branches and where HEAD is
git branch
# Output should show 3+ branches

# Step 8: See a visual tree of all commits
git log --oneline --graph --all
```

**✅ Check:** You should see a branching tree in the log output.

---

### Exercise 1.4 — Tracking Remote Branches (5 min)

**Goal:** Push a branch to GitHub and set up tracking.

```bash
# (Requires a GitHub remote — skip if not set up yet)

# Push branch to GitHub and set it to track the remote
git push -u origin feature/add-login-tests

# After this, you can just use:
git push   # (no need to specify origin + branch name)
git pull   # (pulls from the tracked remote branch)

# See what remote branch your local branch tracks
git branch -vv
```

---

### Exercise 1.5 — Delete Branches (5 min)

**Goal:** Clean up merged branches (a real habit SDETs need).

```bash
# Switch to main first (can't delete branch you're ON)
git switch main

# Delete a branch that's been merged (safe delete)
git branch -d feature/add-login-tests
# Git will WARN you if this branch hasn't been merged yet

# Force delete a branch (use with caution!)
git branch -D feature/add-login-tests
# This deletes even if not merged — data loss possible!

# Delete a remote branch
git push origin --delete feature/add-login-tests
```

---

## 🧠 Branching Cheat Sheet

```
main ──────●──────────────────────────●── (stable)
            \                        /
             ●──●──●  feature/login  (your work)
```

```bash
git switch -c <branch>     # create + switch
git switch <branch>        # switch to existing
git branch                 # list local branches
git branch -a              # list all (local + remote)
git branch -d <branch>     # delete (safe)
git branch -D <branch>     # delete (force)
git log --oneline --graph --all   # visual tree
```

---

## 🎯 SDET Real-World Scenario

> Your team is doing a release. Two scenarios:
> - **You** are working on regression tests for the new `checkout v2` feature → `feature/checkout-v2-regression`  
> - **Teammate** is fixing a flaky test → `bugfix/fix-flaky-payment-test`  
> - **CI/CD** always runs off `main` → protected, nobody commits directly  
>
> Both of you work independently without stepping on each other's code. 🎉

---

**➡️ Next:** Open `02_undoing_redoing/EXERCISES.md`
