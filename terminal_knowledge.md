# Terminal Setup & Knowledge - Reflection

## Setup Completed

### Terminal Client Chosen
I am using **Windows Terminal with PowerShell** on my Windows laptop.
I chose this combination because:
- Windows Terminal comes pre-installed on Windows 11 and is modern,
  clean, and supports multiple tabs and panes
- PowerShell is the standard shell for Windows environments and is
  widely used in professional IT and development settings
- It integrates well with VS Code — I can open a terminal directly
  inside VS Code using Ctrl + ` without switching windows
- As someone working in a Windows environment, learning PowerShell
  is directly transferable to future IT and data roles

### Customisations Made
- Set PowerShell as the default shell in Windows Terminal
- Adjusted the colour theme to a darker scheme to reduce eye strain
  during long work sessions
- Pinned Windows Terminal to the taskbar for quick access

---

## 📝 Reflection

### Which terminal client did I choose and why?
I chose **Windows Terminal with PowerShell** as my primary terminal setup.
Windows Terminal is Microsoft's modern terminal application that supports
multiple tabs, split panes, and customisable themes — making it much more
usable than the old Command Prompt. PowerShell is more powerful than
Command Prompt and supports scripting, which will be useful as I start
working with data pipelines and automation tasks at Focus Bear.

I also use the **integrated terminal in VS Code** (Ctrl + `) for quick
commands while coding, as it keeps everything in one window.

### What customisations did I make?
- Set the default profile to PowerShell
- Applied a dark colour theme to reduce eye strain
- Increased font size slightly for readability during long sessions
- Pinned the terminal to the taskbar so it is always one click away

### Most useful commands I learned today

| Command | What it does |
|---|---|
| `pwd` | Print working directory — shows where you are |
| `ls` / `dir` | List files and folders in current directory |
| `cd foldername` | Change into a folder |
| `cd ..` | Go up one level to the parent folder |
| `mkdir foldername` | Create a new folder |
| `rm filename` | Delete a file |
| `cat filename` | Display contents of a file |
| `clear` | Clear the terminal screen |
| `git status` | Show current Git status of the repo |
| `git add .` | Stage all changed files for commit |
| `git commit -m "message"` | Commit staged changes with a message |
| `git push` | Push commits to GitHub |

### What was the most useful command I learned?
**`git status`** is the most immediately useful command I learned. Before
making any commit, running `git status` shows exactly which files have been
changed, which are staged, and which are untracked. It gives a clear picture
of the current state of the repo before taking any action — which prevents
mistakes like committing the wrong files or forgetting to stage changes.

A close second is **`cd` and `pwd`** — understanding how to navigate the
file system from the terminal is fundamental to everything else. Before
learning these, I was entirely dependent on clicking through folders in
a file explorer. Being able to navigate via the terminal feels much more
efficient once you get used to it.

### How does the terminal improve my workflow?
The terminal removes the need to click through menus and file explorers
for common tasks. Once I memorise the key commands, actions like navigating
to a folder, running a Python script, or pushing code to GitHub become
much faster than doing the same thing through a GUI. For a data analytics
role where I will be running scripts, managing files, and interacting with
Git regularly, terminal fluency is an essential skill to build early.
