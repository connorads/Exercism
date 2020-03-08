using System;

public static class Gigasecond
{
    private const double OneGigasecondInMilliseconds = 1e12;

    public static DateTime Add(DateTime moment) => moment.AddMilliseconds(OneGigasecondInMilliseconds);
}