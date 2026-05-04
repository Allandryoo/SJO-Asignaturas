public class Partida {
    public VideoJuegos juego;
    public Jugador jugador1;
    public Jugador jugador2;

    Partida(VideoJuegos juego, Jugador jugador1, Jugador jugador2){
        this.juego = juego;
        this.jugador1 = jugador1;
        this.jugador2 = jugador2;
    }

    public void iniciarPartida() {
        if (jugador1.nivel >= jugador2.nivel){
            jugador1.puntosAcumulados ++;
            System.out.println("Ha ganado " + jugador1.nickname);
            System.out.println(jugador1.puntosAcumulados);
        } else {
            jugador2.puntosAcumulados ++;
            System.out.println("Ha ganado " + jugador2.nickname);
            System.out.println(jugador2.puntosAcumulados);
        }
    }
}
