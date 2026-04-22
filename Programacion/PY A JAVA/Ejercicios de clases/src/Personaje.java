public class Personaje {
    private String nombre;
    private int nivel;
    private double vida;

    Personaje(String nombre){
        this.nombre = nombre;
        this.nivel = 1;
        this.vida = 100;
    }
    public void recibirDamage(double cantidad) {
        if (this.vida > 0) {
            this.vida -= cantidad;
            System.out.println("Te han atacado");
        } else {
            System.out.println("Personaje muerto");
        }
    }
    public void curar() {
        this.vida = 100;
        System.out.println("Te has curado");
    }
    public void mostrarEstado() {
        System.out.println(this.nombre + " | lvl:" + this.nivel + " | Vida:" + this.vida);
    }
}
