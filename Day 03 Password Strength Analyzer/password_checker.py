import re

password = input("Enter Password: ")

strength = 0

if len(password) >= 8:
    strength += 1
    print("[+] Minimum length verified")
else:
    print("[-] Password too short")

if re.search(r"[A-Z]", password):
    strength += 1
    print("[+] Uppercase letter detected")

if re.search(r"[a-z]", password):
    strength += 1
    print("[+] Lowercase letter detected")

if re.search(r"[0-9]", password):
    strength += 1
    print("[+] Number detected")

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    strength += 1
    print("[+] Special character detected")

print("\nPassword Strength:", end=" ")

if strength == 5:
    print("STRONG")
elif strength >= 3:
    print("MEDIUM")
else:
    print("WEAK")
