import multiprocessing as mp
import time
import math

result_a = []
result_b = []
result_c = []

def make_calculation_one(numbers):
    for number in numbers:
        result_a.append(math.sqrt(number ** 3))
        print(result_a,'from one')


def make_calculation_two(numbers):
    for number in numbers:
        result_b.append(math.sqrt(number ** 3))
        print(result_b,'from two')


def make_calculation_three(numbers):
    for number in numbers:
        result_c.append(math.sqrt(number ** 3))
        print(result_c,'from three')

if __name__ == '__main__':
    number_list = list(range(10))

    p1 = mp.Process(target=make_calculation_one, args=(number_list,))
    p2 = mp.Process(target=make_calculation_two, args=(number_list,))
    p3 = mp.Process(target=make_calculation_three, args=(number_list,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()

    end = time.time()

    print(end-start,'=====================================================')

    # print(result_a)