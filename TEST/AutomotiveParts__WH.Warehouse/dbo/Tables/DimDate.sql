CREATE TABLE [dbo].[DimDate] (
    [DateKey]         INT          NULL,
    [DateValue]       DATE         NULL,
    [Year]            INT          NULL,
    [QuarterNumber]   INT          NULL,
    [MonthNumber]     INT          NULL,
    [MonthName]       VARCHAR (3)  NULL,
    [DayOfMonth]      INT          NULL,
    [YearMonthKey]    INT          NULL,
    [YearMonth]       VARCHAR (10) NULL,
    [DayOfWeekNumber] INT          NULL,
    [DayOfWeekName]   VARCHAR (20) NULL
);


GO