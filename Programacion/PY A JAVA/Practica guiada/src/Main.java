public class Main {
    public static void main(String[] args) {
        Moto moto = new Moto("Suzuki");
        Camion camion = new Camion("Pegaso");

        moto.tocarClaxon();
        camion.tocarClaxon();
    }
}