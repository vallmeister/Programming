#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPowerOfTwo(int n){
    while (n > 0)
    {
        int tmp = n & 1;
        n >>= 1;
        if (tmp == 1 && n > 0) return false;
        else if (tmp == 1 && n == 0) return true;
    }
    return false;
    
}

int main() {
    int input;
    scanf("%d", &input);
    printf("%d\n", isPowerOfTwo(input));
}
