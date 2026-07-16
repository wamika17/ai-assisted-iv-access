
def predict_diva_score(

    bmi,

    vein_visibility,

    skin_type

):

    score = 0

    if bmi > 30:

        score += 2

    if vein_visibility == "Poor":

        score += 2

    if skin_type == "Dark":

        score += 1

    return score
