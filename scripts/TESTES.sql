SELECT  
    @@SERVERNAME AS NomeServidor,
    SERVERPROPERTY('MachineName') AS NomeMaquina,
    SERVERPROPERTY('InstanceName') AS Instancia,
    SERVERPROPERTY('IsLocalDB') AS IsLocalDB

SELECT              
   NAME,
   CREATE_DATE,
   STATE_DESC
FROM sys.databases
ORDER BY NAME



