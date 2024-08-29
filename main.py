from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import FileResponse
from openpyxl import Workbook

app = FastAPI()


async def create_excel() -> str:
    wb = Workbook()
    ws = wb.active
    ws["A1"] = "Hello World"
    file_path = "hello_world.xlsx"
    wb.save(file_path)
    return file_path


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/excel")
async def get_excel():
    file_path = await create_excel()
    return FileResponse(
        file_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

@app.post("/receive_entity")
async def receive_entity(entity: dict):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"entity_{date}.txt", "w") as f:
        f.write(str(entity))
