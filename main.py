ZERO_TOLERANCE = 'На ноль делить нельзя!'
INVALID_OP = "Некорректный оператор!"


# This function asks the user for an integer to pass
# further operations with this number.
def get_num():
    while True:
        first = input()
        if first.isdigit():
            return first
        else:
            print('Введите целое число')


# This function requests an operator from the user.
def get_op():
    while True:
        op = input('Введите оператор действия: ')
        if op == '+' or op == '-' or op == '*' or op == '/':
            return op
        else:
            print("Введите корректный оператор!")


# This function performs calculations with the received numbers and the operator.
def get_result(first, op, second):
    a = int(first)
    b = int(second)
    if op == '+':
        return(a + b)
    elif op == '-':
        return(a - b)
    elif op == '*':
        return(a * b)
    elif op == '/':
        if b == 0:
            return ZERO_TOLERANCE # check division by zero
    else:
        return (a/ b)



# This function prints the entire example.
def print_result(first, op, second, result):
    if result == ZERO_TOLERANCE or result == INVALID_OP:
        print(result)
    else:
        print(first, op, second, '=', result)

# The main function.
def main():
    print('Введите первое число: ')
    first = get_num()
    op = get_op()
    print('Введите второе число: ')
    second = get_num()
    result = get_result(first, op, second)
    print_result(first, op, second, result)


if __name__ == '__main__':
    main()