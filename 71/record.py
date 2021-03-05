class RecordScore:
    """Class to track a game's maximum score"""
    def __init__(self):
      self.scores = set()

    def max_score(self,new_score):
      self.scores.add(new_score)
      return max(self.scores)
    
    def __call__(self,new_score):
      return self.max_score(new_score)

record = RecordScore()
print(record(10))
print(record(11))
print(record(5))

print(record(-5))
print(record(-10))
print(record(-2))
print(record(-10))