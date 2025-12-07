from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import initdb
from src.auth.routes import auth_router

version = 'v1'

@asynccontextmanager
async def life_span(app: FastAPI):
    print('Server is starting...')
    await initdb()
    yield
    print('Server is stoppping...')


app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version= version,
    lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=['auth'])



## the lifespan event
# @asynccontextmanager
# async def lifespan(app: FastAPI):    
#     print("Server is starting...")
#     yield
#     print("server is stopping")



# app = FastAPI(
#     lifespan=lifespan # add the lifespan event to our application
# )

# app.include_router(
#     book_router,
#     prefix="/books",
#     tags=['books']
# )