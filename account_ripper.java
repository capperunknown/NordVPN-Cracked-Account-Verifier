import java.io.File;
import java.io.FileWriter; 
import java.io.FileNotFoundException;
import java.util.Scanner;

public class account_ripper {
    public static void main(String[] args){
        Scanner reader = new Scanner(System.in);
        File data = new File("nord.txt");
        

        try {
            reader = new Scanner(data);
            FileWriter writer = new FileWriter("formattedAccounts.txt");//enter full path

            while(reader.hasNextLine()){
                String line = reader.nextLine();
                String[] temp = line.split(":");
                temp = line.split(" ");
                String credentials = temp[0];
                
                writer.write(credentials+"\n");
            }
            reader.close();
            writer.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
