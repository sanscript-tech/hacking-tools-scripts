import java.util.*;
import java.io.*;
import java.lang.*;
//Node of Linked list
class Node
{   
    int data;   //value of the node
    Node next;  //next node
    /*Constructor*/
    Node(int x)
    {
        data = x;
        next = null;
    }
}
public class DetectLoop
{   //function to create loop in linked list 
    public static void createLoop(Node head, Node tail, int k){
        //base case
        if (x == 0) return;
        Node curr = head;

        for(int i=1; i<k; i++)
            curr = curr.next;// traversing the linked list till k
        tail.next = curr;
    }
    // Driver Code 
    public static void main (String[] args){
        
        Scanner sc = new Scanner(System.in);
        
        //no. of nodes in linked list
        int n = sc.nextInt();
         
        //head of Linked list
        int num = sc.nextInt();
        Node head=new Node(num);
        
        Node tail=head;

        //Linked List created
        for(int i=0; i<n-1; i++)
        {
            num = sc.nextInt();
            tail.next = new Node(num);
            tail = tail.next;
        }

        //Node to check if loop exists or not
        int temp = sc.nextInt();
        
        //creating the loop
        createLoop(head,tail,temp);
        
        //creating object of x
        Solution x = new Solution();
        
        //if loop exists
        if(x.detectLoop(head))
            System.out.println("Loop exists");
        else
            System.out.println("Loop doesn't exists");
    }
}

//detecting if the loop exists or not
class Solution {
    
    public static boolean detectLoop(Node head){
        //base case
        if(head==null||head.next==null)
            return false;

        Node slow = head;
        Node fast = head;

        while(fast != null && fast.next != null) {
            
            slow = slow.next;
            fast = fast.next.next;
            
            //if loop exists slow and fast pointer will surely intersect
            if(slow==fast)
                return true;
        }
         
        return false;
    }
}
