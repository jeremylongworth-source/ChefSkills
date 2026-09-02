$ErrorActionPreference = "Stop"

python .\scripts\validate-skill-files.py
python .\scripts\validate-skillsets.py
python .\scripts\validate-scenarios.py
python .\scripts\validate-router.py
python .\scripts\validate-state.py

Write-Host "All ChefSkills validation checks passed."
