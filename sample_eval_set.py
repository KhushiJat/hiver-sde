import pandas as pd

# Load your filtered Spotify dataset
df = pd.read_csv("SpotifyCares_dataset.csv")

# Randomly sample 200 rows for your golden evaluation set
golden_set = df.sample(n=200, random_state=42)

# Select only the columns you need for evaluation (tweet_id and text)
golden_set = golden_set[["tweet_id", "text"]]

# Add empty columns for your manual labels
golden_set["true_intent"] = ""
golden_set["should_escalate"] = ""
golden_set["ideal_reply"] = ""

# Save to a new CSV file
golden_set.to_csv("golden_evaluation_set.csv", index=False)
print("Saved 200 samples to golden_evaluation_set.csv for manual labeling!")