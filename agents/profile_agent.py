def analyze_profile(age, income, occupation, location):

    if income < 300000:
        income_level = "low"
    else:
        income_level = "middle"

    profile = f"{income_level} income {occupation} from {location}"

    return profile