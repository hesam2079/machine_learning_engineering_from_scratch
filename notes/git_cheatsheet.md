# Complete Git Guide for ML Engineers
**Quick, Practical, and Team-Focused**

---

## Table of Contents
1. [Mental Model](#1-mental-model)
2. [Initial Setup](#2-initial-setup)
3. [Starting a Project & .gitignore](#3-starting-a-project--gitignore)
4. [Daily Workflow](#4-daily-workflow)
5. [Branching](#5-branching)
6. [Collaboration (Remote & GitHub)](#6-collaboration-remote--github)
7. [Merge Conflicts](#7-merge-conflicts)
8. [Undo Operations](#8-undo-operations)
9. [Reverting to Previous Versions](#9-reverting-to-previous-versions)
10. [ML-Specific Tips](#10-ml-specific-tips)
11. [Quick Cheat Sheet](#11-quick-cheat-sheet)

---

## 1. Mental Model

Before commands, understand what Git does. Git has three main spaces:

1. **Working Directory:** The folder you're working in (VS Code/PyCharm)
2. **Staging Area:** A waiting list. Files you want to save go here first (like a shopping cart)
3. **Repository:** Where changes are officially saved (committed) and history is created

**Golden Formula:**
```
Changes in files → Add to staging → Commit
```

---

## 2. Initial Setup

Tell Git who you are (one-time setup):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 3. Starting a Project & .gitignore

**Critical for ML:** We have large files (datasets), trained models (.h5, .pth), and virtual environments (venv). These **should NOT** be tracked by Git.

### Create .gitignore

Create a file named `.gitignore` (with the dot) in your project root:

```text
# Python virtual environments
venv/
env/
.venv/

# Large datasets and models (Git is bad with binary files)
data/
models/
*.h5
*.pth
*.pt
*.onnx

# System and editor files
__pycache__/
.ipynb_checkpoints/
.DS_Store
.vscode/

# Logs
logs/
*.log
```

### Initialize Project

```bash
# 1. Initialize Git repository in current folder
git init

# 2. Connect to remote (e.g., GitHub) - if repo already exists
git remote add origin <URL_REPOSITORY>
```

---

## 4. Daily Workflow

These commands cover 90% of your daily work.

### Check Status (Always start here!)

```bash
git status
```
*Shows what files changed, what's staged, and what's ignored.*

### Add to Staging

```bash
# Add all changes (be careful not to add datasets!)
git add .

# Or add specific files (safer)
git add main.py utils.py
```

### Commit

```bash
git commit -m "feat: add data preprocessing logic"
```
*Tip: Use prefixes like `feat:`, `fix:`, `docs:` to keep history clean.*

---

## 5. Branching

Working with a friend on an ML project? You work on **Model Architecture**, they work on **Data Augmentation**. Never code directly on `main`!

### Create and Switch Branch

```bash
# Create new branch and switch to it (combined)
git checkout -b feature/new-model
# (Or in newer Git versions: git switch -c feature/new-model)
```

### List Branches

```bash
git branch
```

### Merge

When your feature is done and you want to merge it back to `main`:

1. Switch to main: `git checkout main`
2. Merge your branch: `git merge feature/new-model`

---

## 6. Collaboration (Remote & GitHub)

You code and see each other's work on GitHub.

### Push (Upload)

```bash
# Upload current branch to remote (first time)
git push -u origin feature/new-model

# Subsequent times:
git push
```

### Pull (Download)

Before starting to code, **always** check if your friend made changes:

```bash
git pull origin main
```

---

## 7. Merge Conflicts

When you and your friend **change the same line** in the same file, Git gets confused and says "I don't know which is correct". This is a **Conflict**.

When `git pull` or `git merge` gives you a conflict error:

1. Open the file. You'll see something like:
```python
<<<<<<< HEAD
learning_rate = 0.01  # Your code
=======
learning_rate = 0.001 # Friend's code
>>>>>>> branch-name
```

2. **Fix manually:** Delete the wrong code, keep the correct code, and remove the `<<<<` and `====` lines.

3. **Commit:**
```bash
git add .
git commit -m "resolve merge conflict"
```

---

## 8. Undo Operations

Everyone makes mistakes. Don't panic.

### Scenario 1: Changed file but haven't `add`ed yet (restore to previous state)

```bash
git restore filename.py
# (Or in older versions: git checkout -- filename.py)
```

### Scenario 2: `add`ed but haven't `commit`ed (remove from staging)

```bash
git restore --staged filename.py
```

### Scenario 3: `commit`ed but haven't `push`ed (changed my mind)

- **Soft reset:** Remove commit but keep changes in staging (can edit again):
```bash
git reset --soft HEAD~1
```

- **Hard reset (dangerous):** Discard everything and go back to previous commit:
```bash
git reset --hard HEAD~1
```

### Scenario 4: `push`ed and mistake is on the server!

Don't use `reset`! Use `revert` (creates a new commit that undoes the previous one):

```bash
git revert <commit-hash>
```

---

## 9. Reverting to Previous Versions

### Find Available Versions

```bash
git log
```

Output:
```
commit a1b2c3d4e5f6... (HEAD -> main, origin/main)
Author: Ali <ali@example.com>
Date:   Mon Oct 19 10:30:00 2026

    feat: add dropout layer

commit f6e5d4c3b2a1...
Author: Ali <ali@example.com>
Date:   Sun Oct 18 15:20:00 2026

    fix: data loader bug
```

**Note:** The long string like `a1b2c3d4...` is the **Commit Hash**. Usually 7-8 characters are enough (e.g., `a1b2c3d`).

### Shorter Versions:

```bash
# One line per commit (cleaner)
git log --oneline

# Only last 5
git log -5 --oneline
```

Output:
```
a1b2c3d feat: add dropout layer
f6e5d4c fix: data loader bug
9a8b7c6 feat: initial model
```

---

### Three Methods to "Go Back"

#### Method A: Just Want to Look (No History Change)

Want to see or test old code without messing up current branch.

```bash
git checkout <commit-hash>
```

Example:
```bash
git checkout f6e5d4c
```

**What happens?** Git goes to that version, but you're in "detached HEAD" state (not on any branch). You can view code, run it, even commit (to a new branch).

**To return to normal:**
```bash
git checkout main
```

✅ **When to use:** For testing, debugging, or viewing old code without risk.

---

#### Method B: Move Current Branch Backward (Dangerous!)

Want to **completely delete** later commits and move branch back to that point.

```bash
# Changes stay in Staging (can edit again)
git reset --soft <commit-hash>

# Changes stay in Working Directory (but removed from Staging)
git reset --mixed <commit-hash>  # Default

# Discard everything and go back to that version (dangerous!)
git reset --hard <commit-hash>
```

Example:
```bash
git reset --hard f6e5d4c
```

**What happens?** All commits after `f6e5d4c` are **deleted** and `main` branch goes back to that point.

⚠️ **Warning:** If you've `push`ed these commits to GitHub, **don't** use `reset`! It corrupts history and confuses the team.

✅ **When to use:** Only when commits **haven't been pushed yet** and you want to undo mistakes.

---

#### Method C: Undo a Specific Commit (Safe & Professional)

Want to "revert" an old commit but keep the rest of history intact.

```bash
git revert <commit-hash>
```

Example:
```bash
git revert a1b2c3d
```

**What happens?** Git creates a **new commit** that **reverses** the work of commit `a1b2c3d`. History stays intact and the team can see what happened.

✅ **When to use:** When commits **have been pushed** and you want to undo a change without corrupting history.

---

### Quick Comparison Table

| Scenario | Command | History Changes? | Safe for Push? |
| :--- | :--- | :---: | :---: |
| Just looking | `git checkout <hash>` | ❌ No | ✅ Yes |
| Delete recent commits (before push) | `git reset --hard <hash>` | ✅ Yes | ❌ Dangerous |
| Undo a commit (after push) | `git revert <hash>` | ❌ No (new commit added) | ✅ Yes |

---

### Practical Example

Assume you have this history:
```
a1b2c3d feat: add dropout layer        (HEAD -> main)
f6e5d4c fix: data loader bug
9a8b7c6 feat: initial model
```

#### Scenario 1: Want to see code before dropout
```bash
git checkout f6e5d4c
# View code, test it
git checkout main  # Return to normal
```

#### Scenario 2: Dropout was wrong, want to delete it (haven't pushed yet)
```bash
git reset --hard f6e5d4c
# Now history is:
# f6e5d4c fix: data loader bug (HEAD -> main)
# 9a8b7c6 feat: initial model
```

#### Scenario 3: Pushed dropout and now want to revert it
```bash
git revert a1b2c3d
# New commit is created:
# x9y8z7w Revert "feat: add dropout layer"  (HEAD -> main)
# a1b2c3d feat: add dropout layer
# f6e5d4c fix: data loader bug
```

---

### Golden Tip: You Don't Need to Remember Hashes!

Whenever you want to go back to an old version:
1. Run `git log --oneline`
2. Find the commit you want
3. Copy its hash
4. Run the appropriate command

Git **always** keeps history (unless you `reset`), so don't worry about losing commits.

---

### ⚠️ Important Warning for Team Projects

If working with friends on a project:
- **Never** use `git reset --hard` on commits you've `push`ed
- Use `git revert` instead
- If you must `reset`, tell the team to run `git pull --rebase`

---

### 🎁 Bonus: Return to Last Commit (If You Messed Up)

If you ran `reset` and regret it, Git keeps a log of everything you've done:

```bash
git reflog
```

Output:
```
a1b2c3d HEAD@{0}: reset: moving to f6e5d4c
f6e5d4c HEAD@{1}: commit: feat: add dropout layer
9a8b7c6 HEAD@{2}: commit: fix: data loader bug
```

You can go back to the state before `reset`:
```bash
git reset --hard a1b2c3d
```

This is the **most lifesaving** Git command! When everything is broken, `reflog` saves you.

---

## 10. ML-Specific Tips

### 1. Large Files (Git LFS)

Git is built for code (text), not large binary files (like 500MB models). If you commit models, the repository will explode and cloning it will take your friend hours.

- **Solution:** Use **Git LFS** (Large File Storage) or keep models in Google Drive/S3 and put download links in a `download_models.sh` file.

### 2. Jupyter Notebooks (.ipynb)

Notebooks are a nightmare for Git (they save outputs and metadata, causing conflicts).

- **Solution:** Before committing, run `Kernel > Restart & Clear Output` in the notebook.
- **Or:** Use a tool like `nbstripout` that automatically clears outputs before commit.

### 3. Clean History

Try to make small, logical commits.
- ❌ Bad: "fix", "update", "wip"
- ✅ Good: "fix: bug in data loader", "feat: add dropout layer"

---

## 11. Quick Cheat Sheet

| Command | Meaning | When to Use |
| :--- | :--- | :--- |
| `git status` | What's the status? | **Always!** (100 times a day) |
| `git add .` | Add everything to cart | When sure changes are good |
| `git commit -m "msg"` | Seal the package | End of a task or feature |
| `git push` | Send to server | End of work day or feature |
| `git pull` | Get others' changes | **Every morning** before coding |
| `git checkout -b name` | Create parallel world | Start a new feature |
| `git merge name` | Merge parallel worlds | When feature is done |
| `git log --oneline` | See history | Find commits to revert to |
| `git revert <hash>` | Undo a pushed commit | Safe way to go back |
| `git reset --hard <hash>` | Delete commits | Only before push |
| `git reflog` | See all actions | When everything is broken |

---

## 🚀 Practice Exercise (Right Now)

1. Create a folder, run `git init`
2. Create `.gitignore` and add `venv/`
3. Create a `test.py` file
4. `add` and `commit`
5. Create a `dev` branch, change the file, commit
6. Go back to `main` and `merge`

Done! You now know how to work with Git. You'll learn the rest as you go.

---

**Summary:** `git log` to find, `checkout` to look, `reset` to delete (before push), `revert` to undo (after push), `reflog` to save your life.
