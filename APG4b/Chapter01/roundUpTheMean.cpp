#include <iostream>
using namespace std;

int main() {
    int a, b, m;
    cin >> a >> b;
    
    m = (a+b)/2;

    cout << m + (a+b) - 2*m  << endl;
}