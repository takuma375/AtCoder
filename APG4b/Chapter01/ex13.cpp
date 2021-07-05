#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, sum, average;
    cin >> N;

    vector<int> points(N);
    for (int i=0; i<N; i++) cin >> points.at(i);

    for (int i=0; i < points.size(); i++) sum += points.at(i);
    average = sum / N;

    for (int i=0; i < points.size(); i++) {
        if ((points.at(i) - average) >= 0 ){
            cout << points.at(i) - average << endl;
        } else {
            cout << (points.at(i) - average) * (-1) << endl;
        }
    }

    
}