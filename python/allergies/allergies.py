class Allergies:
    ALLERGENS = {
        1: 'eggs',
        2: 'peanuts',
        4: 'shellfish',
        8: 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats',
    }

    def __init__(self, score):
        self.lst = [v for k, v in self.ALLERGENS.items() if score & k]

    def is_allergic_to(self, allergy):
        return allergy in self.lst