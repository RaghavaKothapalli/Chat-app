<h4>to run project<h4>
$env:DJANGO_SETTINGS_MODULE="core.settings"; daphne -b 127.0.0.1 -p 8000 core.asgi:application


<h2>stuff for next update <h2>
<p>
1. ✅ Message timestamps
🕒 Show when each message was sent
📌 Why: Adds realism & DB timestamp integration
📂 How: {{ msg.timestamp|date:'H:i' }} or add timestamp to JSON in consumer

2. ✅ Message delete (only for sender or admin)
🗑️ Add a “Delete” button next to your own messages (or all for admin)
📌 Why: Great showcase of permissions + frontend JS + backend API handling

3. ✅ Responsive mobile layout
📱 Adjust layout for small screens
📌 Why: Looks polished on any device

4. ✅ File upload (images, PDFs)
📎 Send & preview images or files
📌 Why: Adds real-world complexity (FormData, media upload, display)

5. ✅ Notifications (in-browser)
🔔 Toasts when someone sends a message
📌 Why: UX boost & working with JS APIs

6. ✅ Typing indicator
✍️ “Raghava is typing…”
📌 Why: Real-time communication nuance (good use of WebSocket broadcast)

7. ✅ Room creation (dynamic)
➕ Users can create/join any room
📌 Why: DB-backed rooms table, more interactive

8. ✅ User avatars / profile
🖼️ Show user profile pic or initials next to messages
📌 Why: Adds visual ID + upload logic

9. ✅ Rate limiting / spam protection
🚫 Prevent users from spamming messages
📌 Why: Shows awareness of abuse prevention<p>