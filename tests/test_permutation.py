import pytest
from my_app.permutation import permutation, EmptyInputError, LongInputError


@pytest.mark.parametrize(
    "input_str, permutation_rule, expected",
    [
        ("БВААБВАББВАБВА", "АБВ", "АААААБББББВВВВ"),
        (" БВААБВАББВАБ ВА ", "АБВ", "АААААБББББВВВВ"),
        ("БВААбваББВАБВА", "абв", "АААААБББББВВВВ"),
        ("БВААБВАББВАБВА", "А БВ", "АААААБББББВВВВ"),
    ],
    ids=[
        "permutation_all_correct",
        "permutation_space_input_str_correct",
        "permutation_different_case_correct",
        "permutation_space_permutation_rule_correct",
    ],
)
def test_permutation_correct(input_str, permutation_rule, expected):
    """
    Функция тестирования набора корректных входных объектов.
    :param input_str:
    :param permutation_rule:
    :param expected:
    :return:
    """
    assert permutation(input_str, permutation_rule) == expected


@pytest.mark.parametrize(
    "input_str, permutation_rule, expected, exception",
    [
        (
            "БВААБВАББВАБВ1",
            "АБВ",
            "Наборы элементов в строках не совпадают.",
            ValueError,
        ),
        (
            "",
            "АБВ",
            "Поле ввода пустое.",
            EmptyInputError,
        ),
        (
            "БВААБВАББВАБВ",
            "",
            "Поле ввода пустое.",
            EmptyInputError,
        ),
        (
            "БВААБВАББВАБВГГГ",
            "АБВ",
            "Наборы элементов в строках не совпадают.",
            ValueError,
        ),
        (
            "БВААБВАББВАБВ",
            "АБВГ",
            "Наборы элементов в строках не совпадают.",
            ValueError,
        ),
    ],
)
def test_permutation_incorrect(input_str, permutation_rule, expected, exception):
    """
    Функция тестирование некорректных входных объектов.
    :param input_str:
    :param permutation_rule:
    :param expected:
    :param exception:
    :return:
    """
    with pytest.raises(Exception, match=expected):
        permutation(input_str, permutation_rule)
