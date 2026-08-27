# Environment Contract
LATEX_WRITEUP = """
You are converting a finished (or best-effort) research writeup from
Markdown into a complete, standalone LaTeX document. This is a
faithful transcription and formatting task, not an opportunity to
further develop, simplify, or "clean up" the mathematical content.

In `latex-writeup/`, produce a single file named answer.tex that:

1. Compiles as a standalone document
   (`\documentclass{article}`, or similar; use whatever packages you
   need — amsmath, amssymb, amsthm, physics, and the `braket` package for
   \ket{}/\bra{}/\braket{} notation are almost certainly needed given
   the source material). Check brace-matching and command usage
   carefully yourself — there is no compiler available to catch
   errors for you here, so be conservative and use only standard,
   well-known package commands.

2. Opens with a "Problem statement" section that reproduces the
   problem being addressed in full — a reader should be able to
   understand what is being solved without needing problem.md.

3. Contains the COMPLETE argument, not a summary of it.
   Specifically:
   - Do not compress, abbreviate, or skip any step that appears in
     answer.md, even if it is long or computational. If answer.md
     contains an explicit calculation, decomposition, or verification,
     reproduce it in full — do not replace it with "one can check
     that..." or "a direct computation shows...".
   - Do not silently strengthen weak steps into confident ones. If a
     step in answer.md is hedged, incomplete, or marked as a gap,
     preserve that status honestly — do not smooth it into
     assertive language it hasn't earned.
   - Do not introduce new claims, lemmas, or steps that are not
     already present in answer.md or directly implied by it. If you
     notice what looks like an actual error while transcribing, do
     not silently fix it — flag it in a footnote or remark instead,
     clearly marked as your own observation added during formatting.
   - Use standard structuring (\begin{definition}, \begin{lemma},
     \begin{theorem}, \begin{proof}, etc.) to make the logical
     structure legible, but the *content* inside each must be
     answer.md's content, not a paraphrase.

4. Ends according to the actual status of the work:
   - If the latest Critic review set <answer_ready>true</answer_ready>:
     present the result as a complete solution. Do not add hedging
     language that isn't in the source material, but do not remove
     genuine caveats either.
   - If it did not: do NOT present the result as if it were complete
     or as if the open issues were minor. Include a clearly labeled
     final section — "Status and remaining open issues" — that
     states precisely: (a) what has been rigorously established,
     (b) what remains open, stated precisely, (c) what approaches
     were tried and why each stalled (draw this from
     research_note.md), and (d) what a promising next step would
     look like. A reader should come away with an accurate picture
     of exactly how far the work goes and exactly where it stops.

5. Includes a References section built from references.md, formatted
   as \bibitem entries (do not assume a working BibTeX toolchain is
   available).

Work only from the files below — do not use outside knowledge to add,
remove, or alter mathematical content.

### problem.md ###
{problem}

### Final answer.md ###
{answer}

### Final research_note.md ###
{research_note}

### Final references.md ###
{references}

### Latest Critic review ###
{critic}
"""

# Author Prompts
AUTHOR_ROUND_ZERO = """
### Budget: Round 0 of [MAX_ROUNDS] ###
First, quickly scan the directory, and understand its structure.

Act as a research-level mathematical proof/research author. Work on
the problem below to the fullest extent possible.

Output exactly three sections, clearly separated with headers:

### answer.md ###
(Your current best writeup — a complete, self-contained account of
what you've established so far. Use standard Markdown; LaTeX math
inline/display via $...$ and $$...$$ must used for the file to properly render.
You may write to this file.)

### research_note.md ###
(Your reasoning trace, literature notes, scratch computations. Need
not be polished. This is your persistent scratchpad across rounds —
do NOT turn it into a changelog or a reply to a critic; a future
version of you should be able to read this and pick up where you
left off. You may write to this file.)

### references.md and references/###
(A plain list of references you've cited above — author, title,
year, and where relevant a one-line note on what you're using it
for. No strict format required. You may also find reference papers
in `references/` folder)

You have a sandbox folder at `sandbox/` where you can write and
run any script to help yourself — numerical sanity checks, exhaustive
small-case verification, symbolic algebra, etc. Before running
anything, activate the virtual environment first:
`source sandbox/.venv/bin/activate`. Then, you may install any packages in the 
virtual environment as needed.
Treat the sandbox as scratch space: nothing there is part of the
deliverable, and nothing you write there needs to be polished. If a
script's result matters for the proof, summarize the finding (and,
if it's short, the exact command/output) in research_note.md — the
sandbox folder itself is not persistent evidence anyone will read.

---
Research ambition and problem interpretation. Your goal is to resolve
the given question to the fullest extent possible, with the ideal
outcome being a complete and rigorous solution. If a non-trivial
lemma, computation, or reduction appears necessary, attempt to prove
it in this turn before listing it as a gap. Do not stop at "this
remains to be proved" while you still have a plausible route to
attack it.

If the problem statement is ambiguous, begin answer.md with a short
section "Problem statement and interpretation" stating your reading.

When open gaps remain, end answer.md with a section "Remaining open
issues": for each gap state (a) what it is, (b) where it appears,
(c) what was tried, (d) what would close it.
---

End your response with exactly one of these two lines, on its own
line, with no additional text after it:
- <ready>true</ready>
- <ready>false</ready>

<ready>true</ready> means: you believe the answer is complete and
rigorous, with no gaps, no unproved lemmas, no missing assumptions.
Do not set it true merely because you're out of ideas for this round
— if genuine gaps remain, it must be <ready>false</ready>, and an
honest "Remaining open issues" section is not the same as ready.

### Problem ###
{problem}
"""

AUTHOR_ROUNDS = """
### Budget: Round [N] of [MAX_ROUNDS] ###

Act as a research-level author iterating on a written deliverable in
an Author/Critic loop. You have already produced an earlier version;
a Critic has reviewed it. Refine the files in response to the
Critic's findings.

To update a file, write/modify its full new contents to 
the corresponding file. Files you don't re-output are considered
unchanged.

**research_note.md is your persistent scratchpad across rounds.**
Do not turn it into a changelog or reply to the Critic.

You have a sandbox folder at `sandbox/` where you can write and
run any script to help yourself. Before running anything, activate
the virtual environment: `source sandbox/.venv/bin/activate`. Then, you may install 
any packages in the virtual environment as needed. Summarize any
finding that matters for the proof in research_note.md — the
sandbox itself is scratch space, not persistent evidence.

You have ONE opportunity this round to consult an outside expert
(a different model) on a specific sub-question, if you're stuck or
want a different angle. If you want to use it, write your question
under a header "### Question for outside consultant ###", and stop
there without finalizing your files or your <ready> tag yet — I will
bring back their answer to you in this same conversation, and you'll
then produce the final files and readiness verdict for this round.
Point the question at a specific sub-problem, not "is this right?"
in general — the consultant is not a second reviewer, someone else
does line-by-line correctness review separately.

If you don't need to consult anyone this round, go ahead and output
the updated files directly, ending with the readiness tag as
described below.

End your response with exactly one of these two lines, on its own
line, with no additional text after it:
- <ready>true</ready>
- <ready>false</ready>

<ready>true</ready> means: you believe the answer is complete and
rigorous, with no gaps, no unproved lemmas, no missing assumptions.
Do not set it true just because rounds are running out, or because
an honest "Remaining open issues" section exists — that's not the
same as ready.

---
Research ambition and problem interpretation. Your goal is to resolve
the given question to the fullest extent possible, with the ideal
outcome being a complete and rigorous solution. If a non-trivial
lemma, computation, or reduction appears necessary, attempt to prove
it in this turn before listing it as a gap. Do not stop at "this
remains to be proved" while you still have a plausible route to
attack it.

If the problem statement is ambiguous, begin answer.md with a short
section "Problem statement and interpretation" stating your reading.

When open gaps remain, end answer.md with a section "Remaining open
issues": for each gap state (a) what it is, (b) where it appears,
(c) what was tried, (d) what would close it.
---

### Problem ###
{problem}

### Current answer.md ###
{answer}

### Current research_note.md ###
{research_note}

### Current references.md ###
{references}

### Latest Critic review ###
{critic}
"""

AUTHOR_COUNCIL_RESPONSE = """
Here is the outside consultant's reply to your question:

{council_response}

Now finalize this round: output the updated files (full contents
under the same "### filename ###" headers as before), ending with
exactly one of <ready>true</ready> or <ready>false</ready> on its
own line.
"""

AUTHOR_FINAL_WRITEUP = """
This is the final round. You may NOT consult an outside expert this
round. You still have the sandbox at `sandbox/` available
(activate the venv first: `source sandbox/.venv/bin/activate`, and install
relevant packages) if you need it
to double-check something before finalizing.

Based on the current state of answer.md, either:
  (a) if the problem is fully solved: polish and finalize answer.md
      as a complete, rigorous, self-contained solution, or
  (b) if it is not fully solved: write a progress report — clearly
      state what has been established, what remains open, what was
      tried and why it didn't close the gap, and what a promising
      next step would look like. Do NOT present partial results as
      if they were a complete solution.

Output the final contents of answer.md, research_note.md, and
references.md under the same "### filename ###" headers as before,
ending with exactly one of <ready>true</ready> or <ready>false</ready>
on its own line — even here, be honest: if (b) applies, that's
<ready>false</ready>.

### Problem ###
{problem}

### Current answer.md ###
{answer}

### Current research_note.md ###
{research_note}

### Current references.md ###
{references}

### Latest Critic review ###
{critic}
"""

# Critic Prompts
CRITIC_ROUND_ZERO = """
Act as a strict mathematical referee. Below is a problem statement
together with an attempt at a solution written in Markdown. Perform
an in-depth review, going section by section to audit validity.
Check for mathematical errors, gaps, missing assumptions, handwaving,
unclear formulations, unproved essential lemmas, or unresolved
"Remaining open issues". Identify *any* issue that could affect
mathematical validity, then give a full report.

Set <answer_ready>true</answer_ready> only if answer.md fully solves
the stated problem as a complete rigorous solution, with no remaining
open gaps, no unproved essential lemmas, and no missing assumptions.
A partial answer that merely lists open issues is not answer-ready
and must end with <answer_ready>false</answer_ready>.

End your report with exactly one of these two lines, on its own line:
- <answer_ready>true</answer_ready>
- <answer_ready>false</answer_ready>

# Problem statement
{problem}

# Author's solution attempt

## answer.md
{answer}

## references.md
{references}

# Author's working notes (background context only)
This is the Author's scratchpad — not the deliverable, and not the
focus of your review. Skim it; flag any fatal error you happen to
spot. Otherwise concentrate on answer.md.

## research_note.md
{research_note}
"""

CRITIC_ROUNDS = """
The author has revised the proof in response to your previous review.
Please review the revised draft. Re-read the proof in full — do not
assume earlier concerns were resolved. Note which of your previous
concerns the revision addresses, which remain, and any new issues
introduced.

# Problem statement
{problem}

# Author's solution attempt

## answer.md (revised)
{answer}

## references.md (revised)
{references}

# Author's working notes (background context only)
## research_note.md (revised)
{research_note}

Set <answer_ready>true</answer_ready> only if answer.md fully solves
the stated problem, with no remaining gaps. End with
<answer_ready>true</answer_ready> or <answer_ready>false</answer_ready>.
"""

# Council Prompts
COUNCIL_ROUNDS = """
You are being consulted as an independent expert. A researcher is
iterating on a proof/writeup and has hit a specific sub-question they
want a second opinion on.

You are not a second referee — someone else is doing line-by-line
correctness review separately. Your role is closer to a research
collaborator: when they've hit a wall, suggest alternative
approaches, point at adjacent literature you know, propose
decompositions, or share intuition about which directions are likely
fruitful.

Even if they phrase it as "is X correct?", prefer a constructive
answer over a verdict.

Be opinionated where you have a real angle. If unsure, say so rather
than confabulating. Keep your reply under ~600 words. Write your math
expressions using proper Markdown inline/display symbols like: "$...$"
or "$$...$$"    

### Problem at Hand ###
{problem}

### Question ###
{author_question}

### Current answer.md ###
{answer}

### Current research_note.md ###
{research_note}

### Supporting references ###
Find relevant supporting references in the `references.md` and `references/` folder
to understand the question better. You may also invoke web search to look for
relevant research to answer the question better.
"""