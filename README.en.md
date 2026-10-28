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
    An Agent Skill for Claude Code, Codex, Cursor, GitHub Copilot, and Gemini CLI.
    It makes the AI ask you about critical decisions before writing code, show where
    the solution can break, and report honestly what was actually verified.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Agent_Skill-star--engineering-F97316" alt="Agent Skill: star-engineering" />
    <img src="https://img.shields.io/badge/Claude_Code-Supported-D97757" alt="Claude Code Supported" />
    <img src="https://img.shields.io/badge/Codex-Supported-10A37F" alt="Codex Supported" />
    <img src="https://img.shields.io/badge/Cursor-Supported-111827" alt="Cursor Supported" />
    <img src="https://img.shields.io/badge/GitHub_Copilot-Supported-24292F" alt="GitHub Copilot Supported" />
    <img src="https://img.shields.io/badge/License-MIT-16A34A" alt="MIT License" />
  </p>

  <p>
    <a href="README.md">Türkçe</a>
    ·
    <a href="README.en.md"><strong>English</strong></a>
  </p>

  <p>
    <a href="https://softbreak.net"><strong>🌐 Website</strong></a>
    ·
    <a href="https://www.youtube.com/@softbreak"><strong>▶ YouTube Channel</strong></a>
  </p>

</div>

---

## Contents

- [What is this?](#what-is-this)
- [Quick start](#-quick-start)
- [Usage](#-usage)
- [Which installation should I choose?](#-which-installation-should-i-choose)
- [How it works](#️-how-it-works)
- [Examples](#-examples)
- [When to use it](#when-to-use-it)
- [What this repository is not](#what-this-repository-is-not)
- [Repository structure](#repository-structure)
- [Contributing](#contributing)
- [License](#license)

## What is this?

Ask an AI to "add a password reset feature" and you get working code in seconds. But along the way, the AI made many decisions for you: How long is the token valid? Can it be reused? What is returned when the user does not exist? What happens when two requests arrive at once?

**Working code does not mean you own these decisions.**

STAR is a workflow that makes the AI put these invisible decisions on the table before it writes code:

| Without STAR | With STAR |
|---|---|
| The request is turned directly into code. | The request is first defined as a problem with acceptance criteria. |
| The AI silently fills in missing requirements. | Decisions that belong to you are asked explicitly. |
| The first working solution is accepted. | Real alternatives and their costs are compared. |
| Failure points are discovered in production. | Failure scenarios and tests are defined before coding. |
| "Tests pass" is claimed, whether or not they ran. | Checks actually run are reported separately from planned ones. |
| Decisions get lost in chat history. | Decisions are written to a durable handoff (`STAR-HANDOFF.md`). |

> **The goal is not to slow AI down. The goal is to keep engineering responsibility while moving fast.**

## 🚀 Quick start

**Requirements:** [Node.js](https://nodejs.org/) 22.20+ and a supported coding agent.

Run this in the root of your own project:

```bash
npx skills add fatihGunalp/star-ai-engineering-workflow --skill star-engineering
```

The installer asks which agents to install it for. That is it.

To install it for a single agent, for all of your projects:

```bash
npx skills add fatihGunalp/star-ai-engineering-workflow --skill star-engineering -g -a claude-code -y
```

> `npx skills` is a third-party, open-source installer ([Skills CLI](https://github.com/vercel-labs/skills)), not an official Anthropic or OpenAI command. Without Node.js, use the [Python installer](docs/skills-quickstart.md#5-python-ile-manuel--bağımlılıksız-alternatif).

## 💬 Usage

Restart your agent after installation and describe the task as usual. For a meaningful change (new feature, API, data model, payments, authentication...), the agent may select the Skill on its own. To invoke it explicitly:

| Agent | Command |
|---|---|
| Claude Code | `/star-engineering Add a password reset feature.` |
| Codex | `$star-engineering Add a password reset feature.` |

Instead of writing code right away, the agent first responds with something like:

```text
Problem: Users who forget their password cannot get back in without contacting support.

Decisions you need to make:
1. How long should the token stay valid?
2. Should a new request invalidate older active tokens?
3. Should all sessions be signed out after a reset?

Recommendation: A single-use token stored as a hash in the database.
Alternative: A signed stateless token — no storage, but it cannot be revoked.

Failure tests: parallel use of the same token, email service failure, expiry.
```

You make the decisions; the code is then written in small steps. When the work is done, the agent reports what was **actually** verified and writes a handoff to `docs/features/<feature>/STAR-HANDOFF.md`.

For small tasks such as fixing a typo, STAR stays out of the way and the agent simply makes the change.

> Automatic selection is the agent's choice and is not guaranteed. Invoke the Skill explicitly when you want to be sure.

## 🧭 Which installation should I choose?

STAR has **a single source**: [`skills/star-engineering/SKILL.md`](skills/star-engineering/SKILL.md). Every other file is generated from it, so the content is the same on every path. The only difference is **when it is loaded**.

| Path | When is it loaded? | For whom? |
|---|---|---|
| **Agent Skill** (recommended) | Only when the task needs it | Claude Code, Codex, Cursor, Copilot, Gemini CLI |
| **Always-on rule file** | On every message, all the time | Tools without Skill support, or teams that want STAR enforced on all work |
| **Universal text** | When you paste it in | Chat apps such as ChatGPT, project instruction fields |

<details>
<summary><strong>Installing an always-on rule file</strong></summary>

<br />

Copy the file for your tool into your project:

| Tool | Source file | Target location in your project |
|---|---|---|
| Claude Code | `rules/claude-code/CLAUDE.md` | `CLAUDE.md` |
| Codex | `rules/codex/AGENTS.md` | `AGENTS.md` |
| Cursor | `rules/cursor/star-engineering.mdc` | `.cursor/rules/star-engineering.mdc` |
| GitHub Copilot | `rules/github-copilot/copilot-instructions.md` | `.github/copilot-instructions.md` |
| Other tools | `rules/universal/STAR-WORKFLOW.md` | Project instructions or persistent context |

Also add the handoff template; the rules look for it at this location:

```bash
mkdir -p docs/star/templates
cp templates/STAR-HANDOFF.md docs/star/templates/
```

> If your project already has a `CLAUDE.md`, `AGENTS.md`, or similar file, do not overwrite it. Append the STAR content to the existing file.

</details>

For installation, updates, removal, and verification details, see the **[Skill installation guide](docs/skills-quickstart.md)** (Turkish).

## ⚙️ How it works

STAR has two modes:

- **Direct mode** — typos, formatting, small and clearly specified fixes. The agent makes the change and says what it checked. No report, table, or handoff.
- **STAR mode** — changes that affect behavior, contracts, data, security, concurrency, or operations. A change that looks small can still belong here.

In STAR mode, the agent:

1. **Inspects** — reads the relevant code, tests, and conventions; separates observations from assumptions.
2. **Defines** — writes down the problem, current and desired behavior, scope, and acceptance criteria.
3. **Exposes decisions** — asks for the decisions that belong to you and compares real alternatives.
4. **Anticipates failure** — ties retries, concurrency, partial failures, permissions, and timeouts to tests.
5. **Acts when safe** — stops only for blocking decisions and makes the smallest coherent change.
6. **Verifies honestly** — reports executed, passed, failed, and not-run checks separately.
7. **Leaves a handoff** — records decisions, alternatives, costs, tests, and open risks.

At the end, you should be able to answer four questions:

1. **Why this way?**
2. **What other solution existed?**
3. **Where can it break?**
4. **What was actually verified?**

## 📚 Examples

| Example | Contents |
|---|---|
| [Password reset — from request to decisions](examples/password-reset/request.md) | The agent's response before coding and the developer's decisions |
| [Password reset — handoff](examples/password-reset/completed-handoff.md) | A completed `STAR-HANDOFF.md` that does not hide open risks |
| [One order, two payments](skills/star-engineering/references/double-payment.md) | Why locking the button alone is not enough |

## When to use it

**STAR mode:** new features or business rules, API contracts, data models or migrations, authentication and authorization, payments, external integrations, concurrency and consistency, meaningful refactors, persistent architectural decisions.

**Direct mode is enough:** typos, renames, formatting, documentation, behavior-preserving mechanical edits, small bug fixes with clear expected behavior.

## What this repository is not

- It is not a security scanner or an automated code review tool.
- It does not guarantee that code is correct, secure, or production-ready.
- It does not enforce a specific architecture.
- It does not replace review by an experienced engineer.

The rules can make you ask the right questions and keep decisions visible. They cannot always reliably judge whether your answers are actually correct.

> A rule file can make you ask questions. Engineering growth requires your answers to be reviewed. For supervised growth: [Softbreak STAR](https://softbreak.net).

## Repository structure

```text
star-ai-engineering-workflow/
├── skills/star-engineering/     # Single source: the Agent Skill
│   ├── SKILL.md
│   ├── agents/openai.yaml       # Codex interface metadata
│   ├── assets/                  # Handoff template
│   └── references/              # Example scenario
├── rules/                       # Always-on rule files generated from the Skill
├── templates/                   # Handoff (generated) and optional templates
├── examples/                    # Completed examples
├── docs/                        # Installation guide and platform notes
├── scripts/
│   ├── build_rules.py           # Generates rules/ from the Skill
│   └── install_skill.py         # Installation without Node.js
└── tests/                       # Package, installer, and sync tests
```

`FEATURE-BRIEF.md`, `DECISION-RECORD.md`, and `PULL-REQUEST.md` under `templates/` are optional, for teams that want a more formal process.

## Contributing

Open an [issue](https://github.com/fatihGunalp/star-ai-engineering-workflow/issues) to report a problem, suggest an example, or improve a rule.

To change the rule text, **do not edit the files under `rules/` directly**; they are all generated from the Skill:

```bash
# 1. Edit skills/star-engineering/SKILL.md
# 2. Regenerate the derived files
python3 scripts/build_rules.py
# 3. Run the tests
python3 -m unittest discover -s tests -v
```

These tests run automatically on pull requests; CI fails when the generated files do not match the Skill.

## License

[MIT](LICENSE) © Fatih Günalp
