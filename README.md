![Screenshot 2024-12-21 221943](https://github.com/user-attachments/assets/18df87bf-1326-4cd3-8d62-974fdfda93e0)

# 🖥️ CRM System

A powerful and customizable **Customer Relationship Management (CRM)** system built using Django. This project includes a variety of features to manage leads, agents, follow-ups, and more. 🚀

## 🌟 Features

- **Leads Management**: Create, update, delete, and assign leads.
- **Agents Management**: Manage agents with custom permissions.
- **Unassigned Leads**: View and assign unassigned leads.
- **Filters and Categories**: Sort and organize leads for better insights.
- **Follow-Up System**: Track updates and schedule follow-ups.
- **Dashboard**: Centralized view of all activities.
- **User Authentication**: Login, register, and reset password functionality.
- **Profile Page**: Manage your personal information.

## 📂 Project Structure

```plaintext
crm/
├── leads/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── leads_list.html
│   │   ├── lead_detail.html
├── agents/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── dashboard/
│   ├── views.py
│   ├── templates/
│       ├── dashboard.html
├── accounts/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       ├── login.html
│       ├── register.html
│       ├── reset_password.html



🚀 Installation

https://github.com/MDEV-2007/Django-CRM
cd repository

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt


python manage.py migrate
python manage.py runserver


Access the app in your browser at http://127.0.0.1:8000/.

🔧 Technologies Used
Backend: Django
Frontend: HTML, CSS, Bootstrap
Database: SQLite (default, replaceable with PostgreSQL or MySQL)
🤝 Contributions
Contributions are welcome! Feel free to fork this repo, create a feature branch, and submit a pull request. 😊
