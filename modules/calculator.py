class Calculator():

    def __init__(self):
        self.num1 = None
        self.num2 = None
    
    def number_is_integer(self, num):
        return True if isinstance(num, int) else False

    def number_is_float(self, num):
        return True if isinstance(num, float) else False
 
    def number_is_none(self, num):
        return True if num == None else False

    def number_is_string(self, num):
        return True if isinstance(num, str) else False

    def can_convert_to_float(self, num):
        try:
            return isinstance(float(num), float)
        except ValueError:
            return False
        except TypeError:
            return False

    def can_use_number(self, num):
        if self.number_is_integer(num):
            return True
        if self.number_is_float(num):
            return True
        if self.number_is_none(num):
            return False
        if self.number_is_string(num):
            return self.can_convert_to_float(num)

    def can_use_numbers(self, num1, num2):
        return True if self.can_use_number(num1) and self.can_use_number(num2) else False

    def number_is_zero(self, num):
        return True if num == 0 else False

    def add(self, num1, num2):
        if self.can_use_numbers(num1, num2):
            return float(num1) + float(num2)
        else:
            return 'Error: Cannot add values'

    def subtract(self, num1, num2):
        if self.can_use_numbers(num1, num2):
            return float(num1) - float(num2)
        else:
            return 'Error: Cannot subtract values'

    def multiply(self, num1, num2):
        if self.can_use_numbers(num1, num2):
            return float(num1) * float(num2)
        else:
            return 'Error: Cannot multiply values'

    def divide(self, num1, num2):
        if self.can_use_numbers(num1, num2):
            num1 = float(num1)
            num2 = float(num2)
            if self.number_is_zero(num2):
                return 'Error: Cannot divide by zero'
            else:
                return num1 / num2
        else:
            return 'Error: Cannot divide values'