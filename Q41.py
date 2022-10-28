# the author's name is Cadyn Reger
def count_hashtag(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            index += len(target)
        else:
            index += 1
    return total


count_hashtag("#hey#hello", "#")
