class GuessingGame:

    def __init__(self, num):
        self.Answer = num
        self.Solved = False

    def guess(self, user_guess):
        if user_guess > self.answer:
            return "high"
        if user_guess == self.answer:
            self.Solved = True
            return "correct"
        if user_guess < self.answer:
            return "low"
    
    def solved(self):
        return self.Solved

game = GuessingGame(10)
print(game.guess(5))
print(game.solved())

# print(guess1.solved())

