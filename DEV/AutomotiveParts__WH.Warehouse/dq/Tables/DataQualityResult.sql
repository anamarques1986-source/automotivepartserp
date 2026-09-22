CREATE TABLE [dq].[DataQualityResult] (
    [RunId]       VARCHAR (100) NULL,
    [SourceTable] VARCHAR (100) NULL,
    [RuleName]    VARCHAR (150) NULL,
    [Severity]    VARCHAR (20)  NULL,
    [RowsChecked] BIGINT        NULL,
    [FailedRows]  BIGINT        NULL,
    [Status]      VARCHAR (20)  NULL,
    [ExecutedAt]  DATETIME2 (6) NULL
);


GO