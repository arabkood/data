# Challenge Generator Process

## Input Required

- Concept name
- Difficulty (1-5)
- Related concepts (prerequisites)

## Step 1: AI Generation

### Prompt Template

Create a Python coding challenge for Arabic developers.

**Concept:** {CONCEPT}
**Difficulty:** {DIFFICULTY}/5
**Prerequisites:** {PREREQUISITES}

Provide in this exact format:

- Problem Description (Arabic)

[Clear problem statement in Arabic]

- Starter Code

```python
def function_name():
    pass
```

- Unit Tests

```python
# 5 test cases covering:
# - Basic case
# - Edge case 1
# - Edge case 2
# - Error handling
# - Complex case
```

- Solution

```python
[Working solution]
```

- Hint (only if non-obvious)

[Optional hint in Arabic]

## Step 2: Technical Validation (10 min)

Checklist:

- [ ] Run tests against solution (all pass?)
- [ ] Run tests against starter code (all fail?)
- [ ] Tests actually test the concept (not just syntax?)
- [ ] Solution is idiomatic, not clever
- [ ] Difficulty matches rubric (see difficulty-rubric.md)

If any fail → fix or regenerate

## Step 3: Package (2 min)

Run script: `./scripts/package-challenge.sh {concept-name}`

Outputs to: `content/challenges/{track}/{concept-name}/`
