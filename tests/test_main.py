# test_main.py

import importlib


def get_test_results(day, test_answer_part_1, test_answer_part_2):
    module = importlib.import_module('day_{0:d}'.format(day))
    test_input = 'input/day_{0:d}_test.txt'.format(day)
    result_part_1, result_part_2 = module.main(test_input, 0)
    test_part_1 = (result_part_1 == test_answer_part_1)
    test_part_2 = (result_part_2 == test_answer_part_2)
    return test_part_1, test_part_2


def test_day_1():
    day = 1
    test_answer_part_1 = 24000
    test_answer_part_2 = 45000
    test_part_1, test_part_2 = get_test_results(day, test_answer_part_1, test_answer_part_2)
    assert test_part_1 and test_part_2


def test_day_2():
    day = 2
    test_answer_part_1 = 15
    test_answer_part_2 = 12
    test_part_1, test_part_2 = get_test_results(day, test_answer_part_1, test_answer_part_2)
    assert test_part_1 and test_part_2


def test_day_3():
    day = 3
    test_answer_part_1 = 157
    test_answer_part_2 = 70
    test_part_1, test_part_2 = get_test_results(day, test_answer_part_1, test_answer_part_2)
    assert test_part_1 and test_part_2


def test_day_4():
    day = 4
    test_answer_part_1 = 2
    test_answer_part_2 = 4
    test_part_1, test_part_2 = get_test_results(day, test_answer_part_1, test_answer_part_2)
    assert (test_part_1 and test_part_2)


def test_day_5():
    day = 5
    test_answer_part_1 = 'CMZ'
    test_answer_part_2 = 'MCD'
    test_part_1, test_part_2 = get_test_results(day, test_answer_part_1, test_answer_part_2)
    assert (test_part_1 and test_part_2)


def test_day_6():
    day = 6
    test_answer_part_1 = 7
    test_answer_part_2 = 19
    test_part_1, test_part_2 = get_test_results(day, test_answer_part_1, test_answer_part_2)
    assert (test_part_1 and test_part_2)
    
def test_day_7():
    day = 7
    test_answer_part_1 = 95437
    test_answer_part_2 = 24933642
    test_part_1, test_part_2 = get_test_results(day, test_answer_part_1, test_answer_part_2)
    assert (test_part_1 and test_part_2)
    
def test_day_8():
    day = 8
    test_answer_part_1 = 21
    test_answer_part_2 = 8
    test_part_1, test_part_2 = get_test_results(day, test_answer_part_1, test_answer_part_2)
    assert (test_part_1 and test_part_2)
    
def test_day_9():
    test_answer_part_1 = 13
    test_answer_part_2 = 36
    import day_9
    result_part_1 = day_9.main('input/day_9_test_1.txt', 1)
    result_part_2 = day_9.main('input/day_9_test_2.txt', 2)
    test_part_1 = (result_part_1 == test_answer_part_1)
    test_part_2 = (result_part_2 == test_answer_part_2)
    assert (test_part_1 and test_part_2)
