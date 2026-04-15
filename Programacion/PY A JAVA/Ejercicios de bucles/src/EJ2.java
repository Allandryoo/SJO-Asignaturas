import java.util.Scanner;
public class EJ2 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.println("Introduce 5 numeros");

        int[] lista = new int[5];
        for (int i = 0; i < lista.length; i++) {
            int num = sc.nextInt();
            lista[i]=num;
        }
        int suma = 0;
        for (int i = 0; i < lista.length; i++) {
            suma = suma + lista[i];
        }
        System.out.println(suma);
    }
}
