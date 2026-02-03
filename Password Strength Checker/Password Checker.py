import re


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 characters)")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z)")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers (0-9)")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$...)")

    if score <= 2:
        strength = "Weak ❌"
    elif score <= 4:
        strength = "Medium ⚠️"
    else:
        strength = "Strong ✅"

    return strength, feedback


def main():
    print("===== Password Strength Checker =====")
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")

    if feedback:
        print("Suggestions to improve your password:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Great! Your password is very strong 🔥")


if __name__ == "__main__":
    main()
