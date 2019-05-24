import random

contestants = ['Chris', 'Gabe', 'Max', 'Raymond', 'Sean', 'Quoc', 'Connor']
chosen = random.choice(contestants)
print(f"{chosen} will be eliminated.")
contestants.remove(chosen)
chosen = random.choice(contestants)
print(f"{chosen} will be eliminated.")
contestants.remove(chosen)
chosen = random.choice(contestants)
print(f"{chosen} will be eliminated.")
contestants.remove(chosen)
chosen = random.choice(contestants)
print(f"{chosen} will be eliminated.")
contestants.remove(chosen)
chosen = random.choice(contestants)
print(f"{chosen} will be eliminated.")
contestants.remove(chosen)