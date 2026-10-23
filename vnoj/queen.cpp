#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> a, empty_rows, empty_cols;
vector<char> col, d1, d2;

bool dfs(int idx) {
    if (idx == empty_rows.size()) return true;
    int r = empty_rows[idx];
    for (int c : empty_cols) {
        if (col[c] || d1[r + c] || d2[r - c + n]) continue;
        col[c] = d1[r + c] = d2[r - c + n] = 1;
        a[r] = c;
        if (dfs(idx + 1)) return true;
        col[c] = d1[r + c] = d2[r - c + n] = 0;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (cin >> n) {
        a.assign(n + 1, 0);
        col.assign(n + 2, 0);
        d1.assign(2 * n + 3, 0);
        d2.assign(2 * n + 3, 0);
        empty_rows.clear();
        empty_cols.clear();

        for (int i = 1; i <= n; i++) {
            cin >> a[i];
            if (a[i] != 0) {
                col[a[i]] = 1;
                d1[i + a[i]] = 1;
                d2[i - a[i] + n] = 1;
            } else {
                empty_rows.push_back(i);
            }
        }

        for (int i = 1; i <= n; i++) {
            if (!col[i]) empty_cols.push_back(i);
        }

        dfs(0);

        for (int i = 1; i <= n; i++) {
            cout << a[i] << (i < n ? " " : "\n");
        }
    }
    return 0;
}