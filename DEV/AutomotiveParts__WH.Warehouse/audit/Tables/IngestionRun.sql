CREATE TABLE [audit].[IngestionRun] (
    [RunId]         VARCHAR (100) NULL,
    [SourceSystem]  VARCHAR (100) NULL,
    [SourceTable]   VARCHAR (100) NULL,
    [WatermarkFrom] DATETIME2 (6) NULL,
    [WatermarkTo]   DATETIME2 (6) NULL,
    [RowsCopied]    BIGINT        NULL,
    [Status]        VARCHAR (20)  NULL,
    [CompletedAt]   DATETIME2 (6) NULL
);


GO