# 📚 Smart Study Manager

**Smart Study Manager** is a student-focused academic management web application built with **Python and Flask**. It helps students organize their academic activities, track study time, monitor attendance, manage assignments, analyze progress, and generate academic reports from one place.

---

## 🚀 Features

- 🔐 **User Authentication**
  - User registration
  - Secure login
  - Logout functionality
  - Password hashing

- 📚 **Subject Management**
  - Add subjects
  - Store subject codes and teacher information
  - Edit and delete subjects

- 📝 **Task & Assignment Management**
  - Add assignments and tasks
  - Set deadlines
  - Set task priorities
  - Track task status

- ⏱️ **Study Session Tracking**
  - Record study sessions
  - Select subjects
  - Track study duration
  - Add study notes
  - View study history

- 📊 **Attendance Management**
  - Record attendance
  - Calculate attendance percentage
  - Monitor attendance performance
  - Identify attendance below the required level

- 📈 **Analytics Dashboard**
  - View academic statistics
  - Track study hours
  - Analyze attendance
  - Visualize academic progress

- 📄 **Academic Reports**
  - Generate semester reports
  - View student information
  - View subject statistics
  - View attendance and study data
  - Export academic information

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| SQLite | Database |
| HTML5 | Web page structure |
| CSS3 | Website styling |
| JavaScript | Frontend functionality |
| Chart.js | Data visualization |
| Gunicorn | Production server |
| Git & GitHub | Version control |

---

## 📂 Project Structure

```text
SmartStudyManager-Web/
│
├── app.py
├── database.py
├── utils.py
├── requirements.txt
├── Procfile
├── .gitignore
├── README.md
│
├── database/
│   └── study_manager.db
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── subjects.html
│   ├── tasks.html
│   ├── study_sessions.html
│   ├── attendance.html
│   ├── analytics.html
│   └── reports.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd SmartStudyManager-Web
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

---

### 3. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

After activation, you should see:

```text
(venv)
```

in your terminal.

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask development server:

```bash
python app.py
```

The application will normally be available at:

```text
http://127.0.0.1:5000
```

Open the address in your web browser.

---

## 🗄️ Database

Smart Study Manager uses **SQLite** for storing application data.

The database is located at:

```text
database/study_manager.db
```

The application manages data related to:

- Users
- Subjects
- Tasks
- Study Sessions
- Attendance

---

## 📊 Attendance Calculation

Attendance percentage is calculated using:

```text
Attendance % = (Attended Classes / Total Classes) × 100
```

For example:

```text
Attended = 17
Total = 20

Attendance = (17 / 20) × 100
           = 85%
```

The application can highlight attendance that falls below the required level.

---

## 🔐 Security

The application includes basic security practices such as:

- Password hashing
- User authentication
- Session-based login
- User-specific academic records
- SQLite foreign-key relationships

> For production deployment, additional security configuration such as secure secret keys, HTTPS, CSRF protection, and production database configuration should be added.

---

## 🌐 Deployment

The application can be deployed using platforms such as **Render** or other Python-compatible hosting services.

For production deployment, Gunicorn can be used:

```bash
gunicorn app:app
```

The `Procfile` contains:

```text
web: gunicorn app:app
```

---

## 🎯 Project Objective

The main objective of Smart Study Manager is to provide students with a single platform to manage their academic activities efficiently.

Instead of using separate applications or notebooks for subjects, assignments, study schedules, attendance, and academic progress, students can manage everything from one centralized system.

---

## 💡 Future Improvements

Possible future improvements include:

- 📱 Responsive mobile design
- ☁️ Cloud database integration
- 🔔 Assignment deadline notifications
- 📧 Email reminders
- 📅 Study timetable generator
- 🤖 AI-powered study recommendations
- 👨‍🏫 Teacher/admin dashboard
- 📊 Advanced academic analytics
- 🔑 Password reset functionality
- 🌙 Dark mode
- 📱 Progressive Web App support

---

## 🧑‍💻 Project Development

This project was developed as an academic/learning project to demonstrate concepts including:

- Python programming
- Flask web development
- Database management
- CRUD operations
- User authentication
- Web development
- Data visualization
- Software project structure
- Git and GitHub

---

## 📜 License

This project is intended for educational and learning purposes.

You may modify and improve the project according to your requirements.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### Made with ❤️ using Python & Flask
