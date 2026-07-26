<div align="center">

  <img
    src="docs/assets/softbreak-logo.png"
    alt="Softbreak"
    width="170"
  />

  <h1>STAR AI Engineering Workflow</h1>

  <p>
    <strong>Do not lose engineering control while coding with AI.</strong>
  </p>

  <p>
    Ready-to-use project instructions that guide Cursor, Claude Code, GitHub Copilot,
    Codex, and similar AI tools to explain the problem, expose critical decisions,
    compare alternatives, identify failure modes, and record engineering decisions
    before directly generating code.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Workflow-STAR-F97316" alt="STAR Workflow" />
    <img src="https://img.shields.io/badge/Cursor-Supported-111827" alt="Cursor Supported" />
    <img src="https://img.shields.io/badge/Claude_Code-Supported-D97757" alt="Claude Code Supported" />
    <img src="https://img.shields.io/badge/GitHub_Copilot-Supported-24292F" alt="GitHub Copilot Supported" />
    <img src="https://img.shields.io/badge/Codex-Supported-10A37F" alt="Codex Supported" />
    <img src="https://img.shields.io/badge/Language-TR%20%7C%20EN-2563EB" alt="Turkish and English" />
  </p>

  <p>
    <a href="README.md">Türkçe</a>
    ·
    <a href="README.en.md"><strong>English</strong></a>
  </p>

  <p>
    <a href="#-quick-start">🚀 Quick Start</a>
    ·
    <a href="#️-how-it-works">⚙️ How It Works</a>
    ·
    <a href="#-example-engineering-handoff">📄 Example Output</a>
    ·
    <a href="#-the-four-engineering-questions">🧭 Four Questions</a>
  </p>

</div>

---

<details>
<summary><strong>What does STAR AI Engineering Workflow do?</strong></summary>

<br />

This workflow encourages the following behavior during AI-assisted development:

- Reframes the request as a problem before turning it into a coding task.
- Exposes missing acceptance criteria and hidden assumptions.
- Does not silently invent product or architectural decisions that belong to the user.
- Compares viable alternatives and their costs.
- Makes failure modes and the test plan visible before coding.
- Produces changes in small, explainable steps.
- Records decisions in a `STAR-HANDOFF.md` file after implementation.

</details>

## Why Does This Repository Exist?

We often give AI tools a request like this:

```text
Add a password reset feature to this project.
```

AI can produce a working solution in seconds. But while doing so, it may silently make many decisions:

- How will the token be generated?
- Where and in what form will it be stored?
- How long will it remain valid?
- Can it be reused?
- What happens when the user does not exist?
- What happens when multiple requests arrive at the same time?
- Which tests will be written?
- Which security and operational costs will be accepted?

Working code does not mean you own these decisions.

This repository exists to reduce invisible engineering decisions made on your behalf and keep you inside the decision-making process.

> **The goal is not to slow AI down. The goal is to preserve engineering responsibility while moving fast.**

## Before and After

| Without STAR | With STAR |
|---|---|
| The request is translated directly into code. | The request is first reframed as a problem. |
| Missing requirements are silently completed by AI. | Missing decisions are made visible to the user. |
| The first working solution is accepted. | Alternatives and trade-offs are compared. |
| Failure modes are discovered after implementation. | Failure modes and tests are planned before coding. |
| Decisions disappear inside chat history. | Decisions are recorded in a persistent engineering handoff. |
| The developer struggles to explain the code. | The developer receives implementation-specific questions they must be able to defend. |

## 🚀 Quick Start

### 1. Choose Your Tool

| Tool | Source file | Target location in your project |
|---|---|---|
| Cursor | `rules/cursor/star-engineering.mdc` | `.cursor/rules/star-engineering.mdc` |
| Claude Code | `rules/claude-code/CLAUDE.md` | `CLAUDE.md` |
| GitHub Copilot | `rules/github-copilot/copilot-instructions.md` | `.github/copilot-instructions.md` |
| Codex | `rules/codex/AGENTS.md` | `AGENTS.md` |
| Other tools | `rules/universal/STAR-WORKFLOW.md` | Project instructions or persistent context |

### 2. Add the Rule File to Your Project

Example: if you use Cursor, copy

```text
star-ai-engineering-workflow/
└── rules/
    └── cursor/
        └── star-engineering.mdc
```

into your own project:

```text
my-project/
└── .cursor/
    └── rules/
        └── star-engineering.mdc
```

> If your project already contains `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, or a similar instruction file, do not delete the existing content. Merge the STAR rules carefully with project-specific instructions.

### 3. Write Your Normal Request

```text
Add a password reset feature to this project.
```

Instead of immediately generating code, the AI should respond with something similar to:

```text
Problem we are trying to solve:

Allow users to securely set a new password through email without
knowing their current password.

Decisions that need clarification:

- How long should the reset token remain valid?
- Should the token be single-use?
- What response should be returned when the user does not exist?
- Can a new request be created while an active token already exists?

Viable approaches:

1. Store a hashed token in the database
2. Use a signed stateless token

I will not start implementation until these decisions are clarified.
```

### 4. Make the Decisions and Continue

You clarify the decisions that AI cannot safely make without knowing the product requirements.

The code is then produced through:

- small steps,
- explainable changes,
- visible assumptions,
- and predefined test scenarios.

### 5. Receive the Engineering Handoff

At the end of the work, a file such as this is created:

```text
docs/features/password-reset/STAR-HANDOFF.md
```

The file records not only **what** changed, but **why**.

## ⚙️ How It Works

The STAR engineering workflow has three phases.

### 1. Before Coding

The AI:

1. Reframes the request as a problem.
2. Identifies missing acceptance criteria.
3. Exposes decisions that should not be made without the user.
4. Compares viable alternatives.
5. Explains the benefits and costs of its recommendation.
6. Identifies likely failure modes.
7. Lists the required tests before implementation.

### 2. During Coding

The AI:

- makes small and explainable changes,
- does not hide assumptions,
- does not silently expand the scope,
- does not invent product decisions that belong to the user,
- explains not only what changed, but why.

### 3. After Coding

The AI:

1. Summarizes the changes.
2. Records the selected approach and its rationale.
3. Lists alternatives considered.
4. Records failure modes and known limitations.
5. Lists tests added and tests still missing.
6. Keeps open decisions visible.
7. Generates questions the developer must be able to defend.
8. Creates `STAR-HANDOFF.md`.

## 📄 Example Engineering Handoff

```markdown
# Password Reset — Engineering Handoff

## Problem Solved

Allow users to securely set a new password through email without
knowing their current password.

## Acceptance Criteria

- A valid user can request a reset link.
- The same generic response is returned even when the user does not exist.
- The token can be used only once.
- Expired tokens are rejected.
- The previous password becomes invalid after a successful reset.

## Selected Approach

A single-use reset token stored as a hash in the database.

## Why This Approach Was Selected

It allows individual token revocation, usage tracking, and prevention
of token reuse.

## Alternative Considered

A signed stateless token.

### Benefit

Token verification does not require a database query.

### Why It Was Not Selected

Individual revocation, reuse prevention, and usage tracking are harder.

## Decision Cost

- Token generation and verification require database access.
- Expired token records require a cleanup strategy.
- Consistency rules for parallel requests must be defined explicitly.

## Where Can It Break?

- The same token is used twice.
- The same user sends parallel reset requests.
- The email service fails.
- The token expires during the operation.
- The database transaction is interrupted.

## Tests Added

- A valid token changes the password.
- An expired token is rejected.
- A used token cannot be reused.
- A missing user is not disclosed.

## Tests Still Missing

- Parallel token usage
- Email service failure
- Creating a new request while an active token exists

## Known Limitations

Rate limiting has not been implemented yet.

## Questions You Must Be Able to Defend

- Why is the token stored as a hash rather than plaintext?
- Why was the stateless approach not selected?
- Why is user existence hidden?
- How are parallel requests handled?
- Under which condition should this decision change?
```

## 🧭 The Four Engineering Questions

This workflow is centered on four questions.

### 1. Why was this code written this way?

Can you explain the reasoning behind the structure and behavior?

### 2. Could another solution have been used?

Do you know at least one viable alternative and the trade-offs between the two approaches?

### 3. Where can this solution break?

Can you predict what happens with unexpected input, larger data, concurrent operations, or failing dependencies?

### 4. Can you defend this decision to another engineer?

Can you explain not only what the decision is, but why it is acceptable now and under which conditions it should change?

> Working code does not mean these questions have been answered.

## When Should It Be Used?

Use the full STAR workflow for changes such as:

- New features
- Business rule changes
- Public API contracts
- Data model changes
- External service integrations
- Authentication and authorization
- Architectural changes
- Security decisions
- Meaningful multi-file refactoring
- Persistent technical decisions

## When Should It Not Be Used?

Not every small task needs a long decision process.

The following tasks can usually be completed directly:

- Typo correction
- Local variable renaming
- Documentation updates
- Formatting
- Behavior-preserving mechanical changes
- Small bug fixes with explicit expected behavior

However, use STAR when a small-looking change affects security, data, system behavior, or an external contract.

## Templates

| Template | Purpose |
|---|---|
| `FEATURE-BRIEF.md` | Defines the problem, scope, acceptance criteria, and open decisions before coding. |
| `STAR-HANDOFF.md` | Records decisions, risks, evidence, and limitations after implementation. |
| `DECISION-RECORD.md` | Records persistent or costly-to-reverse technical decisions. |
| `PULL-REQUEST.md` | Helps explain not only what changed, but why. |

## Repository Structure

```text
star-ai-engineering-workflow/
│
├── README.md
├── README.en.md
│
├── rules/
│   ├── cursor/
│   │   └── star-engineering.mdc
│   ├── claude-code/
│   │   └── CLAUDE.md
│   ├── github-copilot/
│   │   └── copilot-instructions.md
│   ├── codex/
│   │   └── AGENTS.md
│   └── universal/
│       └── STAR-WORKFLOW.md
│
├── templates/
│   ├── FEATURE-BRIEF.md
│   ├── STAR-HANDOFF.md
│   ├── DECISION-RECORD.md
│   └── PULL-REQUEST.md
│
├── examples/
│   └── password-reset/
│       ├── request.md
│       └── completed-handoff.md
│
└── docs/
    └── assets/
        └── softbreak-logo.png
```

## What This Repository Is Not

This repository is not:

- a prompt collection,
- an automatic code review tool,
- a security scanner,
- a code quality guarantee,
- a mandatory architecture,
- a Clean Architecture template,
- a system that makes every AI answer correct,
- a replacement for a mentor or experienced engineering review.

The rules can make questions and decisions visible.

They cannot always determine whether your answer is actually correct.

## The Boundary of STAR

This repository is not the complete STAR methodology.

It is the workflow layer that makes decisions visible during AI-assisted development.

### Free Workflow

- Reduces invisible AI assumptions.
- Encourages the right questions.
- Records decisions.
- Supports developer self-assessment.

### Supervised Engineering Development

- Challenges whether the answer is actually correct.
- Finds hidden reasoning errors.
- Opens production work to real code review.
- Requires rebuilding after feedback.
- Tracks development over time.
- Creates external accountability.

> A rule file can help you ask questions.  
> Engineering development requires your answers to be reviewed.

## Core Principle

AI can produce code.

But the following still require engineering judgment:

- defining the right problem,
- identifying missing decisions,
- comparing alternatives,
- recognizing incorrect output,
- predicting failure modes,
- opening code to review,
- owning the consequences of a decision.

> **This repository does not give you a new project. It gives you an engineering workflow for working more consciously with AI inside your own project.**

## Contributing

Open an issue to report a problem, suggest an example, propose a tool integration, or improve a rule.

Contribution guidelines will be linked here after `CONTRIBUTING.md` is added.

## License

A license file will be added before the repository becomes public.

---

<div align="center">

  <p>
    <strong>Softbreak STAR</strong>
  </p>

  <p>
    Not a course; a supervised engineering development system.
  </p>

</div>
