import java.util.Scanner;

public class PrimeNumber {
    public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter the number you wanted check: ");
    int number = scanner.nextInt();
        boolean isPrime = true;

        if (number <= 1) {
             isPrime = false;
        } else {
            //for (int i = 2; i < number; i++) { --can use this witout sqrt but it will be less efficient
            for (int i = 2; i <= Math.sqrt(number); i++) {
                if (number % i == 0) {
                    isPrime = false;
                    break;
                }
            }
        }
        scanner.close();
        System.out.println(number + " is prime? " + isPrime);
    }    
}
