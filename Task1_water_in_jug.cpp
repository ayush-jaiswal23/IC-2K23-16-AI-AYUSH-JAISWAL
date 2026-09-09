#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canMeasureWater(int x, int y, int target) {
        
        // Target cannot exceed total capacity
        if (target > x + y) {
            return false;
        }

        // If target is 0, it is already achieved
        if (target == 0) {
            return true;
        }

        // Target must be divisible by gcd(x, y)
        return target % gcd(x, y) == 0;
    }
};
