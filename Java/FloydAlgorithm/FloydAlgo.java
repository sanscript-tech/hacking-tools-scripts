import java.util.*;
import java.io.*;
import java.lang.*;
//Node of Linked list
class Node
{
    int data;
    Node next;
    Node(int x)
    {
        data = x;
        next = null;
    }
}
public class DetectLoop
{
    public static void createLoop(Node head, Node tail, int k){
        if (x == 0) return;
        Node curr = head;

        for(int i=1; i<k; i++)
            curr = curr.next;
        tail.next = curr;
    }
    // } Driver Code 
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        
        //no. of nodes in linked list
        int n = sc.nextInt();
         
        //head of Linked list
        int num = sc.nextInt();
        Node head = new Node(num);
        Node tail = head;

        //Linked List created
        for(int i=0; i<n-1; i++)
        {
            num = sc.nextInt();
            tail.next = new Node(num);
            tail = tail.next;
        }

        //Node to check if loop exists or not
        int temp = sc.nextInt();
     createLoop(head,tail,temp);
    
        Solution x = new Solution();
        
        if( x.detectLoop(head) )
            System.out.println("Loop exists");
        else
            System.out.println("Loop doesn't exists");
    }
}
//  Driver Code Ends
//detecting if the loop exists or not
class Solution {
    public static boolean detectLoop(Node head){
        if(head==null||head.next==null)
            return false;

        Node slow = head;
        Node fast = head;

        while(fast != null && fast.next != null) {
            
            slow = slow.next;
            fast = fast.next.next;
    
            if(slow==fast)
                return true;
        }
         
        return false;
    }
}