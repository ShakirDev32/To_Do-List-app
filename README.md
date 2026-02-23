📝 Python To-Do List App
A simple, interactive Command Line Interface (CLI) application built with Python to help users manage their daily tasks efficiently.

🚀 Features
Add Tasks: Quickly input new items to your list.

View Tasks: See all your current tasks with clear numbering.

Remove Tasks: Delete completed or unwanted tasks by their index number.

Input Validation: Basic error handling for menu choices and task numbers.

🛠️ Requirements
Python 3.x installed on your system.

📥 How to Run
Clone the repository:

Bash
git clone https://github.com/ShakirDev32/To_Do-List-app.git
Navigate to the folder:

Bash
cd To_Do-List-app
Run the script:

Bash
python todo_list.py
📖 How to Use
Once the script is running, follow the on-screen menu:

Press 1 to add a new task (e.g., "Buy groceries").

Press 2 to display your list.

Press 3 to remove a task (enter the number shown next to the task).

Press 4 to exit the application.

💡 Two quick tips for your Python code:
The Newline Bug: In your code, you have print("/n To-Do List"). In Python, the newline character uses a backslash, not a forward slash. Change it to \n to get that extra space at the top.

Cleaner Output: When you use enumerate, your code currently prints the tuple like (1, 'Task Name'). If you want it to look prettier, change your print line to:
print(f"{i}. {task}") (by unpacking the index and task).
