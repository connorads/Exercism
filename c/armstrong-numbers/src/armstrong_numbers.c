#include "armstrong_numbers.h"
#include <math.h>

#define INT_MAX_NUMBER_OF_DIGITS 10

typedef struct Digits
{
    int array[INT_MAX_NUMBER_OF_DIGITS];
    int count;
} Digits;

static Digits get_digits(int number)
{
    Digits digits;
    int i = 0;
    while (number > 0)
    {
        int digit = number % 10;
        digits.array[i] = digit;
        number /= 10;
        i++;
    }
    digits.count = i;
    return digits;
}

static int sum_of_digits_each_raised_to_the_power_of_the_number_of_digits(struct Digits digits)
{
    int sum = 0;
    for (int i = 0; i < digits.count; i++)
    {
        sum += pow(digits.array[i], digits.count);
    }
    return sum;
}

bool is_armstrong_number(int candidate)
{
    Digits digits = get_digits(candidate);

    int sum = sum_of_digits_each_raised_to_the_power_of_the_number_of_digits(digits);

    return sum == candidate;
}