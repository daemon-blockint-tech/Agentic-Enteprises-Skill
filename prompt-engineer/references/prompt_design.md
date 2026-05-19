# Prompt Design Patterns

## Zero-Shot Prompting

**When:** Task is unambiguous; model likely knows the answer from pre-training.

**Template:**
```
[Clear instruction]

[Input]
```

**Example:**
```
Summarize the following text in 2 sentences:

Text: "The Large Hadron Collider (LHC) is the world's largest and most powerful particle accelerator..."
```

## Few-Shot Prompting

**When:** You need consistent formatting, style, or domain-specific reasoning.

**Template:**
```
[Instruction]

Example 1:
Input: [input]
Output: [desired output]

Example 2:
Input: [input]
Output: [desired output]

Now do the same for:
Input: [new input]
Output:
```

**Best practices:**
- 3-5 examples typically sufficient; more can confuse
- Examples should be diverse and cover edge cases
- Include the exact format you want in the output
- If examples are long, use semantic search to retrieve relevant ones (dynamic few-shot)

## Chain-of-Thought (CoT)

**When:** Reasoning tasks — math, logic, multi-hop questions.

**Basic CoT:**
```
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
A: Let's think step by step. Roger starts with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11.
```

**Self-consistency CoT:**
1. Generate 5-10 reasoning chains with temperature > 0
2. Take the most frequent final answer (majority vote)
3. Improves accuracy on complex reasoning tasks

**Tree-of-Thoughts (ToT):**
- Explore multiple reasoning paths
- Evaluate each path's viability
- Backtrack if a path leads to a contradiction
- Best for: games, planning, optimization

## Role-Based Prompting

**When:** You need domain expertise, specific tone, or behavioral guardrails.

**Template:**
```
You are a [role] with [experience/characteristics].

Your task is to [specific task].

Guidelines:
- [Constraint 1]
- [Constraint 2]
- [What to avoid]

[Input]
```

**Example:**
```
You are a senior Python code reviewer with 10 years of experience.

Review the following code for:
- Security vulnerabilities
- Performance issues
- Pythonic style
- Maintainability

Provide your feedback in this format:
1. Summary (1-2 sentences)
2. Critical issues (if any)
3. Suggestions for improvement
4. Positive observations

Code:
```python
def process_user_input(data):
    exec(data)
    return "Done"
```
```

## Structured Output Prompting

**JSON Mode:**
```
Analyze the sentiment of this review. Respond in JSON with this exact schema:
{
  "sentiment": "positive|negative|neutral",
  "confidence": 0.0-1.0,
  "key_phrases": ["string"],
  "suggested_action": "string"
}

Review: "The product arrived broken and customer service was unhelpful."
```

**XML/Tag-Based:**
```
Extract entities from the text. Use these tags:
<PERSON>...</PERSON>
<ORGANIZATION>...</ORGANIZATION>
<LOCATION>...</LOCATION>

Text: "Apple Inc. was founded by Steve Jobs in Cupertino, California."
```

**Function Calling / Tool Use:**
```python
functions = [
    {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City name"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location"]
        }
    }
]
```

## Context Window Management

**Techniques for long contexts:**

| Technique | How | When |
|---|---|---|
| Chunking | Split document into overlapping chunks | RAG, document Q&A |
| Summarization | Compress prior context | Multi-turn conversations |
| Hierarchical | Outline + detailed sections | Complex documents |
| Selective inclusion | Only include relevant sections | Many documents |

**Prompt compression:**
```
Instead of: "Please read this 5000-word article and summarize it"
Use: Summarize these key points: [bullet list of main arguments]
```

## Prompt Delimiters & Formatting

**Use clear separators to reduce ambiguity:**

```
### INSTRUCTION ###
Summarize the article below.

### ARTICLE ###
[article text]

### OUTPUT FORMAT ###
- Title: [title]
- Summary: [2-3 sentences]
- Key points: [bullet list]
```

**Preferred formats:**
- Markdown headers for sections
- XML tags for distinct content types
- Triple backticks for code
- Numbered lists for sequential instructions

## Prompt Chaining

Break complex tasks into sequential prompts:

```
Step 1: Extract key facts from the article.
Step 2: Organize facts into categories.
Step 3: Write a summary using the organized facts.
```

**Benefits:**
- Easier to debug each step
- Can reuse intermediate outputs
- Reduces token usage per call
- Allows human review between steps

## Style & Tone Control

| Desired Output | Prompt Addition |
|---|---|
| Concise | "Answer in 1 sentence." |
| Detailed | "Provide a comprehensive explanation with examples." |
| Formal | "Use academic/professional language." |
| Casual | "Explain like I'm a beginner." |
| Bullet points | "Format as a bulleted list." |
| Table | "Format as a markdown table." |
| Step-by-step | "Number each step." |

## Common Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Vague instructions | "Make it better" | Specific criteria: "Reduce to 100 words" |
| Overloading one prompt | Too many tasks | Split into chained prompts |
| Implicit assumptions | Model lacks context | Provide background explicitly |
| No output format specified | Inconsistent formatting | JSON schema or template |
| Negative instructions only | "Don't do X" | Reframe: "Do Y instead of X" |
| Jargon without definition | Misinterpretation | Define terms or use role prompting |
