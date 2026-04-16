public class EJ5 {
    public static void main(String[] args) {
        double[] ventas = new double[7];
        for (int i = 0; i < ventas.length; i++) {
            double num = Math.random() * 100;
            ventas[i]=num;
        }
        double suma = 0;
        int count = 0;
        double mayor = 0;

        for (int i = 0; i < ventas.length; i++) {
            suma = suma + ventas[i];

            if (ventas[i] > 50) {
                count++;
            }
            if (ventas[i] > mayor) {
                mayor = ventas[i];
            }
        }
        System.out.println("La suma de todas las ventas es: " + suma);
        System.out.println("El numero de ventas superiores a 50 es: " + count);
        System.out.println("La venta mas grande es: " + mayor);
    }
}

