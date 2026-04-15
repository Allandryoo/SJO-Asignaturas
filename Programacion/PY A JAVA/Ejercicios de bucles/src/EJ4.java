public class EJ4 {
    public static void main(String[] args) {
        int[] numeros = new int[10];
        numeros[0] = 3;
        numeros[1] = 3;
        numeros[2] = 3;
        numeros[3] = 3;
        numeros[4] = 3;
        numeros[5] = 7;
        numeros[6] = 3;
        numeros[7] = 3;
        numeros[8] = 3;
        numeros[9] = 3;

        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] == 7) {
                System.out.println("Tesoro encontrado en la posicion " + i + ".");
                break;
            }

        }System.out.println("Mapa vacio");
    }
}
