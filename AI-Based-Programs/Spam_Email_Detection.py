#We are building a basic spam detection system.
# Use a for loop to iterate through emails.
# Check if an email contains "free", "win", or "prize".
# If it contains any of these words, classify it as "Spam".
# Otherwise, classify it as "Not Spam".

emails = [
    "Win a free iPhone now",
    "Meeting scheduled for tomorrow",
    "Claim your prize now",
    "Project submission deadline",
    "Free cash offer"
]
for email in emails:
    cleaned_email = email.strip().lower()
    if "free" in cleaned_email or "win"in cleaned_email or "prize" in cleaned_email:
        classification = "spam"
    else:
        classification = "not_spam" 
print(f"{email} -> {classification}")
