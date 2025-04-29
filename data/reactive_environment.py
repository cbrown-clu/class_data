import numpy as np
import pandas as pd

class ReactiveEnvironment:
  def __init__(self):
    self.choice_A = [-1,0,0,0,1,1,2,2,3]
    self.choice_B = [-1,0,1,1,1,2,2,2,3,3]
    self.time_limit = 100
    self.goal = 100
    self.last_state = None
    self.last_choice = None
  def pull(self,choice):
    if choice == "A" and self.last_choice == "A":
      r1 = np.random.choice(self.choice_A)
      r2 = np.random.choice(self.choice_A)
      r = np.min([r1,r2])
    elif choice == "A" and self.last_choice == "B":     
      r = np.random.choice(self.choice_A)
    elif choice == "B" and self.last_choice == "A":     
      r1 = np.random.choice(self.choice_B)
      r2 = np.random.choice(self.choice_B)
      r = np.max([r1,r2])
    elif choice == "B" and self.last_choice == "B":     
      r1 = np.random.choice(self.choice_B)
      r2 = np.random.choice(self.choice_B)
      r = np.min([r1,r2])
    else:
      r = -1
    self.last_state = r
    self.last_choice = choice
    return r