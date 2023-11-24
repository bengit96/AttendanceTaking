# AttendanceTaking

Simple Attendance Taking app quickly generated with chatgpt.

Scanning the QR code will bring users to a page to input their name.
After they input their name and submit, we will mark them as present.

We use websockets to update the attendance of users in the dashboard page in real-time.

This is a simple project for a recruitment event.

Refer to slides [here](https://docs.google.com/presentation/d/1u7YjUSHHL2uH6AP5SWW0gOJUZRc2rtRntjvD9MIJ1Co/edit#slide=id.p)for deploying onto pythonanywhere.

# Setup

1. Download dependencies

```
pip install flask flask_socketio qrcode
```

2. Run the server

```
python flask_app.py
```

# UI

<img width="701" alt="Screenshot 2023-11-24 at 4 18 42 PM" src="https://github.com/bengit96/AttendanceTaking/assets/47444881/013bb709-b797-4881-a4f0-13fadedab219">
