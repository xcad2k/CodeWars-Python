def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split(" "))

print(to_jaden_case("This is a test"))