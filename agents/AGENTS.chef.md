# ChefSkills Routing

Use this instruction set when a project needs culinary specialist behavior.

Start with `chef-core` for broad cooking, recipe, menu, troubleshooting, or culinary planning requests. Add the smallest useful set of supporting skills:

- Use `culinary-reasoning` for diagnosis, tradeoffs, failure analysis, and recovery.
- Use `ingredient-knowledge` for ingredient function, behavior, storage, and flavor role.
- Use `cooking-techniques` for technique choice, heat transfer, doneness cues, and process control.
- Use `sauce-work` for sauces, emulsions, reductions, gravies, pan sauces, starch thickening, finishing, scaling, holding, and sauce recovery.
- Use `baking-structure` for baked-good texture, crumb, rise, set, hydration, gluten, leavening, binders, pan geometry, and bake-through troubleshooting.
- Use `protein-cookery` for meat, poultry, seafood, eggs, plant proteins, doneness, carryover, searing, braising, resting, moisture control, and protein texture recovery.
- Use `ingredient-substitution` for swaps, omissions, dietary adaptation, and unavailable ingredients.
- Use `recipe-development` for new recipes, recipe cleanup, testing notes, and iteration.
- Use `recipe-scaling` when portions, batch size, vessel size, timing, or service scale changes.
- Use `food-safety` whenever safety, allergens, storage, spoilage, undercooking, reheating, preservation, or vulnerable diners may matter.
- Pair `protein-cookery` with `food-safety` whenever raw animal products, safe doneness, holding, reheating, or vulnerable diners matter.

Default to one primary skill plus one to three supporting skills. Do not load the whole culinary library unless the user asks for broad planning or the task genuinely spans multiple domains.

For complex tasks, produce the goal, constraints, current state, target state, candidate interventions, safety gate, and verification cues before giving final instructions.
