import time
from fastapi import FastAPI, Request
from routers import users, posts

app = FastAPI(title="Pro Blog API")

# 🛠 MIDDLEWARE: Logs how long each request takes
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"Request to {request.url.path} took {process_time}s")
    return response

# Include our modular routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
