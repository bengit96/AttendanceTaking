# app.py
from flask import Flask, render_template, redirect, url_for, request
import qrcode
from flask_socketio import SocketIO
from io import BytesIO

app = Flask(__name__)
socketio = SocketIO(app)

# Sample data structure to store attendance
attendance_data = {'Benjamin Loh': 'Present'}

@app.route('/')
def index():
    return render_template('index.html')

def generate_qrcode(url):
    # Generate a QR code for the student
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

@app.route('/dashboard')
def dashboard():
    img = generate_qrcode('/attendance')
    return render_template('dashboard.html', attendance_data=attendance_data)


@app.route('/attendance', methods=['GET','POST'])
def take_attendance():
    if request.method == 'POST':
        student_name = request.form.get('student_name')
        if student_name:
            attendance_data[student_name] = True
            socketio.emit('update_dashboard', {'student_name':student_name,'student_attendance': True})
            return redirect(url_for('dashboard'))
    else:
        return render_template('attendance.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
