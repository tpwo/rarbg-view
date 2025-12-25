# Copilot Instructions

## Pre-commit Workflow

After making any code changes, always run `pre-commit run --all-files` to ensure code quality and catch lint or syntax issues before considering the task complete.
If pre-commit reports errors, fix them and rerun until all checks pass or only non-blocking warnings remain.
Document this workflow in all future code contributions and automation.


## Docstring Formatting Instruction

When adding or editing Python docstrings, always use the following format:

1. The first line must be a concise, one-line summary of the function or class.
2. Follow the summary with a blank line.
3. Add any additional explanation, rationale, or details (such as why a particular implementation is used) after the blank line.

For example, if a function trims a string to extract a date, include the reason for the trim in the docstring after the summary and blank line.

This ensures clarity and consistency in documentation throughout the codebase.
