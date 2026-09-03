$ErrorActionPreference = "Stop"

python ./scripts/validate-skill-files.py
python ./scripts/validate-skillsets.py
python ./scripts/validate-scenarios.py
python ./scripts/validate-router.py
python ./scripts/validate-state.py
python ./scripts/validate-evaluation.py
python ./scripts/validate-evaluation-reports.py
python ./scripts/validate-scorecards.py
python ./scripts/summarize-scorecards.py --check ./evaluation/scorecards/summary.json

Write-Host "All ChefSkills validation checks passed."
