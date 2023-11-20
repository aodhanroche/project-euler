def sort_names(filename):  # Opens the file, reads, sorts and returns the sorted data
    my_file = open(f"{filename}", "r")
    data = my_file.read()
    sorted_data = [name.strip().strip('"') for name in data.split(",")]
    my_file.close()
    sorted_data.sort()
    return sorted_data


def assign_scores(sorted_data):  # Calculates the score of every name and returns a list of scores
    list_of_name_scores = []
    name_counter = 0
    for name in sorted_data:
        name_counter += 1
        score_counter = 0
        characters = ([*name])
        for character in characters:
            score_counter += ord(character) - 64
        list_of_name_scores.append(score_counter * name_counter)
    return list_of_name_scores


def name_scores(filename):  # Returns the list of scores using sort_names and assign_scores
    list_of_scores = assign_scores(sort_names(filename))
    return list_of_scores


def total_name_scores(filename):  # Returns the total names_scores
    return sum(name_scores(filename))


print(total_name_scores("names.txt"))
# print(name_scores("names.txt"))
