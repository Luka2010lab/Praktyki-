#include <iostream>
#include <string>

using namespace std;

int main( ) {
    //variables
    int number = 10;
    string text = "hello";
    bool bool_var = true;

    //casting
    int a = (int)3.7;
    string b = to_string(123);
    float c = stof("4.5");

    //operations
    int x = 5 + 3;
    int y = 5 - 1;
    int z = 5 / 4;
    int a = 5 * 2;
    double b = 5.5 / 2.1;
    int c = 18 % 9;

    //task
    string name = "Łukasz";
    cout << name << endl;


    //area and curcit of squet and rectangel

    int side1 = 7, side2 = 8;
    //area of squer 
    cout << "area of squer ; " << side1 * side1 << endl;
    //curcit of squer
    cout << "curcit of squer: " << side1 * 4 << endl;

    //area of ractangel
    cout << "area of ractangel : " << side1 * side2 <<endl;
    //curcit of ractangel
    cout << "curcit of ractangel : " << 2 * (side1 + side2) << endl;

    return 0;
}