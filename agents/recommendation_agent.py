def recommend_schemes(income, occupation):

    recommendations = []

    occupation = occupation.lower()

    if occupation == "farmer" and income < 300000:
        recommendations.append({
            "scheme": "PM-KISAN",
            "score": 85,
            "reason": "You are a farmer with income below ₹3,00,000."
        })

    if income < 500000:
        recommendations.append({
            "scheme": "Ayushman Bharat",
            "score": 78,
            "reason": "Low income households are eligible for health coverage."
        })

    if occupation == "student":
        recommendations.append({
            "scheme": "National Scholarship Portal",
            "score": 80,
            "reason": "Students are eligible for educational scholarships."
        })

    return recommendations