# 🚀 Module 5: Advanced Git Topics

> **Topics covered:**
> - `git stash` — temporarily save work in progress
> - `git cherry-pick` — apply a specific commit to another branch
> - `git bisect` — binary search to find a bug-introducing commit
> - `git tags` — mark release points
> - `git log` — power searching history
> - `.gitignore` — what not to commit

---

## 🏋️ EXERCISES

---

### Exercise 5.1 — git stash (Save Work in Progress) (10 min)

**Scenario:** You're in the middle of writing a test, and suddenly your manager says  
"Stop! There's a production bug, fix the flaky test on main RIGHT NOW!"  
You can't commit half-done work. Use `git stash`.

```bash
# Step 1: Start working on a feature branch
git switch main
git switch -c feature/add-inventory-tests

# Step 2: Edit 05_advanced_topics/inventory_tests.py
# Add a half-written test (leave it incomplete, don't make it valid Python yet):
# def test_stock_level_INCOMPLETE:
#     pass

# Step 3: Check status — you have uncommitted changes
git status

# Step 4: URGENT! Need to switch to main for a hotfix
# You can't commit (code is broken), so STASH it
git stash
# Message: Saved working directory and index state WIP on feature/add-inventory-tests

# Step 5: Verify your working directory is clean
git status
# Clean! Your incomplete changes are safely stashed

# Step 6: Switch to main, do the hotfix
git switch main
# Fix the flaky test in 05_advanced_topics/flaky_test.py
# Add a comment: # Fixed: added retry logic
git add 05_advanced_topics/flaky_test.py
git commit -m "fix: add stability to flaky test"

# Step 7: Go back to your feature branch and restore stash
git switch feature/add-inventory-tests
git stash pop
# Your half-written test is back!

git status
# Shows your WIP changes are restored
```

**🔑 Key Stash Commands:**
```bash
git stash                       # stash with auto-name
git stash save "WIP inventory"  # stash with custom name
git stash list                  # see all stashes
git stash pop                   # restore latest stash (and delete it)
git stash apply stash@{1}       # restore a specific stash (keeps it in list)
git stash drop stash@{0}        # delete a stash
git stash clear                 # delete ALL stashes (careful!)
git stash branch feature/new    # create a branch from stash
```

---

### Exercise 5.2 — git cherry-pick (Apply a Specific Commit) (10 min)

**Scenario:** You fixed a critical bug on `main`. The `release/v2.0` branch also needs  
this fix — but you don't want to merge ALL of main into release. Cherry-pick to the rescue!

```bash
# Step 1: On main, make a specific bugfix commit
git switch main

# Edit 05_advanced_topics/flaky_test.py — add a stability fix
git add 05_advanced_topics/flaky_test.py
git commit -m "fix: resolve race condition in payment test"

# Note the commit hash
git log --oneline
# e.g., output: d4e5f6g fix: resolve race condition in payment test

# Step 2: Imagine you have a release branch
git switch -c release/v2.0
# (This branch was cut before your fix)
git log --oneline
# Your fix commit is NOT here

# Step 3: Cherry-pick ONLY that specific fix commit
git cherry-pick d4e5f6g
# (replace d4e5f6g with your actual commit hash)

# Step 4: Verify the commit is now on the release branch
git log --oneline
# You'll see the cherry-picked commit here now!
```

**Real-world Use Cases for SDETs:**
- Hotfix on `main` needs to go to `release/v2.0` without merging all new tests
- A test fix was committed to the wrong branch — cherry-pick it to the right one
- You need just ONE specific test from a feature branch, not the whole branch

---

### Exercise 5.3 — git bisect (Find the Guilty Commit) ⭐ (15 min)

**Scenario:** Tests were passing 10 commits ago. They fail now. WHICH commit broke it?  
`git bisect` does a binary search through commits — finds the culprit in O(log n) steps.

```bash
# Step 1: Create a history with a "bug" in it
# We'll create several commits, one of which introduces a "bug"
git switch main

git commit --allow-empty -m "commit 1: all tests passing"
git commit --allow-empty -m "commit 2: add feature A"
git commit --allow-empty -m "commit 3: add feature B"

# Introduce the "bug" (edit a test to use wrong value)
# Edit 05_advanced_topics/inventory_tests.py — change expected value to wrong number
git add 05_advanced_topics/inventory_tests.py
git commit -m "commit 4: refactor inventory logic"

git commit --allow-empty -m "commit 5: add feature C"
git commit --allow-empty -m "commit 6: minor cleanup"

# Step 2: Note the current (bad) commit and an old (good) commit
git log --oneline
# Copy the hash of commit 1 (GOOD) and current HEAD (BAD)

# Step 3: Start bisect
git bisect start
git bisect bad                  # current commit is BAD
git bisect good <hash of commit 1>  # this commit was GOOD

# Step 4: Git checks out a middle commit — test if it's good or bad
# Check: does the inventory test have the wrong value?
# If YES (bug present): git bisect bad
# If NO (bug not present): git bisect good

# Keep answering git bisect good/bad...
# Git will narrow it down to the EXACT commit that introduced the bug!

# Step 5: When bisect finds it:
# "d4e5f6g is the first bad commit"
# commit 4: refactor inventory logic — FOUND IT!

# Step 6: End bisect (returns to your original HEAD)
git bisect reset
```

**🔑 Key Point:** With 100 commits, bisect finds the bad one in just 7 steps ($\log_2 100 \approx 7$)!

---

### Exercise 5.4 — git tags (Mark Releases) (10 min)

**Scenario:** Your automation suite hits a milestone — v1.0 is stable and ready.  
Tag it so you can always get back to that exact state.

```bash
# Step 1: Make sure you're on the commit you want to tag
git switch main
git log --oneline
# Copy the hash of your "stable" commit

# Step 2: Lightweight tag (just a pointer — like a bookmark)
git tag v1.0.0

# Step 3: Annotated tag (recommended — has message, author, date)
git tag -a v1.0.0-release -m "Release: Automation suite v1.0 - full regression ready"

# Step 4: List all tags
git tag
git tag -l "v1.*"   # filter tags

# Step 5: See tag details
git show v1.0.0-release

# Step 6: Push tags to GitHub (tags are NOT pushed with git push by default!)
git push origin v1.0.0-release   # push specific tag
git push origin --tags            # push ALL tags

# Step 7: Checkout a specific tag (read-only, "detached HEAD")
git checkout v1.0.0-release
# Run your tests at this exact snapshot

# Get back to normal
git switch main

# Step 8: Delete a tag
git tag -d v1.0.0                  # delete local
git push origin --delete v1.0.0   # delete remote
```

**SDET Use Case:**  
Tag your test suite at every sprint release: `v1.0.0`, `v1.1.0`, `v2.0.0`.  
If a regression is found in production, checkout the matching tag to reproduce it.

---

### Exercise 5.5 — git log Power Usage (10 min)

```bash
# Basic log
git log

# Compact (one line per commit)
git log --oneline

# Visual branch tree
git log --oneline --graph --all

# Last 5 commits
git log -5

# Search commits by message
git log --grep="login"

# Search commits by author
git log --author="Santhan"

# Show changes in each commit
git log -p

# Show which files changed
git log --stat

# Commits between two dates
git log --after="2026-01-01" --before="2026-02-22"

# Commits that changed a specific file
git log -- 01_branching/login_tests.py

# Commits that changed a specific string (great for debugging!)
git log -S "TIMEOUT = 30"
# "Which commit added or removed TIMEOUT = 30?"

# Pretty format — custom output
git log --pretty=format:"%h | %an | %ar | %s"
# hash | author | relative time | subject
```

---

### Exercise 5.6 — .gitignore (What NOT to Commit) (10 min)

**Scenario:** You have test output files, credentials, and virtual environment folders  
that should NEVER be committed to git.

```bash
# Step 1: Create a .gitignore file (already in this project!)
# Open .gitignore at the root of the project

# Step 2: Test that ignored files are ignored
# Create a file that should be ignored
echo "secret_key=abc123" > .env
git status
# .env should NOT appear in git status!

# Create a test output file
mkdir test-results
echo "<html></html>" > test-results/report.html
git status
# test-results/ should NOT appear!

# Step 3: Force add an ignored file (sometimes needed)
git add -f .env
# (Don't do this for real secrets!)

# Step 4: If you accidentally committed a file that should be ignored:
# First add it to .gitignore, then:
git rm --cached .env           # remove from tracking (keeps local file)
git commit -m "chore: untrack .env file"
git push
```

---

## 🧠 Advanced Cheat Sheet

```bash
# Stash
git stash                        # save WIP
git stash pop                    # restore WIP
git stash list                   # all stashes

# Cherry-pick
git cherry-pick <hash>           # apply one commit to current branch
git cherry-pick A..B             # apply a range of commits

# Bisect
git bisect start
git bisect bad                   # current commit is bad
git bisect good <hash>           # this commit was good
git bisect reset                 # done

# Tags
git tag -a v1.0.0 -m "message"  # create annotated tag
git push origin --tags           # push all tags
git checkout v1.0.0              # go to tagged commit

# Log
git log --oneline --graph --all  # visual tree
git log -S "search string"       # find when string changed
git log --author="Name"          # filter by author
```

---

**➡️ Next:** Open `06_sdet_workflows/EXERCISES.md`
