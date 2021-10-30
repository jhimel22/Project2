// CS321 Project 2: Assembler Class
// Written by Jackie and Philip


import java.io.FileWriter;
import java.nio.file.Path;

// class to convert postfix expression into assembly
public class Assembler{

	private String[] expr;
	private Postfix postfix;
	private FileWriter fWriter;
	private String f_name;
	private int holder_val;
	private LinkedListStack<String> stack; 


	// initializing method to write results into file
	public Assembler(Filewriter fWriter) {

		this.postfix = new Postfix();
		this.stack = new LinkedListStack<String>();
		this.holder_val = 1;
		this.fWriter = fWriter;
	}

	// for each character (ch) in postfix expression 
	//, if ch is operand then push ch
	// else, pop top of stack 

	// method to split up infix and evaluate for operands
	public String postToAssembly (String infix){

		String [] splitter = infix.split("?<=;");
		String results = "";

		// splitting up infix expression for evaluation
		for(int i=0; i < splitter.length; i++) {

			String operators = "+-*/";
			this.fWriter.write(splitter[i] + "\n--------------\n");
			this.holder_val = 1;
			String str = this.postfix.infixToPostfix(splitter[i]);
			this.fWriter.write(str + "\n-------------\n");
			this.expr = str.split(" ");
			String right;
			String left;
			String operand;

			// getting operands in expression, pop top of stack both left and right
		for (int j=0; j<expr.length(); j++){

			if(operators.contains(expr[j])){

				right = (String)this.stack.pop();
				left = (String)this.stack.pop();
				operand = this.evaluate(left, right, expr[j]);
				stack.push(operand);
			}

			else {
				//this.stack.push(this.expr[j]);
				this.stack.push(splitter[i]);
			}
		}
		results+=(String)this.stack.pop() + "\n------------\n";
	}
	return results;
}

	// method to evaluate infix and produce assemb. and temp memory locations
	private String evaluate(String left, String right, String operator){

		String holder = "Holder obj: " + this.holder_val;

		String result = "";

		// assembly code component
		if (operator == '+'){

			result += "LD" + left + "\n";
			result += "AD" + right + "\n";
			result += "ST" + holder + "\n";
			this.fWriter(evaluated);

		}

		else if(operator == '-'){
			
			result += "LD" + left + "\n";
			result += "SB" + right + "\n";
			result += "ST" + holder + "\n";
			this.fWriter(evaluated);
			
		}

		else if(operator == '*'){

			result += "LD" + left + "\n";
			result += "ML" + right + "\n";
			result += "ST" + holder + "\n";
			this.fWriter(evaluated);
		}

		else if (operator == '/'){

			result += "LD" + left + "\n";
			result += "DV" + right + "\n";
			result += "ST" + holder + "\n";
		}

		else{
			return null;
			System.out.println("Invalid Entry! Please try again.");
		}
		this.holder_val++;
	}
	
	return holder;
}


// main method
public static void main(String args[]){
		
	// print results to a new textfile called results
	Filewriter fWriter = new Filewriter("results.txt");

	if (args.length > 0){

		// filewriting (using imports and methods together)
		Assembler assemb = new Assembler(fWriter);
		Path filename = Path.of((String)args[0]);
		String filePath = Files.readString(filename);
		assemb.assembleExpression(filePath);
		System.out.println("Results printed to: " + filename);
		fWriter.close();
		
	}

	else{
			
		System.out.println("Invalid infix expression.")
	}
}