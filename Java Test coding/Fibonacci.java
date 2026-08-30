public class Fibonacci {
    public static void main(String[] args) {
        int noOfTimes = 10;
        int a = 0, b = 1;
        System.out.println("Fibonacci series upto " + noOfTimes + ": " + "\n" + a + "\n" + b);

        // Logic 1: Using for loop
        for (int i = 2; i < noOfTimes; i++) {
            int c = a + b;
            System.out.println(" " + c);
            a = b;
            b = c;
        }
    }
}
