# Scenario 17 — Wordle

A terminal Wordle-style game with duplicate-letter scoring and guess history.

## Provided files

- `main.py` — entry point.
- `game.py` — game loop and history.
- `feedback.py` — letter-evaluation rules.
- `words.py` — in-memory word list.
- `requirements.txt` — dependency declaration.

## Setup

```bash
python main.py
```

## Before changing the code

Read the feedback implementation carefully. Test guesses containing repeated letters
against targets that contain fewer copies of that letter than the guess.

## Task 1 — Correct duplicate-letter feedback

Implement standard Wordle-style feedback in which exact matches are resolved first and
each occurrence in the target can satisfy at most one occurrence in the guess.

**Done when:** repeated-letter guesses produce correct exact/present/absent results.

## Task 2 — Complete guess handling

Add clean win/loss handling, enforce the six accepted-guess limit, and ensure invalid
guesses do not consume a turn.

## Task 3 — Variable word lengths

Add 4-, 5-, and 6-letter modes using the supplied in-memory words. The feedback logic
must work for all supported lengths.

## Task 4 — Guess history and summary

Display a readable history after each accepted guess and provide a final session summary.
Do not duplicate entries for invalid attempts.

## Fix Summary

- **Task 1:** `evaluate()` marked a guess letter yellow whenever it appeared anywhere in
  the target, without tracking how many copies were already accounted for by green
  matches or earlier yellows. A guess with a repeated letter (e.g. "poppy" against
  "apple") could get more yellow/green marks than the target actually has copies of.
  Now resolves greens first, then caps yellows by the target's remaining letter counts
  via `collections.Counter`.

  Demonstrated in the attached videos with target `apple`, guess `poppy` (two P's in
  the guess, only one spare P in the target after the green match at position 3):

  | | P | O | P | P | Y |
  |---|---|---|---|---|---|
  | Before (buggy) | yellow | gray | green | **yellow** | gray |
  | After (fixed) | yellow | gray | green | **gray** | gray |

  Only one of the two non-green P's should register — the fix makes the 4th letter
  gray instead of a second false yellow.
- **Task 2:** invalid-length/non-alpha guesses no longer consume a turn; win/loss/quit
  are each reported distinctly in the summary.
- **Task 3:** added 4- and 6-letter word lists; length is chosen at startup.
- **Task 4:** guess history prints after every accepted guess, plus a final summary;
  invalid attempts are never added to the history.

## Required testing

Use repeated-letter cases, exact matches, absent letters, invalid lengths, all three
word lengths, winning on the final allowed guess, losing, and quitting.


## LLM usage

You may use an LLM during the lab. The goal is to use it as a coding assistant while
retaining responsibility for understanding and testing the result.

- Inspect the existing code before asking for changes.
- Ask for explanations when you do not understand a proposed change.
- Test generated code against the stated behaviour and edge cases.
- Keep your complete LLM chat history for submission.
- Do not replace the whole project with an unrelated implementation.
- Keep all state in memory; do not add CSV, JSON, SQLite, or other persistence.

## Submission checklist

- [ ] Task 1 completed and the original defect was reproduced and fixed.
- [ ] Tasks 2–4 completed and tested.
- [ ] Boundary and invalid-input cases tested.
- [ ] No unnecessary external dependencies added.
- [ ] No persistent storage added.
- [ ] Code remains understandable and modular.
- [ ] Complete LLM chat-history link included.

## Folder structure

```text
scenario-05-wordle/
├── README.md
├── requirements.txt
├── main.py
├── game.py
├── feedback.py
└── words.py
```

## Submission Checklist

Submission is only the following three things:

- [ ] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [ ] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [ ] The Chat/LLM used page link, with the complete chat history
