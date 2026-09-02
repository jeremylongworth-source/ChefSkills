# Scenario: Sluggish Sourdough Starter

Prompt:

> My sourdough starter has bubbles but barely doubles after feeding. It smells tangy, not moldy. Is it unsafe, and how do I get it strong enough for bread?

Expected routing:

- chef-core
- fermentation
- baking-structure
- culinary-reasoning
- food-safety

Expected behavior:

- Separate food-safety contamination signs from ordinary weak starter activity.
- Recommend discard only for mold, unusual discoloration, or other contamination signs.
- Explain feeding ratio, temperature, flour strength, time, and rise tracking as activity controls.
- Connect starter strength to bread structure and leavening reliability.

Failure modes:

- Treats any slow starter as unsafe without contamination signs.
- Ignores mold or discoloration discard criteria.
- Gives bread advice without starter activity cues.
