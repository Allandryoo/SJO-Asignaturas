public class Main {
    public static void main(String[] args) {
        VideoJuegos juego = new VideoJuegos("Rocekt League", "Coches", 5);
        Jugador player1 = new Jugador("alan", 12, 0);
        Jugador player2 = new Jugador("good boy", 8, 0);

        Partida partida1 = new Partida(juego, player1, player2);

        Partida[] partidas = new Partida[3];

        for(int i =0 ; i < 3; i++){
            partidas[i]=partida1;
        }

        while (player1.puntosAcumulados < juego.PuntosVictoria && player2.puntosAcumulados < juego.PuntosVictoria){
            for (int i = 0; i < partidas.length-1; i++) {
                partidas[i].iniciarPartida();
            }
        }

        if(player1.puntosAcumulados >= player2.puntosAcumulados){
            System.out.println("Gran campeon " + player1.nickname);
        }else {
            System.out.println("Gran campeon " + player2.nickname);
        }
    }
}