import re


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 20
    else:
        feedback.append("❌ Password must be at least 8 characters long")

    if re.search("[a-z]", password):
        score += 20
    else:
        feedback.append("❌ Add at least one lowercase letter")

    if re.search("[A-Z]", password):
        score += 20
    else:
        feedback.append("❌ Add at least one uppercase letter")

    if re.search("[0-9]", password):
        score += 20
    else:
        feedback.append("❌ Add at least one number")

    if re.search("[_@$!#%]", password):
        score += 20
    else:
        feedback.append("❌ Add at least one special character (_@$!#%)")

    return score, feedback


def password_level(score):
    if score == 100:
        return "🔥 Very Strong"
    elif score >= 80:
        return "✅ Strong"
    elif score >= 60:
        return "⚠️ Medium"
    else:
        return "❌ Weak"


# ===============================
# Main Program
# ===============================
password = input("Enter your password: ")

score, feedback = check_password_strength(password)
level = password_level(score)

print("\nPassword Strength Result")
print("-" * 30)
print(f"Score: {score}/100")
print(f"Level: {level}")

if feedback:
    print("\nFeedback:")
    for msg in feedback:
        print(msg)
else:
    print("✔ Your password meets all security requirements")
