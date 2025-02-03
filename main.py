
from fastapi import FastAPI, HTTPException
from model import MessageRequest, MessageResponse
from db import get_collection
from db import collection
from llama import llama_manager
app = FastAPI()
collection = get_collection()

@app.post("/api/message", response_model=MessageResponse)
async def handle_message(request: MessageRequest):
    try:
        
        response = llama_manager.get_response(
            request.user_id,
            request.conversation_id,
            request.message
        )
        document = {
            "user_id": request.user_id,
            "conversation_id": request.conversation_id,
            "message": request.message,
            "response": response,
            
        }
        collection.insert_one(document)
        
        return MessageResponse(**document)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/messages/{user_id}", response_model=list[MessageResponse])
async def get_messages(user_id: str):
    try:
        messages = list(collection.find({"user_id": user_id}))
        for msg in messages:
            msg["_id"] = str(msg["_id"])  
        return messages
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)