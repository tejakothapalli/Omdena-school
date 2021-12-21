#import modules
from area_in_acres import area
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


if __name__ == '__main__':
    uvicorn.run()

# uvicorn fastapp:app --reload