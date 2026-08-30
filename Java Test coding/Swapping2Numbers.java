public class Swapping2Numbers {
    public static void main(String[] args) {
        int a = 5;
        int b = 10;
        System.out.println("Before swapping: a = " + a + ", b = " + b);

        // Logic 1: Swapping using a temporary variable
        int temp = a;
        a = b;
        b = temp;
        System.out.println("After swapping with temporary variable: a = " + a + ", b = " + b);
        
        //Logic 2: Swapping without using a temporary variable
        a = a + b; // a now holds the sum of a and b
        b = a - b; // b now holds the original value of a
        a = a - b; // a now holds the original value of b
        System.out.println("After swapping without temporary variable: a = " + a + ", b = " + b);

        //Logic 3: Swapping using * and /
        a = a * b; 
        b = a / b;
        a = a / b;
        System.out.println("After swapping  * and /: a = " + a + ", b = " + b);
        
        //Logic 4: Bitwise XOR(^)
        a=a^b;
        b=a^b;
        a=a^b;
        System.out.println("After swapping with bitwise XOR: a = " + a + ", b = " + b);
    }
}
