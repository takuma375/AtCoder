#include <iostream>
using namespace std;

int main() {
    string str; cin >> str;
    int count = 0;

    for (int i=0; i<str.size(); i++) {
        if (str.at(i) == '1') count++;
    }

    cout << count << endl;

    return 0;
}