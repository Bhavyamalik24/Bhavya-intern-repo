# Git Merge Conflicts - Understanding & Resolution

## What is a Merge Conflict?
A merge conflict happens when two branches have made different changes to the
same part of the same file, and Git cannot automatically decide which version
to keep. Git stops the merge and asks the developer to manually resolve the
conflict before continuing.

---

## How I Created a Merge Conflict

### Step 1: Created a new branch
Created a branch called `test-conflict` from main in my GitHub repo.

### Step 2: Edited a file on the branch
Edited `README.md` on the `test-conflict` branch by adding a line:

    ### This line was added on the test-conflict branch

Committed the change to the `test-conflict` branch.

### Step 3: Edited the same file on main
Switched back to the `main` branch and edited the same line in `README.md`
with different content:

    # Bhavya-intern-repo

Committed that change to main.

### Step 4: Created a Pull Request
Created a pull request on GitHub to merge `test-conflict` into `main`.
GitHub detected that both branches had conflicting changes to the same
part of `README.md` and flagged it with:

> "This branch has conflicts that must be resolved"

### Step 5: Resolved the conflict
Clicked "Resolve conflicts" in GitHub's web editor. The conflict appeared
in the file like this:

    <<<<<<< main
    # Bhavya-intern-repo
    =======
    ### This line was added on the test-conflict branch
    >>>>>>> test-conflict

- Everything between <<<<<<< main and ======= was the main branch version
- Everything between ======= and >>>>>>> test-conflict was the branch version
- I kept the main branch version and deleted the conflict markers
- Clicked "Mark as resolved" → "Commit merge" → "Merge pull request"

### Step 6: Deleted the branch
After merging, deleted the `test-conflict` branch to keep the repo clean.

---

## What I Learned

### What caused the conflict?
The conflict was caused by editing the same line in the same file on two
different branches. When Git tried to merge them, it had no way of knowing
which version was correct — so it flagged it for manual review. This would
happen in a real team when two developers work on the same file at the same
time without coordinating.

### How did I resolve it?
I used GitHub's built-in web conflict editor to view both versions side by
side. I chose to keep the main branch version as it was the most recent
intentional change, then removed the conflict markers and committed the
resolution.

### Key takeaways
- Merge conflicts are normal and not something to be afraid of
- They happen when two branches edit the same part of the same file
- Always read both versions carefully before deciding which to keep —
  sometimes you need to combine parts of both rather than choosing one
- Good communication in a team reduces conflicts — if two people know
  they are working on the same file, they can coordinate to avoid this
- Deleting branches after merging keeps the repo clean and organised
- In a real project, I would discuss with my teammate before overwriting
  their changes

# 🔀 Git Concepts: Staging vs Committing

## 🔍 Research Summary

### What is Staging?
Staging is the process of telling Git which changes you want to include in
your next commit. When you modify a file, Git sees it as "modified" but does
not automatically include it in the next commit. You have to explicitly stage
it using `git add <file>` or the equivalent in your Git client.

Think of staging as putting items into a box before sealing it. You can
add and remove items from the box as many times as you want before you
finally seal it (commit).

### What is Committing?
Committing is the process of permanently saving the staged changes as a
snapshot in the Git history. Once committed, that snapshot is part of the
repo's history and can always be referred back to. A commit is like sealing
the box and labelling it with a description of what's inside.

---

## 🧪 Experiment

### Step 1: Modified a file
Modified an existing file in my repo by adding a new line of text.
Running `git status` showed:

    Changes not staged for commit:
        modified: README.md

This means Git detected the change but it is not yet staged.

### Step 2: Staged the file
Ran `git add README.md` (or used VS Code's Source Control panel to
stage the file by clicking the + icon next to it).
Running `git status` now showed:

    Changes to be committed:
        modified: README.md

The file is now in the staging area — ready to be committed but not
yet saved to history.

### Step 3: Unstaged the file
Ran `git reset HEAD README.md` to remove the file from the staging area
without losing the changes.
Running `git status` showed the file back as "modified but not staged" —
the changes were still there, just no longer queued for commit.

### Step 4: Committed the file
Staged the file again with `git add README.md` then committed with:

    git commit -m "Update README with new line"

Running `git status` showed:

    nothing to commit, working tree clean

The changes are now permanently saved in the Git history.

---

## Reflection

### What is the difference between staging and committing?

| | Staging | Committing |
|---|---|---|
| What it does | Marks changes to include in next commit | Permanently saves staged changes to history |
| Reversible? | Yes — easy to unstage | Yes but more complex to undo |
| Git command | `git add <file>` | `git commit -m "message"` |
| Analogy | Putting items in a box | Sealing and labelling the box |

### Why does Git separate these two steps?
Git separates staging and committing to give developers precise control
over what goes into each commit. Without a staging area, every modified
file would automatically be included in the next commit — which is often
not what you want.

For example, imagine you are fixing a bug and accidentally modify two
files — one related to the bug fix and one you were just experimenting with.
The staging area lets you add only the bug fix file to the commit and leave
the experimental file out. This keeps your commit history clean, focused,
and meaningful.

### When would you want to stage without committing?
- When you have changed multiple files but only want to commit some of them
- When you want to review exactly what will be committed before finalising
- When you are grouping related changes together before committing them
  as one logical unit
- When you want to pause mid-task, stage what is done, and continue working
  before making the final commit
- When collaborating — staging lets you prepare a clean, focused commit
  that is easy for teammates to review

### Key takeaway
The staging area is one of Git's most powerful features because it gives
you a buffer between making changes and saving them permanently. It
encourages thoughtful, well-organised commits rather than messy snapshots
of half-finished work. Good commits tell a clear story of what changed
and why — and the staging area is what makes that possible.

---
# Branching & Team Collaboration

## Experiment Recap
I created a branch (`test-conflict`), made a change to README.md, committed
it, then switched back to `main`. The change was not visible on `main` —
confirming that branches are isolated copies of the code until they are
explicitly merged back in.

---

## Reflection

### Why is pushing directly to main problematic?
`main` is usually the live, production-ready version of the code — the
version that real users or the rest of the team depend on. Pushing directly
to it is risky because:
- There is no review step, so mistakes or bugs go live immediately
- Other team members may be relying on `main` being stable, and an
  unreviewed change could break their work
- There is no opportunity to catch issues before they affect everyone
- It removes accountability and visibility — nobody else gets to see what
  changed before it's already live

Working on a separate branch creates a safe space to experiment and make
mistakes without affecting the shared, stable codebase.

### How do branches help with reviewing code?
Branches allow a developer to make changes in isolation, then open a Pull
Request when the work is ready. This gives teammates the chance to:
- Review the actual code changes line by line before they go live
- Leave comments or request changes
- Run automated tests against the new code before merging
- Catch bugs, security issues, or style inconsistencies early

This turns coding from a solo, risky activity into a collaborative,
quality-controlled process. It also creates a clear history of what changed,
who changed it, and why — which is valuable for debugging issues later.

### What happens if two people edit the same file on different branches?
If two people edit *different* parts of the same file on different branches,
Git can usually merge both changes automatically without any issue.

However, if both people edit the *same lines* of the same file, Git cannot
automatically decide which version is correct — this creates a merge
conflict, exactly like the one I created and resolved earlier in my onboarding.
Git flags it and requires a human to manually choose which version to keep
(or combine them). This is exactly why communication within a team matters —
if two people know they are both about to touch the same file, they can
coordinate to avoid unnecessary conflicts.

### Key takeaway
Branches exist to protect the stability of `main` while still allowing
multiple people to work simultaneously without stepping on each other's
toes. The combination of branching, pull requests, and code review is what
makes collaborative software development possible at scale — without it,
every change would be a gamble.

---
# Advanced Git Commands & When to Use Them

## Commands Tested

### `git log`
**What it does:** Shows the commit history of the repo — each commit's hash,
author, date, and message. Running `git log --oneline` gives a compact,
one-line-per-commit view.

**What I observed:** Running this in my repo showed a clear list of my
recent commits with short messages, giving a quick overview of what had
changed and when.

**When to use it in a real project:** Essential for understanding the
history of a project, tracking down when a bug was introduced, or reviewing
what a teammate changed before a specific date. In long-running projects with
multiple developers, `git log` is often the first command used to understand
context before making any change.

---

### `git blame <file>`
**What it does:** Shows, line by line, who last modified each line of a
file and in which commit.

**What I observed:** Running `git blame README.md` showed each line
annotated with my commit hash and details, since I have been the only
contributor so far.

**When to use it in a real project:** Extremely useful in a team setting
when you find a bug or confusing piece of code and want to know who wrote
it and why — so you can ask them directly or understand the context of
the original commit message.

---

### `git checkout main -- <file>`
**What it does:** Restores a specific file back to its state on `main`,
discarding local uncommitted changes to that file only — without affecting
any other files you may have changed.

**What I observed:** I added a test line to `README.md`, ran `git status`
to confirm it was modified, then ran `git checkout main -- README.md`.
The test line was removed and the file reverted back to the clean main
version, while any other unrelated changes remained untouched.

**When to use it in a real project:** Useful when you've made unwanted
or experimental changes to one file and want to discard just that file
without losing other work in progress. Much safer than discarding all
changes at once.

---

### `git cherry-pick <commit>`
**What it does:** Applies one specific commit from another branch onto
your current branch, without merging the entire branch and all its other
commits.

**Why I didn't test this hands-on:** Cherry-picking requires a commit to
exist on a separate branch first, and testing it solo adds complexity without
much additional learning value beyond understanding the concept.

**When to use it in a real project:** Very useful in long-running projects
with multiple developers — for example, if a critical bug fix was committed
on a feature branch that isn't ready to be merged yet, cherry-pick lets you
pull just that fix onto `main` immediately without bringing in unfinished
work from the rest of the branch.

---

## Reflection

### What surprised me while testing these commands?
I was surprised by how precise Git's commands are — each one solves a very
specific, narrow problem rather than being a general-purpose tool. `git
checkout -- file` only touches one file, `git blame` only shows attribution,
and `git log` only shows history. This made me realise Git is designed to
give developers fine-grained control rather than blunt, all-or-nothing actions.

I was also surprised that `git blame` doesn't just show the most recent
editor — it tracks line-level history, meaning even a single line edited
months apart from the rest of the file would show its own separate commit
and author. This level of detail would be incredibly useful for understanding
the evolution of a complex file in a real team project.

### Why these commands matter in long-running, multi-developer projects
In a project with many contributors over a long period, these commands
become essential for accountability and debugging:
- `git log` helps you understand the story of the project
- `git blame` helps you find who to ask about a confusing piece of code
- `git checkout -- file` lets you safely undo mistakes without losing
  unrelated work
- `git cherry-pick` lets you move urgent fixes between branches without
  disrupting larger, unfinished work

Together, these commands give developers precision and confidence when
working in complex, shared codebases — rather than relying on broad,
risky actions like deleting and starting over.