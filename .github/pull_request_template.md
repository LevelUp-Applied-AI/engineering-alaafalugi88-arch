## What changed
Set up the Python virtual environment and installed the required dependencies from requirements-prework.txt.
Added the pull request template and checklist files.

## Why
This PR prepares the development environment so the project can run correctly and ensures pull requests include clear descriptions and review steps.

## How to test
1. Activate the virtual environment
2. Install dependencies using:
   pip install -r requirements-prework.txt
3. Run the tests:
   python tests/test_environment.py

## Checklist
- [x] PR title describes one logical change
- [x] Tests pass locally
- [x] README updated if needed
- [x] No debug prints left
- [x] PR does not mix unrelated changes
