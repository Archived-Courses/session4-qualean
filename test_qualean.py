import math
import os
import pytest
import random
import qualean
from decimal import Decimal

README_CONTENT_CHECK_FOR = [
    'Qualean',
    'init',
    'and',
    'or',
    'repr',
    'str',
    'add',
    'eq',
    'float',
    'ge',
    'gt',
    'invertsign',
    'le',
    'lt',
    'mul',
    'sqrt',
    'bool',
    'test_readme_file_for_formatting',
    'test_readme_proper_description',
    'test_readme_exists',
    'test_sum_one_million',
    'test_add_mul_hundred_times',
    'test_sqrt_negative',
    'test_sqrt',
    'test_invert',
    'test_mul',
    'test_le',
    'test_lt',
    'test_gt',
    'test_ge',
    'test_le_eq',
    'test_ge_eq',
    'test_eq',
    'test_add',
    'test_class_str',
    'test_class_repr',
    'test_or_with_valid_q2',
    'test_or_with_valid_q2',
    'test_and_with_undefined_q2',
    'test_and_with_valid_q2',
    'test_invalid_real_part'
]

'''
    Checks if ValueError is returned if a value other than 1, 0 , -1 is passed to Qualean

'''

def test_invalid_real_part():
    with pytest.raises(ValueError):
        q = qualean.Qualean(-2)

def test_and_with_valid_q2():
    q1 = qualean.Qualean(0)
    q2 = qualean.Qualean(0)
    q3 = qualean.Qualean(-1)

    assert False == bool(q1 and q2)
    assert False == bool(q1 and q3)

def test_and_with_undefined_q2():
    q1 = qualean.Qualean(0)
    assert False == bool(q1 and q2)
    

def test_or_with_valid_q2():
    q1 = qualean.Qualean(0)
    q2 = qualean.Qualean(0)
    q3 = qualean.Qualean(-1)

    assert False == bool(q1 or q2)
    assert True == bool(q1 or q3)

def test_or_with_undefined_q2():
    q1 = qualean.Qualean(1)
    assert True == bool(q1 or q2)

def test_class_repr():
    q = qualean.Qualean(1)
    assert 'Qualean ' in q.__repr__()


def test_class_str():
    q = qualean.Qualean(1)
    assert str(q.num) in q.__str__()

def test_add():
    q1 = qualean.Qualean(1)
    q2 = qualean.Qualean(1)

    assert q1 + q2 == q1.num + q2.num

def test_eq():
        
    q1 = qualean.Qualean(0)
    q2 = qualean.Qualean(0)

    assert q1 == q2


def test_gt():
        
    q1 = qualean.Qualean(1)
    q2 = qualean.Qualean(0)

    if q1.num <=0:
        q1.num *= -1

    assert q1 > q2

def test_ge():
        
    q1 = qualean.Qualean(1)
    q2 = qualean.Qualean(0)

    if q1.num < 0:
        q1.num *= -1

    assert q1 >= q2


def test_lt():
        
    q1 = qualean.Qualean(1)
    q2 = qualean.Qualean(0)

    if q1.num >= 0:
        q1.num *= -1

    assert q1 < q2

def test_le_eq():
    
    q1 = qualean.Qualean(0)
    q2 = qualean.Qualean(0)

    assert q1 <= q2


def test_ge_eq():
    
    q1 = qualean.Qualean(0)
    q2 = qualean.Qualean(0)

    assert q1 >= q2

def test_le():
        
    q1 = qualean.Qualean(1)
    q2 = qualean.Qualean(0)

    if q1.num > 0:
        q1.num *= -1

    assert q1 <= q2

def test_mul():
    
    q1 = qualean.Qualean(1)
    q2 = qualean.Qualean(0)
    q3 = qualean.Qualean(-1)

    assert 0 == q1*q2
    assert q1.num * q3.num == q1 * q3
    assert q1.num * 2 == q1*2

def test_invert():
    q1 = qualean.Qualean(1)
    q2 = q1 * -1

    assert ~q1 == q2

def test_sqrt():
    q1 = qualean.Qualean(1)
    q0 = qualean.Qualean(0)
    if q1.num < 0:
        q1.num *= -1
    
    assert Decimal(str(q1)).sqrt() == q1.__sqrt__()
    assert 0 == q0.__sqrt__()

def test_sqrt_negative():
    q1 = qualean.Qualean(1)
    if q1.num > 0:
        q1.num *= -1
    
    temp = q1 * -1
    temp_sqrt = str(temp.sqrt())+'j'

    assert temp_sqrt == q1.__sqrt__()

def test_add_mul_hundred_times():
    q1 = qualean.Qualean(1)
    sum = 0

    for i in range(100):
        sum = q1 + sum

    assert Decimal(round(q1 * 100, 10)) == Decimal(round(sum, 10))


def test_sum_one_million():

    sum = 0
    for i in range(1000000):
        q = qualean.Qualean(random.choice([-1,0,1]))
        sum = q + sum
    assert math.isclose(sum, 0, rel_tol = 10^3)

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10
