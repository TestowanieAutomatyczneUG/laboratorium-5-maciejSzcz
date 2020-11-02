class Hamming:
    def distance(first, second):
        if first == "" or second == "":
            return 0
        elif len(first) == 1 and first == second:
            return 0
        elif len(first) == 1 and len(second) == 1:
            return 1