"""
n8n Webhook Trigger
-------------------
Cómo enviar datos a un flujo de n8n desde Python.
How to send data to an n8n workflow from Python.

Requisitos/Requirements:
pip install requests
"""

import requests
import json

# URL de tu webhook de n8n (Production o Test)
# Your n8n webhook URL (Production or Test)
N8N_WEBHOOK_URL = "https://your-n8n-instance.com/webhook/test-trigger"

def trigger_workflow(data):
    print(f"🚀 Sending data to n8n: {N8N_WEBHOOK_URL}")
    
    try:
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            print("✅ Success! Workflow triggered.")
            print(f"Response: {response.text}")
        else:
            print(f"❌ Failed with status: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    payload = {
        "event": "analysis_completed",
        "summary": "Market is bullish.",
        "recipient": "boss@company.com"
    }
    
    # Comentado para evitar errores reales si no existe la URL
    # trigger_workflow(payload)
    print("Script ready. Set N8N_WEBHOOK_URL to run.")
