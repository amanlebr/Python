------------------------------Data file size---------------------------- 
if exists (select * from tempdb.sys.all_objects where name like '%#dbsize%') 
drop table tempdb..#dbsize 
create table #dbsize 
(Dbname sysname,dbstatus varchar(50)
,Recovery_Model varchar(40) default ('NA')
, file_Size_MB decimal(30,2)default (0)
,Space_Used_MB decimal(30,2)default (0),Free_Space_MB decimal(30,2) default (0)) 
go 
  
insert into #dbsize(Dbname,dbstatus,Recovery_Model,file_Size_MB,Space_Used_MB,Free_Space_MB) 
exec  dbo.sp_MSforeachdb
'use [?]; 
  select DB_NAME() AS DbName, 
    CONVERT(varchar(20),DatabasePropertyEx(''?'',''Status'')) ,  
    CONVERT(varchar(20),DatabasePropertyEx(''?'',''Recovery'')),  
sum(size)/128.0 AS File_Size_MB, 
sum(CAST(FILEPROPERTY(name, ''SpaceUsed'') AS INT))/128.0 as Space_Used_MB, 
SUM( size)/128.0 - sum(CAST(FILEPROPERTY(name,''SpaceUsed'') AS INT))/128.0 AS Free_Space_MB  
from sys.database_files  where type=0 group by type' 
 
go 
  
