def permutation(input_str: str, permutation_rule: str) -> str:
    change_str = []

    for let in list(input_str):
        change_str.append(permutation_rule.index(let))
        change_str.sort()

    return "".join([permutation_rule[idx] for idx in change_str])


# ССЗСКЗЗЗККСЗССКЗ
# ЗСК
