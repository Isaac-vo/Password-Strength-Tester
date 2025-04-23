# Password Strength Tester - APP 

### About the developer:
Hello everyone, my name is Isaac Veneruci de Oliveira, a cybersecurity student and a passionate enthusiast for securing systems. This is the first project out of nine that I have commited to developing this year, ranging from the simplest to the most challenging. So, stay tuned for innovative projects in the cybersecurity realm.

### Level
Beginner

## Description:
The <em>Password Strength Tester APP</em> was developed to help users create strong passwords to make it harder for adversaries to hack. The application is based on the ***NIST (National Institute of Standards and Technology)*** criteria, which include:

1. Minimum length of 8 characters.
2. At least one number [0-9]
3. At least one lowercase letter [a-z]
4. At least one uppercase letter [A-Z]
5. At least one special character [!@#$%^&*()-_=+]

The application was developed using Tkinter a Python library for creating graphical user interfaces (GUIs). Some of the buttons implemented to help users are:

- *Show* - (To hide or show the password typed by the user)
- *Check Password* - (Triggers the function that checks the password's strength)
- *Show Common Passwords - Hashes* - (Displays the compromised password's hashes used to evaluate the strength of the typed password)

The levels of passowords determined by the application are:

- Weak
- Moderate
- Strong

Besides the NIST criteria used to determine password strength, a third party source called ***Pwned Passwords*** was used to enhance the criteria. This API, developed by Troy Hunt, Charlotte Hunt, and Stefán Jökull Sigurðarson came about after what was, at the time, the largest ever single breach of customer accounts. The team often did post-breach analysis of user credentials and kept finding the same accounts exposed over and over again, often with the same passwords which then put the victims at further risk of their other accounts being compromised. The *Pwned Passwords* provides a large database of hashed compromised passwords and emails that users can check to see if any password or email typed has been exposed to any breach.

**Pwned Passwords** = https://haveibeenpwned.com/

The ***Password Strength Tester - APP*** then uses this technology to check in real-time if the password typed by the user is compromised or not, helping users to strengthen even more their passwords and avoid hacking or breaches in the future.
The ***Show Common Passwords - Hashes*** button was added to show the compromised password's hashes related to the typed password for technical users.

## How to use it?

To use the application you should download the **"Password Strength Tester"** folder from my GitHub page at (https://github.com/Isaac-vo), which contains the following files:

- env
- Password.py
- README.md
- requirements.txt

After downloading it, follow the steps below:

1. Open the **"Windows PowerShell"** or **"Command Prompt"**, and navigate to the downloaded folder using the command ***"cd"***.

2. Once the folder is open, you can activate the virtual environment ***"env"*** by typing ***.\env\scripts\activate*** on the command-line. 

3. Install the required dependencies by typing ***pip install -r requirements.txt***

4. After completing the above step, you should be ready to run the program. Type ***python .\Password.py*** on your comman-line, and the application should open.

>PS: It's necessary that you have python installed in your computer in order to make the application work, if you don't have it installed yet, you can download it from python's official website (https://www.python.org/).

## Support

If you have any questions about the app that were not addressed in this introduction, feel free to reach out to me through Github or by email at (veneruci@gmail.com).

Thank you so much for reading until here, and I hope I have helped you improve your security against potencial threats on the internet.

Thank you! 02/28/2025!






