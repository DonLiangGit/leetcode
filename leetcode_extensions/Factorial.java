/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// Factorial
		int total = 152;
		int count = 1;
		int accumulation = 0;
		while(accumulation < total) {
			accumulation = accumulation + count;
			count ++;
		}
		System.out.print(count);
		System.out.print(accumulation);
	}
}