# Scenario: Crowded Sheet Pan Vegetables

Prompt:

> My roasted vegetables came out pale and wet on a full sheet pan. Should I just turn the oven hotter?

Expected routing:

- chef-core
- equipment-cookery
- culinary-reasoning
- cooking-techniques

Expected behavior:

- Identify pan crowding, trapped steam, low airflow, and limited surface contact as likely causes.
- Recommend spacing, batching, drying cut surfaces, preheating, and rack-position adjustments before simply raising oven temperature.
- Explain the browning mechanism and include observable cues such as sizzling, browning edges, and no pooled liquid.

Failure modes:

- Treats higher oven temperature as the only fix.
- Ignores steam, airflow, or pan surface area.
- Gives no verification cue.
