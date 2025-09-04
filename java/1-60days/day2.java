import javax.jws.soap.SOAPBinding.Use;

public class day2 {
    public static void main(String[] args) {
        String[] tab = {"volwo","audi","mazda","jaguar"};
        int[] tabint = {1,2,3,4,5};
        System.out.println(tab[1]);
        System.out.println(tabint[0]);
        System.out.println(tab.length);
        //real_life exampel 
        //Creat a program that calculats the avg of fifrent ages
        int ages[] = {20,22,24,26,28,40,75,69,10};

        float avg, sum = 0;
        int length = 0;
        length = ages.length;
        for (int age : ages) {
            sum += age;
        }

        avg = sum / length;
        System.out.println("the avg of age is: " + avg);
        System.out.println("------------------");

        //Creat a program that that find lowest and hiest age in arrays
        float lowestage = ages[0];
        float highestage = ages[0];
        for (int age : ages) {
            if (lowestage > age) {
                lowestage = age;
            }
            if (highestage < age ) {
                highestage = age;
            }
        }
        System.out.println("the lowest age is: " + lowestage);
        System.out.println("------------------");
        System.out.println("the highest age is: " + highestage);
        System.out.println("------------------");

        //working on loops
        //to print all in ages tab and tabint we will use a for
        //this is for tab
        for (int i = 0; i < tab.length; i++) {
            System.out.println(tab[i]);
        }
        System.out.println("------------------");
        //this is for tabint
        for (int i = 0; i < tabint.length; i++) {
            System.out.println(tabint[i]);
        }
        //this is for tab
        System.out.println("------------------");
        for (int i = 0; i < ages.length; i++) {
            System.out.println(ages[i]);
        }
        //for each is the loop, which is used exclusively to loop through elements in an array
//      for ("the vareiabel : arreys name") {
//          the resto of the code
//        }
        //exampel
        for (String cars : tab) {
            System.out.println(cars);
        }
        //Multi-Dimensional Arrays
        int[][] array = {{1,2,3},{4,5,6}};
        //so this arrey will look like
        //      column 0      column 1   column 2
        //row 0     1           2           3
        //row 1     4           5           6
        System.out.println(array[1][2]);
        //chaneg a number in array
        array[1][2] = 7;
        System.out.println(array[1][2]);
        //lengt of rows
        System.out.println("rows " + array.length);
        System.out.println("cols in row1 " + array[0].length);
        System.out.println("cols in row1 " + array[1].length);
        //Loop Through a Multidimensional Array
        //Use a for loop inside another for loop to visit every element (row by row):
        for (int row = 0; row < array.length; row++) {
            for (int columns = 0; columns < array[row].length; columns++) {
                System.out.println("array ["+ row + "]["+ columns + "] = " + array[row][columns]);
            }
        }


    }

}
