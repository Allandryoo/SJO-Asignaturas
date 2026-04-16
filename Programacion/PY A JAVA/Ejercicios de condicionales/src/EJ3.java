import java.util.Scanner;

public class EJ3 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String[] seguridad = new String[2];

        System.out.println("Introduce tu edad:");
        int edad = in.nextInt();
        System.out.println("Tienes entrada?");
        Boolean entrada = in.nextBoolean();
        System.out.println("Cuanto dinero tienes?");
        double dinero = in.nextDouble();

        if (edad >= 18 && entrada) {
            seguridad[0] = "Acceso permitido";
        } else if (edad < 18 && dinero >= 50) {
            seguridad[0] = "Acceso VIP con tutor";
        } else {
            seguridad[0] = "Acceso denegado";
        }

        if (dinero > 100) {
            seguridad[1] = "Te sobra " + (dinero - 100) + "€";
        } else if (dinero < 100) {
            seguridad[1] = "Te falta" + (100 - dinero) + "€";
        } else {
            seguridad[1] = "Te has quedado justo";
        }

        System.out.println(seguridad[0]);
        System.out.println(seguridad[1]);
    }
}