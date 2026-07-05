# Calorie Counter

## Project Description

Calorie Counter is a simple Django web application that allows users to track their daily calorie intake by adding food items, viewing their calorie values, deleting entries, and calculating the total calories consumed.

---

## Features

- Add food items
- View all food entries
- Delete food items
- Calculate total calories
- Reset the daily calorie count

---

## Project Structure

```text
calorie_counter/

├── calorieProject/
├── calorieApp/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── manage.py
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

```bash
git clone https://github.com/your-username/calorie_counter.git

cd calorie_counter

python -m venv myenv

myenv\Scripts\activate

pip install -r requirements.txt
```

---

## Database

This project uses **PostgreSQL**.

Run the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Technologies Used

- Python
- Django
- PostgreSQL
- HTML
- Git & GitHub

---

## Run the Project

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## Author

**Nathan Kiprono**

