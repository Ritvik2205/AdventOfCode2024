def txt_to_input(file_path):
    with open(file_path, "r") as file:
        return [line.replace("\n", "").split(":") for line in file]

def process_input(input):
    processed_input = []
    for line in input:
        target = int(line[0])
        numbers = list(map(int, line[1].strip().split()))
        processed_input.append((target, numbers))

    return processed_input

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
        elif operators[i-1] == '*':
            result *= numbers[i]
        elif operators[i-1] == '||':
            result = int(str(result) + str(numbers[i]))
    return result

def check_calibrations(input):
    from itertools import product

    result = 0
    for target, numbers in input:
        if len(numbers) == 1:
            continue
        operators = list(product(['+', '*', '||'], repeat=len(numbers)-1))
        for ops in operators:
            if evaluate_expression(numbers, ops) == target:
                result += target
                break
    return result



def main():
    input = txt_to_input("input.txt")
    processed_input = process_input(input)
    print(check_calibrations(processed_input))


if __name__ == "__main__":
    main()

