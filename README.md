📁 File Handling in Python (CRUD)

File handling in Python is used to store, manage, and manipulate data using files. It allows data to be saved permanently and accessed whenever needed. The main operations in file handling are Create, Read, Update, and Delete (CRUD).

🆕 Create File
Creating a file means making a new file and writing data into it. In Python, this is done using the open() function with write mode (w). If the file does not exist, it will be created automatically.

📖 Read File
Reading a file means opening an existing file and retrieving its stored content. This is done using the open() function with read mode (r), which allows you to view the data inside the file.

✏️ Update File
Updating a file means adding new information to an existing file without removing the previous content. This is done using append mode (a) or by modifying the file using appropriate file modes.

🗑️ Delete File
Deleting a file means permanently removing it from the system. In Python, this is done using the os module and the os.remove() function, which deletes the specified file.
