def solution(str):
    """
    Breakdown:

    I'm iterating over the entire string and join all chars back together after manipulation.

    I check if it is a alpha char. If it is I do my stuff otherwise I return the char.

    chr((ord(char) - ord('a') + 13) % 26 + ord('a')
    I'm simply
    """
    return "".join(chr((ord(char) - ord('a' if char.islower() else 'A') + 13) % 26 + ord('a' if char.islower() else 'A')) if char.isalpha() else char for char in str)


print(solution("Aa Bb Cc 1234 Hello"))
