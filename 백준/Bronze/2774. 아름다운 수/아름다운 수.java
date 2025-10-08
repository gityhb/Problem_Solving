import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int t = 0; t < T; t++) {
            int X = sc.nextInt();
            int[] digitCount = new int[10];
            int count = 0;

            while (X > 0) {
                int digit = X % 10;
                if (digitCount[digit] == 0) {
                    count++;
                }
                digitCount[digit]++;
                X /= 10;
            }

            System.out.println(count);
        }

        sc.close();
    }
}
