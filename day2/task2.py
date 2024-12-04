
def txt_to_list(file_path):
    with open(file_path, "r") as file:        
        list1 = [[int(num) for num in (line.replace("\n", "").replace(" ", ",")).split(",")] for line in file]

    return list1

def safety_check(lists):
    result = 0
    # check if every element in the list is a list wither in ascending or descending order and the elements all differe by atleast 1 and at most 3
    for list in lists:
        if list == sorted(list) or list == sorted(list, reverse=True):
            # check if difference between elements is atleast 1 and at most 3 
            if all(abs(list[i] - list[i-1]) <= 3 and abs(list[i] - list[i-1]) >= 1 for i in range(1, len(list))):
                result += 1 

    return result

def safety_check_with_dampners(lists):
    result = 0
    # list is safe if is passes on removing a single element
    for list in lists:
        for i in range(len(list)):
            new_list = list[:i] + list[i+1:]
            if safety_check([new_list]):
                result += 1
                break
    return result   

def main():
    # txt_to_list("input.txt")
    lists = txt_to_list("input.txt")
    
    print(safety_check_with_dampners(lists))



if __name__ == "__main__":
    main()