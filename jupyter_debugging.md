# Debugging Techniques for Jupyter Notebooks

## Overview
Debugging in Jupyter Notebooks is different from debugging regular Python
scripts because notebooks have a kernel that persists state across cells,
cells can be run out of order, and variables from deleted cells can still
exist in memory. Understanding the right tool for each situation is
essential for efficient debugging.

---

## 1. Basic Debugging Techniques

### Print and display()
The simplest and most common debugging technique — inserting print
statements or `display()` calls to inspect variable values at different
points in the analysis.

```python
print(df.shape)
print(df.dtypes)
display(df.head())
```

`display()` is preferred over `print()` in notebooks because it renders
DataFrames, charts, and objects in their formatted form rather than as
plain text. Best for quick checks on small, simple issues.

### %xmode — Controlling Traceback Detail
Controls how much detail appears in error tracebacks.

```python
%xmode Plain      # minimal — just the error message
%xmode Context    # default — shows surrounding code context
%xmode Verbose    # maximum — shows all local variables at error point
```

Use `%xmode Verbose` when an error message alone isn't enough to
understand what went wrong — it shows the values of all variables
at the point of failure.

### %debug — Post-Mortem Debugging
After an error occurs, run `%debug` in the next cell to drop into an
interactive debugger at the exact line where the error happened.

```python
# Cell 1 — this throws an error
def divide(a, b):
    return a / b

divide(10, 0)

# Cell 2 — run immediately after the error
%debug
```

Inside the debugger you can type variable names to inspect their values,
`u` to go up the call stack, `d` to go down, and `q` to quit.

### %pdb on — Automatic Post-Mortem
Enables automatic entry into the debugger every time an exception occurs,
without needing to run `%debug` manually after each error.

```python
%pdb on
```

Run once at the top of your notebook. After that, any unhandled exception
automatically drops you into the debugger. Turn it off with `%pdb off`.

### %%debug — Cell-Level Step Debugging
Putting `%%debug` at the top of a cell lets you step through that cell's
code line by line before it runs.

```python
%%debug
x = 10
y = 0
result = x / y
```

Commands: `n` (next line), `s` (step into function), `c` (continue to
end), `q` (quit), `p variable_name` (print variable value).

---

## 2. JupyterLab Visual Debugger

JupyterLab (the newer interface) has a built-in visual debugger accessible
via the bug icon in the top right of a notebook. It provides:

- **Breakpoints in the gutter:** Click the line number to set a breakpoint
  — execution pauses there automatically
- **Variable inspector:** Shows all variables currently in memory with
  their types and values, updated in real time as you step through code
- **Call stack panel:** Shows the full chain of function calls that led
  to the current point, making it easy to trace where a value came from

**How it differs from pdb/ipdb:**
The visual debugger is more intuitive for beginners — you can see all
variables at once without typing commands. However, `pdb` is faster for
experienced developers and works in classic Jupyter Notebook (not just
JupyterLab). For complex debugging sessions the visual debugger is
generally preferred; for quick post-mortem checks, `%debug` is faster.

---

## 3. Performance Debugging

### %time and %timeit
```python
%time df.groupby("membership").mean()        # runs once, shows elapsed time
%timeit df.groupby("membership").mean()      # runs many times, shows average
```

Use `%time` for slow operations you only want to run once (e.g. loading
a large file). Use `%timeit` for comparing the performance of two
approaches to the same problem.

### %prun — Function Profiling
Shows how much time is spent in each function call during execution.

```python
%prun df.groupby("membership")["focus_minutes"].mean()
```

The output ranks functions by total time spent, making it easy to identify
which part of the code is the bottleneck.

### %lprun — Line-by-Line Profiling
Shows time spent on each individual line of a function (requires
`line_profiler` package).

```python
pip install line_profiler
%load_ext line_profiler
%lprun -f my_function my_function(df)
```

More granular than `%prun` — useful when you know which function is slow
but need to pinpoint exactly which line is the bottleneck.

### %memit — Memory Usage
Shows how much memory a cell uses (requires `memory_profiler` package).

```python
pip install memory_profiler
%load_ext memory_profiler
%memit df.merge(other_df, on="user_id")
```

Essential for identifying memory leaks or operations that consume
unexpectedly large amounts of RAM.

---

## 4. Harder Notebook-Specific Issues

### Stale State from Out-of-Order Cell Execution
**Problem:** Running cells out of order can leave variables in unexpected
states — a variable might still hold a value from a previous run of a
cell that has since been modified.

**Solution:**
- Use **Kernel → Restart & Run All** regularly to confirm the notebook
  works from top to bottom in order
- Avoid reusing variable names across different sections of the notebook
- Use `%who` or `%whos` to see all variables currently in memory

### Kernel Hangs
**Problem:** An infinite loop or a very memory-intensive operation can
cause the kernel to become unresponsive.

**Solution:**
- Click the **Stop** button (square icon) to interrupt the kernel
- If that doesn't work, use **Kernel → Restart**
- Use `%timeit` with a small sample of data first before running on the
  full dataset to estimate runtime

### Memory Leaks Across Cells
**Problem:** Large DataFrames or objects loaded in earlier cells continue
consuming memory even after you're done with them.

**Solution:**
```python
del large_dataframe
import gc
gc.collect()
```

Explicitly delete large objects and call the garbage collector to free
memory when working with large datasets.

### Debugging Code Imported from .py Modules
**Problem:** If you import a function from an external `.py` file and
then edit that file, the notebook uses the old cached version until
the kernel is restarted.

**Solution:** Use autoreload at the top of the notebook:
```python
%load_ext autoreload
%autoreload 2
```

This automatically reloads any imported modules whenever their source
files change, without needing to restart the kernel.

To set breakpoints inside external `.py` files, use `ipdb`:
```python
pip install ipdb
import ipdb
ipdb.set_trace()  # add this line inside the .py file where you want to pause
```

---

## 5. Third-Party Debugging Tools

### icecream
A more readable alternative to print debugging — automatically shows
the variable name alongside its value.

```python
pip install icecream
from icecream import ic

x = df.groupby("membership").mean()
ic(x)  # prints: ic| x: <the value>
```

### snoop
Automatically logs every line of a function as it executes, showing
variable changes without needing to add individual print statements.

```python
pip install snoop
import snoop

@snoop
def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average
```

---

## Key Debugging Strategies Summary

| Situation | Best Tool |
|---|---|
| Quick variable inspection | `print()` / `display()` |
| More detail on an error | `%xmode Verbose` |
| Inspect state after an error | `%debug` |
| Auto-debug every error | `%pdb on` |
| Step through code line by line | `%%debug` or JupyterLab debugger |
| Find slow code | `%prun` or `%lprun` |
| Check memory usage | `%memit` |
| Confirm notebook runs top to bottom | Kernel → Restart & Run All |
| Free memory from large objects | `del` + `gc.collect()` |
| Auto-reload edited .py files | `%load_ext autoreload` + `%autoreload 2` |
| Readable print debugging | `icecream` |
| Automatic line-by-line logging | `snoop` |

---

## Reflection

### Most common debugging techniques in notebooks
Print and `display()` are the most used day-to-day — they are fast and
require no setup. For anything more complex, `%debug` post-mortem is the
next step since it drops you directly into the problem without needing
to add and remove print statements. The JupyterLab visual debugger is
the most powerful option for complex issues, particularly when you need
to inspect many variables at once or trace a multi-function call stack.
Tools like `icecream` and `snoop` sit between print debugging and the
full debugger — more informative than print but less setup than pdb.

### Most effective tools for typical notebook workflows
`%xmode Verbose` and `%debug` together cover most debugging needs in a
typical notebook workflow. `%autoreload 2` is essential whenever working
with external `.py` modules — without it, edited code silently fails to
update and causes confusing behaviour. **Kernel → Restart & Run All** is
the most important habit for preventing stale state issues, which are
the most common source of hard-to-explain bugs in notebooks.

### Debugging harder notebook-specific issues
The most insidious notebook bug is hidden state — a variable that exists
in memory from a previous run but is no longer being set by any current
cell. The only reliable fix is restarting the kernel and running all
cells from scratch. Memory leaks are best caught early using `%memit`
before scaling up to large datasets. Kernel hangs almost always come
from infinite loops or operations running on more data than expected —
profiling with `%timeit` on a small sample first prevents most of these.
