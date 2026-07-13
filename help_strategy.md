# When to Use Google, AI Tools, or Ask for Help?

## Decision-Making Framework

![Help Strategy Decision Flowchart](help-strategy-flowchart.png)

The flowchart above outlines the decision process for choosing between
Google, AI tools, and asking a colleague when stuck on a problem.

### Framework Summary

1. **Does it involve confidential or sensitive data?**
   - YES → Ask a colleague only. Never enter sensitive or proprietary
     data into AI tools or search engines.

2. **Is it a syntax error, concept, or error message?**
   - YES → Google it first. Stack Overflow, official documentation, and
     community forums are the most reliable sources for well-known issues.

3. **Do I need code explained or generated quickly?**
   - YES → Use AI (ChatGPT or Claude). AI is excellent at explaining
     unfamiliar code, generating boilerplate, and debugging with context.

4. **Have I been stuck for 20+ minutes with no progress?**
   - YES → Ask a colleague. Time spent stuck alone past this point is
     rarely productive.
   - NO → Keep trying, then Google or use AI.

---

## Research Summary: ChatGPT on AI vs Google vs Colleagues

### When AI is most useful
Based on my conversation with ChatGPT, AI tools are most helpful when:
- Debugging with an error message, stack trace, or unexpected output
- Explaining what a function, algorithm, or codebase does
- Designing solutions — choosing data structures, APIs, or approaches
- Writing or refactoring code for better readability
- Learning a new language, framework, or concept
- Creating unit tests, edge cases, or validation logic

AI works best when you provide: the programming language, a relevant
code snippet, the exact error message, what you expected to happen,
and any constraints.

### When Google is better
- Finding official documentation, release notes, or announcements
- Looking up the latest news, current prices, or real-time information
- Finding existing resources like libraries, tools, or community answers
- Any situation where you need to find something that already exists
  rather than generate or understand something

### When to ask a colleague
- The problem depends on internal knowledge — company architecture,
  undocumented systems, or historical design decisions
- You need authority or approval — security, compliance, production
  changes, or cross-team impact
- The issue involves team culture, organizational context, or stakeholder
  relationships that AI cannot understand
- You have been stuck for more than 20 minutes and Google and AI have
  not resolved it

---

## Reflection

### When do I prefer using AI vs searching Google?
I prefer AI when I need something explained or generated — understanding
an unfamiliar concept, debugging an error, or getting a starting point
for code I haven't written before. The conversational format of AI lets
me ask follow-up questions and get answers tailored to my exact context,
which a Google search cannot do.

I prefer Google when I need something that already exists — official
documentation, a specific library, or a community-tested solution on
Stack Overflow. Google is also better for anything time-sensitive or
current, since AI training data has a cutoff date and can be outdated
for rapidly changing tools.

In practice I often use both together — Google to find the relevant
documentation or resource, then AI to explain or implement it.

### How do I decide when to ask a colleague?
I ask a colleague when:
- The problem involves something specific to the Focus Bear codebase
  or internal systems that AI and Google cannot know
- I have genuinely tried to solve it myself (using Google and AI) and
  am still stuck after around 20-30 minutes
- The decision has implications for other people or systems — I should
  not be making those calls alone
- I need a second opinion on an approach before investing more time in it

I always try to come to a colleague with context — what I've already
tried, what I found, and a specific question — rather than arriving
with a vague "I'm stuck." This respects their time and makes the
conversation more productive.

### What challenges do developers face when troubleshooting alone?
- **Tunnel vision:** Getting so focused on one approach that simpler
  solutions become invisible. A fresh pair of eyes — or even explaining
  the problem out loud — often reveals the answer immediately.
- **AI hallucinations:** Trusting AI-generated code without verifying
  it, especially for edge cases or newer APIs the model may not know
  accurately.
- **Time wasted:** Spending hours on something a colleague could clarify
  in minutes, particularly when the answer depends on internal knowledge
  that no external resource has.
- **Over-reliance on AI:** Using AI to generate solutions without
  understanding them, which creates technical debt and makes future
  debugging harder.
- **Imposter syndrome:** Feeling embarrassed to ask for help, leading
  to longer time stuck and more frustration — when asking early is
  almost always the more efficient choice.
