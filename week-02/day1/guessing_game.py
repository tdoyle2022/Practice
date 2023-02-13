class GuessingGame:
    pass

    def __init__(self, answer):
        self.answer = answer

    def guess(self, user_guess):
        if user_guess > self.answer:
            return "high"
        if user_guess == self.answer:
            return "correct"
        if user_guess < self.answer:
            return "low"
    
    def solved(self):
        if self.guess == 'correct':
            return True
        else:
            return False

guess1 = GuessingGame(10)
print(guess1.guess(10))
print(guess1.solved())
# print(guess1.solved())

