
class stack:

    """ This class is used to implement stack data Structure  """

    def __init__(self,size): 

        """ Initialize the instance variable, gets the size of the stack as parameter """

        self.index = -1 # Sets the top element to 0 when initialized
        self.stackArray = list() # Creates an array which acts as stack
        self.size  = size   # Initializes the instance variable to the size passed as the parameter by the user

    def isEmpty(stackArray):

        """ This functions checks if a stack is empty.
         If empty it will return True 
        Else it will return False """

        if stackArray.index == -1:
            # Since the index is initialized with -1 when no value is added
            # We check if the index is -1
            # If yes , return true 
            return True
        else:
            return False
        
    def isFull(stackArray):

        """ This function checks if the stack exceeds the user
        given size for the stack"""

        if stackArray.index == stackArray.size-1:
            # If the top element index is stack size - 1 
            # returns true
            return True
        else:
            # If the top element index is less than the stack size -1 
            # Returns false
            return False
        
    def pop(stackArray):

        """ removes the top most value and prints it """

        if stack.isEmpty(stackArray):
            # Checks if the stack is empty using the user defined function
            # If empty, prints the error message
            print("Oops the stack is empty !!")

        else:
            # If the stack is not empty it will remove the top element and prints it
            print(f"Deleted element : {stackArray.stackArray[stackArray.index]}")
            # Decrements the index of the top element by 1
            stackArray.index -= 1

    def push(stackArray,value):

        """ Add element to the stack """

        if stack.isFull(stackArray):
            # Checks if the stack is empty, if so it will print error message
            print("Oops the stack is full !!")
        else:
            # Increments the index and append the value
            stackArray.index += 1
            stackArray.stackArray.append(value)

    def peek(stackArray):

        """ This user defined function prints the top most element """

        if stack.isEmpty(stackArray):
            # Checks if the stack is empty, if empty prints the r=error message
            print("The stack is empty")
        else:
            print(f"Top element : {stackArray.stackArray[stackArray.index]}")

# Creating an object of type array
stackArray = stack(10)

# Adding element to the object
stackArray.push(12)
stackArray.push(13)
stackArray.push(14)
stackArray.push(15)
stackArray.push(16)
stackArray.push(17)
stackArray.push(18)
stackArray.push(19)
stackArray.push(10)
stackArray.push(11)

# Prints the top most element
stackArray.peek()
# Tries to push an element after the stack is full
stackArray.push(324)
# Removes the top most element from the stack
stackArray.pop()
# Prints the top most element from the stack after removing the top element
stackArray.peek()
