package Fibonacci;
public class Fibonacci {
    public static long fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
    
        long[] fib = new long[n+1];
        fib[0] = 0;
        fib[1] = 1;
    
        for (int i = 2; i <= n; i++) {
            fib[i] = fib[i-1] + fib[i-2];
        }
    
        return fib[n];
        // if ((n == 0) || (n == 1))
        //     return n;
        // else
        //     return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main (String[] args) {
        int n = Integer.valueOf(args[0]);
        long fib = fibonacci(n);
        System.out.println("The " + n + "th number in the Fibonacci sequeence is " + fib);
    }

}