# AI Tools for Development - Reflection

## AI Tools I Have Used

### 1. GitHub Copilot
- **What it is:** An AI coding assistant built into VS Code that suggests
  code completions, entire functions, and even generates code from comments
  as you type.
- **How I used it:** Used it for code suggestions while working in VS Code.
  It predicts what you are trying to write and offers completions in grey
  text that you can accept with Tab.

### 2. ChatGPT
- **What it is:** A conversational AI assistant by OpenAI that can answer
  coding questions, explain concepts, debug code, and generate code snippets
  across any programming language.
- **How I used it:** Used it to understand new concepts, ask coding questions,
  and get explanations of error messages in plain English.

### 3. Claude AI
- **What it is:** An AI assistant by Anthropic, similar to ChatGPT but with
  a strong focus on accuracy, safety, and detailed explanations. Particularly
  useful for longer, more complex tasks.
- **How I used it:** Used it extensively throughout my onboarding at Focus
  Bear — for understanding new concepts, writing documentation, and getting
  guidance on tasks. Also used it to help structure and draft markdown
  reflection files throughout my onboarding milestones.

---

## Experiments

### Generating code snippets
I asked both ChatGPT and Claude to generate simple Python snippets for
data manipulation tasks. The output was generally accurate and well
structured, but required review and testing before use. AI is good at
generating boilerplate and starting points but should not be trusted
blindly, the logic needs to be verified.

### Debugging a simple problem
I described an error message to ChatGPT and asked what it meant. It
explained the cause clearly and suggested a fix. This was faster than
searching Stack Overflow for the same answer. However, for more complex
bugs that depend on the specific codebase, AI is less reliable because
it lacks the full context.

### Learning a new concept
I asked Claude to explain how PostgreSQL queries work and how PostHog
event tracking is structured. The explanations were clear, well structured,
and included examples. This is where AI genuinely shines, explaining
concepts in plain English with examples tailored to your level.

---

## Reflection

### What worked well?
- **Explaining concepts:** All three tools are excellent at breaking down
  unfamiliar concepts in plain English. Much faster than reading documentation
  from scratch.
- **Generating starting points:** AI is great at giving you a first draft
  of code or a structure to build from — saving time on boilerplate.
- **Debugging error messages:** Pasting an error message into ChatGPT or
  Claude and getting an instant plain-English explanation is very efficient.
- **Documentation and writing:** Claude in particular is very strong at
  helping structure written content clearly and professionally.

### What didn't work well?
- **Codebase-specific questions:** AI cannot see your actual codebase so
  it makes assumptions that may not match your specific setup. Always verify.
- **Hallucinations:** All AI tools can confidently produce incorrect
  information. I learned to always cross-check AI output against official
  documentation, especially for version-specific syntax.
- **Over-reliance risk:** It is easy to copy-paste AI output without truly
  understanding it. I made a rule for myself — if I cannot explain what the
  code does, I do not use it.

### When is AI most useful for coding?

| Situation | Best AI tool to use |
|---|---|
| Quick code suggestions while typing | GitHub Copilot |
| Explaining an error message | ChatGPT or Claude |
| Learning a new concept | Claude |
| Generating a boilerplate template | ChatGPT or Copilot |
| Writing documentation or reflections | Claude |
| Sensitive or confidential code | None — ask a colleague |

### Key takeaway
AI tools are most useful as a **starting point and learning aid**, not as
a replacement for understanding. The best workflow is: use AI to get
unstuck or generate a first draft, then read, understand, test, and
edit everything before using it. Taking full responsibility for AI-assisted
output is non-negotiable — "the AI wrote it" is never a valid excuse for
errors or privacy issues.
