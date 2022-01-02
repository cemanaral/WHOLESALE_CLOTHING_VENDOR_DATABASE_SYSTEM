Alter View ClothingInventory
As 
Select c.ClothingID, c.Name, i.InventoryCode
From CLOTHING c inner join SHIPMENT s on c.ShipmentId=s.ShipmentID
	 inner join INVENTORY i on s.InventoryCode=i.InventoryCode

GO



ALTER VIEW ClothingTypes
AS
SELECT c.Type,count(*) as Amount
FROM CLOTHING c
Group By c.Type



ALTER VIEW DepartmentsOfEmployees
AS
SELECT e.Ssn,e.FirstName + ' ' + e.LastName as FullName,e.Dno,d.Name
FROM EMPLOYEE e inner join DEPARTMENT d on e.Dno=d.Dno



ALTER VIEW IncomingShipments
AS
SELECT s.ShipmentID,s.ShipmentDate,s.InventoryCode,s.ProducerTaxNumber,s.LogisticsTaxNumber,s.TotalPrice
FROM SHIPMENT s
Where s.ShopTaxNumber is NULL



ALTER VIEW Managers
AS
SELECT e.Ssn,e.FirstName + ' ' + e.LastName as FullName, e.Dno,d.Name
FROM EMPLOYEE e inner join DEPARTMENT d on e.Ssn=d.ManagerSsn



ALTER VIEW NameOfContractedLogistics
AS
SELECT c.CompanyName, log.CompanyName as LogisticsName
FROM COMPANY c inner join CONTRACTED_LOGISTICS_COMPANY clc on c.TaxNumber=clc.CompanyTaxNumber
inner join
(select c2.TaxNumber, c2.CompanyName from COMPANY c2 inner join LOGISTICS l2 on c2.TaxNumber=l2.TaxNumber) log
	on log.TaxNumber=clc.LogisticsTaxNumber


ALTER VIEW OutgoingShipments
AS
SELECT s.ShipmentID,s.ShipmentDate,s.InventoryCode,s.ShopTaxNumber,s.LogisticsTaxNumber,s.TotalPrice
FROM SHIPMENT s
Where s.ProducerTaxNumber is NULL



ALTER VIEW ProfitOfClothes
AS
SELECT c.ClothingID,c.Name,c.Type,c.Color,c.Size,c.SoldPrice - c.BoughtPrice as Profit
FROM CLOTHING c



ALTER VIEW TopFiveEarnerEmployee
AS
SELECT Top 5 e.Ssn,e.FirstName + ' ' + e.LastName as FullName,e.Salary
FROM EMPLOYEE e
Order By e.Salary desc


