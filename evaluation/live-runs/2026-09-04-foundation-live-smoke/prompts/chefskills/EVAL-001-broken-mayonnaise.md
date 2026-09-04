# ChefSkills Prompt: EVAL-001-broken-mayonnaise

Capture role: ChefSkills-enabled
Scenario: broken-mayonnaise
Task type: FIX

## Instructions

Answer the user with ChefSkills enabled.

Use this expected ChefSkills route:

- chef-core
- culinary-reasoning
- cooking-techniques

If your agent host can load local files, use these skill files as the behavioral source:

- skills/chef-core/SKILL.md
- skills/culinary-reasoning/SKILL.md
- skills/cooking-techniques/SKILL.md

Preserve food safety as a hard gate. Do not use the evaluation rubric, expected behavior list, or blocker list as answer content.

Return only the user-facing answer.

## User Prompt

My mayonnaise broke and looks oily and separated. How do I fix it?
