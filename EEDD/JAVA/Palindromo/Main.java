package org.example;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        System.out.println("Escribe una palabra y te dire se palindromo:");
        String inserta=sc.nextLine();
        char [] palabra=inserta.toCharArray();
        String pal = "";

        for (int i = palabra.length-1; i >= 0; i--) {
            int count = 0;
            pal += palabra[i];
        }
        if (pal.equals(inserta)) {
            System.out.println(inserta + " es palindromo");
        } else {
            System.out.println("No es palindromo");
        }
    }
}