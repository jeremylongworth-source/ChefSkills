# GitHub Copilot and `gh skill` Setup

ChefSkills can be used as a GitHub CLI agent-skills source for GitHub Copilot.

The repository uses the Agent Skills discovery convention:

```text
skills/<skill-name>/SKILL.md
```

That means `gh skill install` can install individual ChefSkills skill packages directly from this repository.

## Requirements

- GitHub CLI with `gh skill` support.
- GitHub Copilot or another supported agent host.
- A repository or working directory where you want the skill installed.

Check support:

```powershell
gh skill --help
```

## Preview Before Installing

Preview a skill:

```powershell
gh skill preview jeremylongworth-source/ChefSkills chef-core
```

Preview a pinned release version:

```powershell
gh skill preview jeremylongworth-source/ChefSkills chef-core@v0.1.0-alpha
```

## Install For GitHub Copilot

Install a skill for GitHub Copilot at project scope:

```powershell
gh skill install jeremylongworth-source/ChefSkills chef-core
```

Pin the public-preview release when reproducibility matters:

```powershell
gh skill install jeremylongworth-source/ChefSkills chef-core --agent github-copilot --scope project --pin v0.1.0-public-preview
```

Install a safety skill:

```powershell
gh skill install jeremylongworth-source/ChefSkills food-safety --agent github-copilot --scope project --pin v0.1.0-public-preview
```

Install a specialist skill:

```powershell
gh skill install jeremylongworth-source/ChefSkills equipment-cookery --agent github-copilot --scope project --pin v0.1.0-public-preview
```

You can also run the command without a skill name to choose interactively:

```powershell
gh skill install jeremylongworth-source/ChefSkills
```

## Scope Notes

Project scope installs the skill into the current project for supported hosts.

User scope makes the skill available outside a single repository:

```powershell
gh skill install jeremylongworth-source/ChefSkills culinary-reasoning --agent github-copilot --scope user --pin v0.1.0-public-preview
```

Use project scope when you are testing ChefSkills in one repository. Use user scope only when you deliberately want the culinary skill available across many projects.

## Skillsets Versus Skills

`gh skill install` installs atomic skill folders such as `chef-core`, `food-safety`, or `recipe-development`.

ChefSkills also has YAML skillsets under `skillsets/`, but those are repository composition files and are not installed by `gh skill install`.

For broad culinary use, start with:

- `chef-core`
- `culinary-reasoning`
- `ingredient-knowledge`
- `cooking-techniques`
- `food-safety`

Then add specialist skills only when needed:

- `sauce-work`
- `baking-structure`
- `protein-cookery`
- `fermentation`
- `equipment-cookery`

## Verification

After install, ask Copilot to use the installed skill on a narrow cooking task.

Example prompt:

```text
Use the ChefSkills chef-core skill to reason through why my pan sauce split and how to recover it safely.
```

The response should:

- identify current state and target state
- explain the likely culinary mechanism
- provide a staged intervention
- include stop cues and side effects
- preserve food safety as a hard gate

## Maintenance

Pin installs to a release tag when reproducibility matters:

```powershell
--pin v0.1.0-public-preview
```

Run `gh skill update` when you intentionally want installed skills to move forward.

ChefSkills `v0.1.0-public-preview` remains public-alpha content. Current before/after evaluation evidence is medium-confidence local reviewer simulation evidence, not live benchmark output.
