// ２つの整数 a, b を読み込んで、a と b の大小関係を出力するプログラムを作成して下さい。
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    if (a < b) {
        cout << "a < b" << endl;
    } else if (a > b) {
        cout << "a > b" << endl;
    } else {
        cout << "a == b" << endl;
    }
    return 0;
}