# ↩️ Module 2: Undoing & Redoing Changes

> **Why this matters for SDETs:**  
> You'll accidentally commit debug code, wrong test data, or break something.  
> Git gives you a time machine — but the tools differ in SAFETY. Know which to use!

---

## 📖 The Three Zones of Git

```
┌─────────────────┐    git add     ┌──────────────┐    git commit    ┌──────────────┐
│  Working Dir    │  ──────────►  │ Staging Area │  ──────────────► │  Repository  │
│ (your files)    │               │  (index)     │                  │  (history)   │
└─────────────────┘               └──────────────┘                  └──────────────┘
         ▲                               ▲                                  ▲
   git restore                  git restore --staged               git revert / reset
```

---

## 🚨 Safety Scale (Most Safe → Most Dangerous)

| Command | What it does | Safe? |
|---------|-------------|-------|
| `git restore <file>` | Discard unstaged changes to a file | ✅ Recoverable if staged |
| `git restore --staged <file>` | Unstage a file (keeps changes) | ✅ Very safe |
| `git revert <hash>` | New commit that undoes a commit | ✅ Safest for shared branches |
| `git reset --soft HEAD~1` | Undo commit, keep changes staged | ✅ Safe (local only) |
| `git reset --mixed HEAD~1` | Undo commit, keep changes unstaged | ✅ Safe (local only) |
| `git reset --hard HEAD~1` | Undo commit + DELETE all changes | ⚠️ Data loss! |

> **Golden Rule:** Never use `git reset --hard` on commits that have been pushed to a shared branch!

---

## 🏋️ EXERCISES

### Exercise 2.1 — Discard Unstaged Changes (5 min)

**Scenario:** You accidentally changed the wrong test file and want to undo it.

```bash
# Step 1: Make sure you're on main
git switch main

# Step 2: Make a change to the file (simulate accidental edit)
# Open 02_undoing_redoing/calculator_tests.py
# Change line: assert add(2, 3) == 5   →   assert add(2, 3) == 99

# Step 3: Check status — you'll see the modified file
git status
git diff 02_undoing_redoing/calculator_tests.py

# Step 4: Undo the change (restore from last commit)
git restore 02_undoing_redoing/calculator_tests.py

# Step 5: Verify the file is back to original
git status
# Should show: nothing to commit, working tree clean
```

**✅ Key Insight:** `git restore <file>` is your "undo" for unsaved/unstaged changes.  
⚠️ Warning: This is permanent — the change is gone!

---

### Exercise 2.2 — Unstage a File (5 min)

**Scenario:** You ran `git add` but then realized you don't want to commit that file yet.

```bash
# Step 1: Make changes to TWO files
# - Edit 02_undoing_redoing/calculator_tests.py (add a comment)
# - Edit 02_undoing_redoing/buggy_tests.py (add a comment)

# Step 2: Stage BOTH files
git add 02_undoing_redoing/calculator_tests.py
git add 02_undoing_redoing/buggy_tests.py

# Step 3: Check status — both are staged
git status

# Step 4: Oops! You only want to commit calculator_tests.py for now
# Unstage buggy_tests.py
git restore --staged 02_undoing_redoing/buggy_tests.py

# Step 5: Check status again
git status
# calculator_tests.py should be staged (green)
# buggy_tests.py should be unstaged (red)

# Step 6: Commit only the calculator file
git commit -m "test: add comment to calculator tests"
```

---

### Exercise 2.3 — Undo Last Commit with reset --soft (10 min)

**Scenario:** You committed too early. You want to undo the commit but keep your changes.

```bash
# Step 1: Make a change and commit it
# Edit 02_undoing_redoing/calculator_tests.py — add a new test
git add 02_undoing_redoing/calculator_tests.py
git commit -m "WIP: half done test"

# Step 2: Check the log
git log --oneline
# You'll see your "WIP" commit at the top

# Step 3: Undo the commit but KEEP changes STAGED
git reset --soft HEAD~1

# Step 4: Check status and log
git log --oneline
# Your commit is GONE from history
git status
# But your changes are still STAGED (green) — ready to re-commit!

# Step 5: Now commit properly
git commit -m "test: add divide-by-zero edge case test"
```

**✅ Key Insight:** `HEAD~1` means "one commit before HEAD". `HEAD~2` = two commits back.

---

### Exercise 2.4 — Undo Last Commit with reset --mixed (5 min)

**Scenario:** You committed too early AND want to reorganize which files to stage.

```bash
# Step 1: Make changes to two files and commit both together
# Edit calculator_tests.py AND buggy_tests.py
git add .
git commit -m "test: update two test files"

# Step 2: Undo the commit, put changes back to UNSTAGED
git reset --mixed HEAD~1
# (--mixed is also the DEFAULT: git reset HEAD~1 does the same thing)

# Step 3: Check status
git status
# Both files are now unstaged (red)

# Step 4: Stage and commit them SEPARATELY
git add 02_undoing_redoing/calculator_tests.py
git commit -m "test: update calculator edge cases"
git add 02_undoing_redoing/buggy_tests.py
git commit -m "fix: correct assertion in buggy test"
```

---

### Exercise 2.5 — Revert a Commit (SAFE for shared branches!) (10 min)

**Scenario:** A bad commit was pushed to `main`. You can't use `reset` (would rewrite shared history).  
Use `revert` instead — it creates a NEW commit that undoes the old one.

```bash
# Step 1: Make a "bad" commit
# Edit 02_undoing_redoing/buggy_tests.py — introduce a bug (wrong assertion value)
git add 02_undoing_redoing/buggy_tests.py
git commit -m "test: update expected values"

# Step 2: Pretend this got pushed (or IS on a shared branch)
git log --oneline
# Copy the hash of this "bad" commit (first 7 chars, e.g. a1b2c3d)

# Step 3: Revert it (creates a new undo commit)
git revert a1b2c3d
# Git opens a commit message editor — save and close it
# (In VS Code terminal, type :wq and press Enter if it opens vim)
# OR run with --no-edit to skip the editor:
git revert a1b2c3d --no-edit

# Step 4: Check the log
git log --oneline
# You'll see TWO new entries: the bad commit AND the revert commit
# The file is back to its original state
```

**✅ Key Difference:**
```
reset  → removes the commit from history (rewrites history) — LOCAL only
revert → adds a NEW commit that undoes changes — SAFE for shared/remote branches
```

---

### Exercise 2.6 — Recover a Accidentally Deleted Commit with reflog (10 min)

**Scenario:** You used `git reset --hard` and lost commits. Reflog is your last resort!

```bash
# Step 1: Make a commit
git add .
git commit -m "test: important test I don't want to lose"

# Step 2: Check the log
git log --oneline
# Note your important commit hash

# Step 3: Accidentally hard reset (DANGER ZONE simulation)
git reset --hard HEAD~1
# Your commit is GONE from the log!

# Step 4: Panic... then remember: git reflog
git reflog
# This shows EVERY action git recorded, including your lost commit!
# Find the line that shows your lost commit (e.g., abc1234 HEAD@{1}: commit: test: important test)

# Step 5: Restore it!
git reset --hard abc1234
# (replace abc1234 with the hash from reflog)

# Step 6: Verify
git log --oneline
# Your commit is BACK!
```

**✅ Key Insight:** `git reflog` is your safety net. Git keeps a log of ALL HEAD movements for 90 days.

---

## 🧠 Decision Tree: Which Undo Command?

```
Did you commit yet?
  ├── NO (just edited files)
  │     └── git restore <file>
  │
  └── YES (committed)
        ├── Has it been pushed / shared with others?
        │     ├── NO → git reset (soft/mixed/hard)
        │     └── YES → git revert <hash>
        │
        └── Did you use --hard and lose commits?
              └── git reflog → then git reset --hard <hash>
```

---

**➡️ Next:** Open `03_merging/EXERCISES.md`
