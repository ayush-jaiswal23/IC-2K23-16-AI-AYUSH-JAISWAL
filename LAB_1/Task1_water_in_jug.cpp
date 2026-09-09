#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct State {
    int a;
    int b;
};

void waterJug(int capacityA, int capacityB, int target) {

    // To avoid cycle formation
    vector<vector<bool>> visited(
        capacityA + 1,
        vector<bool>(capacityB + 1, false)
    );

    // To reconstruct the path
    vector<vector<pair<int, int>>> parent(
        capacityA + 1,
        vector<pair<int, int>>(capacityB + 1, {-1, -1})
    );

    queue<State> q;

    // Initial state
    q.push({0, 0});
    visited[0][0] = true;

    State goal = {-1, -1};

    while (!q.empty()) {

        State current = q.front();
        q.pop();

        int a = current.a;
        int b = current.b;

        // Check whether target has been reached
        if (a == target || b == target) {
            goal = current;
            break;
        }

        vector<State> nextStates;

        // 1. Fill Jug A
        nextStates.push_back({capacityA, b});

        // 2. Fill Jug B
        nextStates.push_back({a, capacityB});

        // 3. Empty Jug A
        nextStates.push_back({0, b});

        // 4. Empty Jug B
        nextStates.push_back({a, 0});

        // 5. Pour A -> B
        int transferAB = min(a, capacityB - b);

        nextStates.push_back({
            a - transferAB,
            b + transferAB
        });

        // 6. Pour B -> A
        int transferBA = min(b, capacityA - a);

        nextStates.push_back({
            a + transferBA,
            b - transferBA
        });

        // Visit all new states
        for (State next : nextStates) {

            int na = next.a;
            int nb = next.b;

            if (!visited[na][nb]) {

                visited[na][nb] = true;

                parent[na][nb] = {a, b};

                q.push({na, nb});
            }
        }
    }

    // No solution
    if (goal.a == -1) {
        cout << "No solution exists.\n";
        return;
    }

    // Reconstruct path
    vector<State> path;

    State current = goal;

    while (!(current.a == 0 && current.b == 0)) {

        path.push_back(current);

        auto p = parent[current.a][current.b];

        current = {p.first, p.second};
    }

    path.push_back({0, 0});

    // Reverse because we reconstructed from goal -> start
    reverse(path.begin(), path.end());

    cout << "Solution:\n\n";

    for (int i = 0; i < path.size(); i++) {

        cout << "(" << path[i].a
             << ", " << path[i].b << ")";

        if (i < path.size() - 1)
            cout << " -> ";
    }

    cout << "\n\nMinimum operations: "
         << path.size() - 1 << endl;
}

int main() {

    int capacityA = 4;
    int capacityB = 3;
    int target = 2;

    waterJug(capacityA, capacityB, target);

    return 0;
}