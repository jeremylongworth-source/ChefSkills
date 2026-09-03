# Publication Audit: 2026-09-03

## Scope

This audit reviews ChefSkills before public-alpha repository visibility.

Reviewed surface:

- Tracked tree before this audit artifact: 202 files.
- Git history before this audit commit: 19 commits on all refs.
- Scripts: 10 local validator and scorecard scripts.
- GitHub workflow, issue forms, and pull request template.
- Skill instructions, references, agents metadata, skillsets, router data, state examples, evaluation fixtures, reports, scorecards, and docs.

## Result

Recommendation: approve with follow-up.

No publication blockers were found in tracked content or history.

Public visibility should still wait for final repository settings review, branch or ruleset configuration, and a final release decision about whether `v0.1.0-alpha` can ship with medium-confidence simulated evaluation evidence.

## Evidence

- `git status --short`: clean before audit changes.
- `git ls-files`: 202 tracked files before this audit artifact.
- `git rev-list --all --count`: 19 commits before this audit commit.
- Redacted secret history scan: no secret-like values found in tracked history.
- Dependency manifest scan: no `requirements*.txt`, `pyproject.toml`, `package.json`, lockfiles, Dockerfiles, or compose files found.
- Executable/script inventory: only Python validators, the scorecard summarizer, and `scripts/validate-all.ps1`.
- Hidden instruction scan: no hidden HTML comments, encoded payload markers, prompt-injection phrases, shell download-and-run patterns, or eval/exec/network helper code found in tracked content.
- Link reachability scan: most source links returned `200` or `202`; several official government sites blocked the Python checker with `403`, timeout, or local certificate errors but were spot-checked through browser/search access.
- GitHub Actions supply-chain check: `actions/checkout` and `actions/setup-python` tags were checked with `git ls-remote` and pinned from major tags to exact release tags.
- Local validation: `.\scripts\validate-all.ps1` passed after audit edits.
- GitHub YAML parsing: 6 `.github` YAML files parsed locally.

## Audit Findings

### Secrets And Private Data

Status: pass.

No API keys, OAuth tokens, private keys, database URLs, secret assignments, `.env` files, private credentials, or private project artifacts were found in the current tracked tree or tracked history.

The existing `.gitignore` excludes `.codex/`, `.env`, `.env.*`, bytecode, and OS metadata.

### Prompt Injection

Status: pass.

No instructions were found that tell agents to ignore higher-priority instructions, conceal actions, bypass approval, exfiltrate data, or treat untrusted content as authority.

The repo contains realistic prompts and generated evaluation outputs, but they are structured as scenarios, fixtures, or reports rather than operating instructions.

### Data Exfiltration

Status: pass.

The scripts read repository-local files and print validation results. No script sends data to a network endpoint, reads credential locations, inspects browser profiles, reads home-directory data, uploads reports, or writes issue/PR comments.

External URLs in docs and reports are source references, not automated network sinks.

### Script Permissions

Status: pass with safe-use conditions.

Scripts are local validators and one scorecard summarizer. They do not delete, move, spawn long-running services, install dependencies, run shell commands, or require elevated permissions.

Safe-use condition: `scripts/summarize-scorecards.py --output` writes to the caller-provided output path. Maintainers should keep documented uses inside the repository unless intentionally generating a local copy elsewhere.

### Supply Chain

Status: pass with mitigation applied.

No third-party runtime package dependencies or installer hooks were found.

The GitHub Actions workflow uses GitHub-hosted actions only. It now pins:

- `actions/checkout@v7.0.1`
- `actions/setup-python@v7.0.0`

Re-review trigger: update this audit when workflow actions, runtime dependencies, package managers, or install scripts are added.

### Safety Guidance

Status: pass with source-check caveat.

Tracked food-safety guidance consistently treats safety as a hard gate, requires conservative uncertainty handling, and refuses compliance certification.

Spot-checked official or authoritative source anchors include FoodSafety.gov, USDA FSIS, FDA, CDC, Health Canada, CFIA, NCHFP, CSU Extension, UMN Extension, Pyrex, and Michelin Guide public criteria.

Caveat: this audit checked source reachability and a representative set of current claims. Future exact safety thresholds, regulatory claims, commercial food-service guidance, and manufacturer-dependent equipment guidance still require fresh source checks at the time of change.

### License And Attribution

Status: pass.

The repository has an MIT license. Skill frontmatter uses `license: MIT`.

External source material is linked as source evidence; no copied long-form third-party text or opaque binary assets were found.

## Remaining Before Public Visibility

- Confirm GitHub branch protection or ruleset expectations.
- Confirm the security-policy contact link behaves as expected after public visibility. The unauthenticated URL currently returns `404` while the repository is private.
- Decide whether simulated evaluation evidence is acceptable for `v0.1.0-alpha`, or whether to build a live-output harness first.
- Run `.\scripts\validate-all.ps1` and confirm GitHub Actions before tagging.
- Finalize release notes and tag `v0.1.0-alpha`.
