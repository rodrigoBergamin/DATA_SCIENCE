from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
plt.bar(range(len(movies)), num_oscars)

plt.title('My favorite Movies')
plt.ylabel('# of Academy Awards')
plt.xticks(range(len(movies)), movies)

plt.show()