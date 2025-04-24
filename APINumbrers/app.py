from typing import Union

from fastapi import FastAPI
from service.calculateService import CalculateService


app = FastAPI()


@app.get("/extract-number/{number}")
def reat_item(number : int):
    service = CalculateService()
    return service.extract_number(number)


@app.get("/number-extracted")
def read_root():
    servie = CalculateService()
    return servie.calculate_number_extracted()

