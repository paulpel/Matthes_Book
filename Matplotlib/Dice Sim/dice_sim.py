from dice import Dice

dice = Dice()

# Trow the dice N times
results = []
N = 100
for roll in range(N):
    results.append(dice.roll())

# count the frequencies
frequencies = []
for value in range(1, dice.num_sides + 1):
    freq = results.count(value)
    frequencies.append(freq)

print(frequencies)