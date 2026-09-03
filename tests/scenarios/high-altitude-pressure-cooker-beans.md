# Scenario: High Altitude Pressure Cooker Beans

Prompt:

> I live around 7,000 feet and my beans stay firm in my electric pressure cooker. Should I just keep adding more high-pressure time?

Expected routing:

- chef-core
- equipment-cookery
- ingredient-knowledge
- cooking-techniques

Expected behavior:

- Identify altitude, soaking, bean age, salt/acid timing, pressure level, liquid ratio, foaming, fill level, and release method as relevant.
- Recommend staged adjustments rather than blindly adding high-pressure time.
- Include texture cues and pressure-cooker safety limits for foaming foods.

Failure modes:

- Treats altitude as irrelevant.
- Recommends unlimited extra pressure time without checking liquid, fill, or release.
- Ignores bean age, soaking, or acid timing.
