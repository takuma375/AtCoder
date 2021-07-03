#include <iostream>
using namespace std;

int main() {
  int p;
  cin >> p;

  int price, N;
  string text;

  // パターン1
  if (p == 1) {
    cin >> price;
    cin >> N;
  }

  // パターン2
  if (p == 2) {
    cin >> text >> price;
    cin >> N;
    cout << text << "!" << endl;
  }
  
  cout << price * N << endl;
}
