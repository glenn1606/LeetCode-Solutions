#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> a, empty_rows, empty_cols;
vector<char> col, d1, d2;

bool dfs(int idx) {
    if (idx == empty_rows.size()) return true;
    int min_valid = n + 1;
    int best_row_idx = idx;

    for (int i = idx; i < empty_rows.size(); i++) {
        int r = empty_rows[i];
        int valid_count = 0;
        
        for (int c : empty_cols) {
            if (!col[c] && !d1[r + c] && !d2[r - c + n]) {
                valid_count++;
            }
        }
        if (valid_count < min_valid) {
            min_valid = valid_count;
            best_row_idx = i;
        }
        if (min_valid == 0) return false; 
    }
    swap(empty_rows[idx], empty_rows[best_row_idx]);
    int r = empty_rows[idx];
    
    for (int c : empty_cols) {
        if (col[c] || d1[r + c] || d2[r - c + n]) continue;
        col[c] = d1[r + c] = d2[r - c + n] = 1;
        a[r] = c;        
        if (dfs(idx + 1)) return true;
        col[c] = d1[r + c] = d2[r - c + n] = 0;
    }

    swap(empty_rows[idx], empty_rows[best_row_idx]);
    
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
