
start cmd /k "cd backend && uvicorn main:app --reload --port 8000"
start cmd /k "cd frontend && npm install && npm run dev"
start cmd /k "cd electron && npm start"
