DECLARE @GetInstances TABLE (Value nvarchar(100), InstanceNames nvarchar(100), Data nvarchar(100));
INSERT INTO @GetInstances
EXECUTE xp_regread
    @rootkey = 'HKEY_LOCAL_MACHINE',
    @key = 'SOFTWARE\Microsoft\Microsoft SQL Server',
    @value_name = 'InstalledInstances'
SELECT Value, InstanceNames, Data FROM @GetInstances

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


SELECT * FROM xp_regread
