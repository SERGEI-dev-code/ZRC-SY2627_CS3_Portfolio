 class Patient:
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = float(bill_amount)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_bill_amount(self):
        return self._bill_amount

    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self._bill_amount = float(bill_amount)
        else:
            print("Invalid bill amount!")

    def calculate_bill(self):
        return self._bill_amount

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

  
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

if __name__ == "__main__":
   
    regular_patient = Patient("Juan Dela Cruz", 15000)
    senior_patient = SeniorPatient("Maria Santos", 15000)
    philhealth_patient = PhilHealthPatient("Pedro Penduko", 15000)

    patients = [regular_patient, senior_patient, philhealth_patient]

    print("=== HOSPITAL BILLING SYSTEM ===")
    
    for p in patients:
        print(f"Patient Name: {p.get_name()}")
        print(f"Original Bill: PHP {p.get_bill_amount():.2f}")
        print(f"Final Bill: PHP {p.calculate_bill():.2f}")
        print("-" * 30)