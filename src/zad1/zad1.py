class Hamming:
    def distance(first, second):
        result = 0

        if first == "" or second == "":
            return 0
        elif len(first) != len(second):
            raise ValueError("the length of the strands is different")
        
        for i in range(len(first)):
            if first[i] != second[i]:
                result += 1

        return result