
class Patient:

    def __init__(

        self,

        name,

        age,

        bmi,

        skin_type,

        vein_visibility

    ):

        self.name = name
        self.age = age
        self.bmi = bmi
        self.skin_type = skin_type
        self.vein_visibility = vein_visibility


    def summary(self):

        return {

            "Name": self.name,

            "Age": self.age,

            "BMI": self.bmi,

            "Skin Type": self.skin_type,

            "Vein Visibility": self.vein_visibility

        }
