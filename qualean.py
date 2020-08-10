import random
from decimal import Decimal

"""Class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place. """

class Qualean(object):

    ''' 
        Creates Qualean object with stored value equal to real (input from user) * random generated number 

        Parameters:
            real - a number from [-1, 0, 1]

    ''' 
    def __init__(self, real):
        
        if real not in [-1,0,1]:
            raise ValueError("Real state of Qualean not in [-1,0,1]")

        #self.dict = {-1: "Maybe", 0: "False", 1:"True"}

        self.real = real
        self.imag = random.uniform(-1, 1)
        self.num = Decimal(round(self.imag * real, 10))


    '''
        Return a Boolean value

    '''
    def __bool__(self):
        if self.num == 0:
            return False
        return True

    '''
       Performs AND operation between Qualean objects

       Parameters:
            qvalue - Qualean object

       Return:
            False when qvalue is not defined and current Qualean object is False
            False when both are False
            True otherwise

    '''

    def __and__(self, qvalue):
        
        if not isinstance(qvalue, Qualean) and self.num == 0:
            return False

        if self.num == 0 or qvalue.num == 0:
            return False
        return True
            
    '''
       Performs OR operation between Qualean objects

       Parameters:
            qvalue - Qualean object

       Return:
            True when qvalue is not defined and current Qualean object is False
            False when both are False
            True otherwise

    ''' 
    def __or__(self, qvalue):
             
        if not isinstance(qvalue, Qualean) and self.num !=0:
            return True

        if self.num != 0 or qvalue.num !=0:
            return True

        return False
    
    '''
       Overloads repr method for Qualean objects

    '''
    def __repr__(self):
        return f'Qualean object with value {self.num}'

    '''
	Overloads str method for Qualean objects

    '''
    def __str__(self):
        return str(self.num) 


    '''
	Returns sum of two Qualean objects

    '''
    def __add__(self, qvalue):

        if isinstance(qvalue, Qualean):
            return self.num + qvalue.num

        return self.num + Decimal(qvalue)

    '''
	Equality check for two Qualean objects

    '''

    def __eq__(self, qvalue):

        if isinstance(qvalue, Qualean):
            return self.num == qvalue.num

        return self.num == Decimal(qvalue)

    '''
	Checks if the Qualean object is greater than the other

    '''
    
    def __gt__(self, qvalue):

        if isinstance(qvalue, Qualean):
            return self.num > qvalue.num

        return self.num > Decimal(qvalue)

    '''
	Checks if the Qualean object is greater than or equal to the other

    '''

    def __ge__(self, qvalue):

        if isinstance(qvalue, Qualean):
            return self.num >= qvalue.num

        return self.num >= Decimal(qvalue)


    '''
        Checks if the Qualean object is lesser than the other

    '''
    def __lt__(self, qvalue):

        if isinstance(qvalue, Qualean):
            return self.num < qvalue.num

        return self.num < Decimal(qvalue)

    '''
        Checks if the Qualean object is lesser than or equal to the other

    '''

    def __le__(self, qvalue):

        if isinstance(qvalue, Qualean):
            return self.num <= qvalue.num

        return self.num <= Decimal(qvalue)

    '''
        Returns the product of two Qualean objects
 
    '''

    def __mul__(self, qvalue):
        if isinstance(qvalue, Qualean):
            return self.num * qvalue.num

        return self.num * Decimal(qvalue)

 
    '''
	Returns the Qualean object with its sign inverted

    '''

    def __invertsign__(self):
        self.num *=-1
        return self.num

    def __invert__(self):
        return self.__invertsign__()


    '''
       Returns the float representation of the Qualean object

    '''

    def __float__(self):
        return float(self.num)


    '''
       Returns the integer representation of the Qualean object

    '''
    def __int__(self):
        return int(self.num)

    ''' 
       Returns the square root of the Qualean object
       If the object is negative then the sqrt of absolute value is found 
          and converted into a string representation of complex number

    '''

    def __sqrt__(self):

        if self.num < 0:
            temp = abs(self.num)
            sqrt_val = temp.sqrt()
            return str(sqrt_val)+'j'

        else:
            return self.num.sqrt()

