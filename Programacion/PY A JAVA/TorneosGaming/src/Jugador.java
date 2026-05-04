public class Jugador {
    public String nickname;
    public int nivel;
    public int puntosAcumulados;

    Jugador(String name, int nivel, int puntosAcumulados) {
        this.nickname = name;
        this.nivel = nivel;
        this.puntosAcumulados = puntosAcumulados;
    }

    public void subirNivel(){
        this.nivel ++;
    }
}
