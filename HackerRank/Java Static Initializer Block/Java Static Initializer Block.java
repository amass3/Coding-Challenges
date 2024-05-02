import java.io.*;
import java.util.*;

public class Solution {
        
        /*In a Java class, a static block is a set of instructions that is run only once when a class is loaded into memory.
         A static block is also called a static initialization block. This is because it is an option for initializing or setting up the 
         class at run-time.*/
        
        //Global variable
        static int B, H;
        static boolean flag = false;
        
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        //Getting the input
        Scanner input = new Scanner(System.in);
        B = input.nextInt();
        H = input.nextInt();
        
        //Constraint -100 <= B <= 100 and -100 <= H <= 100
        if((B > 0 && H > 0) && (B <= 100 && H <= 100)){ 
            flag = true;
        }
        
        //If true calculate the area or print error message
        if(flag){
            int area=B*H;
            System.out.print(area);
        }else{
            System.out.print("java.lang.Exception: Breadth and height must be positive");
        }    
    }
}

