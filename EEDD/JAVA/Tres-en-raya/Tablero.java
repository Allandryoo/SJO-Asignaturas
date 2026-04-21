public class Tablero {

    char[][] Tablero = {
        {'1', '2', '3'},
        {'4', '5', '6'},
        {'7', '8', '9'}
    };

    public void mostrar() {
        for (int i = 0; i < Tablero.length; i++) {
            System.out.println(Tablero[i]);
        };
    }

    public boolean comprobarGanador(char player) {

        if (Tablero[0][0] == Tablero[0][1] && Tablero[0][2] == Tablero[0][1]) {
            return true;
        } else if (Tablero[1][0] == Tablero[1][1] && Tablero[1][2] == Tablero[1][1]) {
            return true;
        } else if (Tablero[2][0] == Tablero[2][1] && Tablero[2][2] == Tablero[2][1]) {
            return true;
        } else if (Tablero[0][0] == Tablero[1][0] && Tablero[2][0] == Tablero[1][0]) {
            return true;
        } else if (Tablero[0][1] == Tablero[1][1] && Tablero[2][1] == Tablero[1][1]) {
            return true;
        } else if (Tablero[0][2] == Tablero[1][2] && Tablero[2][2] == Tablero[1][2]) {
            return true;
        } else if (Tablero[0][0] == Tablero[1][1] && Tablero[2][2] == Tablero[1][1]) {
            return true;
        } else if (Tablero[0][2] == Tablero[1][1] && Tablero[2][0] == Tablero[1][1]){
            return true;
        } else {
            return false;
        }
    }
    public void marcar(int pos, char simbolo) {
        switch (pos) {
            case 1 -> Tablero[0][0] = simbolo;
            case 2 -> Tablero[0][1] = simbolo;
            case 3 -> Tablero[0][2] = simbolo;
            case 4 -> Tablero[1][0] = simbolo;
            case 5 -> Tablero[1][1] = simbolo;
            case 6 -> Tablero[1][2] = simbolo;
            case 7 -> Tablero[2][0] = simbolo;
            case 8 -> Tablero[2][1] = simbolo;
            case 9 -> Tablero[2][2] = simbolo;
        }
    }
}
