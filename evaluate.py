import pandas as pd
from agent import SpotifySupportAgent

def run_evaluation():
    # Load your evaluation dataset
    print("Loading evaluation dataset...")
    df = pd.read_csv("golden_evaluation_set.csv")
    
    agent = SpotifySupportAgent()
    
    results = []
    print("Running agent evaluation across samples...")
    
    # Iterate through each sample row
    for index, row in df.iterrows():
        tweet_text = row["text"]
        
        # Run your agent pipeline
        output = agent.run_pipeline(tweet_text)
        
        results.append({
            "tweet_id": row["tweet_id"],
            "text": tweet_text,
            "predicted_intent": output["intent"],
            "escalation_decision": output["escalation_decision"],
            "drafted_reply": output["drafted_reply"]
        })
        
    # Convert results to DataFrame and save
    eval_output_df = pd.DataFrame(results)
    eval_output_df.to_csv("evaluation_results.csv", index=False)
    print("Evaluation complete! Results saved to evaluation_results.csv")

if __name__ == "__main__":
    run_evaluation()