def check_eligibility(income, occupation):

    score = 0

    if income < 100000:
        score += 40
    elif income < 300000:
        score += 30
    elif income < 500000:
        score += 20
    else:
        score += 10

    occupation = occupation.lower()

    if "farmer" in occupation:
        score += 40
    elif "student" in occupation:
        score += 30
    elif "worker" in occupation or "labor" in occupation:
        score += 25
    else:
        score += 15

    if score >= 70:
        level = "High Eligibility"
    elif score >= 40:
        level = "Medium Eligibility"
    else:
        level = "Low Eligibility"

    return score, level