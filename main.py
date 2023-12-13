from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import task

# Define CORS settings
origins = [
    "http://localhost:3000",  # Add your React app's development server URL here
]

# Create the FastAPI app
app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict to specific HTTP methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # You can restrict to specific headers (e.g., ["Authorization"])
)

# Create database tables
Base.metadata.create_all(bind=engine)
#db_dependency = Annotated[Session, Depends(get_db)]


app.include_router(task.router)




