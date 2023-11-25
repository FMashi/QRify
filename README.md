# QRify

QRify is a Django-based web application for generating QR codes from URLs and text content. With QRify, you can easily create and manage QR codes for different purposes, such as sharing links or text information and more.

![QRify Logo](/assets/img/QRify.png)

### Dynamically Generate QR Code Images

QRify empowers users to dynamically generate QR code images for various content types, ensuring a seamless experience in the creation and management of QR codes.

### API Endpoint

QRify's API opens up possibilities for programmatically generating QR code images. Access the API at the following endpoint:
http://localhost:8000/api/

## Features

**1. URL QR Code:**
Generate QR codes for URLs, making it convenient to share links effortlessly.

**2. Text QR Code:**
Create QR codes for text content, enabling users to encode textual information in a QR code.

**3. Phone QR Code:**
Generate QR codes for phone numbers, facilitating easy contact or dialing.

**4. vCard QR Code:**
Create QR codes containing vCard information, streamlining contact sharing.

**5. Email QR Code:**
Generate QR codes for email addresses, making it quick to share contact information.

**6. SMS QR Code:**
Create QR codes for sending SMS messages with pre-filled content.

**7. Wi-Fi QR Code:**
Generate QR codes for Wi-Fi credentials, simplifying the process of connecting to a network.

**8. Social Media QR Code:**
Create QR codes linking to social media profiles, making it easy for others to connect on various platforms.

**9. Post QR Code:**
Generate QR codes for posts, allowing users to share specific content easily.

**10. PDF QR Code:**
Create QR codes for PDF files, enabling quick access to documents.

**11. MP3 QR Code:**
Generate QR codes for MP3 files, facilitating easy sharing of audio content.

**12. App QR Code:**
Create QR codes for applications, providing a convenient way to share or download apps.

Organize QR Codes Efficiently

QRify assists in organizing QR codes into folders based on creation date and content type. This feature enhances the management of QR codes, making it easier to locate and track specific codes.

## Getting Started 🚀

To get started with the QRify Application, follow these steps:

#### Prerequisites

**1. 🐍 Python**: Ensure you have Python installed. You can download Python from the [official Python website](https://www.python.org/downloads/).

**2. 🗂️ Install virtualenv**:
If you don't already have [virtualenv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) installed, you can install it using pip, which is Python's package manager. Open your terminal or command prompt and run:

```shell
pip install virtualenv
```

If you are using Python 3, you can use pip3 instead of pip.

#### 📦 installation

**Clone the Repository:** Clone the project repository to your local machine:

```shell
git clone https://github.com/FMashi/QRify.git
```

**♻️ Activate the Virtual Environment:**

Depending on your operating system, the command to activate the virtual environment will vary:

##### Windows:

```shell
venv\Scripts\activate
```

##### macOS and Linux:

```shell
source venv/bin/activate
```

**🛠️ Install Dependencies:** Install the required Python packages and dependencies listed in the **requirements.txt** file:

```shell
pip install -r requirements.txt
```

**🖇️ Apply Database Migrations:** Run database migrations to create the database schema:

```shell
python manage.py makemigrations
python manage.py migrate
```

**Create a superuser for administrative access:**

```shell
python manage.py createsuperuser
```

**🪄 Running the Application:**

```shell
python manage.py runserver
```

Open your web browser and visit http://localhost:8000/ to access QRify.

<!-- ### 🏷️ Usage

1. Access the QRify web interface by visiting the URL where the app is hosted.

2. Create QR codes and control them through a distinctive control panel and a professional interface.

3. View and manage your QR codes in the user-friendly admin interface.

4. Organize your QR codes into folders based on the creation date and content type.

5. Download QR code images for sharing or printing. -->

### ⚖️ License

QRify is open-source and available under the MIT License.

## ✉️ Contact

For questions, issues, or feedback, please contact Fahad Mashi at [Fahadmashi@hotmail.com](mailto:Fahadmashi@hotmail.com).
