public class Main {
    public static void main(String[] args) {
        // variables
        int number = 10;
        String text = "hello";
        boolean boolVar = true;

        // casting
        int a = (int) 3.7;
        String b = String.valueOf(123);
        float c = Float.parseFloat("4.5");

        // operations
        int sum = 5 + 2;
        int diff = 5 - 2;
        int mul = 5 * 2;
        int divInt = 5 / 2;
        double divDouble = 5.0 / 2.0;
        int mod = 5 % 2;

        // task: print name
        String name = "Łukasz";
        System.out.println(name);

        // area and circumference of square and rectangle
        int side1 = 6, side2 = 8;

        // square
        System.out.println("Area of square: " + (side1 * side1));
        System.out.println("Circumference of square: " + (side1 * 4));

        // rectangle
        System.out.println("Area of rectangle: " + (side1 * side2));
        System.out.println("Circumference of rectangle: " + 2 * (side1 + side2));
    }
}
