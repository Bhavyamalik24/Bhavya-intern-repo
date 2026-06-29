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
