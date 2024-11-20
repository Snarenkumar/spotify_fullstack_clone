# 🎵 Spotify Login Form Project  

Welcome to the **Spotify Login Form** project! This project showcases a login and registration system built with **Django** and connected to a **MySQL database**. It features responsive designs made with **HTML** and **CSS**, offering a smooth user experience.

> ⚠️ **Important Note**:  
> Due to some backend issues, such as database connectivity problems with the hosting platform, the hosted project may not load as expected. You can still run the project locally by following the instructions below.

---

## 🌟 Project Overview  

### Login Page (index.html)  
The first page of the project includes:  
- **Login Fields**:  
  - Email ID or Username  
  - Password  
- Upon successful login, user details are stored in the database, and you are redirected to the **Spotify main page**.  

### Spotify Main Page  
- Designed with **HTML and CSS**, this page emulates the look and feel of a Spotify dashboard.  

### Registration Page  
- The registration page allows users to create an account with:  
  - **Email verification**: Ensures the provided email is valid.  
  - **Password matching**: Confirms both password fields match before proceeding.  

> **Note**: Due to backend issues, the authentication system (email verification and password matching with database values) was not fully implemented.  

---

## 🚀 How to Run  

1. Clone the repository and navigate to the project directory.  
2. Set up and run the project using Django.  
3. Open the project in your browser by navigating to `http://127.0.0.1:8000/`.  

---

## 🎮 Usage Instructions  

### Login Page  
1. Enter your **Email ID or Username** and **Password**.  
2. On successful login, your details are stored in the database.  
3. You are redirected to the **Spotify main page**.  

### Registration Page  
1. Provide your details, including a valid **Email ID** and matching passwords.  
2. Currently, due to backend issues, the email and password verification features are non-functional.  

---

## 🛠️ Prerequisites  

Ensure you have the following installed:  
- **Python** (version 3.8 or higher)  
- **Django**  
- **MySQL**  

---

## 📦 How to Install  

### Step 1: Clone the Repository  
```bash
git clone <your-repository-url>
cd <repository-folder>
