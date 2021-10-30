// CS321 Project 2
// Written by Jackie and Phillip

// reads a set of infix expressions from a file 
// then writes infix and postfix expressions into another file

import java.io.FileWriter;
import java.nio.file.Path;
import java.io.FileReader;
import java.io.BufferedReader;
import java.util.Scanner;
import java.io.File;

public class Postfix{

	private FileWriter fWriter;
	private String f_name;
	//private String input;
	//private String [] input;

	public Postfix(FileWriter fWriter){
		
		this.fWriter = fWriter;
		//this.input = input;
	}

	

	// method to ensure acceptable operands are being used
	static boolean correctChar (char ch){

		if(ch == '+' || ch == '-' || ch == '/' || ch == '*' || ch == '^'){

			return true;
		}

		// otherwise return error/false
		System.out.println("Invalid input. Please try again");
		return false;
	}

	// method to give value to each operand in terms of priority (postfix priority)
	static int higherValOperator(char ch){

		switch(ch){

			// cases: higher val = higher precedence
			case '^':
				return 3;
			
			case '*':
			case'/':
				return 2;

			case '-':
			case'+':
				return 1; 
		}
		return -1;
	}

	public String infixToPostfix(String f_name) {
		LinkedListStack<String> stk = new LinkedListStack<String>();
		File file = new File(f_name);
		Scanner sc = new Scanner(file);
		sc.useDelimiter(" ");

		String token = sc.next();

		while (!token.equals(";")) {

			if (token.equals(")")){
				String right = stk.pop();
				String oper = stk.pop();
				String left = stk.pop();
				stk.push(left + " " + right + " " + oper);
			}
			else {
				if (token.equals("(") ){
					stk.push(token);
				}
			}
			token = sc.next();
		}
		sc.close();
		String post_expr = stk.head;
		return post_expr;
	}

	
	public static void main(String[] args){

		Filewriter fWriter = new Filewriter("postfix.txt");

		Postfix pf = new Postfix(fWriter);
		Path filename =  Path.of((String)args[0]);
		String filePath = Files.readString(filename);
		pf.infixToPostfix(filePath);
		System.out.println("Results printed to: " + filename);

		// example expression
		//String input = "123*7*+1/5-";

		// returning postfix conversion in terminal
		//System.out.println("Postfix: ");
		//System.out.println(infixToPostfix(input));
	}
}



/* 

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.FileWriter;

public class Postfix {

		public static String infixToPostfix(String expr) {
		// create llStack
		LinkedListStack<String> postStack = new LinkedListStack<String>();
		String [] tokens = expr.split(" ");
		
		for (int i=0; i < tokens.length-1; i++) {	

			// while (!(tokens[i].equals(";"))) {

				if (tokens[i].equals(")")) {
					String right = postStack.pop();
					String oper = postStack.pop();
					String left = postStack.pop();
					postStack.push(left + " " + right + " " + oper);
				}
				else {
					if (!(tokens[i].equals("("))) {
						postStack.push(tokens[i]);
					}
				}
			// }
		}

		// Top of stack is a postfix expression
		return postStack.peek();
		
	}


	public static void writeToFile(String filename, String newfile) {
		try {
			// read file
			FileReader reader = new FileReader(filename);
			BufferedReader buffered = new BufferedReader(reader);

			String expr = buffered.readLine();

			// file writing 
			FileWriter writer = new FileWriter(newfile);            

			while(expr!=null) {
				String toWrite = infixToPostfix(expr) + " ;" + "\n";
				// writer.write(infixToPostfix(expr));
				// writer.write(infixToPostfix(expr + " ;" + "\n"));
				writer.write(toWrite);
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

	public static void main(String[] args){
		String input = "( AX + ( B * C ) ) ;";
		String infix = "( ( H * ( ( ( ( A + ( ( B + C ) * D ) ) * F ) * G ) * E ) ) + J ) ;";
		String ex = "( ( A + ( B * C ) ) / ( D - E ) ) ;";
		String ex1 = "( ( AX + ( BY * C ) ) / ( D4 - E ) ) ;";
		System.out.println(infixToPostfix(input));
		System.out.println(infixToPostfix(infix));
		System.out.println(infixToPostfix(ex));
		System.out.println(infixToPostfix(ex1));


		writeToFile("data3-1.txt", "postfix-file.txt");
	}

}
*/
