// たて a cm よこ b cm の長方形の面積と周の長さを求めるプログラムを作成して下さい。
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    cout << a*b << " " << 2*(a+b) << endl;
    return 0;
}