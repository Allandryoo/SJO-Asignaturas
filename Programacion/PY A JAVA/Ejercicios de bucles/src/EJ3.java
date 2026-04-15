import java.util.Scanner;

public class EJ3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Que tabla de multiplicar quieres?");
        int num = sc.nextInt();
        System.out.println("Tabla de multiplicar del " + num);
        for (int i = 1; i < 11; i++) {
            System.out.println(i*num);
        }
    }
}
