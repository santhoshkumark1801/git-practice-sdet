# ✏️ Module 08: Interactive Rebase

> **`git rebase -i` is the most powerful history-editing tool in Git.**  
> Use it to clean up messy commit history before opening a PR —  
> so your teammates see a clean, logical story, not your "WIP" chaos.

---

## 📖 Why Interactive Rebase?

**Without it (messy branch):**
```
abc1234 WIP: half done
def5678 WIP: still fixing
ghi9012 oops typo
jkl3456 REALLY fixing now
mno7890 test: add checkout tests - FINAL
```

**After interactive rebase (clean PR):**
```
pqr1234 test: add checkout flow test suite
```

Much better for code review and git history!

---

## ⚠️ Golden Rules

> 1. **Never rebase commits that have been pushed to a shared branch.**  
> 2. It is **safe** to rebase your own local/feature branches before pushing.  
> 3. After rebasing a pushed branch, you'll need `git push --force-with-lease`.

---

## 📖 The Interactive Rebase Editor

When you run `git rebase -i HEAD~4`, git opens an editor like this:

```
pick abc1234 WIP: half done
pick def5678 WIP: still fixing
pick ghi9012 oops typo
pick jkl3456 REALLY fixing now
pick mno7890 test: add checkout tests - FINAL

# Commands:
# p, pick   = use commit as-is
# r, reword = use commit, but edit the commit message
# e, edit   = use commit, but stop to amend it
# s, squash = combine with previous commit (keeps both messages)
# f, fixup  = combine with previous commit (discards this message)
# d, drop   = remove the commit entirely
# Commits are listed oldest-first (top = oldest)
```

You edit the words (`pick`, `squash`, etc.), save, and close — git does the rest.

---

## 🏋️ EXERCISES

### Exercise 8.1 — Squash: Combine Multiple Commits Into One (15 min)

**Scenario:** You have 4 messy commits on a branch. Squash them into 1 clean commit for PR.

```bash
# Step 1: Set up a branch with multiple commits
git switch main
git switch -c feature/squash-practice

# Make 4 commits (simulate messy work)
# Edit 08_interactive_rebase/test_feature.py — add test 1
git add 08_interactive_rebase/test_feature.py
git commit -m "WIP: start writing feature tests"

# Edit again — add test 2
git add .
git commit -m "WIP: more tests"

# Edit again — fix a typo
git add .
git commit -m "fix typo"

# Edit again — final polish
git add .
git commit -m "done"

# Step 2: Check your 4 messy commits
git log --oneline
# 4 commits at the top of your branch

# Step 3: Start interactive rebase for last 4 commits
git rebase -i HEAD~4

# Step 4: The editor opens. Change it to:
# pick abc1234 WIP: start writing feature tests
# squash def5678 WIP: more tests
# squash ghi9012 fix typo
# squash jkl3456 done

# Step 5: Save and close the editor
# A SECOND editor opens — write the final combined commit message:
# test: add feature test suite covering happy path and edge cases

# Step 6: Save and close → rebase complete!

# Step 7: Verify
git log --oneline
# Only ONE clean commit now!
```

---

### Exercise 8.2 — Fixup: Squash and Discard Message (5 min)

**Scenario:** You made a tiny "oops" fix commit. Fold it into the previous commit silently.

```bash
# Step 1: Make a commit
git add .
git commit -m "test: add payment validation tests"

# Step 2: Realize you forgot to add a docstring — fix it
git add .
git commit -m "oops forgot docstring"

# Step 3: Squash the "oops" into the real commit using fixup
git rebase -i HEAD~2

# In the editor:
# pick abc1234 test: add payment validation tests
# fixup def5678 oops forgot docstring

# Save → The "oops" commit disappears, absorbed into the first one
# The final commit message is "test: add payment validation tests" (clean!)

git log --oneline
# Only ONE commit — the oops is gone
```

**Shortcut — create a fixup commit directly:**
```bash
git commit --fixup abc1234    # creates a commit tagged as fixup for abc1234
git rebase -i --autosquash HEAD~2  # auto-arranges fixup commits correctly
```

---

### Exercise 8.3 — Reword: Change a Commit Message (5 min)

**Scenario:** You made a typo in a commit message. Fix it without changing the code.

```bash
# Step 1: Check your recent commits
git log --oneline
# You see: abc1234 tset: add login test   ← typo!

# Step 2: Interactive rebase to fix it
git rebase -i HEAD~3  # go back 3 commits to find it

# In the editor, change 'pick' to 'reword' (or 'r') for that commit:
# pick xyz9999 previous commit
# reword abc1234 tset: add login test    ← change pick to reword
# pick def5678 later commit

# Step 3: Save the editor
# A NEW editor opens just for that commit's message
# Fix the typo: test: add login test
# Save and close

git log --oneline
# Message is fixed!
```

**For the VERY last commit** — no need for rebase:
```bash
git commit --amend -m "test: add login test"
# Only works for the most recent commit!
```

---

### Exercise 8.4 — Drop: Delete a Commit From History (5 min)

**Scenario:** You accidentally committed debug code or a secret. Remove it from history.

```bash
# Step 1: Make a bad commit
echo "API_KEY=super-secret-123" >> config.py
git add config.py
git commit -m "feat: add API config"

# Step 2: Realize you committed a secret!
# Check what commit to drop
git log --oneline

# Step 3: Interactive rebase
git rebase -i HEAD~2

# In the editor, change 'pick' to 'drop' (or 'd'):
# pick abc1234 previous safe commit
# drop def5678 feat: add API config    ← this commit is gone!

# Save and close

# Step 4: Verify
git log --oneline
# The commit is GONE
cat config.py
# The secret is removed from the file too!
```

> ⚠️ **If the bad commit was already pushed:** You must `git push --force-with-lease` after.  
> Also rotate any leaked credentials immediately — they may still be in GitHub's cache.

---

### Exercise 8.5 — Edit: Pause and Amend a Past Commit (10 min)

**Scenario:** You need to split a past commit into two, or add a file to it.

```bash
# Step 1: Create a commit that did "too much" (changed 2 unrelated things)
# Edit 08_interactive_rebase/test_feature.py  (add a test)
# AND edit 08_interactive_rebase/config.py    (change a setting)
git add .
git commit -m "test: update tests and config"

# Step 2: You want to split this into two commits
git rebase -i HEAD~1

# In the editor, change to 'edit':
# edit abc1234 test: update tests and config

# Save and close
# Git pauses at this commit! Prompt shows: (abc1234... HEAD detached)

# Step 3: Undo the commit but keep changes staged
git reset HEAD~1
# Changes are now UNSTAGED

# Step 4: Add and commit them SEPARATELY
git add 08_interactive_rebase/test_feature.py
git commit -m "test: add new test for feature X"

git add 08_interactive_rebase/config.py
git commit -m "config: update timeout setting"

# Step 5: Continue the rebase
git rebase --continue
# Rebase complete! One commit is now two.

git log --oneline
# Two clean commits!
```

---

### Exercise 8.6 — Reorder Commits (5 min)

**Scenario:** You want to reorder commits so the history tells a logical story.

```bash
# Step 1: Check your commits
git log --oneline
# abc1 test: add order tests
# def2 test: add payment tests
# ghi3 docs: update README

# Step 2: Reorder so README update comes first
git rebase -i HEAD~3

# In the editor — just MOVE the lines:
# Before:
# pick abc1 test: add order tests
# pick def2 test: add payment tests
# pick ghi3 docs: update README

# After (move README line to top):
# pick ghi3 docs: update README
# pick abc1 test: add order tests
# pick def2 test: add payment tests

# Save → git replays in new order!

git log --oneline
# ghi3 docs: update README   ← now first
# abc1 test: add order tests
# def2 test: add payment tests
```

> ⚠️ Reordering can cause conflicts if commits depend on each other. Resolve like a normal merge conflict.

---

### Exercise 8.7 — Full Cleanup Before a PR (Real Workflow) (15 min)

**This combines everything. Do this every time before opening a PR.**

```bash
# Step 1: You're on feature/add-reporting-tests
git log --oneline
# Shows: 7 commits of varying quality:
# WIP: start
# add test
# fix
# fix again  
# add more tests
# oops forgot assert
# FINAL: add reporting tests

# Step 2: Rebase onto latest main first (get any new changes)
git fetch origin
git rebase origin/main
# Resolve any conflicts if they appear

# Step 3: Now clean up your own commits
git rebase -i origin/main   # squash everything since you branched off main

# In the editor:
# pick abc1234 WIP: start                    ← keep (first one must be pick)
# squash def5678 add test                    ← squash
# squash ghi9012 fix                         ← squash
# squash jkl3456 fix again                   ← squash
# squash mno7890 add more tests              ← squash
# fixup  pqr1234 oops forgot assert          ← fixup (discard this message)
# squash stu5678 FINAL: add reporting tests  ← squash

# Write a clean final commit message:
# test(QA-456): add automated reporting test suite
#
# - Covers summary report generation
# - Covers CSV and HTML export formats
# - Covers empty report edge case
#
# Closes #12

# Step 4: Push (force needed because you rewrote history)
git push --force-with-lease origin feature/add-reporting-tests
# --force-with-lease is SAFER than --force:
# It checks nobody else pushed to this branch since you last pulled

# Step 5: Open PR — reviewers see ONE clean commit 🎉
```

---

## 🧠 Interactive Rebase Cheat Sheet

```bash
git rebase -i HEAD~N      # edit last N commits
git rebase -i origin/main # edit all commits since branching off main

# In the editor:
# pick    → keep commit as-is
# reword  → keep commit, change message
# edit    → pause to amend commit
# squash  → merge into previous, combine messages
# fixup   → merge into previous, discard this message
# drop    → delete this commit entirely

# During rebase:
git rebase --continue     # after resolving a conflict or editing
git rebase --abort        # cancel and go back to before rebase started
git rebase --skip         # skip a commit that's causing conflicts

# After rewriting pushed history:
git push --force-with-lease   # safer than --force
```

---

**➡️ Next:** Open `09_git_internals/EXERCISES.md`
