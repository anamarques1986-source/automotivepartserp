CREATE TABLE [dbo].[DimProduct] (
    [ProductKey]     INT             NULL,
    [ProductCode]    VARCHAR (8000)  NULL,
    [ProductName]    VARCHAR (8000)  NULL,
    [Category]       VARCHAR (8000)  NULL,
    [Subcategory]    VARCHAR (8000)  NULL,
    [Brand]          VARCHAR (8000)  NULL,
    [VehicleSegment] VARCHAR (8000)  NULL,
    [UnitOfMeasure]  VARCHAR (8000)  NULL,
    [StandardCost]   DECIMAL (18, 2) NULL,
    [ListPrice]      DECIMAL (18, 2) NULL,
    [WeightKg]       DECIMAL (10, 3) NULL,
    [ActiveFlag]     BIT             NULL,
    [CreatedDate]    DATE            NULL
);


GO