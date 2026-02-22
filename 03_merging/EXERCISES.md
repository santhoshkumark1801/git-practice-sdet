# 🔀 Module 3: Merging & Conflict Resolution

> **Why this matters for SDETs:**  
> You'll frequently merge test branches back to `main`. Sometimes you and a teammate  
> edited the same test file — that's a **merge conflict**. Resolving it is a core skill.

---

## 📖 Types of Merges

### 1. Fast-Forward Merge (Simplest)
When the target branch has no new commits since you branched off — git just moves the pointer forward.
```
main:    A──B
                \
feature:         C──D

After merge:
main:    A──B──C──D   (no merge commit created)
```

### 2. Three-Way Merge (Creates a Merge Commit)
When both branches have diverged — git creates a new "merge commit" that joins them.
```
main:    A──B──E
                \     \
feature:         C──D──M  (M = merge commit)
```

### 3. Squash Merge
All commits from the feature branch are "squashed" into ONE commit on main.
```
feature:  C──D──E──F
main:     A──B──[C+D+E+F]   (looks clean!)
```

### 4. Rebase
Replay your branch's commits ON TOP of the target branch (rewrites history).
```
Before:
main:    A──B──E
feature:    C──D

After rebase:
main:    A──B──E
feature:         C'──D'  (new commits with same changes)
```

---

## 🏋️ EXERCISES

### Exercise 3.1 — Fast-Forward Merge (5 min)

```bash
# Step 1: Make sure main has no extra commits
git switch main
git log --oneline

# Step 2: Create a branch and add commits
git switch -c feature/add-payment-tests
# Edit 03_merging/payment_tests.py — add a new test method
git add 03_merging/payment_tests.py
git commit -m "test: add credit card validation test"

# Add another commit
# Edit 03_merging/payment_tests.py again — add another test
git add 03_merging/payment_tests.py
git commit -m "test: add expired card test"

# Step 3: Merge back to main
git switch main
git merge feature/add-payment-tests

# Step 4: Check the log
git log --oneline --graph --all
# Notice: NO merge commit! Just a straight line (fast-forward)
```

---

### Exercise 3.2 — Three-Way Merge with Merge Commit (10 min)

```bash
# Step 1: Start fresh on main, create a branch
git switch main
git switch -c feature/add-order-tests
# Edit 03_merging/order_tests.py
git add 03_merging/order_tests.py
git commit -m "test: add order creation test"

# Step 2: While you worked, switch to main and add a commit there (simulating teammate)
git switch main
# Edit 03_merging/payment_tests.py — add a comment at top
git add 03_merging/payment_tests.py
git commit -m "docs: add test file description"

# Step 3: Now merge — main has diverged, so git will create a merge commit
git merge feature/add-order-tests
# Git opens editor for merge commit message — save and close

# Step 4: See the merge commit in the log
git log --oneline --graph --all
# Notice the diamond shape in the graph — that's the merge commit!
```

---

### Exercise 3.3 — Squash Merge (Clean History) (10 min)

```bash
# Step 1: Create a branch with multiple messy commits
git switch main
git switch -c feature/fix-test-data

# Commit 1
# Edit 03_merging/order_tests.py — change a test value
git add .
git commit -m "WIP: trying different approach"

# Commit 2
# Edit again
git add .
git commit -m "WIP: still fixing"

# Commit 3
# Edit again — final fix
git add .
git commit -m "fix: correct test data value"

# Step 2: Check all 3 commits on your branch
git log --oneline
# 3 commits (2 WIP + 1 fix) — messy!

# Step 3: Merge with squash back to main
git switch main
git merge --squash feature/fix-test-data

# Step 4: Commit the squashed result with ONE clean message
git commit -m "fix: correct test data in order tests (squashed)"

# Step 5: Check the log
git log --oneline --graph --all
# main has only ONE clean commit — no WIP mess!
```

**✅ Key Insight:** Squash merge is great for keeping `main` history clean when feature branches have noisy/WIP commits.

---

### Exercise 3.4 — Merge Conflict Resolution ⭐ (Most Important!) (15 min)

**Scenario:** You and a teammate both edited the same line. Git can't decide which is correct — it needs YOU.

```bash
# Step 1: On main, edit payment_tests.py line:
# Change: TIMEOUT = 30   →   TIMEOUT = 60
git add 03_merging/payment_tests.py
git commit -m "config: increase payment timeout to 60s"

# Step 2: Create a branch FROM the commit BEFORE this change
git log --oneline
# Copy the hash of the commit BEFORE the timeout change (e.g., abc1234)
git switch -c feature/payment-retry-tests abc1234
# (This simulates your teammate branched off earlier)

# Edit the SAME line in payment_tests.py:
# Change: TIMEOUT = 30   →   TIMEOUT = 45
git add 03_merging/payment_tests.py
git commit -m "config: set payment timeout to 45s for retries"

# Step 3: Switch to main and try to merge
git switch main
git merge feature/payment-retry-tests
# GIT SAYS: CONFLICT! Automatic merge failed.

# Step 4: See what's conflicted
git status
# You'll see: both modified: 03_merging/payment_tests.py

# Step 5: Open the conflicted file
# You'll see conflict markers:
# <<<<<<< HEAD
# TIMEOUT = 60
# =======
# TIMEOUT = 45
# >>>>>>> feature/payment-retry-tests

# Step 6: Resolve the conflict
# Delete the markers and decide: keep 60, keep 45, or pick a new value (e.g., 60)
# Save the file with your chosen value

# Step 7: Mark conflict as resolved and commit
git add 03_merging/payment_tests.py
git commit -m "merge: resolve timeout conflict, use 60s as agreed"

# Step 8: Verify
git log --oneline --graph --all
```

**🔍 Understanding Conflict Markers:**
```
<<<<<<< HEAD              ← Everything BELOW is from YOUR current branch (main)
TIMEOUT = 60
=======                   ← Separator
TIMEOUT = 45
>>>>>>> feature/payment-retry-tests   ← Everything ABOVE is from the INCOMING branch
```
**You must:** Delete the markers AND all but one version, then save.

---

### Exercise 3.5 — Aborting a Merge (3 min)

**Scenario:** You started a merge, got conflicts, and want to BAIL OUT completely.

```bash
# If you're in the middle of a conflicted merge:
git merge --abort

# This puts everything back to how it was before the merge attempt!
git status   # Clean working tree
```

---

### Exercise 3.6 — Rebase (Advanced) (15 min)

```bash
# Step 1: Create a branch from an older point of main
git switch main
git switch -c feature/rebase-practice
# Add a commit
git add .
git commit -m "test: add rebase practice test"

# Step 2: Add new commits to main (simulating team progress)
git switch main
# Edit any file
git add .
git commit -m "chore: update test config"

# Step 3: Rebase your feature branch on top of latest main
git switch feature/rebase-practice
git rebase main

# Step 4: See the result
git log --oneline --graph --all
# Your branch's commits are now ON TOP of main's latest commits
# History looks LINEAR (no merge commit)

# Step 5: Merge to main (will be fast-forward now!)
git switch main
git merge feature/rebase-practice
# Fast-forward! Clean linear history.
```

**⚠️ Rule:** Never rebase branches that others are using! Rebasing rewrites commit history.

---

## 🧠 Merge Strategy Cheat Sheet

| Strategy | Command | Use When |
|----------|---------|----------|
| Fast-Forward | `git merge <branch>` | Branch hasn't diverged |
| Merge Commit | `git merge --no-ff <branch>` | Want to preserve branch history |
| Squash | `git merge --squash <branch>` | Messy WIP commits, want clean main |
| Rebase | `git rebase main` | Want linear history, local only |

---

**➡️ Next:** Open `04_pull_requests/EXERCISES.md`
