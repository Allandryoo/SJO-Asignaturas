import java.util.Scanner;

public class EJ3 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Introduce tu edad:");
        int edad = in.nextInt();
        System.out.println("Tienes entrada?");
        Boolean entrada = in.nextBoolean();
        System.out.println("Cuanto dinero tienes?");
        double dinero = in.nextDouble();
        String acces;
        if (edad >= 18 && entrada) {
            acces = "Acceso permitido";
        } else if (edad < 18 && !entrada) {

        }

    }
}