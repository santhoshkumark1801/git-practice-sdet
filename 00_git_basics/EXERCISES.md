# 🔰 Module 00: Git Basics & Setup

> **Start here if you're new to Git**, or use this as a solid reference.  
> By the end of this module you will understand exactly how Git tracks your work.

---

## 📖 How Git Works — The Big Picture

```
Your Computer
┌──────────────────────────────────────────────────────┐
│                                                      │
│  ┌───────────────┐  git add  ┌──────────────┐        │
│  │  Working Dir  │ ────────► │ Staging Area │        │
│  │  (edit here)  │           │  (index)     │        │
│  └───────────────┘           └──────┬───────┘        │
│          ▲                          │ git commit      │
│          │ git restore              ▼                 │
│          │                  ┌──────────────┐          │
│          └──────────────────│  Local Repo  │          │
│                             │  (.git/)     │          │
│                             └──────┬───────┘          │
└────────────────────────────────────┼─────────────────┘
                                     │ git push
                                     ▼
                           ┌──────────────────┐
                           │   Remote (GitHub) │
                           │   origin/main     │
                           └──────────────────┘
```

**Key insight:**
- `git add` → moves changes to the **staging area**
- `git commit` → saves staged changes to your **local repo**
- `git push` → uploads local commits to **GitHub (remote)**
- `git pull` → downloads remote commits to your **local repo**

---

## 🏋️ EXERCISES

### Exercise 0.1 — Install Git & First-Time Config (5 min)

```bash
# Verify Git is installed
git --version
# Should show: git version 2.x.x

# Set your identity (used on every commit you make)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# Set VS Code as your default editor
git config --global core.editor "code --wait"

# Set default branch name to 'main' (modern standard)
git config --global init.defaultBranch main

# Make git output colorful
git config --global color.ui auto

# See ALL your global config
git config --global --list

# See where config is stored
# Global config: C:\Users\YourName\.gitconfig
# Local config:  .git/config  (per-project, overrides global)
```

---

### Exercise 0.2 — git init vs git clone (5 min)

```bash
# ─── Option A: Start fresh (git init) ─────────────────────────
# Creates a brand new empty repo
mkdir my-new-project
cd my-new-project
git init
# Creates: .git/ folder (the entire git database)
ls -la   # (or dir in Windows) — you'll see .git folder

# ─── Option B: Download existing repo (git clone) ──────────────
# Copies a remote repo to your machine
git clone https://github.com/psf/requests.git
# Creates: requests/ folder with full git history

# Clone into a specific folder name
git clone https://github.com/psf/requests.git my-requests-copy

# Clone only the last N commits (shallow clone — faster for large repos)
git clone --depth 1 https://github.com/psf/requests.git
```

**Difference:**
```
git init   → YOU start the project, then push to GitHub
git clone  → GitHub has the project, you download it
```

---

### Exercise 0.3 — git status (Your Most Used Command) (5 min)

```bash
# Navigate to this project
cd "c:\Users\santh\Documents\Projects\Git Practice Project"

# Check what git knows about your files
git status

# Short format (compact view)
git status -s
# M  = modified
# A  = added (new staged file)
# ?? = untracked (git doesn't know about it yet)
# D  = deleted

# Example output of git status -s:
#  M 00_git_basics/sample_app.py    ← modified, not staged (red M)
# M  00_git_basics/sample_app.py    ← modified, staged (green M)
# ?? 00_git_basics/temp.txt         ← untracked
```

---

### Exercise 0.4 — git add (Staging Changes) (10 min)

```bash
# Stage a single file
git add 00_git_basics/sample_app.py

# Stage multiple specific files
git add 00_git_basics/sample_app.py 00_git_basics/test_sample.py

# Stage ALL changes (all modified + new files)
git add .

# Stage ALL changes in a specific folder
git add 00_git_basics/

# ─── INTERACTIVE STAGING (The Professional Way) ──────────────
# Stage PARTS of a file (choose specific hunks/lines!)
git add -p 00_git_basics/sample_app.py
# Git shows each changed "hunk" and asks:
# Stage this hunk? [y,n,q,a,d,s,e,?]
#   y = yes, stage this hunk
#   n = no, skip this hunk
#   s = split into smaller hunks
#   e = manually edit the hunk
#   ? = help

# WHY use -p? Real example:
# You changed 5 things in one file — 3 are ready to commit, 2 are still WIP
# Use -p to stage only the 3 ready hunks, leave 2 unstaged
```

**Try it:**
```bash
# 1. Open 00_git_basics/sample_app.py
# 2. Make TWO separate changes in the file
# 3. Use git add -p to stage ONLY the first change
# 4. git status   → see partial staging in action
```

---

### Exercise 0.5 — git commit (Saving Your Work) (10 min)

```bash
# Basic commit with inline message
git commit -m "feat: add sample app for git basics exercises"

# Open editor to write a multi-line commit message
git commit
# VS Code opens — write your message, save, close the file

# Stage + commit tracked files in ONE step (skips staging for NEW files)
git commit -am "fix: correct expected value in login test"

# ─── AMEND: Edit your last commit ─────────────────────────────
# Fix the last commit message (before push!)
git commit --amend -m "feat: add sample app with pytest tests"

# Add a forgotten file to the last commit (before push!)
git add forgotten_file.py
git commit --amend --no-edit    # keeps the same commit message

# ─── EMPTY COMMIT (useful for triggering CI) ──────────────────
git commit --allow-empty -m "ci: trigger pipeline rebuild"
```

**✅ Good commit message habits:**
```
✅ feat: add credit card validation test
✅ fix(QA-123): correct timeout assertion in payment test
✅ test: add edge cases for empty cart checkout
✅ refactor: extract common login fixture to conftest.py
✅ chore: upgrade pytest from 7.4 to 8.0

❌ fixed stuff
❌ WIP
❌ asdf
❌ changes
```

---

### Exercise 0.6 — git diff (See Exactly What Changed) (10 min)

```bash
# ─── Diff Types ───────────────────────────────────────────────

# See UNSTAGED changes (what you changed but haven't added yet)
git diff
git diff 00_git_basics/sample_app.py   # specific file only

# See STAGED changes (what will be committed)
git diff --staged
git diff --cached    # same thing, older syntax

# Compare two commits
git diff abc1234 def5678

# Compare two branches
git diff main feature/add-login-tests

# Compare a branch with main
git diff main..feature/add-login-tests

# See only which FILES changed (not the actual lines)
git diff --name-only main..feature/add-login-tests

# See statistics (how many lines added/removed per file)
git diff --stat main..feature/add-login-tests

# See word-level changes (better for text/docs)
git diff --word-diff
```

**Try it:**
```bash
# 1. Edit 00_git_basics/sample_app.py — change any function's return value
# 2. git diff                    → see unstaged red/green lines
# 3. git add 00_git_basics/sample_app.py
# 4. git diff                    → nothing! (it's staged now)
# 5. git diff --staged           → now you see the staged change
# 6. git commit -m "test: verify diff workflow"
# 7. git diff HEAD~1             → see what changed in that last commit
```

---

### Exercise 0.7 — git show (Inspect Any Commit) (5 min)

```bash
# Show the most recent commit (what changed + metadata)
git show

# Show a specific commit by hash
git show abc1234

# Show a commit in a cleaner format
git show abc1234 --stat          # show file names + stats
git show abc1234 --name-only     # just file names

# Show a specific file at a specific commit
git show abc1234:00_git_basics/sample_app.py
# Useful for: "what did this file look like 3 commits ago?"

# Show a specific tag
git show v1.0.0
```

---

### Exercise 0.8 — git remote (Managing Remotes) (10 min)

```bash
# List all remotes
git remote
git remote -v    # verbose — shows fetch and push URLs

# Add a remote called 'origin' (standard name for primary remote)
git remote add origin https://github.com/YOUR_USERNAME/git-practice-sdet.git

# Change a remote's URL (e.g., switch from HTTPS to SSH)
git remote set-url origin git@github.com:YOUR_USERNAME/git-practice-sdet.git

# Rename a remote
git remote rename origin upstream

# Remove a remote
git remote remove upstream

# ─── Push for the first time ──────────────────────────────────
git push -u origin main
# -u sets "upstream tracking" — after this you can just run: git push

# ─── Fetch vs Pull ────────────────────────────────────────────
git fetch origin
# Downloads new commits from remote but does NOT merge them.
# Safe to run anytime — won't change your working files.
# Use: git log origin/main to see what was fetched.

git pull origin main
# = git fetch + git merge
# Downloads AND merges remote changes into your current branch.

git pull --rebase origin main
# = git fetch + git rebase (cleaner history, preferred by many teams)

# Clean up remote-tracking branches that no longer exist on remote
git fetch --prune
git remote prune origin
```

---

### Exercise 0.9 — git clean (Remove Untracked Files) (5 min)

```bash
# Preview what WOULD be deleted (dry run — always do this first!)
git clean -n
git clean --dry-run

# Delete untracked files (files git doesn't know about)
git clean -f

# Delete untracked files AND folders
git clean -fd

# Delete untracked files including those in .gitignore (test outputs, etc.)
git clean -fdx
# ⚠️ This deletes build artifacts, __pycache__, .env files too — careful!

# Interactive mode (choose what to delete)
git clean -i
```

**SDET Use Case:**  
After running tests, your project fills up with `__pycache__/`, `*.pyc`, `test-results/`.  
`git clean -fd` wipes them all so you have a fresh working directory.

---

### Exercise 0.10 — SSH Keys (Secure GitHub Auth) (10 min)

```bash
# Step 1: Generate an SSH key pair
ssh-keygen -t ed25519 -C "your@email.com"
# Press Enter to accept default location: C:\Users\YourName\.ssh\id_ed25519
# Set a passphrase (optional but recommended)

# Step 2: Start the SSH agent and add your key
# On Windows (PowerShell as Admin):
Get-Service ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent
ssh-add $HOME\.ssh\id_ed25519

# Step 3: Copy your PUBLIC key
Get-Content $HOME\.ssh\id_ed25519.pub
# Copy the entire output

# Step 4: Add to GitHub
# Go to: GitHub → Settings → SSH and GPG keys → New SSH key
# Paste your public key → Save

# Step 5: Test the connection
ssh -T git@github.com
# Should say: Hi YOUR_USERNAME! You've successfully authenticated.

# Step 6: Switch remote from HTTPS to SSH
git remote set-url origin git@github.com:YOUR_USERNAME/git-practice-sdet.git
git remote -v   # verify
```

---

### Exercise 0.11 — Git Aliases (Work Faster) (5 min)

```bash
# Set up useful aliases globally
git config --global alias.st "status -s"
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.last "log -1 HEAD --stat"
git config --global alias.unstage "restore --staged"
git config --global alias.undo "reset --soft HEAD~1"
git config --global alias.aliases "config --global --list | grep alias"

# Now use them!
git st          # short status
git lg          # visual log tree
git last        # see last commit details
git unstage .   # unstage everything
git undo        # undo last commit (soft reset)
git aliases     # list all your aliases

# Even more powerful — shell-style aliases with !
git config --global alias.pushf "push --force-with-lease"
# git pushf  →  safer version of git push --force
```

**View and edit your full config:**
```bash
# Open the global config file in VS Code
git config --global --edit
# File: C:\Users\YourName\.gitconfig
```

---

## 🧠 Module 00 Summary

```
git config        → set name, email, editor, aliases
git init          → start a new repo
git clone         → download an existing repo
git status        → see what's changed
git add           → stage changes (use -p for partial staging!)
git commit        → save staged changes locally
git commit --amend→ fix the last commit
git diff          → see line-by-line changes
git show          → inspect any commit
git remote        → manage connections to GitHub
git push          → upload commits to GitHub
git pull          → download + merge from GitHub
git fetch         → download only (don't merge)
git clean         → remove untracked files
SSH keys          → secure, passwordless GitHub auth
aliases           → shortcuts for common commands
```

---

**➡️ Next:** Open `01_branching/EXERCISES.md`
