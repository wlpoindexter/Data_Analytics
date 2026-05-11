movie_list = [  "Interstellar",
    "Parasite",
    "The Grand Budapest Hotel",
    "Everything Everywhere All at Once",
    "Spirited Away",
    "Get Out", ]

print(f"The list movie_list includes my top {len(movie_list)} favorite movies")
print(movie_list)

# sorted() returns a new sorted list — original is unchanged
print(sorted(movie_list))
print(movie_list)

# .sort() changes the list permanently in place
movie_list.sort()
print(movie_list)

movie_list.append("Moonlight")
print(f"The list movie_list includes my top {len(movie_list)} favorite movies")
print(movie_list)