import java.util.Arrays;
import java.util.Scanner;

public class EJ2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Introduce el numero 1");
        int num1 = in.nextInt();
        System.out.println("Introduce el numero 2");
        int num2 = in.nextInt();
        System.out.println("Introduce el numero 3");
        int num3 = in.nextInt();

        int[] Lista ={num1, num2, num3};

        Arrays.sort(Lista);

        for (int i=0;i < Lista.length; i++) {
            System.out.println(Lista[i]);
        }
    }
}