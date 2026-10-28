# Claude Code / Codex Skill alignment

**Reviewed:** 2026-10-28. Primary sources:
- Anthropic: https://code.claude.com/docs/en/skills
- OpenAI: https://learn.chatgpt.com/docs/build-skills
- OpenAI, *Rethinking skills and prompts for GPT-6 Astra* (2026-09-11): https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
- Portable Agent Skills specification: https://agentskills.io/specification

## Shared contract

- **Source:** `skills/star-engineering/SKILL.md` — one provider-neutral name, task-focused description, concise procedural instructions.
- **On demand:** hosts show name/description first; they can load body if task matches. Neither platform guarantees implicit activation.
- **Resources:** the bundled `references/` example and `assets/` template are consulted only for relevant tasks. Skill must not depend on the original repo once installed in a consumer project.
- **Permissions:** the Skill supplies a decision workflow, not tools or extra privileges. It does not grant blanket write, shell or deployment permissions.
- **Proportionality:** reserve consequential decisions, risk/verification work for meaningful changes; no elaborate handoff for a typo. User-approved tasks should not be delayed by ceremonial confirmation.
- **No guarantee:** tests and code review remain necessary. No fabricated execution evidence.

## Claude Code (native)

| Topic | Decision |
|---|---|
| Project location | `.claude/skills/star-engineering/SKILL.md` |
| Personal location | `~/.claude/skills/star-engineering/SKILL.md` |
| Manual invocation | `/star-engineering` at the start of the prompt |
| Implicit invocation | Enabled by default; description specifies meaningful software-change triggers |
| Claude-only frontmatter | Omitted `disable-model-invocation`, `user-invocable`, `allowed-tools`, `context: fork`, `model`; none is needed for this provider-neutral instructional Skill |
| Additional resources | Relative links from the installed Skill directory |
| Validation | Check skill listing, explicit invocation, implicit matching, and non-trigger prompts; `claude plugin validate .claude/skills` can help with frontmatter when supported by installed Claude Code versions |

Claude Code supports separate plugin distribution, but the first release is a direct-installable Skill, not a Claude plugin.

## Codex (native)

| Topic | Decision |
|---|---|
| Project location | `.agents/skills/star-engineering/SKILL.md` |
| Personal location | `~/.agents/skills/star-engineering/SKILL.md` |
| Manual invocation | `$star-engineering` in the prompt; `/skills` lists installed Skills |
| Implicit invocation | Enabled by default; concise description front-loads triggers |
| Optional interface metadata | `agents/openai.yaml` with display name, short description, default prompt |
| MCP dependencies | None; this is an instruction-only Skill with no external MCP server requirements |
| Testing | `$skill-installer` or local install, listing/selection, actual task output; restart if Codex does not detect an update |

OpenAI's current distribution recommendation for sharing Skills widely through ChatGPT and Codex is a **plugin**. This repository currently provides a portable Skill and third-party CLI/manual distribution; it does **not** claim to be in the OpenAI plugin directory.

## Installation paths and distribution are separate concerns

`npx skills add ...` is from the third-party Skills CLI and has been exercised in this repo's GitHub Actions against both Claude Code and Codex consumer paths. It is not a native Anthropic/OpenAI install command. `scripts/install_skill.py` is an independent, stdlib-based fallback. Both install the same provider-neutral folder. This avoids maintaining divergent behavior across `CLAUDE.md`, `AGENTS.md`, and the Skill itself.

## What tests actually prove

- Automated CI tests the package metadata, bundled references, and installed file locations in **separate** consumer projects.
- A successful CLI file installation **does not prove** either model actually chooses the Skill or follows the workflow.
- Manual evaluation cases in `tests/skill-evaluation-cases.md` cover explicit activation, implicit activation, non-activation, uncertain evidence, security boundaries, and portability.
- Only claim runtime behavior when a real Claude Code/Codex session has produced observable evidence.
