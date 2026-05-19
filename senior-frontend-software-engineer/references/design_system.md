# Design system

## Table of contents

1. [Token usage](#token-usage)
2. [Extending components](#extending-components)
3. [Storybook](#storybook)

## Token usage

- Colors, spacing, radius, font from CSS variables or theme
- No hardcoded hex in feature code unless token missing—add token first
- Dark mode via `prefers-color-scheme` or class strategy consistent with app

## Extending components

1. Check if existing primitive supports variant
2. Propose token or variant in design system PR if reusable
3. Local wrapper only for one-off if approved

## Storybook

Document: default, all variants, disabled, error, loading, keyboard focus story.
