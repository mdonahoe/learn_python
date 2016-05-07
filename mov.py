"""
Print out pairs of movie titles that can be joined together on shared words.

Ex:
Guardians of the Galaxy Quest
Veronica Mars Attacks!
"""
# Step 1: make list of movie titles, split on whitespace

fin = file('movies.txt')
movies = []

for line in fin:
    movie = line.split()
    movies.append(movie)

# Step 2: Check the last word of one with the first from another...

for movie in movies:
    last = movie[-1]
    for m in movies:
        if m == movie:
            continue
        if last == m[0]:
            print ' '.join(movie + m[1:])
