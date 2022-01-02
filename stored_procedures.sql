CREATE Procedure sp_AverageAgeOfDepartment
  @dno int
As
Begin
	Select d.Dno,avg(e.Age * 1.0) as AverageAge
	From EMPLOYEE e inner join DEPARTMENT d on e.Dno=d.Dno
	Group By d.Dno
	Having @dno = d.Dno

End



Create Procedure sp_CreateClothing
  @Name nvarchar(50),
  @PTax int,
  @Type nvarchar(25),
  @Gender char(1),
  @Size nvarchar(5),
  @Color nvarchar(25),
  @BPrice int,
  @SPrice int,
  @ShipmentId int

As
Begin
	Insert Into CLOTHING (Name,ProducerTaxNumber, Type, Gender, Size, Color, BoughtPrice, SoldPrice, ShipmentId)
	Values	(@Name, @PTax, @Type, @Gender, @Size, @Color, @BPrice, @SPrice, @ShipmentId)
	exec sp_UpdateTotalPrice
End




CREATE Procedure sp_CreateDepartment(
	@Dno int,
	@Name nvarchar(50)
)
As
Begin
	Insert Into DEPARTMENT
	Values (@Dno, @Name, NULL, 0)
End


CREATE Procedure sp_CreateEmployee
	@Ssn int,
	@FirstName nvarchar(50),
	@LastName nvarchar(50),
	@BirthDate smalldatetime,
	@Dno int,
	@Gender char(1),
	@Country nvarchar(25),
	@City nvarchar(25),
	@PostalCode nchar(5),
	@Salary int
As
Begin
	Insert Into EMPLOYEE Values
		(@Ssn,
		@FirstName,
		@LastName,
		@BirthDate,
		@Dno,
		@Gender,
		@Country,
		@City,
		@PostalCode,
		@Salary)	
	
End






Create Procedure sp_CreateIncomingShipment
  @InventoryCode int, @ProducerTaxNumber int, @LogisticsTaxNumber int
As
Begin
	Insert Into SHIPMENT (ShipmentDate, InventoryCode, ProducerTaxNumber, LogisticsTaxNumber) 
	Values (GETDATE(), @InventoryCode,@ProducerTaxNumber,@LogisticsTaxNumber)
End



CREATE Procedure sp_CreateOutgoingShipment
  @InventoryCode int, @ShopTaxNumber int, @LogisticsTaxNumber int
As
Begin
	Insert Into SHIPMENT (ShipmentDate, InventoryCode, ShopTaxNumber, LogisticsTaxNumber) 
	Values (GETDATE(), @InventoryCode,@ShopTaxNumber,@LogisticsTaxNumber)
End



CREATE Procedure sp_CreateProducer
	@TaxNumber int,
	@CompanyName nvarchar(50),
	@Country nvarchar(25),
	@City nvarchar(25),
	@PostalCode nchar(5),
	@BankAccountNumber nvarchar(50)
As
Begin
	Insert Into COMPANY Values (
		@TaxNumber,
		@CompanyName,
		@Country,
		@City,
		@PostalCode,
		@BankAccountNumber
	)

	Insert Into PRODUCER Values (@TaxNumber)
End







CREATE Procedure sp_CreateShop
	@TaxNumber int,
	@CompanyName nvarchar(50),
	@Country nvarchar(25),
	@City nvarchar(25),
	@PostalCode nchar(5),
	@BankAccountNumber nvarchar(50)
As
Begin
	Insert Into COMPANY Values (
		@TaxNumber,
		@CompanyName,
		@Country,
		@City,
		@PostalCode,
		@BankAccountNumber
	)

	Insert Into SHOP Values (@TaxNumber)
End



Create Procedure sp_DeleteEmployee
	@Ssn int
As
Begin
	Delete From EMPLOYEE
	Where Ssn=@Ssn
End


Create Procedure sp_DeleteProducer
	@TaxNumber int
As
Begin
	Delete From PRODUCER Where TaxNumber=@TaxNumber
	Delete From COMPANY Where TaxNumber=@TaxNumber
End




Create Procedure sp_DeleteShop
	@TaxNumber int
As
Begin
	Delete From SHOP Where TaxNumber=@TaxNumber
	Delete From COMPANY Where TaxNumber=@TaxNumber
End






Create Procedure sp_EmptyManager(
	@Dno int
)
As
Begin
	Update DEPARTMENT
	Set ManagerSsn=NULL
	Where Dno=@Dno
End




Create Procedure sp_SetManager(
	@Ssn int,
	@Dno int
)
As
Begin
	Update DEPARTMENT
	Set ManagerSsn=@Ssn
	Where Dno=@Dno
End


Create Procedure sp_UpdateTotalPrice
As
Begin
	Update s
	Set s.TotalPrice= new.TotalPrice
	From SHIPMENT s inner join (Select s.ShipmentID,sum(c.SoldPrice) as TotalPrice
		  From CLOTHING c inner join SHIPMENT s on c.ShipmentId=s.ShipmentID
		  Group By s.ShipmentID) new on s.ShipmentID=new.ShipmentID
End




