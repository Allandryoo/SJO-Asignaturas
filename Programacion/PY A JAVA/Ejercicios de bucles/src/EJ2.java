import java.util.Scanner;
public class EJ3 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.println("Introduce 5 numeros");

        Boolean salir = false;

        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int num3 = sc.nextInt();
        int num4 = sc.nextInt();
        int num5 = sc.nextInt();

        int[] lista = new int[5];

        lista[0] = num1;
        lista[1] = num2;
        lista[2] = num3;
        lista[3] = num4;
        lista[4] = num5;
        int suma = 0;
        for (int i = 0; i < lista.length; i++) {
            suma = suma + lista[i];
        }
        System.out.println(suma);
    }
}
