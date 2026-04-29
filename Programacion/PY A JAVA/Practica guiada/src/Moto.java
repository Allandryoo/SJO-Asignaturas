public class Moto extends Vehiculo{

    public Moto(String marca){
        this.marca = marca;
        this.velocidad = 0;
    }

    public void tocarClaxon() {
        System.out.println("Piii");
    }
}
