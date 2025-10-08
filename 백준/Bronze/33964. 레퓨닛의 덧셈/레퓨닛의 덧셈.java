import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt();
        int Y = sc.nextInt();

        String repunitX = "";
        String repunitY = "";

        for (int i = 0; i < X; i++) {
            repunitX += "1";
        }

        for (int i = 0; i < Y; i++) {
            repunitY += "1";
        }

        int numX = Integer.parseInt(repunitX);
        int numY = Integer.parseInt(repunitY);

        System.out.println(numX + numY);
    }
}