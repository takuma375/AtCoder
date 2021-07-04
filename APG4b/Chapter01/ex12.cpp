#include <iostream>
using namespace std;

int main() {
    string S; cin >> S;
    int result = 1;

    for (int i=1; i<S.size(); i+=2) {
        if (S.at(i) == '+') {
            result += 1;
        } else if (S.at(i) == '-') {
            result -= 1;
        } else {
            cout << "error" << endl;
            break;
        }
    }
    cout << result << endl;
    
}