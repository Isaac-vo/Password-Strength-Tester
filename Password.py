import tkinter as tk
import re
import requests
import hashlib

# List of common password to block retrieved from a third party source
def load_common_passwords(password):
    url = "https://api.pwnedpasswords.com/range/" # "Have I been Pwned" API URL
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    response = requests.get(url + prefix)

    if response.status_code == 200:
        common_passwords = [line.split(':')[0] for line in response.text.split('\n')]
        print(common_passwords) # Print the common passwords to check if it is working
        return common_passwords
    else:
        print("Failed to load common passwords", response.status_code)
        return []
    
# Main password checker function
def password_strength(password):
    score = 0

    # Load common passwords
    common_passwords = load_common_passwords(password)

    # Check password length
    if len(password) < 8:
        score -= 1
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 15:
        score += 1
    if len(password) <= 64:
        score += 1

    # Check for digits, letters, and special characters
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[!@#$%^&*()-_=+]', password):
        score += 1

    # Deduct points for common passwords and predictable patterns
    if hashlib.sha1(password.encode('utf-8')).hexdigest().upper()[5:] in common_passwords:
        score -= 3
    if re.search(r'(.)\1{2,}', password): # For repeated characters on password
        score -= 2
    if re.search(r'1234|abcd|qwerty|asdf', password, re.IGNORECASE): # Common sequences
        score -= 2
                    
    # Ensure score is returned as an integer
    return max(score,0)

def check_password_strength():
    password = entry.get()
    strength = password_strength(password)
    update_checklist(password)
    if strength is not None:
        if strength <= 3:
            result_label.config(text="Weak password", fg="red")
        elif strength <= 6:
            result_label.config(text="Moderate password", fg="orange")
        else:
            result_label.config(text="Strong password", fg="green")
    else:
        result_label.config(text="Invalid password", fg="red")

def update_checklist(event=None):
    password = entry.get()
    checklist_items = [
        (len(password) >= 8, length_label),
        (re.search(r'[0-9]', password), digit_label),
        (re.search(r'[a-z]', password), lowercase_label),
        (re.search(r'[A-Z]', password), uppercase_label),
        (re.search(r'[!@#$%^&*()\-_=+]', password), special_char_label),
    ]

    for condition, label in checklist_items:
        if condition:
            label.config(fg="green")
        else:
            label.config(fg="red")

def toggle_password_visibility():
    if entry.cget('show') == '*':
        entry.config(show='')
        toggle_button.config(text='Hide')
    else:
        entry.config(show='*')
        toggle_button.config(text='Show')

def show_common_passwords():
    common_passwords_text.delete(1.0, tk.END) # Clear the text widget
    password = entry.get()
    common_passwords = load_common_passwords(password)
    for common_password in common_passwords:
        common_passwords_text.insert(tk.END, common_password + "\n") # Insert each password


# Create the main window for the application
root = tk.Tk()
root.title("Password Strength Tester")

# Set the initial window size
root.geometry("350x450")

# Create a frame to hold entry and toggle button side by side
frame = tk.Frame(root)
frame.pack(pady=10)

# Create and place the input field with larger font
entry = tk.Entry(frame, show="*")
entry.pack(side=tk.LEFT)
entry.bind('<KeyRelease>', update_checklist) # Bind the <KeyRelease> event

# Create and place the Toggle button
toggle_button = tk.Button(frame, text="Show", command=toggle_password_visibility)
toggle_button.pack(side=tk.LEFT)

# Create and place the Check button 
check_button = tk.Button(root, text="Check Password", command=check_password_strength)
check_button.pack(pady=5)

# Creating the checklist labels
length_label = tk.Label(root, text="At least 8 characteres length", fg="red")
digit_label = tk.Label(root, text="At least one number [0-9]", fg="red")
lowercase_label = tk.Label(root, text="At least one lowercase letter [a-z]", fg="red")
uppercase_label = tk.Label(root, text="At least one uppercase letter [A-Z]", fg="red")
special_char_label = tk.Label(root, text="At least one special character [!@#$%^&*()-_=+]", fg="red")

# Pack the checklist Labels
length_label.pack()
digit_label.pack()
lowercase_label.pack()
uppercase_label.pack()
special_char_label.pack()

# Create and place the result label 
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Create and place the Show Common Passwords button
show_button = tk.Button(root, text="Show Common Passwords - Hashes", command=show_common_passwords)
show_button.pack(pady=5)

# Create and place the text widget to display common passwords
common_passwords_text = tk.Text(root, height=10, width=40)
common_passwords_text.pack(pady=5)

# Run the application
root.mainloop()