ALTER TRIGGER tg_IncrementNoOfWorkers
	on EMPLOYEE
AFTER INSERT 
As
Begin
	Update DEPARTMENT
	Set NoOfWorkers=NoOfWorkers + 1
	Where Dno=(Select Dno From Inserted)
End





ALTER TRIGGER tg_DecrementNoOfWorkers
	on EMPLOYEE
AFTER DELETE 
As
Begin
	Update DEPARTMENT
	Set NoOfWorkers=NoOfWorkers - 1
	Where Dno=(Select Dno From Deleted)
End