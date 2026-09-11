import os
import pandas as pd

# Define a simple rule-based or LLM-powered agent structure
class SpotifySupportAgent:
    def __init__(self):
        # Define a small set of intents for Spotify Cares
        self.intents = [
            "Playback/Skipping Issue", 
            "Billing/Premium Subscription", 
            "Login/Account Access", 
            "Device Compatibility", 
            "General Inquiry"
        ]

    def classify_intent(self, text: str) -> str:
        text_lower = text.lower()
        if "skip" in text_lower or "stop" in text_lower or "playing" in text_lower or "pause" in text_lower:
            return "Playback/Skipping Issue"
        elif "bill" in text_lower or "premium" in text_lower or "charge" in text_lower or "payment" in text_lower:
            return "Billing/Premium Subscription"
        elif "login" in text_lower or "password" in text_lower or "account" in text_lower or "access" in text_lower:
            return "Login/Account Access"
        elif "device" in text_lower or "speaker" in text_lower or "android" in text_lower or "ios" in text_lower:
            return "Device Compatibility"
        else:
            return "General Inquiry"

    def decide_escalation(self, text: str, intent: str) -> dict:
        text_lower = text.lower()
        # Escalate if it involves account security, payment failures, or extreme frustration/anger
        if "refund" in text_lower or "hack" in text_lower or "fraud" in text_lower or "😡" in text_lower or "fucking" in text_lower:
            return {
                "action": "Escalate to Human",
                "reason": "Customer is highly frustrated or reporting a financial/security dispute requiring human intervention."
            }
        else:
            return {
                "action": "Auto-handle",
                "reason": "Standard technical or account query that can be resolved via troubleshooting steps."
            }

    def draft_reply(self, intent: str, text: str) -> str:
        if intent == "Playback/Skipping Issue":
            return "Hi there! Sorry to hear about the playback trouble. Could you try logging out, restarting your device, and logging back in? Let us know how it goes! /AY"
        elif intent == "Billing/Premium Subscription":
            return "Hi there! We'd love to look into your account details. Please send us a DM with the email address linked to your account so we can help. /MU"
        elif intent == "Device Compatibility":
            return "Hi! What device and operating system are you using? Drop us the details so our team can check this out for you. /CP"
        else:
            return "Hi there! Thanks for reaching out. Send us a DM with more info so we can help you sort this out. /AY"

    def run_pipeline(self, customer_message: str) -> dict:
        intent = self.classify_intent(customer_message)
        escalation = self.decide_escalation(customer_message, intent)
        reply = self.draft_reply(intent, customer_message)
        
        return {
            "message": customer_message,
            "intent": intent,
            "escalation_decision": escalation["action"],
            "escalation_reason": escalation["reason"],
            "drafted_reply": reply
        }

# Test the agent with a sample tweet
if __name__ == "__main__":
    agent = SpotifySupportAgent()
    sample_tweet = "My music keeps skipping every 2 seconds on my android phone, please fix this!"
    
    result = agent.run_pipeline(sample_tweet)
    print("--- Agent Execution Result ---")
    for k, v in result.items():
        print(f"{k}: {v}")