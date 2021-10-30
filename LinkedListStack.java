// Jackie, Philip
// CS321 Project 2

import java.util.Iterator;
import java.util.NoSuchElementException;


public class LinkedListStack <T> implements Iterable <T>{

    private int size;          // size of the stack
	private Node head;     // top of stack


    // helper linked list class
	private class Node {
		private T data;
		private Node next;
	}

   /**
	 * Initializes an empty stack.
	 */
	public LinkedListStack() {
		this.head = null;
		this.size = 0;
	}

	/**
	 * Returns true if this stack is empty.
	 *
	 * @return true if this stack is empty; false otherwise
	 */
	public boolean isEmpty() {
		return this.head==null;
	}

	/**
	 * Returns the number of items in this stack.
	 *
	 * @return the number of items in this stack
	 */
	public int size() {
		return this.size;
	}

	/**
	 * Adds the item to this stack.
	 *
	 * @param  item the item to add
	 */
	public void push(T val) {
		Node prev = this.head;
		this.head = new Node();
		this.head.data = val;
		this.head.next = prev;
		this.size++;
	}

	/**
	 * Removes and returns the item most recently added to this stack.
	 *
	 * @return the item most recently added
	 * @throws NoSuchElementException if this stack is empty
	 */
	public T pop() {
		if (this.isEmpty()) { 
			// throw NoSuchElementException("Stack is empty");
			return null;
		} 
		T data = this.head.data;
		head = head.next;
		this.size--;
		return data;
	}

     /**
	 * Returns (but does not remove) the item most recently added to this stack.
	 *
	 * @return the item most recently added to this stack
	 * @throws NoSuchElementException if this stack is empty
	 */

     public T peek() {
		if (this.isEmpty()) {
			// throw NoSuchElementException("Stack is empty");
			return null;
		}
		return this.head.data;
	}

	/**
	 * Returns a string representation of this stack.
	 *
	 * @return the sequence of items in this stack in LIFO order, separated by spaces
	 */
	public String toString() {
		StringBuilder s = new StringBuilder();
		for (T item : this) {
			s.append(item);
			s.append(' ');
		}
		return s.toString();
	}
	   

	/**
	 * Returns an iterator to this stack that iterates through the items in LIFO order.
	 *
	 * @return an iterator to this stack that iterates through the items in LIFO order
	 */
	public Iterator<T> iterator() {
		return new ListIterator();
		}

	/**
	 * an iterator. we did not implement remove() since we don't use it here
	 */
	private class ListIterator implements Iterator<T> {
		
		private Node current = head;
		
		public boolean hasNext() {
			return current != null;
		}

		public void remove() {
			throw new NoSuchElementException();
		}

		public T next() {
			if (!hasNext()) {
				// throw new NoSuchElementException();
				return null;
			}
			T curData = (T) current.data;
			current = current.next;
			return curData;
		}
	}

    // unit testing
    public static void main (String[] args){

        LinkedListStack<Integer> stack = new LinkedListStack<Integer>();

        stack.push(20);
        stack.push(33);
        stack.push(87);

        System.out.println("Head node is: " + stack.peek());

		stack.push(37);
		stack.push(99);
		stack.push(12);

		System.out.println("After push, size of the stack: " + stack.size());
		System.out.println("Top is now: " + stack.peek());
	   
		System.out.println("*** Testing pop ***");
		while (!stack.isEmpty()){
			System.out.println("popped: " + stack.pop());
		}
	   
		System.out.println("After popping, size of the stack: " + stack.size());
    }
}
