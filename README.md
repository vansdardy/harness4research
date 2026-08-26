# Building a Harness for Research Purposes

The intent of this project is to leverage AI tools to accelerate the research process relevant to quantum computing, computer science, and mathematics.

Harness is a construct designed to orchestrate agentic AI and their corresponding LLMs to complete a task in an orderly fashion.

The workflow of this harness is going to use the design of [System A (IMProofBench ProofCouncil)](https://github.com/1stproof/batch-2/tree/274625a22e4748d5f9264ba3614353461520bd20/batch-2-submissions/improofbench) from [1st Proof Second Batch submission](https://1stproof.org/second-batch.html).

## The Workflow

We will propose two different workflows, one based on leveraging coding agents like Claude Code and Codex through its CLI (meaning that a human would be copying and pasting prompts into CLIs), the other one will be developed along the way where a Python script directly calling API endpoints perform the entire research process.

### Through the CLI

This workflow will involve `MAX_ROUNDS` of rounds, where `MAX_ROUNDS` is defined in `config.py`.

Starting Round 0, similar to the process in that of aforementioned System A, an `Author` agent will be prompted to read the problem and start working on the problem. After this round, the `Author` agent will pass on the current progress to a `Critic` agent where the current progress will be checked for correctness and completeness.

In each round, a new `Author` agent and a new `Critic` agent will be invoked to prevent context contamination.

From Round 1 to Round `MAX_ROUNDS`, for each round, the `Author` agent has ONE opportunity to ask a `Council` agent questions for assistance. **To maximize the capability of LLMs, a different model will be used for the `Council` agent than the `Author` agent.** This implies that a human will physically copy-paste the question asked by the `Author` agent and feed it to the `Council` agent through prompting. This further results in the fact that `Council`'s answer will be given to the `Author` in the same round (unlike IMProofBench's design). To ensure the `Council` agent understands the scope of the question, relevant documents will be provided to the agent.

In the last round, which is Round `MAX_ROUNDS + 1`, the `Author` will not be able to further ask questions and must write up an answer (if the problem is solved) or a progress report (if the problem remains unsolved), which will be checked by a `Critic` agent one last time for correctness and completeness.
This completes the workflow.

Additionally, we borrow the design from System A, where the core files will remain `answer.md`, `research_notes.md`, `references/`, `references.md`, and `problem.md`, throughout this workflow for agents to access and check against. A `sandbox/` folder is also provided for `Author`'s use to write Python scripts for mathematical calculation. Note that the agent must activate `venv`.

### Through API

(To be designed)

## Choice of Model

Among all submissions for 1st Proof Second Batch, we see the "contestants" almost all used ChatGPT-5.5-Pro as their main model.

From [the report published by 1st Proof](https://1stproof.org/assets/docs/report.pdf), and comparing the logs generated along the way for System A and System B, we have made a preliminary conclusion that the model capability is a stronger indicator than the actual workflow design. We can see that System B and System C produced similar performance even when their workflows are designed completely differently (System B - a complete harness, System C - one-shot prompt), while System A outperformed System B. One particular outperformance is in Problem 5, where System A's Council system (introducing other models) had produced a correct solving direction (specifically, it was Opus-4.7 who proposed the correct idea). We treat this as an indication that multi-model collaboration with the best models involved can produce unexpected "breakthroughs".

Therefore, for this project, we will attempt to use the current best models available on the market: ***GPT-5.6-Sol*** and ***Fable-5***, though we may switch to more cost-efficient models like ***Opus-5*** and ***GPT-5.6-Luna*** if the best models are out of budget.

As of right now, there is no restriction on our side stating that the agents mentioned must use a specific model. The only "restriction" in place is we should use different models for `Author` agents and `Council` agents.