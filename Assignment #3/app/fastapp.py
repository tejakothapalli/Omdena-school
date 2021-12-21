#import modules
from app.area_in_acres import area
import uvicorn
from fastapi import FastAPI, Request

# instantiate fastapi object object
app = FastAPI()


@app.get("/")
async def get_input(request:Request):
    packet= await request.json()
    Length = packet['Length']
    width = packet['width']
    area_acres = area(Length,width)

    return {"Total area in acres" :area_acres}




# uvicorn fastapp:app --reload
