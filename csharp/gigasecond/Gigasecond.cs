using System;

public static class Gigasecond
{
    private const long OneGigasecondInTicks = 1000000000000L * TimeSpan.TicksPerMillisecond;

    public static DateTime Add(DateTime moment) =>
        new DateTime(moment.Ticks + OneGigasecondInTicks);
}