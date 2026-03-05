import javax.swing.JOptionPane;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        boolean partida = true;

        Tablero tablero = new Tablero();

        System.out.println("Nombre jugador 1:");
        String nom1 = sc.nextLine();
        Jugador jugador1 = new Jugador(nom1,'X');

        System.out.println("Nombre jugador 2:");
        String nom2 = sc.nextLine();
        Jugador jugador2 = new Jugador(nom2,'0');

        while (partida) {

            tablero.mostrar();
            if (tablero.comprobarGanador(jugador2.getSimbolo())) {
                jugador2.Ganador();

                partida = false;
                break;
            }
            System.out.println("Turno jugador " + jugador1.getNombre());
            int posx = sc.nextInt();
            tablero.marcar(posx, 'x');

            tablero.mostrar();
            if (tablero.comprobarGanador(jugador1.getSimbolo())) {
                jugador1.Ganador();

                partida = false;
                break;
            }
            System.out.println("Turno jugador " + jugador2.getNombre());
            int poso = sc.nextInt();
            tablero.marcar(poso, 'o');
        }
    }
}
