public class EJ4 {
    public static void main(String[] args) {
        double lunes = 17.2;
        double martes = 17.2;
        double miercoles = 17.2;
        double jueves = 40.2;
        double viernes = 17.2;
        double sabado = 17.2;
        double domingo = 30.2;

        double[] temperaturas= new double[7];
        temperaturas[0]=lunes;
        temperaturas[1]=martes;
        temperaturas[2]=miercoles;
        temperaturas[3]=jueves;
        temperaturas[4]=viernes;
        temperaturas[5]=sabado;
        temperaturas[6]=domingo;

        double media = (temperaturas[0] + temperaturas[3] + temperaturas[6]) / 3;

        boolean alerta=false;

        if (media >= 30) {
            alerta=true;
        }
        System.out.println("La temperatura del miercoles: " + temperaturas[2]);
        System.out.println("Promedio calculad: " + media);
        System.out.println("Estado de alerta: " + alerta);
    }
}