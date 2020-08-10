# session4-qualean

Welcome to EPAi Session 4 assignment! 

The repo contains a Qualean class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. 
* It implements these functions (with exactly the same names)
__and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__, __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__

## Description

It contains the following files:

* qualean.py - This file contains the methods for Qualean class and are defined below. 
* test_qualeon.py - This file contains the tests using the framework pytest. 

### Qualean

#### init

Creates Qualean object with stored value equal to real (input from user) * random generated number

#### bool
Returns False for Qualean value = 0; True otherwise

#### and
Performs AND operation between Qualean objects

#### or
Performs OR operation between Qualean objects

#### repr
Overloads repr method for Qualean objects

#### str

Overloads str method for Qualean objects

#### add
Sums up the values of the Qualean objects. If the user provides an object other than Qualean object then the argument is converted into Decimal before summing up. 

#### eq
Checks equality between the values of the Qualean object 

#### gt
Returns True if the value is greater than passed argument else False

#### ge

Returns True if the value is greater than or equal to the passed argument else False


#### lt
Returns True if the value is lesser than passed argument else False

#### le

Returns True if the value is lesser than or equal to the passed argument else False

#### mul

Returns the product of the values of the Qualean objects. If the user provides an object other than Qualean object then the argument is converted into Decimal before calculating the product

#### invertsign
Returns the Qualean object with its sign inverted

#### float
Returns the float representation of the Qualean object

#### int
Returns the integer representation of the Qualean object

#### sqrt
Returns the square root of the Qualean object. If the object is negative then the sqrt of absolute value is found and converted into a string representation of complex number


### Testcases
#### test_invalid_real_part 
Checks if ValueError is returned if a value other than 1, 0 , -1 is passed to Qualean

#### test_and_with_valid_q2
Checks and for valid q1 and q2 

#### test_and_with_undefined_q2
Checks if q1 and q2 returns False when q2 is not defined as well and q1 is False

#### test_or_with_valid_q2
Checks or for valid q1 and q2

#### test_or_with_valid_q2
Checks if q1 or q2 returns True when q2 is not defined as well and q1 is not false

#### test_class_repr
Checks if repr is overloaded correctly

#### test_class_str
Checks if the string representation of Qualean is returned

#### test_add
Checks the addition of 2 Qualeans returns the sum of their numeric values

#### test_eq
Checks if the Qualeans created with 0 are equal

#### test_gt
Checks if q1 > q2 given q1's numeric value is larger


#### test_ge
Checks if q1 >= q2 given q1's numeric value is larger


#### test_lt
Checks if q1 < q2 given q1's numeric value is smaller


#### test_le
Checks if q1 < q2 given q1's numeric value is smaller

#### test_le_eq
Checks if q1 <= q2 when both are equal


#### test_ge_eq
Checks if q1 => q2 when both are equal

#### test_mul
Checks if the product of q1 and q2 is equal to the product of their numeric values

#### test_invert
Checks if the sign is inverted. A positive value becomes negative and vice versa.

#### test_sqrt
Checks if Decimal(str(q1)).sqrt() == q1.__sqrt__()

#### test_sqrt_negative
Checks if square root of negative Qualean is equal to a string rep of complex number 

#### test_add_mul_hundred_times
Checks if q + q + q ... 100 times = 100 * q

#### test_sum_one_million
Checks if sum of 1 million different qs is very close to zero

####  test_readme_exists
Checks if the ReadMe file exists in the repo

#### test_readme_contents
Checks if the readme contains atleast 500 words

#### test_readme_proper_description
Checks if the readme contains all functions

#### test_readme_file_for_formatting
Checks if the ReadMe is formatted correctly

