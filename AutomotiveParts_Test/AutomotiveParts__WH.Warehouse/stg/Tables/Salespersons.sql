CREATE TABLE [stg].[Salespersons] (
    [SalespersonId]   INT            NULL,
    [SalespersonCode] VARCHAR (8000) NULL,
    [SalespersonName] VARCHAR (8000) NULL,
    [Region]          VARCHAR (8000) NULL,
    [ActiveFlag]      BIT            NULL,
    [SilverLoadedAt]  DATETIME2 (6)  NULL
);


GO