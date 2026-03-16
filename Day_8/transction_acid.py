# ACID properties 

"""
ACID stands for atomicity , consistency , isolation , durability 

atomacity means either all or none 
    a transaction that executed in which  multiple operations are performing can be executed all until commit either if it 
    is failed means any operation inn that treansation is failed then it restart 
    you can say that the failed transaction cannot be resumed it will be restart ...

consistency means before the transaction starts or after the transactons completed the amount or you can say that the status
would be same 
        for exapmle ::
        money transfer from one account to another acccount through online mode 
        DB remains valid before and after transaction.

isocaltion 
        when multiple transactoins that running parallaly which means the multiple of the transactions are executing at the same time 
        and cpu will be switching for that tasks then the isolation property ensure that the transactions connot affect each other 

Durability 
        durability means once the changes or updates would be commited the then they would be permanently saved until 
        if system crashes 

        
"""

