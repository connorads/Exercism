#include "armstrong_numbers.h"
#include <math.h>

bool is_armstrong_number(int candidate)
{
    int count = 0, n = candidate;
    while (n > 0)
    {
        n /= 10;
        ++count;
    }

    int sum = 0;
    n = candidate;
    while (n > 0)
    {
        sum += round(pow(n % 10, count));
        n /= 10;
    }

    return sum == candidate;
}
