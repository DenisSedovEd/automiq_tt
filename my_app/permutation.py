class EmptyInputError(Exception):
    pass


class WithNumbersInputError(Exception):
    pass


class LongInputError(Exception):
    pass


def permutation(input_str: str, permutation_rule: str) -> str:
    """
    Функция сортировки входного набора объектов.
    :param input_str:
    :param permutation_rule:
    :return:
    """
    change_str = []
    input_str = input_str.replace(" ", "").upper()
    permutation_rule = permutation_rule.replace(" ", "").upper()

    if len(input_str) > 50:
        raise LongInputError(f"Указанная строка больше 50 символов.({len(input_str)})")
    elif not input_str or not permutation_rule:
        raise EmptyInputError("Поле ввода пустое.")
    elif not set(input_str) == set(permutation_rule):
        raise ValueError("Наборы элементов в строках не совпадают.")

    for let in list(input_str):
        if let.isalpha() and permutation_rule[permutation_rule.index(let)].isalpha():
            change_str.append(permutation_rule.index(let))
            change_str.sort()
        else:
            raise ValueError("Строка содержит символ, не букву.")
    result = "".join([permutation_rule[idx] for idx in change_str])
    return result
