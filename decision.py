import random

def decide(anxiety):
    if random.random() < anxiety:
        return "Avoid"
    else:
        return "Act"

print(decide(0.5))
