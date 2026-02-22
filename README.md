# 🧪 Git & GitHub Mastery for SDETs
### A Complete, Practical, Hands-On Learning Path

> **Start here if you're a beginner** → Module 00  
> **Start here if you know basics** → Module 01  
> **Goal:** Full mastery of Git & GitHub for professional SDET work.

---

## 📚 Complete Learning Path (Do In Order)

| # | Topic | Folder | Level | Time |
|---|-------|--------|-------|------|
| 0 | 🔰 Git Basics & Setup | `00_git_basics/` | Beginner | ~45 min |
| 1 | 🌿 Branching | `01_branching/` | Beginner | ~30 min |
| 2 | ↩️ Undoing & Redoing | `02_undoing_redoing/` | Intermediate | ~40 min |
| 3 | 🔀 Merging & Conflicts | `03_merging/` | Intermediate | ~45 min |
| 4 | 🔁 Pull Requests (PRs) | `04_pull_requests/` | Intermediate | ~30 min |
| 5 | 🚀 Advanced Git | `05_advanced_topics/` | Advanced | ~60 min |
| 6 | 🧪 SDET Git Workflows | `06_sdet_workflows/` | Advanced | ~45 min |
| 7 | 🐙 GitHub Features | `07_github_features/` | Intermediate | ~60 min |
| 8 | ✏️ Interactive Rebase | `08_interactive_rebase/` | Advanced | ~45 min |
| 9 | 🔩 Git Internals | `09_git_internals/` | Expert | ~60 min |

---

## 🗂️ What's Covered (Every Topic)

<details>
<summary><b>Module 00 — Git Basics & Setup</b></summary>

- Installing Git & first-time config (`user.name`, `user.email`, editor)
- `git init` vs `git clone`
- The three zones: Working Dir → Staging → Repository
- `git status`, `git add`, `git add -p` (partial staging)
- `git commit`, `git commit --amend`
- `git push`, `git pull`, `git fetch`
- `git remote` (add, remove, rename, -v)
- `git diff` (unstaged, staged, between commits)
- `git show` (inspect any commit)
- `git clean` (remove untracked files)
- SSH key setup for GitHub
- Git aliases (shortcuts)
</details>

<details>
<summary><b>Module 01 — Branching</b></summary>

- Creating, switching, and deleting branches
- `HEAD` and what it points to
- Remote tracking branches
- Branch naming conventions (SDET style)
- `git branch -vv` (see tracking info)
</details>

<details>
<summary><b>Module 02 — Undoing & Redoing</b></summary>

- `git restore` (discard changes)
- `git restore --staged` (unstage)
- `git reset --soft / --mixed / --hard`
- `git revert` (safe undo for shared branches)
- `git reflog` (recover anything)
- Decision tree: which undo command?
</details>

<details>
<summary><b>Module 03 — Merging & Conflicts</b></summary>

- Fast-forward merge
- Three-way merge (merge commit)
- Squash merge
- `git rebase`
- Conflict markers and resolution
- `git merge --abort`
- `git mergetool`
</details>

<details>
<summary><b>Module 04 — Pull Requests</b></summary>

- Full PR lifecycle
- PR description templates
- Code review best practices for test code
- Addressing review feedback
- Merge strategies (merge/squash/rebase)
- Branch protection rules
- Fork + upstream workflow (open source)
</details>

<details>
<summary><b>Module 05 — Advanced Git</b></summary>

- `git stash` (save/restore WIP)
- `git cherry-pick` (apply specific commits)
- `git bisect` (binary search for bugs)
- Annotated tags & releases
- `git log` power usage
- `.gitignore` patterns
</details>

<details>
<summary><b>Module 06 — SDET Workflows</b></summary>

- Daily SDET workflow simulation
- GitFlow / GitHub Flow / Trunk-Based
- Release branch workflow
- Hotfix workflow
- `git blame`
- Pre-commit hooks
- Conventional commits
</details>

<details>
<summary><b>Module 07 — GitHub Features</b></summary>

- Issues (creating, labeling, closing via commits)
- Milestones & Projects (Kanban)
- GitHub Actions / CI (running tests automatically)
- GitHub Releases
- GitHub CLI (`gh`)
- Dependabot & security alerts
- GitHub Wiki
- `CODEOWNERS` file
</details>

<details>
<summary><b>Module 08 — Interactive Rebase</b></summary>

- `git rebase -i` (the most powerful git command)
- Squash: combine multiple commits into one
- Fixup: squash silently (discard message)
- Reword: change a commit message
- Drop: delete a commit from history
- Edit: pause and amend a past commit
- Reorder: change commit order
- Splitting a commit into two
</details>

<details>
<summary><b>Module 09 — Git Internals</b></summary>

- How git stores data (blob, tree, commit objects)
- SHA-1 hashes explained
- The `.git` folder structure
- `HEAD`, refs, and branches as pointers
- Detached HEAD state
- Packfiles & garbage collection
- `git config` deep dive (local/global/system)
- Custom git aliases
</details>

---

## ⚡ Quick Command Reference

```bash
# ─── SETUP ────────────────────────────────────────────────────
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
git config --global core.editor "code --wait"   # VS Code as editor
git config --list                                 # see all config

# ─── BASICS ───────────────────────────────────────────────────
git init                          # new local repo
git clone <url>                   # copy remote repo
git status                        # what's changed?
git add <file>                    # stage a file
git add .                         # stage everything
git add -p                        # interactive/partial staging
git commit -m "message"           # commit staged changes
git commit --amend                # edit last commit (message or files)
git diff                          # unstaged changes
git diff --staged                 # staged changes
git show <hash>                   # show a specific commit
git clean -fd                     # delete untracked files & dirs

# ─── REMOTE ───────────────────────────────────────────────────
git remote -v                     # list remotes
git remote add origin <url>       # add a remote
git push -u origin main           # push and set tracking
git push                          # push (after tracking set)
git pull                          # fetch + merge
git fetch                         # download but don't merge
git fetch --prune                 # clean up deleted remote branches

# ─── BRANCHING ────────────────────────────────────────────────
git branch                        # list branches
git switch -c <branch>            # create + switch
git switch <branch>               # switch
git branch -d <branch>            # delete (safe)
git branch -D <branch>            # delete (force)
git push origin --delete <branch> # delete remote branch
git branch -vv                    # show tracking info

# ─── UNDOING ──────────────────────────────────────────────────
git restore <file>                # discard unstaged changes
git restore --staged <file>       # unstage
git reset --soft HEAD~1           # undo commit, keep staged
git reset --mixed HEAD~1          # undo commit, keep unstaged
git reset --hard HEAD~1           # undo commit + DELETE changes ⚠️
git revert <hash>                 # safe undo (new commit)
git reflog                        # full history safety net

# ─── MERGING ──────────────────────────────────────────────────
git merge <branch>                # merge into current
git merge --no-ff <branch>        # always create merge commit
git merge --squash <branch>       # squash all commits to one
git merge --abort                 # cancel a conflict
git rebase main                   # replay commits on top of main
git rebase -i HEAD~3              # interactive rebase (last 3 commits)

# ─── ADVANCED ─────────────────────────────────────────────────
git stash                         # save WIP
git stash pop                     # restore WIP
git cherry-pick <hash>            # apply a specific commit
git bisect start                  # binary search for bug
git tag -a v1.0.0 -m "msg"       # annotated tag
git push origin --tags            # push all tags
git blame <file>                  # who changed what line
git log -S "search string"        # find when string changed
git log --oneline --graph --all   # visual commit tree
```

---

## 🏁 How to Start

```bash
# 1. Open your terminal and navigate to this folder
cd "c:\Users\santh\Documents\Projects\Git Practice Project"

# 2. Initialize git
git init
git add .
git commit -m "chore: initial commit - git learning exercises"

# 3. Set your identity (skip if already set globally)
git config user.name "Your Name"
git config user.email "your@email.com"

# 4. Start learning — begin with Module 00 if you want a complete foundation
# Open: 00_git_basics/EXERCISES.md
# Or jump to: 01_branching/EXERCISES.md if you know the basics
```

---

## 💡 SDET-Specific Git Concepts Covered

- ✅ Feature branch workflows for test automation
- ✅ Branching strategies for test environments (dev/staging/prod)
- ✅ Using `git bisect` to find when a test started failing
- ✅ Cherry-picking hotfixes to release branches
- ✅ Tagging releases for traceability
- ✅ PR reviews for test code quality
- ✅ Protecting the `main` branch
- ✅ Git hooks for running tests before commit
- ✅ GitHub Actions CI — running pytest on every push
- ✅ Interactive rebase to clean up WIP commits before PR
- ✅ Conventional commits for readable release notes
- ✅ `git blame` to audit test file history
- ✅ Forking & open source contribution workflow
- ✅ `CODEOWNERS` to enforce test review by QA team

---

*Each module folder has an `EXERCISES.md` with step-by-step instructions.*  
*Work through them in order for the best learning experience.*
