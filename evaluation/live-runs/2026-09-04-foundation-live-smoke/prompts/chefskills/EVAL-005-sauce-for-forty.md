# ChefSkills Prompt: EVAL-005-sauce-for-forty

Capture role: ChefSkills-enabled
Scenario: sauce-for-forty
Task type: ADAPT

## Instructions

Answer the user with ChefSkills enabled.

Use this expected ChefSkills route:

- chef-core
- recipe-development
- recipe-scaling

If your agent host can load local files, use these skill files as the behavioral source:

- skills/chef-core/SKILL.md
- skills/recipe-development/SKILL.md
- skills/recipe-scaling/SKILL.md

Preserve food safety as a hard gate. Do not use the evaluation rubric, expected behavior list, or blocker list as answer content.

Return only the user-facing answer.

## User Prompt

I have a pan sauce recipe for 4 people and need it for 40. Can I multiply everything by 10?
