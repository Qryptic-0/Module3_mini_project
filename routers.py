from fastapi import APIRouter, Depends, BackgroundTasks
from dependencies import verify_token

router = APIRouter()

# Dummy database
posts_db = []

def send_notification(email: str, message: str):
    # This mimics a slow process like sending an email
    time.sleep(2) 
    print(f"Notification sent to {email}: {message}")

@router.post("/", dependencies=[Depends(verify_token)])
async def create_post(title: str, content: str, background_tasks: BackgroundTasks):
    new_post = {"title": title, "content": content}
    posts_db.append(new_post)
    
    # 🏃 BACKGROUND TASK: Don't make the user wait for the email
    background_tasks.add_task(send_notification, "admin@blog.com", f"New post: {title}")
    
    return {"message": "Post created!", "post": new_post}
  
