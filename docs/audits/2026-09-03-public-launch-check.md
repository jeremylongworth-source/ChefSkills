# Public Launch Check

Date: 2026-09-03

## Scope

This check records the public `v0.1.0-alpha` launch state after repository visibility changed from private to public.

Reviewed surface:

- public repository URL
- repository description
- `v0.1.0-alpha` tag and GitHub prerelease
- `main` branch protection
- GitHub security and maintenance settings
- community profile and public security policy page
- issue template files
- funding metadata
- latest validation status

## Result

Public alpha launch complete.

Repository URL: https://github.com/jeremylongworth-source/ChefSkills

Release URL: https://github.com/jeremylongworth-source/ChefSkills/releases/tag/v0.1.0-alpha

Repository description: Open-source culinary skills, reasoning frameworks, routing, safety, and evaluation tools for building capable AI chef agents.

## Release State

- Repository visibility: public
- Default branch: `main`
- Release tag: `v0.1.0-alpha`
- Tag target: `8b0f2ee`
- GitHub release: created as a prerelease
- Latest validation before tag: GitHub Actions `Validate` run `33703426237`, successful

## Branch Protection

`main` is protected with:

- required status check: `Validate ChefSkills` from GitHub Actions
- strict status checks: enabled
- pull request reviews required: 1 approval
- stale review dismissal: enabled
- conversation resolution: required
- linear history: required
- force pushes: disabled
- branch deletion: disabled
- admin enforcement: disabled, preserving maintainer recovery access

No repository rulesets are configured at launch; classic branch protection is the active control.

## Security And Maintenance

Enabled:

- Dependabot security updates
- Dependabot alerts
- Dependabot automated security fixes
- Dependabot version updates for GitHub Actions through `.github/dependabot.yml`
- secret scanning
- secret scanning push protection

Not enabled at launch:

- secret scanning non-provider patterns
- secret scanning validity checks

The repository has no package dependency manifest or lockfile at launch, so dependency maintenance scope is limited to GitHub Actions.

## Community And Reporting

GitHub community profile health: 100%.

Publicly visible:

- `README.md`
- `LICENSE`
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `.github/FUNDING.yml`
- `.github/pull_request_template.md`
- public Security policy page

Issue forms are present in `.github/ISSUE_TEMPLATE/`:

- `routing_bug.yml`
- `skill_proposal.yml`
- `food_safety_concern.yml`
- `evaluation_fixture.yml`

The unauthenticated issue chooser redirects to GitHub sign-in, which is expected for creating issues from an anonymous browser session. The issue form files are present in the public repository.

## Residual Follow-Ups

- Monitor the first outside issue or pull request for template clarity.
- Watch Dependabot and secret scanning alerts after public indexing has settled.
- Keep public release language clear that current before/after evidence is simulated.
- Build the live-output evaluation harness before beta or broader launch claims.
