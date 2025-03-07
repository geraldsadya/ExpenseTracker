
# 💰 Expense Tracker CLI

A **powerful yet simple** command-line tool built in Python to help you **track and manage expenses effortlessly.**  
This tool allows you to **add, update, delete, list, and summarize expenses**—all from your terminal. No extra dependencies required!

🎯 **Key Features**
- 📌 **Add Expenses** – Quickly log expenses with a description and amount.
- 📜 **List Expenses** – View your expenses in a clean, tabular format.
- ❌ **Delete Expenses** – Remove expenses by ID with a simple command.
- ✏ **Update Expenses** – Modify existing expenses with new details.
- 📊 **Summarize Expenses** – View total spending, with optional filtering by month.
- 🔥 **Lightweight & Fast** – Uses a simple JSON file to store expenses.

---

## 🚀 Demo
🎥 *Check out the Expense Tracker CLI in action!*  

![Expense Tracker Demo](path/to/your/demo.gif)  
*(Replace `path/to/your/demo.gif` with the actual file path or URL.)*

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/ExpenseTracker.git
cd ExpenseTracker
```

### **2️⃣ (Optional) Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Run the Expense Tracker**
```bash
python main.py --help
```

This will show you all available commands.

---

## 🎯 How to Use

### 🟢 **Add an Expense**
```bash
python main.py add --description "Lunch" --amount 20
```
✔ **Output:**  
```
Expense added successfully (ID: 1)
```

---

### 📜 **List All Expenses**
```bash
python main.py list
```
✔ **Output:**
```
ID    Date         Description          Amount    
--------------------------------------------------
1     2024-08-06   Lunch                $20.00    
2     2024-08-06   Dinner               $10.00    
```

---

### ❌ **Delete an Expense**
```bash
python main.py delete --id 2
```
✔ **Output:**
```
Expense deleted successfully (ID: 2)
```

---

### ✏ **Update an Expense**
```bash
python main.py update --id 1 --description "Brunch" --amount 25
```
✔ **Output:**
```
Expense updated successfully (ID: 1)
```

---

### 📊 **View Summary of Expenses**
#### **Total Expenses**
```bash
python main.py summary
```
✔ **Output:**
```
Total expenses: $30.00
```

#### **Total Expenses for a Specific Month**
```bash
python main.py summary --month 8
```
✔ **Output:**
```
Total expenses for August: $20.00
```

---

## 🛠 Under the Hood
🔹 **Programming Language:** Python  
🔹 **Storage:** JSON (lightweight & easy to manage)  
🔹 **CLI Parsing:** Python’s built-in `argparse`  

---

## 💡 Future Enhancements
Want to take this to the next level? Here are some **potential upgrades**:
- 📌 **Categorize expenses** (e.g., Food, Transport, Entertainment)
- 🔔 **Budget Warnings** when exceeding a predefined limit
- 📂 **CSV Export** to analyze expenses in Excel or Google Sheets
- 🌍 **Multi-Currency Support**
- 📊 **Graphical Reports** using `matplotlib`

*(Contributions are welcome! Feel free to fork and add new features.)*

---

## 🎖 Why Use This?
✔ **No dependencies** – Runs on vanilla Python, no extra installs.  
✔ **Fast & lightweight** – Minimal storage footprint.  
✔ **Customizable** – Easily tweak and extend functionality.  
✔ **Great for learning** – Teaches file handling, CLI interactions, and modular programming.

---

## 🏆 Contributors & Acknowledgments
Built with ❤️ by [Gerald Sadya](https://github.com/geraldsadya).  
Inspired by the need for a **quick, no-fuss way to track expenses** without spreadsheets.  

---

## ⚖ License
📜 **MIT License** – Feel free to use and modify this project as you wish.  

---

🔹 *If you found this project helpful, don’t forget to ⭐ star the repo!* 🔹  
🚀 **Let's track expenses the smart way!** 🚀
```

