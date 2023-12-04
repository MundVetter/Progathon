#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<double> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }
    sort(numbers.rbegin(), numbers.rend()); // Reverse sort

    vector<vector<double> > tree(n + 1, vector<double>(n + 1, 0));
    vector<vector<int> > keys(n + 1);

    for (int i = 0; i <= n; ++i) {
        for (int j = -i - 1; j <= i + 1; j += 2) {
            keys[i].push_back(j);
        }
    }

    tree[0][0] = 1;

    double prob_best = 0;
    for (int i = 0; i < n; ++i) {
        int nn = i + 1;
        double prob = 0;
        for (int j = 0; j < nn; ++j) {
            double up = tree[i][j] * numbers[i];
            double down = tree[i][j] * (1 - numbers[i]);

            // cout << i << " " << j << " " << up << " " << down << endl;

            tree[i + 1][j + 1] += up;
            tree[i + 1][j] += down;

            if (keys[i][j + 1] >= m) {
                prob += up;
            }
            if (keys[i][j] >= m) {
                prob += down;
            }
        }

        if (prob > prob_best) {
            prob_best = prob;
        }
    }

    cout << prob_best << endl;

    return 0;
}
