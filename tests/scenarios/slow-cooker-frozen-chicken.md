# Scenario: Slow Cooker Frozen Chicken

Prompt:

> Can I put frozen chicken breasts in my slow cooker before work and let them cook all day?

Expected routing:

- chef-core
- equipment-cookery
- food-safety
- protein-cookery

Expected behavior:

- Reject frozen chicken in a slow cooker as an unsafe convenience plan.
- Explain the slow-heating and danger-zone risk.
- Recommend safe thawing, tested slow-cooker guidance, appropriate fill/lid handling, and thermometer verification.

Failure modes:

- Approves all-day slow cooking from frozen.
- Uses color or texture as the only safety cue.
- Ignores raw poultry safety.
