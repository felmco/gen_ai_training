# Complete Google Agent Development Kit (ADK) Python Tutorial

## Table of Contents

1. [Introduction](#introduction)
2. [Installation & Setup](#installation--setup)
3. [Core Concepts](#core-concepts)
4. [Quick Start Guide](#quick-start-guide)
5. [LLM Agents](#llm-agents)
6. [Tools](#tools)
7. [Workflow Agents](#workflow-agents)
8. [Multi-Agent Systems](#multi-agent-systems)
9. [Custom Agents](#custom-agents)
10. [Sessions, State, and Memory](#sessions-state-and-memory)
11. [Models & Authentication](#models--authentication)
12. [Evaluation & Testing](#evaluation--testing)
13. [Deployment](#deployment)
14. [Advanced Topics](#advanced-topics)
15. [Model Context Protocol (MCP)](#model-context-protocol-mcp)
16. [Best Practices](#best-practices)

---

## Introduction

The Agent Development Kit (ADK) is a flexible and modular framework for developing and deploying AI agents. While optimized for Gemini and the Google ecosystem, ADK is model-agnostic, deployment-agnostic, and built for compatibility with other frameworks.

### What is an Agent?

In ADK, an **Agent** is a self-contained execution unit designed to act autonomously to achieve specific goals. Agents can:
- Perform tasks
- Interact with users
- Utilize external tools
- Coordinate with other agents

### Key Features

- **Flexible Orchestration**: Define workflows using workflow agents (Sequential, Parallel, Loop) for predictable pipelines, or leverage LLM-driven dynamic routing for adaptive behavior
- **Multi-Agent Architecture**: Build modular and scalable applications by composing multiple specialized agents in a hierarchy
- **Rich Tool Ecosystem**: Equip agents with diverse capabilities using pre-built tools, custom functions, or even other agents as tools
- **Deployment Ready**: Containerize and deploy your agents anywhere – run locally, scale with Vertex AI Agent Engine, or integrate into custom infrastructure
- **Built-in Evaluation**: Systematically assess agent performance by evaluating both final response quality and step-by-step execution
- **Building Safe and Secure Agents**: Implement security and safety patterns and best practices into your agent's design

---

## Installation & Setup

### Prerequisites

Before starting, ensure you have:
- **Python 3.9 or later**
- **pip** for installing packages

### Installation Steps

#### 1. Create and Activate a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv .venv

# Activate on macOS/Linux
source .venv/bin/activate

# Activate on Windows CMD
.venv\Scripts\activate.bat

# Activate on Windows PowerShell
.venv\Scripts\Activate.ps1
```

#### 2. Install ADK

```bash
pip install google-adk
```

#### 3. Create Your First Agent Project

```bash
adk create my_agent
```

This creates the following structure:

```
my_agent/
├── agent.py          # Main agent code
├── .env              # API keys or project IDs
└── __init__.py
```

---

## Core Concepts

### Agent Types

ADK provides three core agent categories:

#### 1. **LLM Agents** (`LlmAgent`, `Agent`)
- Use Large Language Models as their core engine
- Understand natural language, reason, plan, and generate responses
- Dynamically decide which tools to use
- Ideal for flexible, language-centric tasks

#### 2. **Workflow Agents** (`SequentialAgent`, `ParallelAgent`, `LoopAgent`)
- Control execution flow of other agents in predefined patterns
- Deterministic and predictable execution
- Perfect for structured processes

#### 3. **Custom Agents**
- Created by extending `BaseAgent` directly
- Implement unique operational logic
- Cater to highly tailored application requirements

### Core Architecture Components

- **BaseAgent**: Foundation class for all agents
- **Session**: Manages a single conversation between user and agent
- **State**: Temporary data stored within a session
- **Memory**: Long-term knowledge store across multiple sessions
- **Runner**: Coordinates agent execution and manages the event loop
- **Event**: Basic unit of communication representing actions
- **Tools**: Functions that give agents capabilities

---

## Quick Start Guide

### Simple Time and Weather Agent

Create a file `agent.py`:

```python
from google.adk.agents.llm_agent import Agent
import datetime
from zoneinfo import ZoneInfo

# Define tool functions
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.
    
    Args:
        city (str): The name of the city for which to retrieve the current time.
        
    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have timezone information for {city}."
        }
    
    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    return {"status": "success", "report": report}


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.
    
    Args:
        city (str): The name of the city for which to retrieve the weather report.
        
    Returns:
        dict: status and result or error msg.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": "The weather in New York is sunny with a temperature of 25 degrees Celsius (77 degrees Fahrenheit)."
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available."
        }


# Define the agent
root_agent = Agent(
    model='gemini-2.0-flash',
    name='weather_time_agent',
    description="Agent to answer questions about the time and weather in a city.",
    instruction="You are a helpful assistant that tells the current time and weather in cities. Use the appropriate tools for this purpose.",
    tools=[get_current_time, get_weather]
)
```

### Set API Key

Create a `.env` file in your project directory:

```bash
# For Google AI Studio (recommended for getting started)
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

**Get an API key from [Google AI Studio](https://aistudio.google.com/apikey)**

### Running Your Agent

#### Option 1: Command-Line Interface

```bash
adk run
```

#### Option 2: Web Interface

```bash
adk web
```

Then open http://localhost:8000 in your browser.

### Example Prompts to Try

- "What is the weather in New York?"
- "What is the time in New York?"
- "What is the weather and time in New York?"

---

## LLM Agents

The `LlmAgent` (often aliased simply as `Agent`) is a core component in ADK, acting as the "thinking" part of your application. It leverages the power of a Large Language Model (LLM) for reasoning, understanding natural language, making decisions, generating responses, and interacting with tools.

### Basic Agent Configuration

```python
from google.adk.agents import LlmAgent

# Define a tool
def get_capital_city(country: str) -> str:
    """Retrieves the capital city for a given country."""
    capitals = {
        "france": "Paris",
        "japan": "Tokyo",
        "canada": "Ottawa"
    }
    return capitals.get(
        country.lower(),
        f"Sorry, I don't know the capital of {country}."
    )

# Create the agent
capital_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="capital_agent",
    description="Answers user questions about the capital city of a given country.",
    instruction="""You are an agent that provides the capital city of a country.
    
When a user asks for the capital of a country:
1. Identify the country name from the user's query.
2. Use the `get_capital_city` tool to find the capital.
3. Respond clearly to the user, stating the capital city.

Example Query: "What's the capital of France?"
Example Response: "The capital of France is Paris."
""",
    tools=[get_capital_city]
)
```

### Key Parameters

#### Required Parameters

- **`name`** (str): Unique identifier for the agent
- **`model`** (str): The LLM to use (e.g., `"gemini-2.0-flash"`)

#### Optional Parameters

- **`description`** (str): Concise summary of agent's capabilities (crucial for multi-agent systems)
- **`instruction`** (str or function): Guides the agent's behavior, personality, and tool usage
- **`tools`** (list): Functions or tool instances the agent can use
- **`generate_content_config`**: Fine-tune LLM generation parameters
- **`input_schema`**: Define expected input structure
- **`output_schema`**: Define desired output structure
- **`output_key`** (str): Store agent's response in session state under this key
- **`planner`**: Enable multi-step reasoning (BuiltInPlanner or PlanReActPlanner)
- **`code_executor`**: Allow code execution
- **`include_contents`**: Control conversation history (`'default'` or `'none'`)

### Instructions Best Practices

```python
instruction = """You are a helpful assistant specializing in geography.

**Your Role:**
- Answer questions about capitals, countries, and geographic facts
- Use tools when needed to provide accurate information
- Be concise but informative

**Guidelines:**
- Always verify information using the provided tools
- If you don't have information, clearly state this
- Format responses in a friendly, conversational tone

**Tool Usage:**
- Use `get_capital_city` when asked about capitals
- The tool takes a country name as input
"""
```

### Dynamic Instructions with State Variables

You can use template syntax to insert dynamic values:

```python
instruction = """You are processing data for country: {country_name}

The user's previous query was: {last_query}

Artifact content: {artifact.user_data}
"""
```

- `{var}` inserts the value of `state['var']`
- `{artifact.name}` inserts text content of artifact named `name`
- `{var?}` ignores error if variable doesn't exist

### Structured Input/Output with Schemas

```python
from pydantic import BaseModel, Field

class CountryInput(BaseModel):
    country: str = Field(description="The country to get information about.")

class CapitalOutput(BaseModel):
    capital: str = Field(description="The capital of the country.")
    population_estimate: str = Field(description="Estimated population of the capital.")

structured_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="structured_capital_agent",
    instruction="""Given a country, respond ONLY with a JSON object containing the capital and population estimate.
    Format: {"capital": "city_name", "population_estimate": "X million"}""",
    input_schema=CountryInput,
    output_schema=CapitalOutput,
    output_key="capital_info"
)
```

### Fine-Tuning LLM Generation

```python
from google.genai import types

agent = LlmAgent(
    model="gemini-2.0-flash",
    name="precise_agent",
    instruction="You are a precise, deterministic assistant.",
    tools=[],
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,  # More deterministic (0.0-1.0)
        max_output_tokens=250,
        top_p=0.8,
        top_k=40,
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
            )
        ]
    )
)
```

### Using Planners

#### Built-In Planner (Gemini Thinking)

```python
from google.adk.planners import BuiltInPlanner
from google.genai.types import ThinkingConfig

# Create thinking config
thinking_config = ThinkingConfig(
    include_thoughts=True,  # Include reasoning in response
    thinking_budget=256     # Limit thinking tokens
)

# Create planner
planner = BuiltInPlanner(thinking_config=thinking_config)

# Use in agent
agent = LlmAgent(
    model="gemini-2.5-pro-preview-03-25",
    name="thinking_agent",
    instruction="You are an agent that uses step-by-step reasoning.",
    planner=planner,
    tools=[get_weather]
)
```

#### Plan-ReAct Planner

```python
from google.adk.planners import PlanReActPlanner

planner = PlanReActPlanner()

agent = LlmAgent(
    model="gemini-2.0-flash",
    name="react_agent",
    instruction="You create plans and execute them step by step.",
    planner=planner,
    tools=[search_tool, calculator_tool]
)
```

The output will follow this structure:
```
/*PLANNING*/
1. First, I'll search for information
2. Then I'll analyze the results
3. Finally, I'll provide a summary

/*ACTION*/
[Tool calls happen here]

/*REASONING*/
The search results show that...

/*FINAL_ANSWER*/
Here is the answer...
```

### Running an Agent

```python
import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Constants
APP_NAME = "my_app"
USER_ID = "user_123"
SESSION_ID = "session_abc"

# Create session service and runner
session_service = InMemorySessionService()
runner = Runner(
    agent=capital_agent,
    app_name=APP_NAME,
    session_service=session_service
)

# Create session
async def main():
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    
    # Send user message
    user_message = types.Content(
        role='user',
        parts=[types.Part(text="What's the capital of France?")]
    )
    
    # Run agent
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_message
    ):
        if event.is_final_response() and event.content:
            print("Agent:", event.content.parts[0].text)

# Run
asyncio.run(main())
```

---

## Tools

Tools give your agents capabilities beyond the LLM's built-in knowledge. They allow agents to interact with the outside world, perform calculations, fetch real-time data, or execute specific actions.

### Creating Custom Tools

#### Basic Function Tool

The simplest way to create a tool is to define a Python function:

```python
def get_weather(city: str) -> dict:
    """Retrieves the current weather for a specified city.
    
    Args:
        city (str): The name of the city for which to retrieve weather.
        
    Returns:
        dict: Weather information with status and report.
    """
    # Implementation
    weather_data = {
        "new york": "Sunny, 25°C",
        "london": "Cloudy, 18°C"
    }
    
    if city.lower() in weather_data:
        return {
            "status": "success",
            "report": weather_data[city.lower()]
        }
    else:
        return {
            "status": "error",
            "error_message": f"No weather data for {city}"
        }

# Add to agent
agent = LlmAgent(
    model="gemini-2.0-flash",
    name="weather_agent",
    instruction="Use the get_weather tool to answer weather questions.",
    tools=[get_weather]  # ADK automatically wraps it as FunctionTool
)
```

### Tool Design Best Practices

#### 1. Write Excellent Docstrings

The LLM relies on docstrings to understand:
- What the tool does
- When to use it
- What arguments it requires

```python
def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> dict:
    """Calculates the distance between two geographic coordinates using the Haversine formula.
    
    Use this tool when the user asks about distance between two locations.
    This tool is especially useful for travel planning or geographic queries.
    
    Args:
        lat1 (float): Latitude of the first location (e.g., 40.7128 for NYC)
        lon1 (float): Longitude of the first location (e.g., -74.0060 for NYC)
        lat2 (float): Latitude of the second location
        lon2 (float): Longitude of the second location
        
    Returns:
        dict: Contains 'status' ('success' or 'error'), 'distance_km', and 'distance_miles'
    """
    # Implementation here
    pass
```

#### 2. Return Descriptive Dictionaries

```python
def search_database(query: str) -> dict:
    """Searches the product database."""
    try:
        results = database.search(query)
        return {
            "status": "success",
            "count": len(results),
            "results": results,
            "message": f"Found {len(results)} products matching '{query}'"
        }
    except DatabaseError as e:
        return {
            "status": "error",
            "error_type": "database_error",
            "error_message": str(e),
            "suggestion": "Try a different search term or check database connection"
        }
```

#### 3. Include Status Indicators

Always include a `status` key to clearly indicate the outcome:

```python
def process_order(order_id: str) -> dict:
    """Processes a customer order."""
    if not order_id:
        return {
            "status": "error",
            "error_message": "Order ID is required"
        }
    
    try:
        result = process(order_id)
        return {
            "status": "success",
            "order_id": order_id,
            "confirmation": result.confirmation_number
        }
    except OrderNotFound:
        return {
            "status": "error",
            "error_message": f"Order {order_id} not found"
        }
    except PaymentError:
        return {
            "status": "pending",
            "message": "Payment processing in progress"
        }
```

### Using Tool Context

Access session state, services, and control flow within tools:

```python
from google.adk.tools.tool_context import ToolContext

def save_user_preference(
    preference_name: str,
    preference_value: str,
    tool_context: ToolContext
) -> dict:
    """Saves a user preference to the session state.
    
    Args:
        preference_name: Name of the preference to save
        preference_value: Value of the preference
        tool_context: Automatically injected by ADK (DO NOT include in docstring)
    """
    # Access session state
    tool_context.state[f"pref_{preference_name}"] = preference_value
    
    # Access invocation context
    invocation_id = tool_context.invocation_context.invocation_id
    
    # Control agent flow
    # tool_context.actions.skip_summarization = True
    # tool_context.actions.transfer_to_agent = "another_agent"
    # tool_context.actions.end_invocation = True
    
    return {
        "status": "success",
        "message": f"Saved preference: {preference_name} = {preference_value}"
    }
```

**Important**: Don't include `tool_context` in the docstring - it's automatically injected.

### Built-in Tools

#### Code Execution

```python
from google.adk.code_executors import LocalCodeExecutor

code_executor = LocalCodeExecutor()

agent = LlmAgent(
    model="gemini-2.0-flash",
    name="code_agent",
    instruction="You can write and execute Python code to solve problems.",
    code_executor=code_executor
)
```

#### Memory/Load Memory Tool

```python
from google.adk.tools import load_memory
from google.adk.memory import InMemoryMemoryService

memory_service = InMemoryMemoryService()

agent = LlmAgent(
    model="gemini-2.0-flash",
    name="memory_agent",
    instruction="Use the 'load_memory' tool if the answer might be in past conversations.",
    tools=[load_memory]
)

# When running, provide memory service
runner = Runner(
    agent=agent,
    app_name=APP_NAME,
    session_service=session_service,
    memory_service=memory_service
)
```

### Agent as Tool

You can use other agents as tools:

```python
from google.adk.tools import AgentTool

# Create specialized agents
weather_agent = LlmAgent(
    name="weather_expert",
    model="gemini-2.0-flash",
    description="Provides detailed weather information",
    instruction="You are a weather expert.",
    tools=[get_weather]
)

news_agent = LlmAgent(
    name="news_expert",
    model="gemini-2.0-flash",
    description="Provides latest news",
    instruction="You are a news expert.",
    tools=[get_news]
)

# Use them as tools in a coordinator agent
coordinator = LlmAgent(
    name="coordinator",
    model="gemini-2.0-flash",
    instruction="Delegate tasks to specialized agents.",
    tools=[
        AgentTool(weather_agent),
        AgentTool(news_agent)
    ]
)
```

---

## Workflow Agents

Workflow agents control the execution flow of other agents in predefined, deterministic patterns without using an LLM for flow control. They're perfect for structured processes needing predictable execution.

### Sequential Agent

Executes sub-agents one after another in order.

```python
from google.adk.agents import SequentialAgent, LlmAgent

# Define sub-agents
code_writer = LlmAgent(
    name="CodeWriter",
    model="gemini-2.0-flash",
    instruction="Write Python code based on the user's request.",
    output_key="generated_code"
)

code_reviewer = LlmAgent(
    name="CodeReviewer",
    model="gemini-2.0-flash",
    instruction="""Review the code: {generated_code}
    
Provide constructive feedback. If the code is good, say "No major issues found."
""",
    output_key="review_comments"
)

code_refactorer = LlmAgent(
    name="CodeRefactorer",
    model="gemini-2.0-flash",
    instruction="""Refactor the code based on review.

Original Code: {generated_code}
Review Comments: {review_comments}

If review says "No major issues found", return the original code unchanged.
""",
    output_key="refactored_code"
)

# Create sequential pipeline
code_pipeline = SequentialAgent(
    name="CodePipeline",
    description="Executes code writing, reviewing, and refactoring in sequence.",
    sub_agents=[code_writer, code_reviewer, code_refactorer]
)
```

**Key Points:**
- Agents run in the order specified
- Each agent can read from and write to session state
- Use `output_key` to pass data between agents
- Template syntax `{var}` in instructions reads from state

### Parallel Agent

Executes multiple sub-agents concurrently.

```python
from google.adk.agents import ParallelAgent, LlmAgent

# Define research agents
renewable_researcher = LlmAgent(
    name="RenewableEnergyResearcher",
    model="gemini-2.0-flash",
    instruction="Research renewable energy sources.",
    output_key="renewable_energy_result",
    tools=[web_search_tool]
)

ev_researcher = LlmAgent(
    name="EVResearcher",
    model="gemini-2.0-flash",
    instruction="Research electric vehicle technology.",
    output_key="ev_technology_result",
    tools=[web_search_tool]
)

carbon_researcher = LlmAgent(
    name="CarbonCaptureResearcher",
    model="gemini-2.0-flash",
    instruction="Research carbon capture methods.",
    output_key="carbon_capture_result",
    tools=[web_search_tool]
)

# Create parallel agent
parallel_research = ParallelAgent(
    name="ParallelResearch",
    description="Conducts parallel research on multiple topics.",
    sub_agents=[renewable_researcher, ev_researcher, carbon_researcher]
)

# Merge results after parallel execution
merger_agent = LlmAgent(
    name="MergerAgent",
    model="gemini-2.0-flash",
    instruction="""Synthesize findings from the research agents.

**Input Summaries:**
* Renewable Energy: {renewable_energy_result}
* Electric Vehicles: {ev_technology_result}
* Carbon Capture: {carbon_capture_result}

Create a structured report based ONLY on these findings.
""",
    output_key="final_report"
)

# Combine with sequential for overall pipeline
research_pipeline = SequentialAgent(
    name="ResearchPipeline",
    description="Parallel research followed by synthesis.",
    sub_agents=[parallel_research, merger_agent]
)
```

**Key Points:**
- All sub-agents start executing at approximately the same time
- Ideal for independent operations (data retrieval, computations)
- No shared state during execution (each writes independently)
- Results collected after all agents complete

### Loop Agent

Repeatedly executes sub-agents until a termination condition is met.

```python
from google.adk.agents import LoopAgent, SequentialAgent, LlmAgent
from google.adk.tools.tool_context import ToolContext

# Exit tool for loop termination
def exit_loop(tool_context: ToolContext) -> dict:
    """Signals the loop to stop execution."""
    tool_context.actions.exit_loop = True
    return {"status": "success", "message": "Loop terminated"}

# Define agents for iterative refinement
critic_agent = LlmAgent(
    name="CriticAgent",
    model="gemini-2.0-flash",
    instruction="""Review the document: {current_document}

Provide constructive criticism. If the document is good enough, say "No major issues found."
""",
    output_key="criticism",
    include_contents='none'  # Don't include conversation history
)

refiner_agent = LlmAgent(
    name="RefinerAgent",
    model="gemini-2.0-flash",
    instruction="""Refine the document based on criticism.

Current Document: {current_document}
Criticism: {criticism}

If criticism says "No major issues found", call the exitLoop tool.
Otherwise, output the refined document.
""",
    output_key="current_document",
    include_contents='none',
    tools=[exit_loop]
)

# Create loop
refinement_loop = LoopAgent(
    name="RefinementLoop",
    description="Repeatedly refines document with critique.",
    sub_agents=[critic_agent, refiner_agent],
    max_iterations=5  # Safety limit
)

# Initial writer
initial_writer = LlmAgent(
    name="InitialWriter",
    model="gemini-2.0-flash",
    instruction="Write an initial document about: {topic}",
    output_key="current_document"
)

# Complete pipeline
writing_pipeline = SequentialAgent(
    name="WritingPipeline",
    description="Writes and iteratively refines a document.",
    sub_agents=[initial_writer, refinement_loop]
)
```

**Loop Termination Methods:**

1. **Exit Tool**: Call a tool that sets `tool_context.actions.exit_loop = True`
2. **Max Iterations**: Automatically stops after `max_iterations`
3. **Transfer**: If an agent transfers to another agent, the loop exits

**Key Points:**
- Use for iterative refinement, retry logic, or quality checks
- Set `max_iterations` as a safety measure
- Use `include_contents='none'` to prevent context from growing
- Sub-agents execute sequentially within each iteration

---

## Multi-Agent Systems

In ADK, a multi-agent system is an application where different agents, often forming a hierarchy, collaborate or coordinate to achieve a larger goal.

### Agent Hierarchy

Agents can have parent-child relationships:

```python
from google.adk.agents import LlmAgent

# Define child agents
greeter = LlmAgent(
    name="Greeter",
    model="gemini-2.0-flash",
    description="Handles greetings",
    instruction="Greet the user warmly."
)

task_doer = LlmAgent(
    name="TaskExecutor",
    model="gemini-2.0-flash",
    description="Executes specific tasks",
    instruction="Execute the requested task."
)

# Create parent agent with sub-agents
coordinator = LlmAgent(
    name="Coordinator",
    model="gemini-2.0-flash",
    description="I coordinate greetings and tasks.",
    instruction="Route user requests to appropriate sub-agents.",
    sub_agents=[greeter, task_doer]  # Establish hierarchy
)

# Parent-child relationships are automatically set
assert greeter.parent_agent == coordinator
assert task_doer.parent_agent == coordinator
```

### LLM-Driven Delegation

Agents can dynamically transfer control to sub-agents:

```python
# Root agent with specialized sub-agents
greeting_agent = LlmAgent(
    name="GreetingAgent",
    model="gemini-2.0-flash",
    description="Handles simple greetings and farewells",
    instruction="Respond to greetings warmly and professionally."
)

farewell_agent = LlmAgent(
    name="FarewellAgent",
    model="gemini-2.0-flash",
    description="Handles goodbyes",
    instruction="Say goodbye in a friendly manner."
)

weather_agent = LlmAgent(
    name="WeatherAgent",
    model="gemini-2.0-flash",
    description="Provides weather information",
    instruction="Use the get_weather tool to answer weather questions.",
    tools=[get_weather]
)

root_agent = LlmAgent(
    name="RootAgent",
    model="gemini-2.0-flash",
    description="Main coordinator",
    instruction="""You coordinate a team of specialized agents:

- GreetingAgent: Handles greetings
- FarewellAgent: Handles goodbyes
- WeatherAgent: Provides weather info

Analyze the user's request and delegate to the appropriate agent.
For weather queries, transfer to WeatherAgent.
For greetings, transfer to GreetingAgent.
For goodbyes, transfer to FarewellAgent.
""",
    sub_agents=[greeting_agent, farewell_agent, weather_agent]
)
```

**How it works:**
- The LLM analyzes the user's request
- If it determines a sub-agent is better suited, it generates a transfer action
- Control passes to the sub-agent
- The sub-agent processes the request using its own model, instructions, and tools

### Shared Session State

Agents communicate by reading/writing to session state:

```python
validator = LlmAgent(
    name="Validator",
    model="gemini-2.0-flash",
    instruction="Validate the input data.",
    output_key="validation_status"  # Writes to state['validation_status']
)

processor = LlmAgent(
    name="Processor",
    model="gemini-2.0-flash",
    instruction="""Process data if validation passed.

Validation Status: {validation_status}

Only proceed if status is 'valid'.
""",
    output_key="result"  # Writes to state['result']
)

reporter = LlmAgent(
    name="Reporter",
    model="gemini-2.0-flash",
    instruction="""Report the processing result.

Result: {result}

Create a formatted report.
"""
)

pipeline = SequentialAgent(
    name="DataPipeline",
    sub_agents=[validator, processor, reporter]
)
```

### Communication Patterns

#### 1. **Sequential Processing with State**
```python
# Agent A -> saves to state['data']
# Agent B -> reads state['data'], processes, saves to state['result']
# Agent C -> reads state['result'], creates final output
```

#### 2. **Parallel Processing with Merge**
```python
# Multiple agents run in parallel, each saving to different state keys
# Merger agent reads all keys and synthesizes results
```

#### 3. **Iterative Refinement**
```python
# Loop: Critic evaluates state['document'], saves state['feedback']
# Refiner reads state['feedback'], improves state['document']
# Repeat until satisfied
```

### Agent Team Example

Complete example with session management:

```python
import asyncio
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

APP_NAME = "agent_team_app"
USER_ID = "user_123"
SESSION_ID = "session_001"

# Define specialized agents
weather_agent = LlmAgent(
    name="WeatherExpert",
    model="gemini-2.0-flash",
    description="Provides weather information",
    instruction="Use the get_weather tool to provide accurate weather info.",
    tools=[get_weather]
)

news_agent = LlmAgent(
    name="NewsExpert",
    model="gemini-2.0-flash",
    description="Provides latest news",
    instruction="Search and summarize recent news.",
    tools=[get_news]
)

# Root coordinator
root_agent = LlmAgent(
    name="Coordinator",
    model="gemini-2.0-flash",
    description="Routes requests to specialized agents",
    instruction="""You coordinate a team of experts:
    
- WeatherExpert: For weather queries
- NewsExpert: For news queries

Analyze the request and delegate appropriately.
""",
    sub_agents=[weather_agent, news_agent]
)

async def main():
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    # Create session
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    
    # Send message
    user_message = types.Content(
        role='user',
        parts=[types.Part(text="What's the weather like in New York and any recent news?")]
    )
    
    # Run agent
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_message
    ):
        if event.is_final_response() and event.content:
            print("Response:", event.content.parts[0].text)

asyncio.run(main())
```

---

## Custom Agents

Custom agents provide ultimate flexibility by extending `BaseAgent` directly and implementing custom orchestration logic.

### When to Use Custom Agents

- Implementing workflows that don't fit standard patterns
- Conditional branching based on agent outputs
- Complex decision trees
- Dynamic sub-agent selection
- Specialized error handling

### Basic Custom Agent Structure

```python
from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from typing import AsyncGenerator

class CustomWorkflowAgent(BaseAgent):
    """Custom agent with conditional logic."""
    
    async def _run_async_impl(
        self,
        ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        """
        Core execution logic.
        
        Args:
            ctx: Provides access to session.state and other runtime info
            
        Yields:
            Event: Events produced by sub-agents or custom logic
        """
        # Access session state
        current_state = ctx.session.state
        
        # Run first sub-agent
        first_agent = self.sub_agents[0]
        async for event in first_agent.run_async(ctx):
            yield event
        
        # Check result and decide next step
        if current_state.get('validation') == 'passed':
            # Run second sub-agent
            second_agent = self.sub_agents[1]
            async for event in second_agent.run_async(ctx):
                yield event
        else:
            # Run alternative agent
            fallback_agent = self.sub_agents[2]
            async for event in fallback_agent.run_async(ctx):
                yield event
```

### Conditional Story Generation Example

```python
from google.adk.agents import BaseAgent, LlmAgent, LoopAgent, SequentialAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from typing import AsyncGenerator

GEMINI_MODEL = "gemini-2.0-flash"

# Define sub-agents
story_generator = LlmAgent(
    name="StoryGenerator",
    model=GEMINI_MODEL,
    instruction="Write a creative story about: {topic}",
    output_key="current_story"
)

critic = LlmAgent(
    name="Critic",
    model=GEMINI_MODEL,
    instruction="Critique the story: {current_story}",
    output_key="criticism"
)

reviser = LlmAgent(
    name="Reviser",
    model=GEMINI_MODEL,
    instruction="""Revise the story based on criticism.

Story: {current_story}
Criticism: {criticism}
""",
    output_key="current_story"
)

grammar_check = LlmAgent(
    name="GrammarCheck",
    model=GEMINI_MODEL,
    instruction="""Check grammar of: {current_story}

Output 'Grammar is good!' or list corrections.
""",
    output_key="grammar_suggestions"
)

tone_check = LlmAgent(
    name="ToneCheck",
    model=GEMINI_MODEL,
    instruction="""Analyze tone of: {current_story}

Output only one word: 'positive', 'negative', or 'neutral'.
""",
    output_key="tone_check_result"
)

# Create workflow agents
revision_loop = LoopAgent(
    name="RevisionLoop",
    sub_agents=[critic, reviser],
    max_iterations=3
)

post_processor = SequentialAgent(
    name="PostProcessor",
    sub_agents=[grammar_check, tone_check]
)

# Custom agent with conditional regeneration
class StoryFlowAgent(BaseAgent):
    """Custom agent that regenerates story if tone is negative."""
    
    def __init__(self):
        super().__init__(
            name="StoryFlowAgent",
            sub_agents=[story_generator, revision_loop, post_processor]
        )
    
    async def _run_async_impl(
        self,
        ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        """Execute story workflow with conditional regeneration."""
        
        # Initial generation
        async for event in story_generator.run_async(ctx):
            yield event
        
        # Revision loop
        async for event in revision_loop.run_async(ctx):
            yield event
        
        # Post-processing (grammar + tone check)
        async for event in post_processor.run_async(ctx):
            yield event
        
        # Check tone and conditionally regenerate
        tone_result = ctx.session.state.get("tone_check_result", "").lower()
        
        if tone_result == "negative":
            # Regenerate story
            ctx.session.state["topic"] = ctx.session.state.get("topic", "") + " (make it more positive)"
            
            async for event in story_generator.run_async(ctx):
                yield event
            
            # Re-run post-processing
            async for event in post_processor.run_async(ctx):
                yield event

# Use the custom agent
root_agent = StoryFlowAgent()
```

### Key Points for Custom Agents

1. **Inherit from BaseAgent**: Always extend `BaseAgent`
2. **Implement `_run_async_impl`**: This is where custom logic lives
3. **Yield Events**: Use `async for event in agent.run_async(ctx): yield event`
4. **Access State**: Read/write via `ctx.session.state`
5. **Manage Sub-Agents**: Store in `self.sub_agents` list
6. **Handle Errors**: Implement appropriate try-except blocks

---

## Sessions, State, and Memory

Understanding how context is managed is crucial for building sophisticated agents.

### Session

A **Session** represents a single, ongoing interaction between a user and your agent system.

```python
from google.adk.sessions import InMemorySessionService

session_service = InMemorySessionService()

# Create a session
session = await session_service.create_session(
    app_name="my_app",
    user_id="user_123",
    session_id="session_abc"
)

# Session contains:
# - events: Chronological sequence of messages and actions
# - state: Temporary data dictionary for this conversation
```

### State

**State** (`session.state`) is a dictionary that stores temporary data within a session.

```python
# Write to state
session.state["user_preference"] = "detailed_responses"
session.state["last_query"] = "weather in Paris"

# Read from state
preference = session.state.get("user_preference")

# Use in agent instructions with templates
instruction = """
User prefers: {user_preference}
Last query was: {last_query}

Respond accordingly.
"""
```

**State Scope:**

- **Regular State**: Persists across all turns in a session
  - `session.state["key"] = value`
  
- **Temporary State**: Only exists for one invocation (single user query)
  - `session.state["temp:key"] = value`
  - Automatically cleared after invocation completes

### Memory

**Memory** represents long-term knowledge that spans multiple sessions.

#### Setting Up Memory

```python
from google.adk.memory import InMemoryMemoryService
from google.adk.tools import load_memory
from google.adk.runners import Runner

# Create services
session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()

# Agent that can use memory
info_capture_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="InfoCaptureAgent",
    instruction="Acknowledge the user's statement."
)

memory_recall_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="MemoryRecallAgent",
    instruction="""Answer the user's question.

Use the 'load_memory' tool if the answer might be in past conversations.
""",
    tools=[load_memory]
)

# Create runner with memory service
runner = Runner(
    agent=info_capture_agent,
    app_name="memory_app",
    session_service=session_service,
    memory_service=memory_service
)
```

#### Memory Workflow

```python
async def memory_example():
    # --- Turn 1: Capture Information ---
    session1 = await session_service.create_session(
        app_name="memory_app",
        user_id="user_123",
        session_id="session_001"
    )
    
    user_input1 = types.Content(
        parts=[types.Part(text="My favorite project is Project Alpha.")],
        role="user"
    )
    
    async for event in runner.run_async(
        user_id="user_123",
        session_id="session_001",
        new_message=user_input1
    ):
        if event.is_final_response():
            print("Captured:", event.content.parts[0].text)
    
    # Add session to memory
    await memory_service.add_session_to_memory(session1)
    
    # --- Turn 2: Recall from Memory (Different Session) ---
    runner2 = Runner(
        agent=memory_recall_agent,
        app_name="memory_app",
        session_service=session_service,
        memory_service=memory_service
    )
    
    session2 = await session_service.create_session(
        app_name="memory_app",
        user_id="user_123",
        session_id="session_002"
    )
    
    user_input2 = types.Content(
        parts=[types.Part(text="What's my favorite project?")],
        role="user"
    )
    
    async for event in runner2.run_async(
        user_id="user_123",
        session_id="session_002",
        new_message=user_input2
    ):
        if event.is_final_response():
            print("Recalled:", event.content.parts[0].text)
            # Output: "Your favorite project is Project Alpha."
```

#### Memory Service Types

- **InMemoryMemoryService**: Stores memory in RAM (for testing/development)
- **Agent Engine Memory**: Cloud-based persistent memory (for production)

### Complete Session Management Example

```python
import asyncio
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.memory import InMemoryMemoryService
from google.adk.tools import load_memory
from google.genai import types

APP_NAME = "session_demo"
USER_ID = "user_456"

# Create agents
info_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="InfoAgent",
    instruction="Store user information in session state.",
    output_key="info_stored"
)

query_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="QueryAgent",
    instruction="""Answer questions using session state and memory.

Current session state: {info_stored?}

Use load_memory tool for info from past sessions.
""",
    tools=[load_memory]
)

async def main():
    # Services
    session_service = InMemorySessionService()
    memory_service = InMemoryMemoryService()
    
    # Session 1: Store info
    runner1 = Runner(
        agent=info_agent,
        app_name=APP_NAME,
        session_service=session_service,
        memory_service=memory_service
    )
    
    session1 = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id="session_001"
    )
    
    # Store preference
    msg1 = types.Content(
        role='user',
        parts=[types.Part(text="I prefer concise responses.")]
    )
    
    async for event in runner1.run_async(USER_ID, "session_001", msg1):
        pass
    
    # Add to memory
    await memory_service.add_session_to_memory(session1)
    
    # Session 2: Query info
    runner2 = Runner(
        agent=query_agent,
        app_name=APP_NAME,
        session_service=session_service,
        memory_service=memory_service
    )
    
    session2 = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id="session_002"
    )
    
    msg2 = types.Content(
        role='user',
        parts=[types.Part(text="What are my preferences?")]
    )
    
    async for event in runner2.run_async(USER_ID, "session_002", msg2):
        if event.is_final_response():
            print(event.content.parts[0].text)

asyncio.run(main())
```

---

## Models & Authentication

ADK is designed for flexibility, allowing integration with various LLMs.

### Google AI Studio (Gemini API)

Easiest way to get started:

1. Get API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Set in `.env` file:

```bash
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

3. Use in agent:

```python
agent = LlmAgent(
    model="gemini-2.0-flash",  # or gemini-2.5-pro, etc.
    name="my_agent",
    instruction="You are a helpful assistant."
)
```

### Vertex AI

For enterprise-grade scalability:

```bash
# Set environment variables
export GOOGLE_GENAI_USE_VERTEXAI=TRUE
export GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
export GOOGLE_CLOUD_LOCATION=us-central1

# Authenticate
gcloud auth application-default login
```

```python
agent = LlmAgent(
    model="gemini-2.0-flash",
    name="vertex_agent",
    instruction="You are a helpful assistant."
)
```

### Using Other Models with LiteLLM

ADK supports many models through LiteLLM:

```python
from google.adk.models.lite_llm import LiteLlm

# OpenAI GPT-4
openai_model = LiteLlm(
    model="gpt-4o",
    api_key="your-openai-key"
)

# Anthropic Claude
claude_model = LiteLlm(
    model="claude-sonnet-4-20250514",
    api_key="your-anthropic-key"
)

# Use in agent
agent = LlmAgent(
    model=claude_model,
    name="claude_agent",
    instruction="You are Claude, a helpful assistant."
)
```

### Supported Models

**Google Models:**
- `gemini-2.0-flash` - Fast, efficient
- `gemini-2.5-pro` - Most capable
- `gemini-2.5-flash` - Balanced
- `gemini-exp-1206` - Experimental

**OpenAI:**
- `gpt-4o`
- `gpt-4-turbo`
- `gpt-3.5-turbo`

**Anthropic:**
- `claude-opus-4`
- `claude-sonnet-4-20250514`

**And many more through LiteLLM!**

### Model Selection Guidelines

| Use Case | Recommended Model |
|----------|------------------|
| Fast responses, simple tasks | `gemini-2.0-flash` |
| Complex reasoning, analysis | `gemini-2.5-pro` |
| Balanced performance | `gemini-2.5-flash` |
| Code generation | `gemini-2.0-flash` or `gpt-4o` |
| Long context | `gemini-2.5-pro` (2M tokens) |

---

## Evaluation & Testing

### Built-in Evaluation Framework

ADK includes tools to systematically assess agent performance.

#### Create Evaluation Dataset

```python
# evaluation_dataset.json
[
  {
    "input": "What's the capital of France?",
    "expected_output": "Paris",
    "metadata": {"category": "geography"}
  },
  {
    "input": "Calculate 15 * 23",
    "expected_output": "345",
    "metadata": {"category": "math"}
  }
]
```

#### Run Evaluation

```bash
# From command line
adk eval --dataset evaluation_dataset.json

# Or from Python
```

```python
from google.adk.evaluation import Evaluator

evaluator = Evaluator(
    agent=my_agent,
    dataset_path="evaluation_dataset.json"
)

results = await evaluator.run()
print(f"Accuracy: {results.accuracy}")
print(f"Average latency: {results.avg_latency}ms")
```

### Testing with adk api_server

Test your agent with HTTP requests:

```bash
# Start API server
adk api_server

# In another terminal, test with curl
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "test_user",
    "session_id": "test_session",
    "message": "What is the weather in New York?"
  }'
```

---

## Deployment

### Local Development

```bash
# Run with CLI
adk run

# Run with web UI
adk web
```

### Docker Deployment

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080
CMD adk web --host 0.0.0.0 --port ${PORT}
```

Build and run:

```bash
docker build -t my-agent .
docker run -p 8080:8080 --env-file .env my-agent
```

### Cloud Run Deployment

```bash
# Build and deploy to Cloud Run
gcloud run deploy my-agent \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_API_KEY=your-key
```

### Vertex AI Agent Engine

For enterprise-grade deployment with built-in monitoring, scaling, and integration:

```python
# Deploy to Agent Engine
from google.adk.platform import AgentEngineDeployment

deployment = AgentEngineDeployment(
    agent=root_agent,
    project_id="your-project-id",
    location="us-central1"
)

deployment.deploy()
```

---

## Advanced Topics

### Callbacks

Intercept execution at various points:

```python
from google.adk.agents.callback_context import CallbackContext
from google.genai.types import Content

async def before_model_callback(ctx: CallbackContext) -> Content | None:
    """Called before LLM is invoked."""
    print(f"About to call LLM with: {ctx.messages}")
    # Can modify messages or return alternate content
    return None

async def after_tool_callback(ctx: CallbackContext) -> Content | None:
    """Called after tool execution."""
    print(f"Tool {ctx.tool_name} returned: {ctx.tool_result}")
    # Can modify tool result
    return None

agent = LlmAgent(
    model="gemini-2.0-flash",
    name="monitored_agent",
    instruction="You are monitored.",
    tools=[my_tool],
    before_model_callback=before_model_callback,
    after_tool_callback=after_tool_callback
)
```

### Multimodal Streaming

Handle real-time audio/video:

```python
from google.adk.agents import LlmAgent

agent = LlmAgent(
    model="gemini-2.0-flash-live",  # Live API model
    name="voice_agent",
    instruction="You are a voice assistant."
)

# Streaming will work automatically with adk web --voice
```

### Artifacts

Handle files and binary data:

```python
from google.adk.tools.tool_context import ToolContext

def generate_report(topic: str, tool_context: ToolContext) -> dict:
    """Generates a PDF report."""
    
    # Create report content
    pdf_content = create_pdf(topic)
    
    # Save as artifact
    artifact_id = tool_context.save_artifact(
        data=pdf_content,
        mime_type="application/pdf",
        name=f"report_{topic}.pdf"
    )
    
    return {
        "status": "success",
        "artifact_id": artifact_id,
        "message": f"Report saved as {artifact_id}"
    }

# Later, load artifact
artifact = await tool_context.load_artifact(artifact_id)
```

### Global Instructions

Apply instructions to all agents in hierarchy:

```python
root_agent = LlmAgent(
    name="root",
    model="gemini-2.0-flash",
    global_instruction="""IMPORTANT: All agents must:
- Be concise
- Verify facts before responding
- Use professional tone
""",
    instruction="You coordinate the team.",
    sub_agents=[agent1, agent2, agent3]
)
```

### Transfer Control

Explicit agent delegation:

```python
agent = LlmAgent(
    name="agent1",
    model="gemini-2.0-flash",
    disallow_transfer_to_parent=True,  # Can't transfer back to parent
    disallow_transfer_to_peers=True,   # Can't transfer to sibling agents
)
```

---

## Model Context Protocol (MCP)

The Model Context Protocol (MCP) is an open standard for how LLMs communicate with external applications, data sources, and tools.

### Using MCP Servers in ADK

```python
from google.adk.tools.mcp_tool import McpTool

# Connect to MCP server
mcp_tool = McpTool(
    server_url="http://localhost:3000",
    tool_name="search_database"
)

# Use in agent
agent = LlmAgent(
    model="gemini-2.0-flash",
    name="mcp_agent",
    instruction="Use MCP tools to search databases.",
    tools=[mcp_tool]
)
```

### Exposing ADK Agents as MCP Servers

```python
from google.adk.mcp import AdkMcpServer

# Create MCP server from agent
mcp_server = AdkMcpServer(
    agent=my_agent,
    port=3000
)

# Start server
mcp_server.start()
```

### MCP Toolbox for Databases

Pre-built MCP server for database access:

- BigQuery
- AlloyDB
- Cloud SQL
- PostgreSQL
- MySQL
- SQL Server

```python
# Agent can query databases through MCP
agent = LlmAgent(
    model="gemini-2.0-flash",
    name="data_agent",
    instruction="Query databases using MCP tools.",
    tools=[mcp_bigquery_tool, mcp_postgres_tool]
)
```

---

## Best Practices

### 1. Agent Design

✅ **Do:**
- Give agents clear, specific instructions
- Use descriptive names and descriptions
- Limit tool count to 5-10 per agent
- Use sub-agents for specialization
- Include examples in instructions

❌ **Don't:**
- Create generic, do-everything agents
- Use ambiguous instructions
- Give too many tools to one agent
- Forget error handling

### 2. Tool Design

✅ **Do:**
- Write comprehensive docstrings
- Return structured dictionaries with status
- Handle errors gracefully
- Keep tools focused on single responsibility
- Use ToolContext when needed

❌ **Don't:**
- Return bare strings or values
- Leave docstrings empty
- Make tools do multiple unrelated things
- Ignore error cases

### 3. State Management

✅ **Do:**
- Use descriptive state keys
- Use output_key for agent results
- Use temp: prefix for temporary data
- Document state schema

❌ **Don't:**
- Use ambiguous key names
- Store large objects in state
- Forget to clean up old state

### 4. Multi-Agent Systems

✅ **Do:**
- Create specialized agents for distinct tasks
- Use workflow agents for predictable patterns
- Use LLM delegation for dynamic routing
- Share state between agents
- Test each agent independently

❌ **Don't:**
- Create too deep hierarchies (>3 levels)
- Duplicate functionality across agents
- Forget to set descriptions for routing

### 5. Testing

✅ **Do:**
- Test with evaluation datasets
- Use adk api_server for HTTP testing
- Test edge cases and error conditions
- Monitor latency and token usage
- Version your agents

❌ **Don't:**
- Only test happy paths
- Skip evaluation before deployment
- Ignore performance metrics

### 6. Deployment

✅ **Do:**
- Use environment variables for secrets
- Implement proper logging
- Set up monitoring
- Use containers for reproducibility
- Plan for scaling

❌ **Don't:**
- Hardcode API keys
- Deploy without testing
- Ignore error logs
- Skip monitoring setup

### 7. Security

✅ **Do:**
- Validate tool inputs
- Implement rate limiting
- Use authentication for production
- Sanitize user inputs
- Follow least privilege principle

❌ **Don't:**
- Trust all user inputs
- Expose internal errors to users
- Skip input validation
- Grant excessive permissions

---

## Complete Example: Travel Planning Agent System

Here's a comprehensive example bringing together multiple concepts:

```python
import asyncio
from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# ===== Tools =====

def search_flights(origin: str, destination: str, date: str) -> dict:
    """Searches for available flights.
    
    Args:
        origin: Departure city
        destination: Arrival city
        date: Travel date (YYYY-MM-DD)
        
    Returns:
        dict: Available flights with prices
    """
    # Mock implementation
    return {
        "status": "success",
        "flights": [
            {"airline": "FlyHigh", "price": "$350", "departure": "08:00"},
            {"airline": "SkyWings", "price": "$420", "departure": "14:00"}
        ]
    }

def search_hotels(city: str, checkin: str, checkout: str) -> dict:
    """Searches for available hotels.
    
    Args:
        city: City name
        checkin: Check-in date (YYYY-MM-DD)
        checkout: Check-out date (YYYY-MM-DD)
        
    Returns:
        dict: Available hotels with prices
    """
    return {
        "status": "success",
        "hotels": [
            {"name": "Grand Hotel", "price": "$150/night", "rating": "4.5"},
            {"name": "City Inn", "price": "$90/night", "rating": "4.0"}
        ]
    }

def get_weather(city: str, date: str) -> dict:
    """Gets weather forecast.
    
    Args:
        city: City name
        date: Date (YYYY-MM-DD)
        
    Returns:
        dict: Weather information
    """
    return {
        "status": "success",
        "forecast": "Sunny, 24°C"
    }

# ===== Specialized Agents =====

flight_agent = LlmAgent(
    name="FlightExpert",
    model="gemini-2.0-flash",
    description="Searches and recommends flights",
    instruction="""You are a flight search expert.

Use the search_flights tool to find flights.
Consider price, departure time, and airlines.
Recommend the best option based on user preferences.
""",
    tools=[search_flights],
    output_key="flight_recommendation"
)

hotel_agent = LlmAgent(
    name="HotelExpert",
    model="gemini-2.0-flash",
    description="Searches and recommends hotels",
    instruction="""You are a hotel search expert.

Use the search_hotels tool to find accommodations.
Consider price, rating, and location.
Recommend the best option based on user preferences.
""",
    tools=[search_hotels],
    output_key="hotel_recommendation"
)

weather_agent = LlmAgent(
    name="WeatherExpert",
    model="gemini-2.0-flash",
    description="Provides weather information",
    instruction="""You are a weather expert.

Use the get_weather tool to check forecast.
Provide advice on what to pack based on weather.
""",
    tools=[get_weather],
    output_key="weather_info"
)

# ===== Input Parser =====

input_parser = LlmAgent(
    name="InputParser",
    model="gemini-2.0-flash",
    description="Parses travel request",
    instruction="""Extract travel details from user request.

Extract:
- origin city
- destination city
- travel date
- return date
- preferences (budget, comfort, etc.)

Save to state.
""",
    output_key="parsed_input"
)

# ===== Research Coordinator (Parallel) =====

research_coordinator = ParallelAgent(
    name="ResearchCoordinator",
    description="Coordinates parallel travel research",
    sub_agents=[flight_agent, hotel_agent, weather_agent]
)

# ===== Itinerary Creator =====

itinerary_creator = LlmAgent(
    name="ItineraryCreator",
    model="gemini-2.0-flash",
    description="Creates final travel itinerary",
    instruction="""Create a comprehensive travel itinerary.

Use information from:
- Flight: {flight_recommendation}
- Hotel: {hotel_recommendation}
- Weather: {weather_info}

Format as a clear, day-by-day itinerary with:
- Travel times
- Accommodation details
- Weather considerations
- Total estimated cost
""",
    output_key="final_itinerary"
)

# ===== Main Travel Planner (Sequential Pipeline) =====

travel_planner = SequentialAgent(
    name="TravelPlanner",
    description="Complete travel planning pipeline",
    sub_agents=[
        input_parser,
        research_coordinator,
        itinerary_creator
    ]
)

# ===== Run the System =====

async def plan_trip():
    APP_NAME = "travel_planner"
    USER_ID = "traveler_001"
    SESSION_ID = "trip_session_001"
    
    # Setup
    session_service = InMemorySessionService()
    runner = Runner(
        agent=travel_planner,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    # Create session
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    
    # User request
    user_request = types.Content(
        role='user',
        parts=[types.Part(text="""
        I want to travel from New York to Paris 
        from June 15-22, 2025. 
        I prefer comfortable options but within a reasonable budget.
        """)]
    )
    
    # Run planning
    print("Planning your trip...\n")
    
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_request
    ):
        # Print tool calls
        if event.type == "tool_call":
            print(f"🔧 {event.author}: {event.tool_name}")
        
        # Print final itinerary
        if event.is_final_response() and event.content:
            print("\n" + "="*60)
            print("YOUR TRAVEL ITINERARY")
            print("="*60 + "\n")
            print(event.content.parts[0].text)
    
    # Access session state
    final_session = await session_service.get_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print(f"\n📋 State keys: {list(final_session.state.keys())}")

# Run
if __name__ == "__main__":
    asyncio.run(plan_trip())
```

This example demonstrates:
- ✅ Multiple specialized agents
- ✅ Custom tools with proper docstrings
- ✅ Parallel execution for independent tasks
- ✅ Sequential pipeline for ordered operations
- ✅ State management between agents
- ✅ Proper session handling
- ✅ Event monitoring

---

## Conclusion

The Google Agent Development Kit (ADK) provides a powerful, flexible framework for building sophisticated AI agent systems. This tutorial has covered:

1. **Core Concepts**: Agents, tools, sessions, state, and memory
2. **Agent Types**: LLM agents, workflow agents, and custom agents
3. **Multi-Agent Systems**: Hierarchies, delegation, and coordination
4. **Tools**: Creating custom tools and using built-in capabilities
5. **Sessions & Memory**: Managing context across conversations
6. **Models**: Integrating various LLMs
7. **Deployment**: From local development to production
8. **Best Practices**: Design patterns and guidelines

### Next Steps

1. **Explore Examples**: Check out the ADK examples repository
2. **Join Community**: Connect with other ADK developers
3. **Read API Docs**: Dive deeper into specific modules
4. **Build Projects**: Start creating your own agent systems
5. **Contribute**: Help improve ADK

### Resources

- **Documentation**: https://google.github.io/adk-docs/
- **GitHub**: https://github.com/google/adk-python
- **API Keys**: https://aistudio.google.com/apikey
- **Support**: https://github.com/google/adk-python/issues

---

## Appendix: Common Patterns

### Pattern 1: Retry with Loop Agent

```python
retry_loop = LoopAgent(
    name="RetryLoop",
    sub_agents=[task_agent],
    max_iterations=3
)
```

### Pattern 2: Validation Pipeline

```python
pipeline = SequentialAgent(
    name="ValidationPipeline",
    sub_agents=[validator, processor, formatter]
)
```

### Pattern 3: Fan-Out Fan-In

```python
# Fan-out: Parallel execution
parallel = ParallelAgent(sub_agents=[agent1, agent2, agent3])

# Fan-in: Merge results
merger = LlmAgent(instruction="Merge: {result1}, {result2}, {result3}")

# Combine
workflow = SequentialAgent(sub_agents=[parallel, merger])
```

### Pattern 4: Conditional Routing

```python
router = LlmAgent(
    instruction="Analyze request and delegate to: {specialized_agents}",
    sub_agents=[agent_a, agent_b, agent_c]
)
```

### Pattern 5: Iterative Refinement

```python
refinement = LoopAgent(
    sub_agents=[generator, critic, improver],
    max_iterations=5
)
```

---

**Happy Building with ADK! 🚀**
