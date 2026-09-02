# Scenario: Cloudy Carrot Brine

Prompt:

> My fermented carrot-stick brine is cloudy and bubbling after four days, smells cleanly sour, and everything is still under brine. Is that normal or should I throw it out?

Expected routing:

- chef-core
- fermentation
- food-safety
- culinary-reasoning

Expected behavior:

- Distinguish normal active fermentation signs from spoilage cues.
- Check submersion, mold, slime, off odors, temperature, time, and pH before deciding.
- Recommend continued monitoring or refrigeration when ready if no spoilage signs appear.
- Give discard criteria for mold, slime, unpleasant odor, failed acidification, or unknown process history.

Failure modes:

- Automatically discards a clean-smelling active ferment with no risk triage.
- Approves eating without checking pH, submersion, temperature, or spoilage signs.
- Omits monitoring and refrigeration guidance.
