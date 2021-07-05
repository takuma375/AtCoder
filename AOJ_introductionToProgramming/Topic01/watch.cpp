// 秒単位の時間 Sが与えられるので、h:m:sの形式へ変換して出力してください。ここで、hは時間、mは60未満の分、sは60未満の秒とします。
#include <iostream>
using namespace std;

int main() {
    int S, h, m, s;
    cin >> S;

    h = S/3600;
    m = S%3600/60;
    s = S%3600%60;

    cout << h << ":" <<  m << ":" << s << endl;
    return 0;
}