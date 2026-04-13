# Exercise 01: Your First Claude Task

## Goal

Practice the complete GitHub Integration workflow: create an issue, trigger Claude, review the result.

---

## The Task

Ask Claude to add a function to `demo/github_integration_demo.py` that:

- Takes a list of steps (strings)
- Returns a numbered markdown checklist

**Expected output:**
```
1. [ ] Step one
2. [ ] Step two
3. [ ] Step three
```

---

## Steps

1. **Create a new issue** in your repo titled: `Add checklist formatter to demo script`

2. **Write the issue body:**
   ```
   Add a `format_checklist(steps: list[str]) -> str` function to
   `demo/github_integration_demo.py`.

   The function should return a numbered markdown checklist where each
   item is formatted as: `{n}. [ ] {step}`.

   Include a test call in `main()` that prints a sample checklist.
   ```

3. **Comment on the issue:**
   ```
   @claude please implement this
   ```

4. **Watch Claude work** — check the issue comments for progress updates.

5. **Review the PR** Claude creates and merge it.

---

## What to Look For

- Claude reads the issue context correctly
- The implementation matches the spec
- The code is clean and works
- The PR is ready to merge without modification

---

## Stretch Goal

After merging, open a new issue asking Claude to add unit tests for the function.
