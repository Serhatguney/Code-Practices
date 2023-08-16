class maths(object):
    
    def __init__(self,m,n):
        self.value1 = m
        self.value2 = n
    
    def add(self):
        result = self.value1 + self.value2
        print("\nResult: ", result)
        
    def subtraction(self):
        result = self.value1 - self.value2
        print("\nResult: ", result)
        
    def multiply(self):
        result = self.value1 * self.value2
        print("\nResult: ", result)
        
    def divide(self):
        result = self.value1 / self.value2
        print("\nResult: ", result)

operations = [1,2,3,4]
continueControl = "yes"
while continueControl == "yes":
    while True:
        try: 
            operation = int(input("\nType 1 to use addition, 2 to use subtraction, 3 to use multiplication, and 4 to use division: "))
            while operation not in operations:
                operation = int(input("\nYou entered an incorrect number.\n\nType 1 to use addition, 2 to use subtraction, 3 to use multiplication, and 4 to use division: "))
            break
        except:
            print("\nYou entered an incorrect number.")
            
    while True :
        
        try:
            v1 = int(input("\nEnter first number: "))
            v2 = int(input("\nEnter second number: "))
            abc = maths(v1, v2)
                
            if operation == 1:
                abc.add()
            elif operation == 2:
                abc.subtraction()
            elif operation == 3:
                abc.multiply()
            elif operation == 4:
                abc.divide()               
            
            break
        except ZeroDivisionError:
            print("\nYou entered an incorrect value")
        except:
            print("\nYou entered an incorrect value.")
            
    continueControl = input("Want to do another math operation?\n\nyes or no\n")
        
    if continueControl == "yes":
        pass
    elif continueControl == "no":
        break
    else:
        while continueControl != "yes" and continueControl != "no":
            continueControl = input("Want to do another math operation?\n\nyes or no\n")