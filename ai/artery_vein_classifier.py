

def classify_vessel(heart_rate, spo2):

    if spo2 > 95:

        return "Likely Vein"

    return "Further Assessment Required"
