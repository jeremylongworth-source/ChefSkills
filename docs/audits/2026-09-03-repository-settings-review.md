# Repository Settings Review

Date: 2026-09-03

## Scope

This review covers the live GitHub repository settings visible through the GitHub CLI and API, the local `.github` collaboration files, and public-alpha settings that must be confirmed after visibility changes.

Sources checked:

- GitHub REST API for `jeremylongworth-source/ChefSkills`
- GitHub community profile API for `jeremylongworth-source/ChefSkills`
- GitHub branch protection and rulesets API responses for `main`
- GitHub Docs for branch protection, rulesets, security settings, security policies, and Dependabot GitHub Actions updates
- Local repository files under `.github/`

## Result

Approve with public-switch follow-up.

The repository has enough operations scaffolding for the next public-alpha step, but branch protection or repository rulesets cannot be configured while this private repository is on the current GitHub plan. GitHub returned `403` for both branch protection and ruleset API checks with the message that the repository must be public or upgraded.

## Live Repository Settings

- Repository: `jeremylongworth-source/ChefSkills`
- Visibility: private
- Default branch: `main`
- Issues: enabled
- Projects: enabled
- Wiki: disabled
- Merge commits: allowed
- Squash merges: allowed
- Rebase merges: allowed
- Delete branch on merge: enabled during this pass
- GitHub Actions validation: active on push, pull request, and manual dispatch
- Dependabot alerts: enabled during this pass
- Dependabot automated security fixes: enabled during this pass
- Dependabot version updates: configured during this pass for GitHub Actions in `.github/dependabot.yml`

## Community Profile

GitHub reported a 100% community profile health score for the private repository through the API.

Detected files:

- `README.md`
- `LICENSE` with MIT SPDX metadata
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `.github/pull_request_template.md`

Local issue forms are present under `.github/ISSUE_TEMPLATE/`, although the community profile API returned `issue_template: null`. Confirm the public GitHub UI shows the four issue forms after the repository is public.

## Branch And Ruleset Gate

Branch protection and rulesets should be configured after the repository becomes public, unless the account plan changes first.

Recommended `main` protection for public alpha:

- require pull requests before merging
- require the `Validate ChefSkills` status check before merge
- require conversation resolution before merge
- block force pushes
- block branch deletion
- keep admins able to bypass only for urgent maintainer recovery, with any bypass noted in the changelog or release notes when release-relevant

Rulesets are preferred if available because GitHub documents them as the clearer repository-level policy mechanism. A classic branch protection rule is acceptable if rulesets are not available in the UI.

## Security And Maintenance Gate

Keep these enabled or confirm them immediately after public visibility:

- Dependabot alerts
- Dependabot automated security fixes
- Dependabot GitHub Actions version updates
- secret scanning
- push protection
- CodeQL or code scanning if GitHub offers a useful Python setup for this repository
- public security policy page generated from `SECURITY.md`

The project currently has no package dependency manifest or lockfile, so dependency update scope is limited to GitHub Actions unless future dependency manifests are added.

## Remaining Follow-Ups

- Make the repository public only after the simulated-evidence release decision is explicit.
- After public visibility, configure branch protection or a repository ruleset for `main`.
- After public visibility, confirm the public Security policy page resolves from GitHub's Security and quality tab.
- After public visibility, confirm issue forms appear in the public UI.
- Re-run local validation and GitHub Actions before creating the `v0.1.0-alpha` tag.
