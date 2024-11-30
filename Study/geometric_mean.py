def geometric_mean(numlist):
    if len(numlist) == 0:
        return "\"geometric_mean\" error: List is empty!"
    not_int_or_float = 0
    type_list = []
    for i in numlist:
        type_list.append(i)
        if type(i) != int and type(i) != float:
            not_int_or_float = 1
    if not_int_or_float == 1:
        return f"\"geometric_mean\" error: At least one list item is not \"str\" or \"float\".\n\nClasses: {type_list}"
    else:
        product = 1
        iteration_count = 0
        for i in numlist:
            product *= i
            iteration_count += 1

        answer = product ** (1 / iteration_count)

        if answer % 1 == 0:
            answer = int(answer)
        else:
            answer = round(answer, 2)

        return answer
