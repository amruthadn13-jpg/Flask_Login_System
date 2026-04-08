
# Flask Login System (Mini Project)

## 📌 Project Overview

This project is a simple **Login System built using Flask**, where users can enter their credentials and receive a response based on validation.

It combines multiple backend concepts like routing, templates, forms, and conditional logic.

---

## 🚀 Features

* User login form (username & password)
* Secure data handling using POST method
* Backend validation logic
* Dynamic response displayed using templates

---

## 🛠️ Technologies Used

* Python
* Flask
* HTML (Jinja Templates)

---

## 📂 Project Structure

```
flask-login-mini-project/
│
├── app.py
└── templates/
    ├── login.html
    └── result.html
```

---

## ⚙️ How It Works

1. User opens the login page (`/`).
2. Enters username and password.
3. Form submits data using POST method.
4. Flask receives data using:

   ```
   request.form.get()
   ```
5. Backend checks credentials:

   * If username = `admin` and password = `1234`
     → Login Successful
   * Otherwise → Invalid Credentials
6. Result is displayed using a template.

---

## ▶️ How to Run the Project

1. Install Flask:

   ```
   pip install flask
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

---

## 🧠 Concepts Learned

* Flask routing
* HTML templates (`render_template`)
* GET vs POST methods
* request.form handling
* Conditional logic in backend
* Passing data from Flask to HTML

---

## 🔄 Example Flow

* Input:
  Username → admin
  Password → 1234

* Output:
  Login Successful ✅

---

## 🎯 Future Improvements

* Connect with database (SQLite)
* Add user registration system
* Implement password hashing
* Improve UI using CSS

---

## 👨‍💻 Author

Amrutha D N
