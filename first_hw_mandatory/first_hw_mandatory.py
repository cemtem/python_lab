def task_2_0():
    result = []
    for num in range(1, 101):
        if num % 3 == 0:
            result.append('Fizz')
        elif num % 5 == 0:
            result.append('Buzz')
        elif num % 50 == 0:
            result.append('FizzBuzz')
        else:
            result.append(num)
    return result


def task_2_1(string):
    count = 0
    for _ in string:
        count += 1
    return count


def task_2_2(string):
    result = {}
    for c in string.lower():
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result


def task_2_3(words):
    result = []
    for word in words:
        result.append(word)

    return sorted(set(result))


def task_2_4(integers):
    return [x for x in integers if x < 5]


def task_2_5(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)

    return set(result)


def task_2_6(num):
    result = []
    for x in range(1, num + 1):
        if num % x == 0:
            result.append(x)
    return result


def task_2_7(dictionary):
    return sorted(dictionary, reverse=True)


def task_2_8(dict_list):
    result = []
    for dictionary in dict_list:
        result += dictionary.values()

    return set(result)


def task_2_9(int_tuple):
    result = ''
    for x in int_tuple:
        result += str(x)

    return int(result)


def task_2_10(a, b, c, d):
    y_start = a - 1
    y_end = b + 1
    x_start = c - 1
    x_end = d + 1
    for row in range(y_start, y_end):
        for col in range(x_start, x_end):
            if row == y_start:
                if col == x_start:
                    print(" ", end='\t')
                else:
                    print(col, end='\t')
            elif col == x_start:
                if row == y_start:
                    print(" ", end='\t')
                else:
                    print(row, end='\t')
            else:
                print(row * col, end="\t")
        print()


if __name__ == '__main__':
    print('task 2_0: ' + str(task_2_0()))
    print('task 2_1: ' + str(task_2_1('word word')))
    print('task 2_2: ' + str(task_2_2('Oh, it is python')))
    print(task_2_3(['red', 'white', 'black', 'red', 'green', 'black']))
    print(task_2_4([11, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))
    print(task_2_5([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    print(task_2_6(60))
    print(task_2_7({2: "two", 1: "one", 3: "three"}))
    print(task_2_8([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                    {"VIII": "S007"}]))
    print(task_2_9((1, 2, 3, 4)))
    task_2_10(2, 4, 3, 7)
