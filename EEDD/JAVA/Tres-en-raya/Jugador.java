import javax.swing.JFrame;
import javax.swing.JOptionPane;
public class Jugador {
    String nombre;
    char simbolo;

    public Jugador(String nombre, char simbolo) {
        this.simbolo = simbolo;
        this.nombre = nombre;
    }

    public char getSimbolo() {
        return simbolo;
    }

    public String getNombre() {
        return  nombre;
    }

    public void setSimbolo(char simbolo) {
        this.simbolo = simbolo;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void Ganador () {
        JFrame frame = new JFrame();
        frame.setAlwaysOnTop(true);
        frame.setVisible(true);
        frame.toFront();
        frame.requestFocus();
        JOptionPane.showMessageDialog(frame, "Ha ganado " + this.nombre);
    }
}
