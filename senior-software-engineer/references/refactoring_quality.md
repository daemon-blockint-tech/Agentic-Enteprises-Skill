# Refactoring and quality

## Table of contents

1. [Code smells](#code-smells)
2. [Safe sequence](#safe-sequence)
3. [Technical debt](#technical-debt)

## Code smells

| Smell | Action |
|---|---|
| God class | Extract responsibilities |
| Shotgun surgery | Consolidate related change behind facade |
| Feature envy | Move method to owning module |
| Primitive obsession | Introduce value types |

## Safe sequence

1. Green tests on current behavior
2. Refactor without behavior change
3. Add feature in clean structure
4. Remove old path behind flag

Avoid "refactor while adding feature" unless slice is tiny.

## Technical debt

Log debt item: symptom, interest (slow dev, incidents), paydown proposal, owner.

Pay down when touching area or when interest exceeds estimate of fix.
