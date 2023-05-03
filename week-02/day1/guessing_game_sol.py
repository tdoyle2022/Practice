class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        self.solved == False
    
    def guess(self, num):
        if self.answer < num:
            self.solved == False
            return 'high'
        elif self.answer > num:
            self.solved == False
            return 'low'
        else:
            self.solved = True
            return 'correct'
    
    def solved(self):
        return self.solved
        
        
# Define your GuessingGame class here...


game = GuessingGame(10)


print(game.guess(5))
print(game.guess(20))
print(game.guess(10))
print(game.solved())
