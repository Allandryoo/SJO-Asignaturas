import java.util.Scanner;

public class EJ4 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int a, b, c;

        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        if ((a + b) < c) {
            System.out.println("Error");
        }else {
            if (a == b && b == c) {
                System.out.println("Equilatero");
            } else if (a == b || a == c || b == c) {
                System.out.println("Isosceles");
            } else if (a != b && a != c && b != c) {
                System.out.println("Escaleno");
            }
        }

    }
}
