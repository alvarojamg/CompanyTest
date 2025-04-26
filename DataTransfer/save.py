import pandas as pd
from repository.company_repository import Repository
import numpy as np
from datetime import datetime
import asyncio

try:
   #En este scrip se carga el scv a la base de datos, se ejecuta con el comando python save.py
    df = pd.read_csv("data/clean_data.csv")
    df.info()
    
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df = df.where(pd.notnull(df), None)
    
    now_date = datetime.now().isoformat()

    df['cdate'] = now_date
    df['udate'] = now_date

    df = df.rename(columns={"name": "company_name"})
    df = df.rename(columns={"id": "charges_id"})
    
    chage_columns = ['charges_id','amount','status','created_at', 'paid_at', 'cdate','udate']
    charge_data = df[chage_columns].to_dict('records')
    
    company_colums = ['company_id','company_name','cdate','udate','charges_id']
    company_data = df[company_colums].to_dict('records')
    
    
    async def save_companies():
        await Repository.insert_table_companies(company_data)
    
    async def save_charges():
        await Repository.insert_table_charges(charge_data)
    
    async def main():
        await asyncio.gather(save_charges(), save_companies())
        
    asyncio.run(main())
    
    print("finish query")
        
except ZeroDivisionError:
    print("error in data set")

