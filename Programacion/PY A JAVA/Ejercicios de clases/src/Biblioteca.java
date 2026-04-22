public class Biblioteca {
    private String titulo;
    private String autor;
    private boolean prestado;
    private Personaje persona;
    
    Biblioteca(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor;
        this.prestado = false;
        this.persona = null;
    }
    
    public boolean prestar(Personaje p) {
        if (!this.prestado) {
            this.prestado=true;
            this.persona = p;
            System.out.println("Libro " + this.titulo + " prestado a " + this.p.nombre);
        }
        return this.prestado;
    }

    public boolean devolver(Personaje p) {
        if (this.prestado) {
            this.prestado=false;
            this.persona=p;
            System.out.println(this.p.nombre + " has devuelto el libro.");
        }
        return this.prestado;
    }
}
