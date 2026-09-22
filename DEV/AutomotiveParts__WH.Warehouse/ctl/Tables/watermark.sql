CREATE TABLE [ctl].[watermark] (
    [SourceSystem]    VARCHAR (100) NULL,
    [SourceTable]     VARCHAR (100) NULL,
    [WatermarkColumn] VARCHAR (100) NULL,
    [LastWatermark]   DATETIME2 (6) NULL,
    [LastRunStatus]   VARCHAR (20)  NULL,
    [LastRunAt]       DATETIME2 (6) NULL
);


GO