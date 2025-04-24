
from config.config import DbContext;
from pandas import DataFrame

class Repository:
  
        async def insert_table_charges(data):
            
            client = DbContext.get_client()
            table_name = "charges"
            
            try:
               
                client.table(table_name).insert(data).execute()
                
                print("query finished")
            except Exception as e:
                print(f"Error al crear la tabla: {e}")
                return None
        
        async def insert_table_companies(data):
            
            client = DbContext.get_client()
            table_name = "companies"
            
            try:
            
                client.table(table_name).insert(data).execute()
                
                print("query finished")
            except Exception as e:
                print(f"Error al crear la tabla: {e}")
                return None
         
        
        
        async def update_table_charges(data):
            
            client = DbContext.get_client()
            table_name = "charges"
            
            try:
               
                client.table(table_name).insert(data).execute()
                
                print("query finished")
            except Exception as e:
                print(f"Error al crear la tabla: {e}")
                return None
                    
        
        async def update_table_companies(data):
            
            client = DbContext.get_client()
            table_name = "companies"
            
            try:
            
                client.table(table_name).update(data).execute()
                
                print("query finished")
            except Exception as e:
                print(f"Error al crear la tabla: {e}")
                return None