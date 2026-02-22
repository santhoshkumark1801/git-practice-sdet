# 🔁 Module 4: Pull Requests (PRs)

> **Why this matters for SDETs:**  
> PRs are how test code gets reviewed before merging to `main`. As an SDET you'll  
> BOTH raise PRs (for your test code) AND review teammates' PRs (code quality gate).

---

## 📖 PR Lifecycle

```
1. Create Branch         git switch -c feature/...
       ↓
2. Make Commits          git commit -m "..."
       ↓
3. Push Branch           git push -u origin feature/...
       ↓
4. Open PR on GitHub     GitHub UI → "New Pull Request"
       ↓
5. Code Review           Teammates comment, request changes
       ↓
6. Address Feedback      Push more commits to same branch
       ↓
7. Approval              Reviewer approves ✅
       ↓
8. Merge PR              GitHub UI → "Merge Pull Request"
       ↓
9. Delete Branch         GitHub auto-deletes or do manually
```

---

## 🏋️ EXERCISES

> ⚠️ **Note:** Exercises 4.1–4.6 require a GitHub account and a remote repository.  
> **Setup:** Create a new repo at github.com first, then connect it.

### Setup — Connect to GitHub

```bash
# Step 1: Create a new repo on GitHub (github.com → New Repository)
# Name it: git-practice-sdet
# Make it PUBLIC
# DO NOT initialize with README (you already have files)

# Step 2: Connect your local repo to GitHub
git remote add origin https://github.com/YOUR_USERNAME/git-practice-sdet.git

# Step 3: Push main branch
git push -u origin main

# Step 4: Verify
git remote -v
# Should show: origin  https://github.com/YOUR_USERNAME/git-practice-sdet.git
```

---

### Exercise 4.1 — Create and Push a Feature Branch (5 min)

```bash
# Step 1: Create a new branch for a feature
git switch main
git switch -c feature/add-checkout-tests

# Step 2: Add a new test file
# Create 04_pull_requests/checkout_tests.py (already exists in this folder)
# Add a comment with your name and today's date at the top

# Step 3: Commit it
git add 04_pull_requests/checkout_tests.py
git commit -m "test: add checkout flow test cases"

# Step 4: Push to GitHub
git push -u origin feature/add-checkout-tests
# After this, check GitHub — you'll see the branch there!
```

---

### Exercise 4.2 — Open a Pull Request on GitHub (10 min)

**Do this in your browser:**

1. Go to your GitHub repo
2. You'll see a yellow banner: **"feature/add-checkout-tests had recent pushes"**  
   → Click **"Compare & pull request"**
3. Fill in the PR form:
   - **Title:** `test: add checkout flow test suite`
   - **Description:** Use the template below ↓
4. Set **base:** `main` ← **compare:** `feature/add-checkout-tests`
5. Click **"Create Pull Request"**

**📋 PR Description Template (use this every time!):**
```markdown
## What does this PR do?
Adds test cases for the checkout flow covering happy path, out-of-stock, and coupon scenarios.

## Test Cases Added
- [ ] test_checkout_happy_path
- [ ] test_checkout_out_of_stock
- [ ] test_apply_coupon_code

## How to test locally
1. Run: pytest 04_pull_requests/checkout_tests.py
2. All 3 tests should pass

## Related Issue
Closes #12  (or: N/A)
```

---

### Exercise 4.3 — Review Someone Else's PR (10 min)

**Option A:** Swap GitHub usernames with a friend and review each other's PRs.  
**Option B (solo practice):** Review your OWN PR using the GitHub UI.

**What to look for in test code reviews:**

| Check | Question |
|-------|----------|
| Test naming | Is `test_checkout_happy_path` descriptive? |
| Assertions | Is there at least one `assert` per test? |
| Test data | Is test data hardcoded? Should it be in a fixture? |
| Edge cases | Are negative/edge cases covered? |
| Dependencies | Does the test have external dependencies (real DB, real API)? |
| DRY | Is code duplicated across test methods? |

**How to leave a review on GitHub:**
1. Go to the PR → click **"Files changed"** tab
2. Hover over a line → click the **+** button to add a comment
3. Write a comment like: `"Consider using a pytest fixture for the test user data"`
4. Click **"Start a review"**
5. When done → **"Finish your review"** → choose: **Comment / Approve / Request Changes**

---

### Exercise 4.4 — Address PR Feedback (5 min)

**After someone requests changes:**

```bash
# You're still on the same feature branch
git switch feature/add-checkout-tests

# Make the requested changes
# e.g., add a pytest fixture for test data

# Commit the fix
git add 04_pull_requests/checkout_tests.py
git commit -m "refactor: use pytest fixture for checkout test data"

# Push — this automatically updates the SAME open PR!
git push
# The PR on GitHub will show the new commit
```

**Key Point:** You don't need to open a new PR. Every `git push` to the same branch updates the open PR.

---

### Exercise 4.5 — Merge the PR (GitHub UI) (5 min)

1. On GitHub, go to your PR
2. If there are no conflicts and approvals are met:
3. Click **"Merge pull request"** dropdown — you'll see 3 options:

| Option | What it does | When to use |
|--------|-------------|-------------|
| **Create a merge commit** | Preserves all commits + adds merge commit | Default — full history |
| **Squash and merge** | Squashes all PR commits to 1 | Messy branch, clean main |
| **Rebase and merge** | Replays commits linearly on main | Want linear history |

4. For this exercise, choose **"Squash and merge"**
5. Click **"Confirm squash and merge"**
6. Click **"Delete branch"** (cleanup!)

```bash
# Update your local main
git switch main
git pull
git log --oneline
# You should see the squashed commit!

# Delete local branch too
git branch -d feature/add-checkout-tests
```

---

### Exercise 4.6 — Protect the Main Branch (GitHub Settings) (5 min)

> As an SDET, you should ADVOCATE for branch protection — it prevents direct commits to `main`.

1. Go to GitHub repo → **Settings** → **Branches**
2. Click **"Add rule"** (or "Add branch protection rule")
3. Branch name pattern: `main`
4. Enable:
   - ✅ **Require a pull request before merging**
   - ✅ **Require approvals** (set to 1)
   - ✅ **Require status checks to pass** (if CI is set up)
   - ✅ **Do not allow bypassing the above settings**
5. Click **"Save changes"**

**Test it:** Try to push directly to main — you should get rejected!

```bash
git switch main
# Make a change
echo "# test" >> README.md
git add .
git commit -m "test direct push (should fail)"
git push
# ERROR: remote: error: GH006: Protected branch update failed...
```

---

### Exercise 4.7 — PR from Fork (Open Source Workflow) (10 min)

This is how you contribute to open source projects you don't own.

```bash
# Step 1: Fork a repo on GitHub (click "Fork" button on any public repo)
# E.g., fork: https://github.com/psf/requests

# Step 2: Clone YOUR fork
git clone https://github.com/YOUR_USERNAME/requests.git
cd requests

# Step 3: Add the ORIGINAL repo as 'upstream'
git remote add upstream https://github.com/psf/requests.git

# Step 4: Create a branch, make changes, push to YOUR fork
git switch -c fix/typo-in-docs
# make changes
git push -u origin fix/typo-in-docs

# Step 5: On GitHub, open PR from YOUR fork → ORIGINAL repo
# This is the standard open source contribution flow!

# Step 6: Keep your fork in sync with upstream
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

---

## 🧠 PR Best Practices for SDETs

```
✅ DO:
  - Keep PRs small and focused (< 400 lines changed)
  - Write a clear PR description with test cases covered
  - Link to the related JIRA/ticket
  - Make sure CI passes before requesting review
  - Respond to review comments within 24 hours

❌ DON'T:
  - Commit directly to main
  - Open PRs with commented-out test code
  - Merge your own PRs without review (unless solo project)
  - Leave PRs open for more than 2-3 days
  - Push credentials, test passwords, or API keys
```

---

**➡️ Next:** Open `05_advanced_topics/EXERCISES.md`
