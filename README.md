# Password Manager

A simple password manager application built with Python and Tkinter. This application allows you to generate and store passwords securely in a local JSON file.

## Features

- Generate strong, random passwords
- Save website login credentials (website, username/email, password)
- Search for saved credentials by website name
- Copy generated passwords to clipboard

## Prerequisites

- Python 3.x
- Required Python libraries:
  - tkinter
  - pyperclip

## Installation

1. Clone the repository to your local machine:
git clone https://github.com/yared27/password-manager.git
cd password-manager


2.Install the required libraries:
pip install pyperclip
Usage
1.Run the password_manager.py script:
python password_manager.py
2.The application window will appear. Use the following features:

Website: Enter the website name.
Email/Username: Enter your email or username.
Password: Enter your password or click "Generate Password" to create a strong password.
Add: Save the entered credentials.
Search: Search for saved credentials by website name.
3.All saved credentials are stored in data.json in the application's directory.

Contributing
Contributions are welcome! Please fork the repository and create a pull request.
