# PR Description Templates for SDET Teams
# =========================================
# Copy these templates when opening pull requests on GitHub.

## 📋 Template 1: New Test Suite

```markdown
## 📝 What does this PR do?
<!-- One sentence describing the change -->

## 🧪 Test Cases Added / Modified
- [ ] test_name_1 — what it covers
- [ ] test_name_2 — what it covers
- [ ] test_name_3 — what it covers

## 🔗 Related Issue
Closes #<issue-number>

## ✅ How to verify locally
```bash
pytest <path/to/tests.py> -v
```
Expected: All X tests pass.

## 📊 Test Run Screenshot
<!-- Paste a screenshot of the local test run here -->

## ⚠️ Notes for Reviewer
<!-- Anything unusual the reviewer should know -->
```

---

## 📋 Template 2: Bug Fix in Test

```markdown
## 🐛 What bug is fixed?
<!-- Describe the broken behavior -->

## 🔍 Root Cause
<!-- Why was the test failing? -->

## 🔧 Fix Applied
<!-- What change was made to fix it? -->

## 🔗 Related Issue
Fixes #<issue-number>

## ✅ Before / After
| | Before | After |
|--|--------|-------|
| Test status | ❌ FAIL | ✅ PASS |
| Error message | `AssertionError: ...` | N/A |
```

---

## 📋 Template 3: Refactor / Cleanup

```markdown
## ♻️ What was refactored?
<!-- Describe what changed structurally (not new tests, just cleanup) -->

## 💡 Why?
<!-- DRY, performance, readability, etc. -->

## ✅ No behavior change — tests still pass
```bash
pytest -v --tb=short
```
All X tests pass. No new failures.

## 🔗 Related Issue
Relates to #<issue-number>
```
