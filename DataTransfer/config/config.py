

import os
from supabase import create_client, Client
from dotenv import load_dotenv

class DbContext:
    _client: Client = None
    
    @staticmethod
    def get_client() -> Client:
        
        load_dotenv("enviroment.env")
        url_env = os.getenv("SUPABASE_URL")
        key_env = os.getenv("SUPABASE_KEY")
                
        if DbContext._client is None:
            url = url_env
            key = key_env
            
            if not url or not key:
                raise ValueError("Las variables SUPABASE_URL y SUPABASE_KEY deben estar definidas en el entorno.")

            DbContext._client = create_client(url, key)
        
        return DbContext._client
       
       
    