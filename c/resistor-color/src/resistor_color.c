#include "resistor_color.h"

int color_code(resistor_band_t color)
{
    return color;
}

resistor_band_t codes[] =
    {BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY, WHITE};

resistor_band_t *colors(void)
{
    return codes;
}