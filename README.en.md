<!-- Improved compatibility of Back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>



<!-- LANGUAGE SWITCHER -->
<div align="right">
  <strong>Language:</strong> <a href="README.en.md">English</a> | <a href="README.md">Русский</a>
</div>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">Conceptual News Django</h3>

  <p align="center">
    Simple Django application for publishing news
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Preview](4g.webp)

![Preview](3.webp)

Conceptual News Django is a simple web application built with Django for publishing and displaying news. The project demonstrates basic functionality of working with data models, views, and templates using the Django framework.

<details>
  <summary><strong>Project Goals and Objectives</strong></summary>

**Goals:**
* Create a simple and functional web application for publishing news
* Demonstrate basic Django framework capabilities
* Implement a news display system with author and publication date information
* Set up an admin panel for news management

**Key Objectives:**
* Develop a data model for storing news information
* Create a user interface for viewing news
* Set up an admin panel for data management
* Implement a basic template structure with inheritance
* Configure static files and styles

</details>

<details>
  <summary><strong>Results</strong></summary>

**Implemented Functionality:**
* Viewing news list (available to all users)
* Displaying complete news information: title, author, short description, text, and publication date
* Admin panel for news management
* Basic template with navigation and styling

**Created Components:**
* Django application `news` for working with news
* `News_post` model with fields: title, short description, text, publication date, and author
* HTML pages: news list with basic template
* Static files (CSS, images) for styling

</details>

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



### Built With

Main technologies and libraries used in the project:

* [![Django][Django-badge]][Django-url]
* [![Python][Python-badge]][Python-url]

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- GETTING STARTED -->
<details>
  <summary><strong>Getting Started</strong></summary>

Instructions for installing and running the project locally.

### Prerequisites

To work with the project, you need to install:

* Python 3.x
  ```sh
  # Check Python version
  python --version
  ```

### Installation

Below are instructions for installing and configuring the application.

1. Clone the repository
   ```sh
   git clone https://github.com/your_username/repo_name.git
   cd The-simplest-Django-case
   ```

2. Create a virtual environment (recommended)
   ```sh
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations
   ```sh
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server
   ```sh
   python manage.py runserver
   ```

7. Open in browser:
   - Main page: http://127.0.0.1:8000/news/
   - Admin panel: http://127.0.0.1:8000/admin/

</details>

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<details>
  <summary><strong>Usage</strong></summary>

The application provides the following pages and functionality:

### Main Pages:

1. **News List** (`/news/`)
   - Displays all news from the database
   - Available to all users without authorization
   - Shows title, author, short description, full text, and publication date for each news item
   - News sorted by publication date (newest first)

2. **Admin Panel** (`/admin/`)
   - Standard Django admin panel
   - Full access to news management
   - Filtering by publication date and author
   - Search by title, short description, text, and author
   - Date hierarchy for convenient navigation

### Features:

- Dark design with background image
- Responsive layout
- Convenient navigation between pages
- Informative display of publication dates

</details>

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

<details>
  <summary><strong>Show Completed Development Stages</strong></summary>

### Completed Stages:

- [x] **Stage 1: Basic Project Structure**
  - [x] Creating Django project `myproject`
  - [x] Creating `news` application
  - [x] Setting up basic URL structure and routing

- [x] **Stage 2: Data Model**
  - [x] Developing `News_post` model with fields: title, short description, text, publication date
  - [x] Creating and applying database migrations
  - [x] Adding `author` field to specify news author
  - [x] Setting up sorting by publication date (newest first)

- [x] **Stage 3: Basic Views and Templates**
  - [x] Implementing view for displaying news list
  - [x] Creating HTML templates for news list (`news.html`)
  - [x] Setting up basic template with navigation (`layout.html`)
  - [x] Implementing template inheritance

- [x] **Stage 4: Admin Panel**
  - [x] Setting up Django admin panel for News_post model
  - [x] Adding filters by publication date and author
  - [x] Implementing search by title, short description, text, and author
  - [x] Setting up date hierarchy for convenient navigation
  - [x] Configuring field display in news list

- [x] **Stage 5: Static Files and Styling**
  - [x] Configuring static files in settings.py
  - [x] Creating CSS file for page styling
  - [x] Implementing dark design with background image
  - [x] Styling news blocks and interface elements

- [x] **Stage 6: Localization**
  - [x] Setting up Russian language for models
  - [x] Translating model field names to Russian
  - [x] Russian names in admin panel

- [x] **Stage 7: URL Routing**
  - [x] Setting up root URL file with redirect to news
  - [x] Creating URL configuration for news application
  - [x] Setting up named URLs for navigation

</details>

### Planned Improvements:

- [ ] User authentication system
- [ ] Web interface form for adding/editing news
- [ ] Pagination for news list
- [ ] News detail page
- [ ] News categories
- [ ] News tags
- [ ] News search on page
- [ ] Comments on news
- [ ] Image upload for news
- [ ] RSS news feed
- [ ] API endpoints (REST API)
- [ ] Unit tests
- [ ] CI/CD pipeline
- [ ] Design and responsiveness improvements

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- CONTACT -->
## Contact

* [![GitHub][GitHub-badge]][GitHub-url]
* [![Gmail][Gmail-badge]][Gmail-url]
* [![Telegram][Telegram-badge]][Telegram-url]

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I express sincere gratitude to [Zerocoder](https://zerocoder.ru/) University and its entire team for creating an inspiring and professional educational environment. For preparing "IT-astronauts" at the Zerocoder "cosmodrome".

Special thanks to:

[Kirill Pshinnik](https://kpshinnik.ru/), the university director, for inspiring achievements;

Teachers [Nina Stefantsova](https://neural-courses.ru/teacher/nina-stefancova/), [Maxim Vershinin](https://neural-courses.ru/teacher/maksim-vershinin/), and [Darya Bobrovskaya](https://neural-courses.ru/teacher/darya-bobrovskaya/) — for deep knowledge, patience, and willingness to always help;

Nikita Murkin, course curator, for clear organization and mentoring;

Elizaveta, manager, for care, efficiency, and constant friendliness.

Thanks to you, this project became possible!

<p align="right">(<a href="#readme-top">Back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Django-badge]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[GitHub-badge]: https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white
[GitHub-url]: https://github.com/Z01coder
[Gmail-badge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[Gmail-url]: mailto:zolotuxin.alexey@gmail.com
[Telegram-badge]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[Telegram-url]: https://t.me/AZVXAN

