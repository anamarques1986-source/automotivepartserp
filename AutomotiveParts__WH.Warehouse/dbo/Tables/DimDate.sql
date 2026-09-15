CREATE TABLE [dbo].[DimDate] (
    [DateKey]         INT          NULL,
    [DateValue]       DATE         NULL,
    [Year]            INT          NULL,
    [QuarterNumber]   INT          NULL,
    [MonthNumber]     INT          NULL,
    [MonthName]       VARCHAR (20) NULL,
    [DayOfMonth]      INT          NULL,
    [DayOfWeekNumber] INT          NULL,
    [DayOfWeekName]   VARCHAR (20) NULL,
    [YearMonthKey]    INT          NULL
);


GO