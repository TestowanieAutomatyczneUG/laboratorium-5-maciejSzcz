class Hamming:
    def distance(first, second):
        result = 0

        if first == "" or second == "":
            result = 0    
        
        for i in range(len(first)):
            if first[i] != second[i]:
                result += 1
        return result