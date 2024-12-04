

# convert txt file as a list of integers
def convert_txt_to_list(file):
    with open(file, 'r') as f:
        return [int(line) for line in f]
    
def total_distance(list1, list2):
    list1.sort()
    list2.sort()

    result = 0
    for i in range (len(list1)):
        result += abs(list2[i] - list1[i])

    return result

def similarity_score(list1, list2):
    # multpily each element of list1 with how many times it appears in list2
    # then sum all the results
    return sum([list1[i] * list2.count(list1[i]) for i in range(len(list1))])

def main():
    list1 = convert_txt_to_list('list1.txt')
    list2 = convert_txt_to_list('list2.txt')
    
    # print(similarity_score(list1, list2))

    print(int(1234567890*(1234567891)/2))


if __name__ == '__main__':
    main()