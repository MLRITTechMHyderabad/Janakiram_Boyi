import re

def extract_hashtags(text):
    # Hashtag pattern: starts with # followed by letters, numbers, or underscores
    pattern = r'#\w+'
    hashtags = re.findall(pattern, text)
    return hashtags

# Example input
tweet = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"

# Extract and print hashtags
valid_hashtags = extract_hashtags(tweet)
print(valid_hashtags)
