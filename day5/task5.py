def txt_to_list(file_path):
    with open(file_path, "r") as file:       
        list = []
        for line in file:
            processed_line = line.replace("\n", "").split("|") 
            list.append([int(num) for num in processed_line])
    return list
        

def txt_to_ordering(file_path):
    with open(file_path, "r") as file:        
        list1 = [[int(num) for num in (line.replace("\n", "").replace(" ", ",")).split(",")] for line in file]

    return list1

def valid_rule(ordering, rule):
    for a, b in ordering:
        if a in rule and b in rule and rule.index(a) > rule.index(b):
            return False
    return True

def sum_of_mid(ordering, rules, corrected=False):
    result = 0
    for rule in rules:
        is_valid = valid_rule(ordering, rule)
        if not corrected and is_valid:
            middle_index = len(rule) // 2
            result += rule[middle_index]
        elif corrected and not is_valid:
            corrected_rule = correct_rule(ordering, rule)
            middle_index = len(corrected_rule) // 2
            result += corrected_rule[middle_index]
    return result

def correct_rule(ordering, rule):
    corrected_rule = rule[:]
    changed = True
    while changed:
        changed = False
        for a, b in ordering:
            if a in corrected_rule and b in corrected_rule:
                a_index = corrected_rule.index(a)
                b_index = corrected_rule.index(b)
                if a_index > b_index:
                    corrected_rule[a_index], corrected_rule[b_index] = corrected_rule[b_index], corrected_rule[a_index]
                    changed = True
    return corrected_rule

def main():
    ordering = txt_to_list("ordering.txt")
    rules = txt_to_ordering("rules.txt")

    result = sum_of_mid(ordering, rules)
    # print(result)

    corrected_result = sum_of_mid(ordering, rules, corrected=True)
    print(corrected_result)


if __name__ == '__main__':
    main()