#include <iostream>
using namespace std;

int main() {
    int s;
    cin >> s;

    cout << (s / 100) + (s%100/10) + (s%100%10) << endl;
}