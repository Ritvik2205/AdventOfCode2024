import re

def txt_to_list(file_path):
    with open(file_path, "r") as file:        
        list = [str(line) for line in file]

    return list


def detect_pattern_with_stops(lst):
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")
    result = 0
    mul_enable = True
    for line in lst:
        pos = 0
        while pos < len(line):
            do_match = do_pattern.search(line, pos)
            dont_match = dont_pattern.search(line, pos)
            mul_match = mul_pattern.search(line, pos)
            
            next_match = min(
                (m for m in [do_match, dont_match, mul_match] if m),
                key=lambda m: m.start(),
                default=None
            )
            
            if not next_match:
                break
            
            pos = next_match.end()
            
            if next_match == do_match:
                mul_enable = True
            elif next_match == dont_match:
                mul_enable = False
            elif mul_enable and next_match == mul_match:
                result += int(next_match.group(1)) * int(next_match.group(2))
    
    return result
    

def detect_pattern(lst):
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    result = 0
    for line in lst:
        matches = mul_pattern.search(line)
        if matches:
            result += int(matches.group(1)) * int(matches.group(2))

    return result


def main():
    # txt_to_list("input.txt")
    list = txt_to_list("input.txt")
    result = detect_pattern_with_stops(list)
    # print(list)
    print(result)


if __name__ == "__main__":
    main()