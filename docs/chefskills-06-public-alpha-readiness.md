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
- Remote GitHub Actions validation confirmed on `main`.
- Publication audit for the current tracked tree and history.
- Repository settings review with Dependabot alerts, automated security fixes, and GitHub Actions version updates enabled where available before public visibility.
- Evidence-confidence decision approving simulated before/after evidence for `v0.1.0-alpha` with explicit public caveats.

## CI Assumptions

- Host: GitHub Actions.
- Runner: `ubuntu-latest`.
- Python: `3.13`, set explicitly through `actions/setup-python@v7.0.0`.
- Actions: `actions/checkout@v7.0.1` and `actions/setup-python@v7.0.0`.
- Permissions: read-only repository contents.
- Secrets: none.
- Primary gate: `./scripts/validate-all.ps1`.
- Cache: none, because current validators use the Python standard library only.
- Dependency maintenance: `.github/dependabot.yml` checks GitHub Actions weekly.

## Readiness Gates

Given a pull request, when the GitHub Actions workflow runs, then the full validation suite should execute and fail on broken references, invalid routing, invalid scorecards, or stale scorecard summaries.
Evidence: `.github/workflows/validate.yml` and remote Actions validation on `main`.

Given a contributor opens a new issue, when they choose a template, then the template should collect scenario, expected route, safety relevance, source evidence, and affected files where appropriate.
Evidence: `.github/ISSUE_TEMPLATE/`.

Given a contributor opens a pull request, when they fill out the template, then validation, source-check, safety, scorecard, and public-alpha documentation expectations should be visible before review.
Evidence: `.github/pull_request_template.md`.

Given a public reader reviews the project, when they read the README and evaluation docs, then they should understand the alpha status, validation command, first useful skillset paths, safety boundaries, contribution paths, and simulated evidence caveat.
Evidence: `README.md`, `CONTRIBUTING.md`, `evaluation/README.md`, `evaluation/reports/README.md`, and `evaluation/scorecards/README.md`.

Given the repository is audited before public visibility, when secrets, prompt-injection, data-exfiltration, script-permission, supply-chain, safety-guidance, license, and attribution checks run, then no publication blockers should remain in tracked files or history.
Evidence: `docs/audits/2026-09-03-publication-audit.md`.

Given the repository settings are reviewed before public visibility, when GitHub plan and visibility constraints are checked, then maintainers should know which security and branch-policy settings are complete now and which settings must wait until the repository is public.
Evidence: `docs/audits/2026-09-03-repository-settings-review.md`.

Given the alpha evidence decision, when the release notes and public docs describe evaluation evidence, then they should state that current before/after outputs are medium-confidence local reviewer simulations and should not claim live benchmark, certification, or compliance proof.
Evidence: `docs/releases/v0.1.0-alpha-evidence-decision.md`.

## Remaining Before Public Visibility

- Keep the simulated-evidence caveat visible in README, evaluation docs, and release notes.
- Configure GitHub branch protection or ruleset settings after the repository is public; GitHub currently blocks these settings while the repository is private on the current plan.
- Confirm the security-policy contact link behaves as expected after public visibility.
- Finalize and tag `v0.1.0-alpha`.
