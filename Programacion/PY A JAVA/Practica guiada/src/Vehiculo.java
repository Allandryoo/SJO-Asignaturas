public class Vehiculo {
    public String marca;
    public int velocidad;

    public void tocarClaxon() {
        System.out.println("claxon");
    }

    public void avanzar() {
        this.velocidad += 1;
        System.out.println(this.velocidad);
    }

    public void frenar() {
        this.velocidad=0;
        System.out.println(this.velocidad);
    }
}
