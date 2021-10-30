// CS321 Project 2: Assembler Class
// Written by Jackie and Philip


import java.io.IOException;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

// converts postfix expression into assembly.
public class Assembler {
	// the temp memory tracker
	static int temp_memory_num = 1;
	
	// method to convert an infix expression 
	// into postfix, then into assembly code
	public static String assemble(String expr) {

		// operators we're dealing with
		String operators = "+-*/";

		// create llstack
		LinkedListStack<String> ass_Stk = new LinkedListStack<String>();

		// convert infix expr to postfix
		String post_expr = Postfix.infixToPostfix(expr);
		
		// split by white spaces
		String [] tokens = post_expr.split(" ");

		// While (not done with expr)
		for (int i=0; i < tokens.length; i++) {
			// t = next token in expr
			String t = tokens[i];

			// if t is NOT an operator then
			if (!(operators.contains(t))) {
				ass_Stk.push(t);
			}
			else {
				String right = ass_Stk.pop();
				String left = ass_Stk.pop();
				ass_Stk.push(evaluate(left, t, right));
			}
		}
		// Top of stack has value
		return ass_Stk.peek();
	}


	// method that produces the assembly and temporary memory locations. outputs the assembly to the terminal
	public static String evaluate(String left, String operator, String right) {
		// temporary memory location
		String temp_memory = "TMP" + temp_memory_num ;
		String solution = "";

		// FileWriter fw = new FileWriter("assembly.txt");

		if (operator.equals("+")){
			try{    
			solution += "LD " + left + "\n";
			solution += "AD " + right + "\n";
			solution += "ST " + temp_memory;
			System.out.println(solution);
				// this.fw.write(solution);     
			}
			catch(Exception e){System.out.println(e);}    
		}
		else if (operator.equals("-")){
			try{    
			solution += "LD " + left + "\n";
			solution += "SB " + right + "\n";
			solution += "ST " + temp_memory;
			System.out.println(solution);
				// this.fw.write(solution);     
			}
			catch(Exception e){System.out.println(e);}    
		}
		else if (operator.equals("*")){
			try{    
			solution += "LD " + left + "\n";
			solution += "ML " + right + "\n";
			solution += "ST " + temp_memory;
			System.out.println(solution);
				// this.fw.write(solution);     
			}
			catch(Exception e){System.out.println(e);}    
		}
		else if (operator.equals("/")){
			try{    
			solution += "LD " + left + "\n";
			solution += "DV " + right + "\n";
			solution += "ST " + temp_memory;
			System.out.println(solution);
				// this.fw.write(solution);     
			}
			catch(Exception e){System.out.println(e);}    
		}
		// else{
		// 	System.out.print("Not a Valid Operation");
		// 	return null;
		// }
		temp_memory_num++;
		return temp_memory;
	}

	// will write results to a file
	public static void writeToFile(String filename, String newfile) {
		try {
			// read file
			FileReader reader = new FileReader(filename);
			BufferedReader buffered = new BufferedReader(reader);

			String expr = buffered.readLine();

			// file writing 
			FileWriter writer = new FileWriter(newfile);            

			while(expr!=null) {
				String infixToWrite = "Infix Expression : " + expr + "\n";
				String postToWrite = "Postfix Expression : " + Postfix.infixToPostfix(expr) + " ;" + "\n";
				String assemblyToWrite = "Assembly Expression : " + assemble(postToWrite);
				writer.write(infixToWrite + postToWrite + assemblyToWrite);
				expr = buffered.readLine();
			}
			buffered.close();
			writer.close();
		}
			
		// error catching
		catch(FileNotFoundException e) {
			System.out.println("Unable to open file " + filename);
		}

		catch(IOException ex) {
			System.out.println("Error reading file " + filename);
		}
	}

// // // main method
// public static void main(String args[]){
		
// 	// print results to a new textfile called results
// 	Filewriter fWriter = new Filewriter("results.txt");

// 	if (args.length > 0){

// 		// filewriting (using imports and methods together)
// 		Assembler assemb = new Assembler(fWriter);
// 		Path filename = Path.of((String)args[0]);
// 		String filePath = Files.readString(filename);
// 		assemb.assembleExpression(filePath);
// 		System.out.println("Results printed to: " + filename);
// 		fWriter.close();
		
// 	}

// 	else{
			
// 		System.out.println("Invalid infix expression.")
// 	}
	public static void main(String args[])throws IOException{
		//  Assembler as = new Assembler();
		String exp1 = "( ( AX + ( BY * C ) ) / ( D4 - E ) ) ;";
		String exp2 = "( ( A + ( B * C ) ) / ( D - E ) ) ;";
		System.out.println("infix: " + exp1);
		assemble(exp2);
		System.out.println("infix: " + exp2);
		assemble("Assembly : "  + "/n" + exp2);
		// System.out.println(sol);
		// System.out.println(sol1);

		// writeToFile("data3-1.txt", "diff_expr.txt");
	}
}