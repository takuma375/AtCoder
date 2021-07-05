// ３つの整数を読み込み、それらを値が小さい順に並べて出力するプログラムを作成して下さい。
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int temp;
    if (a > b) {
        temp = a;
        a = b;
        b = temp;
    }
    if (b > c) {
        temp = b;
        b = c;
        c = temp;
    }
    if (a > b) {
        temp = a;
        a = b;
        b = temp;
    }

    cout << a << " " << b << " " << c << endl;
    return 0;
}