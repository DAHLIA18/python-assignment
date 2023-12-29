import java.util.Scanner;
public class PoliticalZones{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

String geoPoliticalZone = input.next();


Switch(geoPoliticalZone){
	case Oyo state, Ekiti state, Osun state, Ondo state, Lagos state, Ogun state -> System.out.println("You are from SouthWest");
	
	case Bayelsa state, Akwa Ibom state, Edo state, Rivers state, Cross Rivers state, Delta state -> System.out.println("You are from SouthWest");
	
	case Enugu state, Ebonyi state, Imo state, Abia state, Anambra state -> System.out.println -> System.out.println("You are from SouthEast);
	
	case Zamfara state, Sokoto state, Kaduna state, Kebbi state, Kastina state, Kano state, Jigawa state -> (You are from NorthWest");

	case Bauchi state, Borno state, Adamawa state, Taraba state, Gombe state, Yobe state -> ("You are from NorthEast");

	case Kogi state, Kwara state, Plateau state, Niger state, Benue state, fct, Nasarawa state -> ("You are from NorthCentral");
   }

 }


}