---
last-updated: 2026-08-11
difficulty: beginner
---

# Claude Certified Associate - Foundations (CCAO-F) - Practice Questions

15 questions for the CCAO-F exam, weighted toward output evaluation and validation (21%), workflow integration and solution design (16%), governance, risk, and responsible use (15%), prompting and task execution (14%), product and model selection (12%), configuration and knowledge management (12%), and troubleshooting and optimization (10%).

> **Cert page:** [exams/anthropic/claude-certified-associate-foundations/](../../exams/anthropic/claude-certified-associate-foundations/)

---

### Question 1
**Scenario:** Claude produces a fluent, confident summary containing several statistics and two named source reports. A consultant asks how much she can trust it.

A. Fluency is not accuracy: statistics, quotes, and citations are the high-risk elements and must be verified against real sources before external use
B. Trust it if the summary is internally consistent
C. Claude never invents sources, so only the statistics need checking
D. Confident, well-structured output indicates the facts are correct

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Claude can state false claims and cite non-existent reports with complete fluency. Names, numbers, quotes, and citations are the falsifiable "checkables" that verification targets first. Internal consistency and polish tell you nothing about factual accuracy.
</details>

---

### Question 2
**Scenario:** A team debates how thoroughly to verify Claude outputs: one member wants every output fully fact-checked, another wants no checking at all.

A. Checking is only needed for outputs longer than a page
B. Never check; that defeats the time savings
C. Scale verification to stakes: skim a private brainstorm, spot-check an internal summary, fully verify a client deliverable, and require expert human review for legal, financial, or people decisions
D. Fact-check everything, always

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Proportionality is the tested principle, and it cuts both ways: under-verifying a client deliverable is a risk failure, and audit-grade review of a throwaway brainstorm is a cost failure. Risk level, not length, drives the depth of review.
</details>

---

### Question 3
**Scenario:** An analyst wants Claude's answers about an uploaded contract to be reliably grounded in the document.

A. Instruct Claude to answer only from the document, say so when the answer is not in it, and quote the supporting passage for each claim - then spot-check the quotes against the source
B. Ask Claude to be extra careful
C. Upload the contract twice for emphasis
D. Ask Claude to review its own answer, which counts as verification

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Grounding plus required citations creates a fast audit trail; a quoted passage that is not actually in the document flags the output immediately. Self-review is a useful first filter but shares the model's blind spots, so it never substitutes for checking against the source.
</details>

---

### Question 4
**Scenario:** A delivery lead is deciding which step of a proposal workflow Claude should own.

A. Claude should only be used for spell-checking
B. Claude should do the whole workflow end to end, including final approval
C. Alternate authorship randomly between Claude and the team
D. Pick the language-shaped steps (drafting, summarizing, tailoring boilerplate) for Claude, keep pricing and final approval with humans, and define an explicit review gate before anything leaves the team

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Good solution design is surgical: Claude accelerates the drafting-shaped steps while accountable decisions and external release keep a human checkpoint. "Claude drafts, human approves" is the default pattern for deliverables.
</details>

---

### Question 5
**Scenario:** An operations manager pilots a Claude-assisted reporting workflow and wants to know if it is working before rolling it out to 30 people.

A. Baseline the current process, pilot with a few users, measure time per report and edits needed per draft, fix the setup, then expand
B. Roll out immediately; measurement can come later
C. Compare against a different team doing different work
D. Ask the pilot users if it "feels faster"

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** The rollout pattern the exam rewards is pilot, measure against a baseline with named metrics, improve, then expand. Feelings and mismatched comparisons cannot show whether the workflow actually saves time or maintains quality.
</details>

---

### Question 6
**Scenario:** Team members keep copy-pasting Slack threads into Claude to get discussion summaries and draft replies.

A. Keep copy-pasting; it works
B. This friction signals an integration fit: Claude in Slack brings the capability to where the conversation already lives
C. Print the threads and retype them
D. Ban Slack

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** When the work and its context live in another tool and copy-paste is the recurring friction, an integration is the designed solution. Workflow design includes choosing the surface where Claude meets the work, not just the prompt.
</details>

---

### Question 7
**Scenario:** A consultant with a personal Claude Pro account and access to her firm's Enterprise workspace needs to analyze a client's confidential financials.

A. Use whichever is open in her browser
B. Use the personal account but delete the chat afterward
C. Use the personal account; the underlying model is the same
D. Use the firm's Enterprise workspace, confirm the engagement permits AI processing, and share only the portions of the data the analysis needs

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Client-confidential data belongs in the organization's governed workspace under commercial terms, subject to the engagement's rules, and minimized to what the task requires. Identical model quality is irrelevant; the difference is data terms and governance, and after-the-fact deletion does not repair using the wrong workspace.
</details>

---

### Question 8
**Scenario:** Claude refuses a request that a manager believes is legitimate.

A. File a bug report; refusals are always errors
B. Claim the request is fiction to bypass the refusal
C. Rephrase deceptively or split the task into innocent-looking pieces until it complies
D. If the intent was misread, restate the genuine purpose and context honestly; if the task truly crosses a policy line, accept the refusal and use the proper channel

<details>
<summary>Answer</summary>

**Correct: D**

**Why:** Honest clarification resolves most misunderstanding-refusals, and that is fine. Deceptive rephrasing, task-splitting, and fake framing are policy violations even when the underlying goal is legitimate - and a refusal of a genuinely prohibited task is the system working correctly.
</details>

---

### Question 9
**Scenario:** A consultant's prompt "write a proposal for the client" produced generic boilerplate.

A. Add "be creative and specific" to the prompt
B. Regenerate until something better appears
C. Rebuild the prompt with the missing information: audience, scope, win themes, format and length constraints, and a past successful proposal as an example
D. Switch to the most capable model with the same prompt

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Generic output is the signature of a context-free prompt. Role, task, context, constraints, format, and an example of what good looks like supply the information specificity requires. Regeneration re-rolls the same gap, and a stronger model just writes more eloquent boilerplate.
</details>

---

### Question 10
**Scenario:** A project lead needs Claude to produce a complete 20-page strategy document.

A. Ask for the document 20 times and pick the best
B. One giant prompt requesting all 20 pages at once
C. Work stepwise: agree an outline first, draft section by section with review between steps, then run a final consistency pass
D. Large documents are impossible with Claude

<details>
<summary>Answer</summary>

**Correct: C**

**Why:** Decomposing big tasks with human checkpoints between steps produces better structure and lets you steer early, which is cheaper than repairing a monolithic draft. This is the core task-execution pattern for substantial deliverables.
</details>

---

### Question 11
**Scenario:** A manager must handle two jobs: a one-time deep analysis of a dense 90-page regulatory filing for the board, and 2-line summaries of 300 short routine meeting notes.

A. Most capable model tier for the deep analysis where quality dominates; fastest and cheapest tier for the high-volume simple summaries
B. The most capable model for both
C. The fastest model for both
D. Model choice never affects outcome

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Tier matching is the tested skill: step up from the balanced default when quality dominates a hard one-off task, step down when volume and speed dominate simple tasks. Flagship-for-everything and cheapest-for-everything are both standard distractors.
</details>

---

### Question 12
**Scenario:** A team on client work is choosing between individual Free accounts and a Team plan.

A. Free accounts; the models answer the same questions
B. A Team plan: commercial data terms, shared Projects, and collaboration are the point when business use involves client data
C. Plans differ only in usage limits
D. Personal Pro accounts with reimbursement

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Plan selection is a governance choice as much as a feature choice. Client work needs the commercial terms and shared, admin-manageable workspace that business plans provide; personal accounts for business data is the recurring wrong answer.
</details>

---

### Question 13
**Scenario:** A user retypes the same role, tone rules, and report template into every new chat for a weekly workstream.

A. Promote the durable context into a Project: standing rules into project instructions, the template and exemplary reports into project knowledge, leaving only the week's inputs for each chat
B. Make the chats longer instead
C. Keep retyping; repetition improves results
D. Put the template into account-wide personal preferences so it applies to every chat, including unrelated ones

<details>
<summary>Answer</summary>

**Correct: A**

**Why:** Anything repeatedly retyped belongs in configuration at the right scope: workstream rules in project instructions, reference material in project knowledge. Account-wide preferences are the wrong scope; they drag workstream-specific rules into every unrelated chat.
</details>

---

### Question 14
**Scenario:** A shared Project's answers started citing outdated prices for every team member after a price change.

A. Delete the Project
B. Curate the Project's knowledge: remove the stale rate card, upload the current one, and re-test
C. Switch the team to a more capable model
D. Everyone adds "use the new prices" to each prompt

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** A failure that hits every user of a Project regardless of prompt phrasing is a configuration problem, and stale knowledge files are the classic cause. Curation at the root fixes it permanently; per-prompt patches fight the configuration forever, and model capability cannot correct wrong reference data.
</details>

---

### Question 15
**Scenario:** After two weeks in one very long chat with several re-scopes and abandoned drafts, Claude keeps mixing old draft content into new sections.

A. Complain in the chat about the mistakes
B. Ask Claude to summarize the agreed decisions and constraints, verify the summary, and continue in a fresh chat seeded with it - promoting durable context into a Project if the work continues
C. Continue in the same chat and hope it self-corrects
D. Start blank and rebuild all context from memory every session

<details>
<summary>Answer</summary>

**Correct: B**

**Why:** Long conversations accumulate contradictions and superseded drafts that degrade attention. The standard reset is distill, verify, restart warm; a Project holds the durable context for ongoing work. Complaints add tokens without removing the contaminated history, and a blank restart throws away signal along with noise.
</details>
