# Creating a class linkedList
class linkedList:
    # Set the instance variable head to None
    #i.e when the list is first create it just points to none
    def __init__(self):
        self.head = None
    
    # Creating a class node
    class node:
        #Node has two instance variables
        # One stores the value 
        # Another points to the next value 
        def __init__(self,value):
            #This instance variable holds the value 
            self.value = value
            #We initialize the pointer with none 
            #As the last element doesn't point to anything
            self.pointer = None


    def insert(linkedlist,value):

        """ This function is used to insert values 
         at the end of the list """
        
        # Creates a object of class linked list 
        # and set the node value 
        newNode = linkedList.node(value)

        # Head is the first element in the linked list
        # We first cheekc if it is pointing to anything

        if linkedlist.head == None:
            # If it is pointing to none then it is empty
            # Meaning we are going to ad the first element
            linkedlist.head = newNode
            # Since it is the first element we simply say
            # Head = the new node
        else:

            # In case head is not None we iterate through the list to find the lost node
            lastNode = linkedlist.head
            while lastNode.pointer != None:
                #The loop runs till the node pointer is None
                #Once it finds it, the lastNode value will be the last node
                lastNode = lastNode.pointer

            #We assign the last node pointer to the new node
            lastNode.pointer = newNode
        
    def printlist(linkedlist):

        """ This function iterates through the linked list and prints each element one by one  """

        lastNode = linkedlist.head
        #The loop iterates through the linked list till the 
        #Node is pointing to Null
        
        while lastNode.pointer != None:
                
                print(lastNode.value,end="-->")
                lastNode = lastNode.pointer
        #Last element won't be printed as the loop ends 
        #We print it over here 
        print(lastNode.value,end="-->None")

firstval = linkedList()

linkedList.insert(firstval,12)
linkedList.insert(firstval,13)
linkedList.insert(firstval,14)
linkedList.insert(firstval,15)
linkedList.insert(firstval,16)

linkedList.printlist(firstval)