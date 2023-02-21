package DataStructnAlgo.JAVA.Stack;

public class stackexe {
    public static void main(String[] args) {
        // Creating an object of class stack with size 10
        stack stackArrayn = new stack(10);

        // Inserting values inside the stack
        stackArrayn.push(stackArrayn, 120);
        stackArrayn.push(stackArrayn, 110);
        stackArrayn.push(stackArrayn, 100);
        stackArrayn.push(stackArrayn, 1200);
        stackArrayn.push(stackArrayn, 1202);
        stackArrayn.push(stackArrayn, 1209);

        // Printing the top element from the stack
        stackArrayn.peek(stackArrayn);

        // Removing the top element from the stack 
        stackArrayn.pop(stackArrayn);

        // Printing the top elelmetn from the stack 
        stackArrayn.peek(stackArrayn);
    }
}

// Creating stack class
class stack {

    // Declaring the instance variable
    int size; // This variable sets the size of the stack
    int stackArray[]; // This will be the array that acts as stack
    int index; // Holds the index of the top most element

    //Constructor
    stack(int size) {

        // Assigning the parameter to the instance variable size 
        this.size = size;
        // Creating an array object with the size 
        stackArray = new int[size];

        // Setting the index to -1 as when initialized the stack is empty
        index = -1;
    }
    
    
    public void push(stack stackArray3, int value) {
        /* This function gets the stack an integer value as the argument and 
         * assign the value to the array in the corresponding index
         * then increments the index by 1 to point to the top most value 
         */
        if (isFull(stackArray3)) {
            // Checks if the stack is fully using the user defined function
            System.out.println("The stack is full");
        } else {
            //increments the index to top positin
            stackArray3.index++;
            //assigns the value to the index
            stackArray3.stackArray[stackArray3.index] = value;
        }
    }
    
    public void pop(stack stackArray5) {
        /* Decrements the index by 1, and returns the previous index value
         */
        if (isEmpty(stackArray5)) {
            // Checks if the array is empty usign the user defined function
            System.out.println("The stack is empty");
        }
        else {
            // Prints the top element
            System.out.print("Deleted element is : " + stackArray5.stackArray[stackArray5.index]);
            // Decrements the index
            stackArray5.index--;
        }
    }

    public void peek(stack stackArray6) {
        /* This function prints the top most element */
        if (isEmpty(stackArray6)) {
            // Checks if the stack is empty
            System.out.println("The stack is empty");
        }
        else {
            // Prints the top element in the stack
            System.out.println("peek "+stackArray6.stackArray[stackArray6.index]);
        }
    }

    public boolean isFull(stack stackArray2) {
        /* This function checks if the array is full
         * If full returns true 
         * Else returns false
         */
        if (stackArray2.index == stackArray2.size - 1) {
            // We check if the index of top element is size of the array -1 
            // If yes we return true
            return true;
        } else {
            // If the index of top element is not equal to the size of the array -1
            // Returns false
            return false;
        }
    }
    
    public boolean isEmpty(stack stackArray4) {
        /* Checks if the stack is empty
         * If empty it will return true
        Else it will return false
         */
        if (stackArray4.index == -1) {
            // Since the instance variable is initialized to -1, we check if index = -1
            // If it is equal to -1 return true
            return true;
        }
        else {
            // If index is not -1 , returns false
            return false;
        }
    }
}
