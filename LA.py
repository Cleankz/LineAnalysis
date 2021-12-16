def LineAnalysis(line):
    string =line.split("*")
    if len(line) == 1 and line == "*":
        return True
    if line[0] != "*" or line[len(line)-1] != "*":
        return False
    string.remove(string[len(string)-1])
    string.remove(string[0])
    check = string[0]
    for i in string:
        if i != check:
            return False
    return True