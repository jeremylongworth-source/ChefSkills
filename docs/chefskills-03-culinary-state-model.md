# CHEFSKILLS-03 Culinary State Model

## Purpose

The culinary state model gives ChefSkills a shared representation for reasoning about food as a changing physical system.

The model supports troubleshooting, substitution, scaling, planning, preservation, and safety decisions. It is not a replacement for recipes. Recipes describe instructions; state describes what is true, what is desired, what is changing, and how an intervention can be verified.

## Core State Surfaces

- Ingredient state: identity, culinary role, preparation, physical condition, storage, and constraints.
- Dish state: target profile, observed profile, quality dimensions, defects, and service state.
- Transformation state: browning, gelatinization, denaturation, emulsification, reduction, hydration, fermentation, leavening, and related drivers.
- Equipment state: capacity, surface area, heat behavior, batching, and constraints.
- Workflow state: prep, active cooking, holding, service, cooling, storage, reheating, and recovery.
- Observation state: visual, aroma, texture, sound, taste, measured values, confidence, and missing observations.
- Recovery state: problem, mechanism, intervention, side effects, verification, and irreversible conditions.
- Safety state: status, hazards, missing facts, required actions, and review level.

## Reasoning Flow

Use this flow when a user reports a live cooking state or asks for adaptation:

1. Capture the goal and task context.
2. Record current ingredient, dish, equipment, workflow, observation, and safety state.
3. Define the target state.
4. Identify the gap and likely mechanisms.
5. Choose a low-risk intervention.
6. Predict side effects.
7. Define verification cues.
8. Apply the safety gate before final advice.

## Acceptance Criteria

Given the CHEFSKILLS-03 state model, when a maintainer runs `python .\scripts\validate-state.py`, then every required state file, top-level section, controlled vocabulary, and example rule validates.
Evidence: command output.

Given a safety-relevant state example, when the validator reads `state/state-examples.yaml`, then the example includes `safety_gate`.
Evidence: `scripts/validate-state.py`.

Given a troubleshooting example, when a reviewer reads `state/state-examples.yaml`, then the example includes observation, mechanism, intervention, and verification cue fields.
Evidence: state examples and validation.

Given a scaling or planning example, when a reviewer reads the example, then equipment or workflow state appears when it materially changes the culinary decision.
Evidence: state example surfaces.

Given the full repository validation command, when a maintainer runs `.\scripts\validate-all.ps1`, then state validation runs with the other checks.
Evidence: command output.

## Boundary With Router

The router selects skills and task classes. The state model describes the culinary facts those skills reason over.

For example:

- Router says `thin-gravy` routes to `chef-core`, `culinary-reasoning`, and `cooking-techniques`.
- State model says observed texture is too thin, target texture is spoon-coating, likely mechanisms include insufficient reduction or starch gelatinization, intervention is staged thickening or reduction, and verification cue is nappage.

Keeping these layers separate prevents the router from becoming a culinary encyclopedia.
