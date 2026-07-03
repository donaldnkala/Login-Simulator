correct_email = "donaldnkala@gmail.com"
correct_password = "trump"

email = input("Enter email: ")
password = input("Enter password: ")

if email == correct_email and password == correct_password:
    print("Login successful! Welcome.")
else:
    print("Login failed! Wrong email or password.")