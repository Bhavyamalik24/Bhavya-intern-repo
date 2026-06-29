# 🔧 Git Setup & Knowledge - Reflection

## ✅ Setup Completed

### Git Installation
Verified Git is installed by running `git --version` in the terminal.
Git was already available on my system as part of the development environment
setup.

### Git Client Choice
I am using **Git directly through GitHub** (web interface) combined with
**VS Code's built-in Git integration** for local changes. I chose this
combination because:
- The GitHub web interface is straightforward for creating files, branches,
  and pull requests without needing the command line
- VS Code has Git built in so I can stage, commit, and push without leaving
  my code editor
- This setup keeps things simple while I build confidence with Git fundamentals

---

## 📝 Reflection

### Have I used Git before?
Yes, but only at a basic level during university projects. I used Git mainly
to submit assignments — cloning a repo, making changes, and pushing them back.
I had limited understanding of branching, merging, or pull requests at the time.
Everything was done mostly as a solo contributor so I never experienced the
collaborative side of Git.

### Which Git client did I choose and why?
I am primarily using the **GitHub web interface** and **VS Code's integrated
Git tools** rather than a standalone client like GitHub Desktop. My reasoning:
- GitHub's web editor is accessible from any browser without additional setup
- VS Code's Source Control panel shows changes visually and makes committing
  intuitive
- Both tools are widely used in professional environments so learning them
  now is directly transferable

If the codebase becomes more complex, I would consider adding GitHub Desktop
for a more visual branching experience.

### What was the most interesting thing I learned about Git today?

The most interesting thing I learned was how merge conflicts actually work
under the hood. I had always thought of them as something scary and complicated,
but going through the exercise of intentionally creating one and resolving it
showed me that Git is just being transparent — it's saying "I found two
different versions of the same thing and I need a human to decide."

The conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) that appear in the
file are actually very logical once you understand them. They show you exactly
what each branch contributed, and resolving it is simply a matter of deciding
which version (or combination) to keep.

I also found it interesting that Git tracks changes at the line level, not
the file level — which is why two people can edit different parts of the same
file without conflict, but editing the same line causes one.

### Key Git concepts I now understand
- **Branch:** An independent copy of the code where you can make changes
  safely without affecting main
- **Commit:** A saved snapshot of your changes with a description of what
  you did
- **Push:** Sending your local commits to the remote repo on GitHub
- **Pull Request:** A formal request to merge your branch into main,
  allowing for review before changes go live
- **Merge Conflict:** When two branches edit the same part of the same file
  and Git cannot automatically decide which to keep
- **Clone:** Downloading a copy of a remote repo to work on locally
