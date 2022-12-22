import time
import random


def get_div(n):
    return random.choice([x for x in range(1, n + 1) if n % x == 0])


def oneMinuteMath():
    d_list = ['+', '-', '*', '/']
    begin_time = time.time()
    total, correct = 0, 0
    questions = []
    while time.time() - begin_time <= 60:
        a = random.randint(1, 50)
        rule = random.choice(d_list)
        if rule == '/':
            b = get_div(a)
        else:
            b = random.randint(1, 50)
        # answer
        a_op_b = '{}{}{}'.format(a, rule, b)
        print(a_op_b)
        c = int(eval(a_op_b))
        # input
        try:
            input_ans = int(input('{} = '.format(a_op_b)))
        except:
            input_ans = ''

        if time.time() - begin_time <= 60:
            if c == input_ans:
                print('Correct! time remain {} seconds'.format(int(60 - (time.time() - begin_time))))
                correct += 1
            else:
                print('Wrong! time remain {} seconds'.format(int(60 - (time.time() - begin_time))))
            total += 1
    print('{} questions, correct rate {:.2f}%'.format(total, correct / total * 100))



oneMinuteMath()
