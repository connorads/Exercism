using System;

public static class Gigasecond
{
    private const double OneGigasecond = 1e9;

    public static DateTime Add(DateTime moment) => moment.AddSeconds(OneGigasecond);
}