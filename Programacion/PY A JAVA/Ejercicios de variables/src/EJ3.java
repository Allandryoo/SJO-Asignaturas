public class EJ3 {
    public static void main(String[] args) {
        String nombreProducto = "Ratones";
        double precio = 15.00;
        int cantidad = 7;

        double total = precio * cantidad;

        System.out.println(total);

        Object[] listaDatos= new Object[4];
        listaDatos[0]=nombreProducto;
        listaDatos[1]=precio;
        listaDatos[2]=cantidad;
        listaDatos[3]=total;

        System.out.println("El inventario " + nombreProducto + " asciende a " + total);
    }
}