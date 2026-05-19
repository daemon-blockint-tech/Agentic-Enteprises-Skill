# Agent Orchestration

## ReAct (Reasoning + Acting)

### Pattern
```
Thought: I need to find the current weather in Paris.
Action: get_weather(location="Paris")
Observation: {"temperature": 22, "condition": "sunny"}
Thought: I have the weather data. I can now answer the user.
Final Answer: It's 22°C and sunny in Paris.
```

### Implementation Template
```python
class ReActAgent:
    def __init__(self, tools, llm):
        self.tools = {t.name: t for t in tools}
        self.llm = llm
    
    def run(self, query, max_iterations=10):
        context = f"Question: {query}\n\n"
        
        for i in range(max_iterations):
            response = self.llm.complete(context + "Thought:")
            
            if "Final Answer:" in response:
                return response.split("Final Answer:")[-1].strip()
            
            action = self._parse_action(response)
            if action:
                tool = self.tools.get(action.name)
                observation = tool.run(**action.params)
                context += f"{response}\nObservation: {observation}\n\n"
            else:
                context += f"{response}\n"
        
        return "Max iterations reached without answer."
```

### Prompt Template
```
You are a helpful assistant that can use tools to answer questions.

Available tools:
{tool_descriptions}

Use this format:
Thought: [your reasoning about what to do]
Action: [tool_name]([param1]=[value1], [param2]=[value2])
Observation: [tool result will appear here]
...
Final Answer: [your answer to the user]

Question: {user_question}
```

## Plan-and-Solve

### Pattern
1. **Plan**: Break task into subtasks
2. **Execute**: Complete each subtask (may use tools)
3. **Verify**: Check correctness
4. **Refine**: Fix if needed

### Implementation
```python
def plan_and_solve(task, tools):
    # Step 1: Generate plan
    plan = llm.complete(f"Break this task into steps:\n{task}")
    steps = parse_plan(plan)
    
    results = []
    for step in steps:
        # Step 2: Execute with tools if needed
        result = execute_step(step, tools)
        results.append(result)
    
    # Step 3: Verify and synthesize
    final = llm.complete(f"Task: {task}\nSteps and results:\n{results}\n\nSynthesize the final answer.")
    return final
```

## Reflexion (Self-Improvement)

### Pattern
```
Attempt 1:
  Execute task → Get result
  Evaluate: Is this correct? → No, error is X
  Reflect: I made mistake X because I didn't check Y

Attempt 2:
  Execute task with reflection in context
  Evaluate: Is this correct? → Yes
  Return result
```

### Prompt
```
You attempted this task and got it wrong.

Your previous attempt: {previous_output}
Error: {error_description}

Reflect on what went wrong and try again.

Task: {task}
```

## Multi-Agent Systems

### Coordinator Pattern
```
Coordinator Agent:
  - Receives user request
  - Determines which specialist agents needed
  - Delegates subtasks
  - Synthesizes final answer

Specialist Agents:
  - CodeAgent: Handles programming tasks
  - DataAgent: Handles data analysis
  - ResearchAgent: Handles information retrieval
```

### Communication Protocol
```python
class Message:
    def __init__(self, from_agent, to_agent, content, message_type="task"):
        self.from_agent = from_agent
        self.to_agent = to_agent
        self.content = content
        self.type = message_type  # task, response, question, error
```

### Implementation Example
```python
coordinator = CoordinatorAgent(
    specialists=[CodeAgent(), DataAgent(), ResearchAgent()]
)

result = coordinator.run("Build a dashboard showing sales trends")
# Coordinator delegates: DataAgent fetches data, CodeAgent builds dashboard
```

## Tool Design Best Practices

### Tool Schema
```python
class Tool:
    name: str
    description: str  # Used by LLM to decide when to use
    parameters: dict  # JSON schema
    
    def run(self, **kwargs) -> str:
        # Execute and return string result
        pass
```

### Good Tool Descriptions
- Clear: "Search the web for current information"
- Specific: "Calculate the sum of a list of numbers"
- Scoped: "Query the user database by email or ID"

### Bad Tool Descriptions
- Vague: "Do something useful"
- Overlapping: Multiple tools for similar tasks
- Too powerful: "Execute any Python code" (security risk)

## Memory Management

### Types of Memory

| Type | Scope | Implementation |
|---|---|---|
| Working memory | Current conversation | Context window |
| Short-term memory | Session | In-memory buffer |
| Long-term memory | Across sessions | Vector database (Chroma, Pinecone) |
| Entity memory | Facts about users/entities | Key-value store |

### Retrieval-Augmented Generation (RAG)

```python
# Store documents
vector_store.add_documents(documents)

# Retrieve relevant context
context = vector_store.similarity_search(query, k=5)

# Generate with context
prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
response = llm.complete(prompt)
```

### Conversation Memory

```python
class ConversationBuffer:
    def __init__(self, max_tokens=4000):
        self.messages = []
        self.max_tokens = max_tokens
    
    def add(self, role, content):
        self.messages.append({"role": role, "content": content})
        self._trim()
    
    def _trim(self):
        while self.token_count > self.max_tokens:
            self.messages.pop(0)  # Remove oldest
```

## Error Handling in Agents

| Error Type | Response |
|---|---|
| Tool failure | Retry once, then escalate to user |
| Timeout | Return partial results with explanation |
| Invalid tool output | Log error, ask user for clarification |
| Max iterations | Return best effort with caveat |
| Hallucination | Cross-check with retrieval, add citations |

## Agent Evaluation

| Metric | How to Measure |
|---|---|
| Task success rate | % of tasks completed correctly |
| Steps to completion | Average number of reasoning steps |
| Tool use accuracy | % of correct tool selections |
| User satisfaction | Post-task rating |
| Cost per task | Token usage + API calls |
| Latency | Time from request to final answer |
