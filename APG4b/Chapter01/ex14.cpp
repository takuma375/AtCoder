#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int A, B, C;
    cin >> A >> B >> C;

    int max_v, min_v;
    
    max_v = max(A, max(B, C));
    min_v = min(A, min(B, C));

    cout << max_v - min_v << endl;
}