# Contributing

ChefSkills prioritizes small, reviewable culinary skills over bulk-generated content.

Good contributions:

- improve a skill's decision criteria, workflow, or output contract
- add a focused reference that changes agent behavior
- add realistic scenarios with expected routing
- tighten safety guidance with cited, reviewable reasoning
- improve validators or documentation

Avoid:

- large recipe dumps
- unreviewed food-safety claims
- generic cooking advice that does not improve agent decisions
- adding a new skill when an existing skill can be improved

## Skill Quality Bar

Each skill should include:

- concise frontmatter with `name`, `description`, and `license`
- a clear core workflow
- an output contract or deliverable shape
- at least one focused reference file
- `agents/openai.yaml` metadata

Run validation before submitting changes:

```powershell
.\scripts\validate-all.ps1
```
