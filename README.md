# Module3_mini_project
Advanced Routing and Middleware

## ❓ Why This Architecture?
In a basic API, code is often cluttered and difficult to scale. I chose this **Advanced Modular Pattern** for three reasons:
 * **Separation of Concerns:** By splitting logic into main.py, dependencies.py, and routers.py, the codebase remains readable. If the "User" logic needs an update, I don't have to risk breaking the "Post" logic.
 * **Performance Monitoring:** The inclusion of custom Middleware ensures that every request is timed. In a production environment, this is critical for identifying slow endpoints before they affect users.
 * **Security & DRY (Don't Repeat Yourself):** Using Dependency Injection for authentication means I only write the security logic *once*. I can then "inject" it into any route that needs protection, ensuring consistent security across the app.
## How To Use
To interact with this API and see the advanced features in action:
### 1. Installation
Ensure you have Python installed, then run:
```bash
pip install fastapi uvicorn

```
### 2. Run the Server
Launch the application using Uvicorn:
```bash
uvicorn main:app --reload

```
### 3. Testing the Protected Routes
 * **The Public Route:** Navigate to http://127.0.0.1:8000/users to see the public user list.
 * **The Protected Route:** To create a post, you must send a **POST** request to /blog/ (or / depending on your prefix).
 * **The Header:** You must include a custom header:
   * **Key:** x-token
   * **Value:** super-secret-token
 * **Observation:** If you miss the header, the API will return a 400 Bad Request. If you include it, the background task will trigger, and the post will be created!
### 4. Check Performance
Open your browser's **Network Tab** (F12) after a request. Look at the **Response Headers** to find X-Process-Time. This proves the Middleware is successfully calculating the server's response speed!

***SYSYTEM ARCHITECTURE***
To ensure scalability, I implemented the following patterns:
1. **Middleware**: A custom HTTP middleware monitors API performance by calculating request latency and injecting it into response headers.
2. **Dependency Injection**: Created a centralised verify_blog_access dependency to handle authentication logic, keeping route functions clean and focused on business logic.
3. **Background tasks(Asynchronous Provessing)**: To optimise User Experience (UX), I integrated BackgroundTasks. When a post is created, the API returns a success message immediately, while the "heavy" notification logic runs in the background, preventing server-side blocking 
