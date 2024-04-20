from fastapi import FastAPI

from app import all_router

app = FastAPI()

app.include_router(all_router)


@app.get("/")
async def read_root():
    return {"message": "可以开始使用啦，那么就表示你配置好了"}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=16699, reload=True)
