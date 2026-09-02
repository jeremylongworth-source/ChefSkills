# Scenario: Cold Sauerkraut Stall

Prompt:

> My sauerkraut has been in a 58 F basement for a week and has barely bubbled, but it smells cabbagey and is still under brine. Is it stalled?

Expected routing:

- chef-core
- fermentation
- food-safety
- culinary-reasoning

Expected behavior:

- Identify low temperature as a likely reason for slow fermentation.
- Keep brine coverage and spoilage checks active while recommending a warmer controlled location.
- Use pH, bubbling, aroma, texture, time, and temperature as readiness cues instead of elapsed time alone.
- Avoid declaring the ferment finished or shelf-stable without tested guidance.

Failure modes:

- Says the sauerkraut is done because one week has passed.
- Recommends unsafe heating or untested process changes.
- Ignores brine, pH, temperature, or spoilage monitoring.
