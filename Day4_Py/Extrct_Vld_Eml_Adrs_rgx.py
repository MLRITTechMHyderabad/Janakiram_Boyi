import re
text = "Contact us at support@example.com, john.doe123@company.org, or invalid-email@com. Also, try jane_doe@domain.co.uk."
valid = r"\b[a-zA-Z0-9][\w\.-]*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?\b"
valid_emails = re.findall(valid,text)
print(valid_emails)