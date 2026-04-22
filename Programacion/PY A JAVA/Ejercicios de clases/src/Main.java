public class Main {
    public static void main(String[] args) {
        Libro libro1 = new Libro("Libro1","Alan1",100);
        libro1.MostrarLibro();
        Libro libro2 = new Libro("Libro2","Alan2",200);
        libro2.MostrarLibro();
        Libro libro3 = new Libro("Libro3","Alan3",300);
        libro3.MostrarLibro();

        Personaje mago = new Personaje("Alan");
        Personaje guerrero = new Personaje("Fran");

        mago.recibirDamage(20);
        mago.mostrarEstado();
        mago.curar();
        mago.mostrarEstado();
        guerrero.mostrarEstado();
    }
}