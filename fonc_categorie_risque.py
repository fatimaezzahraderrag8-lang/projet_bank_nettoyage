def categorie_risque(score_credit):
    if score_credit >= 700:
        return "Low"
    elif score_credit >= 580:
        return "Medium"
    else:
        return "High"