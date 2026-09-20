CREATE TABLE [dbo].[DimWarehouse] (
    [WarehouseKey]  INT            NULL,
    [WarehouseCode] VARCHAR (8000) NULL,
    [WarehouseName] VARCHAR (8000) NULL,
    [CountryCode]   VARCHAR (8000) NULL,
    [City]          VARCHAR (8000) NULL,
    [CapacityUnits] INT            NULL,
    [ActiveFlag]    BIT            NULL
);


GO