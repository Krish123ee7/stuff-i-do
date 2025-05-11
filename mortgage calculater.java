import java.text.NumberFormat;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int principal,months;
        double rate;
        while (true){
            System.out.print("Principal($1K to $1M): ");
            principal = scanner.nextInt();
            if (principal<1_000 || principal>1_000_000)
                System.out.print ("please enter a value between $1K and $1M: ");
            else
                break;
        }
        while (true){
            System.out.print("Annual Interest rate(1 to 30): ");
            rate = scanner.nextDouble();
            if (rate <=0 || rate >30)
                System.out.print("please enter a value between 1 and 30: ");
            else {
                rate = rate / 100 / 12;
                break;
            }
        }
        while (true){
            System.out.print("Years(1 to 30): ");
            months = scanner.nextInt();
            if (months <=0 || months >30)
                System.out.print("please enter a value between 1 and 30: ");
            else {
                months = months*12;
                break;
            }
        }

        double mortgage = principal*rate*(Math.pow((1+rate),months))/(Math.pow((1+rate),months)-1);
        String mortgageCurrency = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("Mortgage: "+mortgageCurrency);
    }
}
