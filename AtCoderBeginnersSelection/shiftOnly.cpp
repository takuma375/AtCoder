#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N; cin >> N;

    vector<int> vec(N);
    for (int i=0; i<N; i++) {
        cin >> vec.at(i);
    }
    int count = 0;
    bool flag = true;

    while (flag) {
        for (int i=0; i<vec.size(); i++) {
            cout << vec.at(i) << endl;
            if (vec.at(i) % 2 != 0) {
                flag = false;
            } else {
                
                vec.at(i) = vec.at(i) / 2;
            }
            cout << vec.at(i) << endl;
        }
    }
    

    cout << count/N << endl;
     
}