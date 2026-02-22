# 🔩 Module 09: Git Internals

> **You don't NEED this to use Git, but understanding it makes you unstoppable.**  
> When something goes wrong (and it will), internals knowledge lets you fix anything.

---

## 📖 How Git Actually Stores Data

Git is a **content-addressable file system**. Every piece of data is stored as an object,  
identified by a **SHA-1 hash** of its contents.

### The 4 Git Object Types

```
┌──────────────────────────────────────────────────────┐
│                  COMMIT OBJECT                        │
│  tree:    abc123  (points to the root tree)          │
│  parent:  def456  (previous commit)                  │
│  author:  Santhan <s@email.com> 1708598400 +0000     │
│  message: "test: add login tests"                    │
└──────────────────┬───────────────────────────────────┘
                   │ points to
                   ▼
┌──────────────────────────────────────────────────────┐
│                   TREE OBJECT                         │
│  blob  sha111  README.md                             │
│  blob  sha222  01_branching/login_tests.py           │
│  tree  sha333  01_branching/  (sub-directory)        │
└──────────────────┬───────────────────────────────────┘
                   │ points to
                   ▼
┌──────────────────────────────────────────────────────┐
│                   BLOB OBJECT                         │
│  (raw file contents — no filename, just bytes)       │
└──────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────┐
│                    TAG OBJECT                         │
│  object: abc123 (the commit it points to)            │
│  tagger: Santhan                                     │
│  message: "Release v1.0.0"                           │
└──────────────────────────────────────────────────────┘
```

---

## 🏋️ EXERCISES

### Exercise 9.1 — Explore the .git Folder (10 min)

```bash
cd "c:\Users\santh\Documents\Projects\Git Practice Project"

# Look at the .git folder structure
ls .git/
# Key folders/files:
# HEAD          ← where you are right now (current branch)
# config        ← this repo's local git config
# objects/      ← ALL git objects (blobs, trees, commits, tags)
# refs/         ← branch and tag pointers
# logs/         ← reflog data
# hooks/        ← git hook scripts

# Read HEAD — it's just a text file!
cat .git/HEAD
# Output: ref: refs/heads/main
# This means HEAD points to the branch 'main'

# Read what 'main' points to
cat .git/refs/heads/main
# Output: a commit hash like: d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2

# Look at the objects folder
ls .git/objects/
# You'll see 2-letter folders (first 2 chars of SHA hash)
ls .git/objects/ab/   # all objects starting with "ab"
```

---

### Exercise 9.2 — Inspect Git Objects (10 min)

```bash
# Get the latest commit hash
git log --oneline -1
# e.g.: d4e5f6g test: add login tests

# Inspect a COMMIT object
git cat-file -p d4e5f6g
# Output:
# tree abc1234...
# parent xyz5678...
# author Santhan <s@email.com> 1708598400 +0000
# committer Santhan <s@email.com> 1708598400 +0000
#
# test: add login tests

# Find out the type of any object
git cat-file -t d4e5f6g
# Output: commit

# Inspect the TREE object from that commit
git cat-file -p abc1234   # (use the tree hash from above)
# Output:
# 100644 blob sha111   README.md
# 040000 tree sha222   00_git_basics
# 040000 tree sha333   01_branching

# Inspect a BLOB (file contents)
git cat-file -p sha111    # (use the blob hash from above)
# Output: the raw file contents!

# See the SHA hash that would be created for a string
echo "hello git" | git hash-object --stdin
# Always outputs the same hash for "hello git" — deterministic!
```

**Key insight:** The same file content ALWAYS produces the same SHA-1 hash.  
That's why git is so efficient — identical files share the same blob object!

---

### Exercise 9.3 — Understanding HEAD and Branches (10 min)

```bash
# HEAD is just a pointer to a branch (or commit in detached mode)
cat .git/HEAD
# ref: refs/heads/main   ← HEAD → main branch

# A branch is just a pointer to a commit
cat .git/refs/heads/main
# d4e5f6g...   ← main → this commit

# So the full chain is:
# HEAD → refs/heads/main → commit d4e5f6g → tree → blobs

# Visualize all refs
git show-ref
# Lists all: branches, tags, remote-tracking branches

# See where HEAD, main, origin/main all point
git log --oneline --decorate -5
# Output:
# d4e5f6g (HEAD -> main, origin/main) test: add login tests
```

---

### Exercise 9.4 — Detached HEAD State (10 min)

**Detached HEAD** means HEAD points directly to a commit, not a branch.  
This happens when you checkout a specific commit or tag.

```bash
# Step 1: Checkout a specific commit (not a branch!)
git log --oneline
# Copy any older commit hash, e.g., abc1234

git checkout abc1234
# Warning: You are in 'detached HEAD' state.

# Step 2: Check HEAD
cat .git/HEAD
# abc1234...  ← HEAD points directly to a commit, not a branch!

git log --oneline -1
# Shows: (HEAD) abc1234 ...

# Step 3: You CAN make commits in detached HEAD
# But they won't belong to any branch — they'll be LOST when you switch!

# Make a commit
echo "# temp" >> temp.txt
git add .
git commit -m "temporary test"
# New commit created, but on no branch!

# Step 4: If you WANT to keep this work, create a branch HERE
git switch -c experiment/detached-test
# Now your commits are safe on a branch

# Step 5: Return to main (if you don't want to keep the work)
git switch main
# Commits made in detached HEAD are now orphaned (garbage collected eventually)

# Step 6: Useful detached HEAD use cases
git checkout v1.0.0         # inspect production code at a tag
git checkout HEAD~5         # look at code from 5 commits ago
# Always use 'git switch main' or 'git switch -c new-branch' to exit
```

---

### Exercise 9.5 — git config Deep Dive (10 min)

```bash
# ─── Config Levels (lowest to highest priority) ───────────────
# 1. System:  C:\Program Files\Git\etc\gitconfig  (all users)
# 2. Global:  C:\Users\YourName\.gitconfig        (your user)
# 3. Local:   .git/config                          (this repo)
# Local OVERRIDES global OVERRIDES system

# View config at each level
git config --system --list    # system
git config --global --list    # global (your user settings)
git config --local --list     # local (this repo's settings)
git config --list             # all (merged)

# Set a LOCAL config (only for this project)
git config user.email "work-account@company.com"
# Different from your personal global email — useful for work vs personal projects

# Set a LOCAL config to override global
git config core.autocrlf false    # Windows line endings override for this repo

# Edit configs in VS Code
git config --global --edit     # opens ~/.gitconfig in VS Code
git config --local --edit      # opens .git/config in VS Code

# Sample .gitconfig structure:
# [user]
#     name = Santhan
#     email = santhan@email.com
# [core]
#     editor = code --wait
#     autocrlf = true
# [init]
#     defaultBranch = main
# [alias]
#     lg = log --oneline --graph --all
#     st = status -s
```

---

### Exercise 9.6 — Useful git config Settings (5 min)

```bash
# ─── Must-Have Settings ────────────────────────────────────────

# Auto-correct typos (after 1 second delay)
git config --global help.autocorrect 10   # 10 = 1 second (in tenths)
# git comit -m "msg"  →  git suggests: did you mean 'commit'?

# Always rebase instead of merge on pull
git config --global pull.rebase true
# git pull  →  now runs  git pull --rebase  (cleaner history)

# Push only the current branch (not all branches)
git config --global push.default current

# Show whitespace errors in diffs
git config --global core.whitespace "trailing-space,space-before-tab"

# Always use --force-with-lease instead of --force
git config --global alias.pushf "push --force-with-lease"

# Better merge conflict style (shows common ancestor too)
git config --global merge.conflictstyle diff3

# ─── Windows-Specific ──────────────────────────────────────────

# Handle Windows line endings automatically
git config --global core.autocrlf true
# Files are stored with LF in git, but converted to CRLF on Windows checkout

# Long path support (Windows limit is 260 chars by default)
git config --global core.longpaths true
```

---

### Exercise 9.7 — Custom Git Aliases (Power User) (10 min)

```bash
# Set these up for massive productivity gains

git config --global alias.st "status -s"
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.ll "log --oneline --stat -5"
git config --global alias.last "log -1 HEAD --stat"
git config --global alias.undo "reset --soft HEAD~1"
git config --global alias.unstage "restore --staged"
git config --global alias.aliases "config --global --list | grep alias"
git config --global alias.branches "branch -a --sort=-committerdate"
git config --global alias.whoami "config user.email"
git config --global alias.contributors "shortlog --summary --numbered --no-merges"

# Advanced: shell command aliases start with !
git config --global alias.root "rev-parse --show-toplevel"   # show repo root
git config --global alias.pushf "push --force-with-lease"
git config --global alias.gone "!git fetch --prune && git branch -vv | awk '/: gone]/{print \$1}' | xargs git branch -d"
# git gone  →  delete all local branches where remote was deleted

# Test your aliases
git st          # short status
git lg          # visual tree
git undo        # undo last commit
git whoami      # your configured email
git contributors # list contributors by commit count
```

---

### Exercise 9.8 — git reflog (Your Safety Net) (10 min)

```bash
# reflog records EVERY movement of HEAD
git reflog

# Output format:
# abc1234 HEAD@{0}: commit: test: add login tests       ← most recent
# def5678 HEAD@{1}: checkout: moving from feature to main
# ghi9012 HEAD@{2}: rebase -i (finish): returning to refs/heads/main
# jkl3456 HEAD@{3}: commit: WIP: start tests            ← 3 actions ago

# See reflog for a specific branch
git reflog show main
git reflog show feature/add-tests

# Recover ANY lost commit/state
git reset --hard HEAD@{3}         # go back to 3 actions ago
git checkout -b recovered HEAD@{2} # create branch from a past state

# Reflog entries expire after 90 days by default
git config --global gc.reflogExpire 180   # keep for 180 days instead
```

**SDET Scenario — the ultimate recovery:**
```bash
# You ran git reset --hard and lost 3 commits!
git reflog
# Find the last good state: abc1234 HEAD@{3}: commit: test: critical test

git reset --hard abc1234
# ALL 3 commits are restored! 🎉
```

---

### Exercise 9.9 — Garbage Collection & Maintenance (5 min)

```bash
# Git accumulates loose objects over time — gc packs and cleans them
git gc
# Compresses objects into packfiles, removes unreachable objects

# More aggressive cleanup
git gc --aggressive --prune=now

# See repo size and object count
git count-objects -v
# Output:
# count: 15        ← loose objects
# size: 60         ← size in KB
# in-pack: 1523    ← packed objects
# size-pack: 312   ← packfile size in KB

# Check repo health
git fsck
# Checks for dangling commits (reachable via reflog but no branch pointing to them)
# Useful for finding "lost" commits

# Prune unreachable objects (be careful — they can't be recovered!)
git prune
git remote prune origin   # clean up deleted remote-tracking branches
```

---

## 🧠 Git Internals Summary

```
.git/
├── HEAD              → points to current branch
├── config            → repo-local git config
├── objects/          → all git objects (blob, tree, commit, tag)
│   ├── ab/
│   │   └── cdef...   → object stored as 2-char-folder + rest of SHA
│   └── pack/         → packed objects (after git gc)
├── refs/
│   ├── heads/        → local branches (each file = branch → commit hash)
│   │   ├── main
│   │   └── feature/x
│   ├── tags/         → tags
│   └── remotes/      → remote tracking branches
│       └── origin/
│           └── main
└── logs/
    ├── HEAD          → reflog for HEAD
    └── refs/heads/   → reflog per branch
```

**The 3 things to remember:**
1. **Everything in git is content-addressed** — SHA-1 hash of contents = identity
2. **Branches and HEAD are just text files** containing a commit hash
3. **`git reflog` can recover almost anything** lost in the last 90 days

---

## ✅ Final Checklist — You've Completed the Course!

Go back to [06_sdet_workflows/EXERCISES.md](../06_sdet_workflows/EXERCISES.md) and check off everything you've learned.

**🎓 You now have professional SDET-level Git & GitHub skills!**
