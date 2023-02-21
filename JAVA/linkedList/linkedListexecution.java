package DataStructnAlgo.JAVA.linkedList;

public class linkedListexecution {
    public static void main(String[] args) {
        linkedlist first = new linkedlist();
        first.insert(first, 100);
        first.insert(first, 12);
        first.insert(first, 121);
        first.insert(first, 221);
        first.insert(first, 21);
        first.printlist(first);
    }
}

class linkedlist {
    node head;

    static class node {
        float value;
        node pointer;

        node(float value) {
            this.value = value;
            this.pointer = null;
        }
    }

    public static linkedlist insert(linkedlist linlist, float data) {
        node newNode = new node(data);

        if (linlist.head == null) {
            linlist.head = newNode;
        } else {
            node lastNode = linlist.head;
            while (lastNode.pointer != null) {
                lastNode = lastNode.pointer;
            }
            lastNode.pointer = newNode;
        }
        return linlist;
    }
    
    public static linkedlist printlist(linkedlist linklist) {
        node lastNode = linklist.head;
        while(lastNode.pointer != null) {
            System.out.println(lastNode.value);
            lastNode = lastNode.pointer;
        }
        return null;
    }
}