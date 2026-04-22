public class Libro {
    private String Titulo;
    private String Autor;
    private int Paginas;

    Libro(String Titulo, String Autor, int Paginas) {
        this.Titulo = Titulo;
        this.Autor = Autor;
        this.Paginas = Paginas;
    }

    public void MostrarLibro(){
        System.out.println("Titulo: " + Titulo + " | Autor: " + Autor + " | Paginas: " + Paginas);
    }
}


