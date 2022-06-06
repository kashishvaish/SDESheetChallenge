#include <bits/stdc++.h> 
vector<vector<long long int>> printPascal(int n) 
{
//  Time: O(n^2) Space: O(n^2)
    vector<vector<long long int>> pascal(n);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j <= i; j++) {
            pascal[i].push_back(1);
        }
    }
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < i; j++) {
            pascal[i+1][j+1] = pascal[i][j] + pascal[i][j+1];
        }
    }
    return pascal;
}


// Approach

// given n 

// initialize pascal as
// [1]
// [1][1]
// [1][1][1]

// for row -> (0, n-1)
//    for col -> (0, row)
//        pascal[row+1][col+1] = pascal[row][col] + pascal[row][col+1]

// Time: O(n^2)
// Space: O(n^2)
