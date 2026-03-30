# Knowledge QA Forum 📚

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Development-lightgrey.svg)](https://www.sqlite.org/)
[![Markdown](https://img.shields.io/badge/Markdown-Supported-brightgreen.svg)](https://www.markdownguide.org/)

A modern, full-stack Q&A community built with Django. This platform features a clean UI, Markdown support, and a robust search engine to help users share and discover knowledge efficiently.

一个基于 Django 构建的现代化全栈问答社区。该平台拥有简洁的用户界面、Markdown 支持以及强大的搜索引擎，帮助用户高效地分享和发现知识。

---

## 🌟 Key Features / 主要功能

* **Content Creation**: Full Markdown support for writing posts with automatic summary generation.
* **内容创作**：完全支持 Markdown 编写文章，并自动生成摘要。

* **Advanced Search**: Integrated search bar supporting keyword queries across titles and post content.
* **高级搜索**：集成搜索栏，支持按标题和文章内容进行关键词检索。

* **Dynamic Tagging**: Sidebar navigation with real-time post counts for each category.
* **动态标签**：侧边栏导航，实时显示每个分类下的文章数量。

* **User Interaction**: Systems for liking posts, favoriting content, and threaded comments.
* **用户互动**：支持点赞文章、收藏内容以及嵌套评论系统。

* **Personalized Profiles**: Enhanced user dashboards displaying activity stats, post history, and collections.
* **个性化主页**：增强的用户仪表板，展示活动统计、发文历史和收藏内容。

* **Account Security**: Secure registration, login, and a custom-styled password reset workflow.
* **账户安全**：安全的注册、登录以及自定义样式的密码重置流程。

---

## 🛠️ Tech Stack / 技术栈

| Category | Technologies |
|----------|---------------|
| **Backend** | Django 5.x, Python 3.10+ |
| **Frontend** | HTML5, CSS3 (Flexbox/Grid), JavaScript |
| **Database** | SQLite (Development) |
| **Styling** | Custom CSS with modern UX/UI principles |
| **Markdown** | Markdown support for rich text |

---

## 🚀 Getting Started / 快速开始

### Prerequisites / 环境要求

- **Python 3.10+** - [Download](https://www.python.org/downloads/)
- **pip** (Python package manager, comes with Python)
- **Git** (for cloning the repository)

---

### Installation / 安装步骤

#### 1. Clone the repository / 克隆项目

```bash
git clone https://github.com/YourUsername/KnowledgeQAForum.git
cd KnowledgeQAForum
```

> 💡 Replace `YourUsername` with your actual GitHub username.  
> 请将 `YourUsername` 替换为你实际的 GitHub 用户名。

---

#### 2. Set up a virtual environment / 创建虚拟环境

```bash
# Create virtual environment / 创建虚拟环境
python -m venv .venv

# Activate on Windows / Windows 激活
.venv\Scripts\activate

# Activate on macOS/Linux / macOS/Linux 激活
source .venv/bin/activate
```

> ✅ You should see `(.venv)` appear at the beginning of your terminal prompt.  
> 激活成功后，终端提示符前会出现 `(.venv)`。

---

#### 3. Install dependencies / 安装依赖包

```bash
pip install -r requirements.txt
```

> ⏳ This may take a minute. Wait for all packages to install successfully.  
> 这可能需要一分钟，请等待所有依赖包安装完成。

> **Note**: If `requirements.txt` doesn't exist, generate it with:
> ```bash
> pip freeze > requirements.txt
> ```

---

#### 4. Apply database migrations / 应用数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

> 📦 This creates the SQLite database file (`db.sqlite3`) in your project root.  
> 这将在项目根目录下创建 SQLite 数据库文件（`db.sqlite3`）。

---

#### 5. Create a superuser (admin account) / 创建超级管理员账户

```bash
python manage.py createsuperuser
```

You will be prompted to enter:
系统会提示你输入：

- **Username** (e.g., `admin`)
- **Email address** (optional, e.g., `admin@example.com`)
- **Password** (twice for confirmation)

---

#### 6. (Optional) Load sample data / 加载示例数据

If you have fixture files for testing:

```bash
python manage.py loaddata sample_data.json
```

> 💡 Skip this step if you want to start with an empty database.  
> 如果想从空数据库开始，可以跳过此步骤。

---

#### 7. Run the development server / 运行开发服务器

```bash
python manage.py runserver
```

You should see output similar to:
你会看到类似如下的输出：

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 5.x, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

#### 8. Access the application / 访问应用

Open your browser and visit:
打开浏览器并访问：

- **Forum homepage** / **论坛首页**: http://127.0.0.1:8000/
- **Admin panel** / **管理后台**: http://127.0.0.1:8000/admin/ (login with superuser credentials)

---

### Common Issues / 常见问题

| Issue / 问题 | Solution / 解决方案 |
|--------------|---------------------|
| `pip: command not found` | Install pip: `python -m ensurepip --upgrade` |
| `ModuleNotFoundError: No module named 'django'` | Activate virtual environment and run `pip install -r requirements.txt` again |
| Port 8000 already in use / 端口被占用 | Run `python manage.py runserver 8001` (use different port) |
| Migration errors / 迁移错误 | Delete `db.sqlite3` and `migrations/` folder (except `__init__.py`), then re-run migrations |

---

## 📁 Project Structure / 项目结构

```
KnowledgeQAForum/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── db.sqlite3            # SQLite database
├── core/                 # Project settings
│   ├── settings.py
│   └── urls.py
├── forum/                # Main application
│   ├── models.py         # Database models
│   ├── views.py          # Request handlers
│   ├── urls.py
│   └── templates/        # HTML templates
└── static/               # CSS, JS, images
```

---

## 🤝 Contributing / 贡献指南

Contributions are welcome! Please feel free to submit a Pull Request.

欢迎贡献！请随时提交 Pull Request。

---

## 📄 License / 许可证

This project is open source and available under the [MIT License](LICENSE).

本项目开源，基于 [MIT 许可证](LICENSE)。

---

## 📧 Contact / 联系方式

For questions or feedback, please open an issue on GitHub.

如有问题或反馈，请在 GitHub 上提交 Issue。

---
