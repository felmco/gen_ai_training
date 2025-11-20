"""
Swarm Handoff Pattern Demo
--------------------------
Simulación del patrón de 'Handoff' (traspaso) entre agentes especializados.
Simulation of the 'Handoff' pattern between specialized agents.
"""

class Agent:
    def __init__(self, name, instructions):
        self.name = name
        self.instructions = instructions

def triage_agent_instructions(context):
    return "You are the triage agent. Direct users to Sales or Support."

def sales_agent_instructions(context):
    return "You are sales. Sell the pen."

def support_agent_instructions(context):
    return "You are support. Help with bugs."

# Definición de Agentes / Agent Definitions
triage_agent = Agent(name="Triage", instructions=triage_agent_instructions)
sales_agent = Agent(name="Sales", instructions=sales_agent_instructions)
support_agent = Agent(name="Support", instructions=support_agent_instructions)

def run_swarm_demo(user_query):
    print(f"\nUser: '{user_query}'")
    print(f"🤖 Current Agent: {triage_agent.name}")
    
    # Lógica de Handoff simulada (normalmente el LLM decidiría esto llamando a una función)
    # Simulated Handoff logic (normally the LLM would decide this by calling a function)
    
    active_agent = triage_agent
    
    if "buy" in user_query.lower():
        print("   --> Deciding to transfer to Sales...")
        active_agent = sales_agent
    elif "help" in user_query.lower() or "broken" in user_query.lower():
        print("   --> Deciding to transfer to Support...")
        active_agent = support_agent
        
    print(f"🤖 New Active Agent: {active_agent.name}")
    print(f"   Instructions: {active_agent.instructions({})}")

if __name__ == "__main__":
    run_swarm_demo("I want to buy a subscription")
    run_swarm_demo("My screen is broken, help!")
