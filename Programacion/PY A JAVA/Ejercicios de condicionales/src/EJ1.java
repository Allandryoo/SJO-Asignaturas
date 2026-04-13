import java.util.Scanner;

public class EJ1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Introduce una nota: ");
        float nota = in.nextFloat();
        
        if (nota >= 10) {
            System.out.println("Sobresaliente");
        } else if (nota >= 7) {
            System.out.println("Notable");
        } else if (nota >= 5) {
            System.out.println("Aprobado");
        } else {
            System.out.println("Suspendido");
        }
    }
}