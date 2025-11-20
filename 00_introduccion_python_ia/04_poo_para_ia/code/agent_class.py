"""
OOP for AI Agents
-----------------
Construcción de una clase Agente base y subclases especializadas.
Building a base Agent class and specialized subclasses.
"""

class BaseAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.memory = []
        
    def think(self, query: str):
        """Método genérico que debe ser implementado o usado por hijos"""
        print(f"🤔 {self.name} ({self.role}) is thinking about: '{query}'")
        self.memory.append(query)
        
    def reply(self) -> str:
        raise NotImplementedError("Subclasses must implement reply()")

class ChatAgent(BaseAgent):
    def reply(self) -> str:
        return f"Hello! As a {self.role}, I can help you."

class MathAgent(BaseAgent):
    def reply(self) -> str:
        return "The answer is 42 (Calculated)."

if __name__ == "__main__":
    # Polimorfismo: Tratamos a ambos igual, pero se comportan diferente
    agents = [
        ChatAgent("Alice", "Assistant"),
        MathAgent("Bob", "Mathematician")
    ]
    
    query = "Help me"
    
    for agent in agents:
        print(f"\n--- Agent: {agent.name} ---")
        agent.think(query)
        response = agent.reply()
        print(f"Response: {response}")
