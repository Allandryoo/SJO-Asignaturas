public class Main {
    public static void main(String[] args) {
        VideoJuegos juego = new VideoJuegos("Rocekt League", "Coches", 5);
        Jugador player1 = new Jugador("alan", 12, 0);
        Jugador player2 = new Jugador("good boy", 8, 0);

        Partida partida1 = new Partida(juego, player1, player2);
        Partida partida2 = new Partida(juego, player1, player2);
        Partida partida3 = new Partida(juego, player1, player2);

        Partida[] partidas = new Partida[3];

        partidas[0] = partida1;
        partidas[1] = partida2;
        partidas[2] = partida3;
        while (player1.puntosAcumulados < juego.PuntosVictoria && player2.puntosAcumulados < juego.PuntosVictoria){
            for (int i = 0; i < partidas.length-1; i++) {
                partidas[i].iniciarPartida();
            }
        }
    }
}