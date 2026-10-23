#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, k;
    cin >> n >> k;

    priority_queue<long long, vector<long long>, greater<long long>> pq; 
    long long ans = 0;

    for (long long i = 1; i <= n; i++) {
        long long p;
        cin >> p;
        long long q = p - k * i;         

        if (!pq.empty() && pq.top() < q) {
            ans += q - pq.top();          
            pq.pop();
            pq.push(q);                   
        }
        pq.push(q);                       
    }

    cout << ans << "\n";
    return 0;
}