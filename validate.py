import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|net|io|org|gov)$", email, re.IGNORECASE): # r = raw string, prevents pythong from interpreting backslash
    print("Valid")
else:
    print("Invalid")
