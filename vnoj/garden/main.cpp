#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long X, Y, Z;
    if (!(cin >> n >> X >> Y >> Z)) return 0;


    priority_queue<long long> P_pq;
    priority_queue<long long> Q_pq;

    long long total_cost = 0;

    for (int i = 1; i <= n; ++i) {
        long long a, b;
        cin >> a >> b;


        long long common = min(a, b);
        a -= common;
        b -= common;

        while (b > 0) {

            if (!P_pq.empty() && P_pq.top() - Z * i > 0) {
                long long v = P_pq.top();
                P_pq.pop();
                total_cost += X - (v - Z * i);
                Q_pq.push(3 * Z * i - v);
            } else {
                total_cost += X;
                Q_pq.push(X + Y + Z * i);
            }
            b--;
        }

        while (a > 0) {
            if (!Q_pq.empty() && Q_pq.top() - Z * i > 0) {
                long long v = Q_pq.top();
                Q_pq.pop();
                total_cost += Y - (v - Z * i);
                P_pq.push(3 * Z * i - v);
            } else {
                total_cost += Y;
                P_pq.push(X + Y + Z * i);
            }
            a--;
        }
    }

    cout << total_cost << "\n";

    return 0;
}
