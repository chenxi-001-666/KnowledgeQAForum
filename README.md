# Knowledge QA Forum 🚀

A modern, full-stack Q&A community built with Django. This platform features a clean UI, Markdown support, and a robust search engine to help users share and discover knowledge efficiently.

## 🌟 Key Features
* **Content Creation**: Full Markdown support for writing posts with automatic summary generation.
* **Advanced Search**: Integrated search bar supporting keyword queries across titles and post content.
* **Dynamic Tagging**: Sidebar navigation with real-time post counts for each category.
* **User Interaction**: Systems for liking posts, favoriting content, and threaded comments.
* **Personalized Profiles**: Enhanced user dashboards displaying activity stats, post history, and collections.
* **Account Security**: Secure registration, login, and a custom-styled password reset workflow.

## 🛠️ Tech Stack
* **Backend**: Django 5.x (Python)
* **Frontend**: HTML5, CSS3 (Flexbox/Grid), JavaScript
* **Database**: SQLite (Development)
* **Styling**: Custom CSS with a focus on modern UX/UI principles.

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* pip (Python package manager)

### Installation
1. **Clone the repository**
   ```bash
   git clone [https://github.com/YourUsername/KnowledgeQAForum.git](https://github.com/YourUsername/KnowledgeQAForum.git)
   cd KnowledgeQAForum
2. **Set up a virtual environment**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
4. **Apply migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
5. **Create a superuser**
    ```bash
    python manage.py createsuperuser
6. **Run the development server**
    ```bash
    python manage.py runserver