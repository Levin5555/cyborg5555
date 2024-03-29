


import pandas as pd

class MedicalExpertSystem:
    def __init__(self):
        self.symptoms = []
        self.diagnosis = None
        self.patient_data = pd.DataFrame(columns=["Symptoms", "Diagnosis"])

    def ask_question(self, question):
        answer = input(question + " (yes/no): ").strip().lower()
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
            return self.ask_question(question)

    def diagnose(self):
        if self.ask_question("Do you have a fever?"):
            self.symptoms.append("fever")
        if self.ask_question("Do you have a headache?"):
            self.symptoms.append("headache")
        if self.ask_question("Do you have a cough?"):
            self.symptoms.append("cough")

        self.patient_data = self.patient_data._append({"Symptoms": ", ".join(self.symptoms), "Diagnosis": ""}, ignore_index=True)

        if "fever" in self.symptoms and "headache" in self.symptoms:
            self.diagnosis = "You might have the flu."
        elif "fever" in self.symptoms and "cough" in self.symptoms:
            self.diagnosis = "You might have a cold."
        else:
            self.diagnosis = "Your condition is unclear. Please consult a doctor."

        self.patient_data.loc[self.patient_data.index[-1], "Diagnosis"] = self.diagnosis

    def run(self):
        print("Welcome to the Medical Expert System.")
        self.diagnose()
        print("Diagnosis:", self.diagnosis)
        print("Patient Data:")
        print(self.patient_data)

if __name__ == "__main__":
    expert_system = MedicalExpertSystem()
    expert_system.run()