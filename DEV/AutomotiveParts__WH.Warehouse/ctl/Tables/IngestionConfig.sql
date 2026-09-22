CREATE TABLE [ctl].[IngestionConfig] (
    [SourceSystem]    VARCHAR (100) NULL,
    [SourceSchema]    VARCHAR (50)  NULL,
    [SourceTable]     VARCHAR (100) NULL,
    [TargetSchema]    VARCHAR (50)  NULL,
    [TargetTable]     VARCHAR (100) NULL,
    [WatermarkColumn] VARCHAR (100) NULL,
    [KeyColumn]       VARCHAR (100) NULL,
    [IsActive]        BIT           NULL
);


GO