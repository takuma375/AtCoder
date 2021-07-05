// 長方形の中に円が含まれるかを判定するプログラムを作成してください。
// 次のように、長方形は左下の頂点を原点とし、右上の頂点の座標(W,H)が与えられます。
// また、円はその中心の座標(x,y)と半径rで与えられます。
#include <iostream>
using namespace std;

int main() {
    int W, H, x, y, r;
    cin >> W >> H >> x >> y >> r;
    if ((0 <= (x-r) && (x+r) <= W) && (0 <= (y-r) && (y+r) <= H)) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}