CREATE TABLE [ctl].[data_quality_log] (
    [RunId]       VARCHAR (100) NULL,
    [CheckTime]   DATETIME2 (6) NULL,
    [SourceTable] VARCHAR (100) NULL,
    [CheckName]   VARCHAR (150) NULL,
    [FailedRows]  BIGINT        NULL,
    [Status]      VARCHAR (20)  NULL,
    [Details]     VARCHAR (500) NULL
);


GO