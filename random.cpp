#include <stdlib.h>

int** random_array(int n) {
    int** arr = new int*[n];
    for (int i = 0; i < n; i++) {
        arr[i] = new int[2];
        arr[i][0] = rand() % 10;
        arr[i][1] = rand() % 10;
    }
    return arr;
}



