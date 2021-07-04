#include <iostream>
#include <vector>
using namespace std;

int main() {
    int P; cin >> P;

    vector<int> vec;
    vec = {1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800};

    int count = 0;
    int current = 0;
    int flag = 0;

    for (int i=9; i>=0; --i) {
        if (P < vec.at(i)) {
            continue;
        } else if (flag == 0){
            count = P / vec.at(i);
            current = P % vec.at(i);
            flag = 1;
            continue;
        } else {
            count += current / vec.at(i);
            current %= vec.at(i);
            continue;
        }
    }
    cout << count << endl;
    
}
