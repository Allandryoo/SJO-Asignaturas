import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

public class Main {
    public static void main(String[] args) {
        final String FILE_NAME="demo.txt";
        try{
            FileWriter fw=new FileWriter(FILE_NAME);
            BufferedWriter bw=new BufferedWriter(fw);
            bw.write("Hola mundo;)");
            bw.close();

            FileReader fr=new FileReader(FILE_NAME);
            BufferedReader br=new BufferedReader(fr);
            String line=br.readLine();
            while(line!=null){
                System.out.println(line);
                line=br.readLine();
            }
        }catch (Exception e){
            System.out.println(e.getMessage());
        }
    }
}