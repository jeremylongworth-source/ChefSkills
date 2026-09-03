# CHEFSKILLS-06 Public Alpha Readiness

## Purpose

This milestone prepares ChefSkills for a public `v0.1.0-alpha` release without changing repository visibility yet.

The release surface is documentation, skill instructions, router data, state examples, evaluation artifacts, validation scripts, and public collaboration workflow files. ChefSkills remains a culinary reasoning framework, not a recipe database or compliance authority.

## Current Pass

This pass adds the first public-alpha workflow layer:

- GitHub Actions validation on pull requests, pushes to `main`, and manual dispatch.
- Issue forms for routing bugs, skill proposals, food-safety concerns, and evaluation fixtures.
- A pull request template with validation, safety, source-check, scorecard, and public-alpha review prompts.
- README quickstart, requirements, safety boundary, evaluation-confidence, and contribution paths.
- Evaluation docs that label current before/after evidence as medium-confidence local reviewer simulations.
- Draft `v0.1.0-alpha` release notes.

## CI Assumptions

- Host: GitHub Actions.
- Runner: `ubuntu-latest`.
- Python: `3.13`, set explicitly through `actions/setup-python`.
- Permissions: read-only repository contents.
- Secrets: none.
- Primary gate: `./scripts/validate-all.ps1`.
- Cache: none, because current validators use the Python standard library only.

## Readiness Gates

Given a pull request, when the GitHub Actions workflow runs, then the full validation suite should execute and fail on broken references, invalid routing, invalid scorecards, or stale scorecard summaries.
Evidence: `.github/workflows/validate.yml` and the first remote Actions run after push.

Given a contributor opens a new issue, when they choose a template, then the template should collect scenario, expected route, safety relevance, source evidence, and affected files where appropriate.
Evidence: `.github/ISSUE_TEMPLATE/`.

Given a contributor opens a pull request, when they fill out the template, then validation, source-check, safety, scorecard, and public-alpha documentation expectations should be visible before review.
Evidence: `.github/pull_request_template.md`.

Given a public reader reviews the project, when they read the README and evaluation docs, then they should understand the alpha status, validation command, first useful skillset paths, safety boundaries, contribution paths, and simulated evidence caveat.
Evidence: `README.md`, `CONTRIBUTING.md`, `evaluation/README.md`, `evaluation/reports/README.md`, and `evaluation/scorecards/README.md`.

## Remaining Before Public Visibility

- Confirm the GitHub Actions workflow passes remotely.
- Run publication audits for secrets, prompt injection, data exfiltration, script permissions, supply chain, safety guidance, license, and attribution.
- Decide whether `v0.1.0-alpha` can ship with simulated evaluation evidence or whether a live-output harness is required first.
- Review GitHub branch protection or ruleset settings after the repository is public.
- Finalize and tag `v0.1.0-alpha`.
