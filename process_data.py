import pandas as pd

# Load the full dataset
print("Loading dataset...")
df = pd.read_csv("twcs/twcs.csv")

# Choose a brand to analyze
brand_name = "SpotifyCares"

print(f"Filtering conversations for {brand_name}...")
# Get tweets sent by the brand
brand_tweets = df[df["author_id"] == brand_name]

# Find customer tweets responding to this brand
response_ids = brand_tweets["in_response_to_tweet_id"].dropna().unique()
customer_tweets = df[df["tweet_id"].isin(response_ids)]

print(f"Found {len(customer_tweets)} customer conversations.")

# Save the extracted customer issues to a new CSV file
output_filename = f"{brand_name}_dataset.csv"
customer_tweets.to_csv(output_filename, index=False)
print(f"Saved filtered data to {output_filename}")