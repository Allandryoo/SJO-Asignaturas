public class Camion extends Vehiculo{

    public Camion(String marca) {
        this.marca = marca;
        this.velocidad = 0;
    }

    public void tocarClaxon() {
        System.out.println("Pooo");
    }
}
