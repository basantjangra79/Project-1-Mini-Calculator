# 🧮 Mini Calculator

A simple command-line calculator built with Python that performs basic arithmetic operations such as Addition, Subtraction, Multiplication, and Division. The program includes input validation, division-by-zero handling, and a loading animation for a better user experience.

---

## 📌 Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* 🚫 Division by zero protection
* ⚠️ Invalid input handling
* ⌨️ Keyboard interrupt support (`Ctrl + C`)
* 🎬 Loading animation at startup
* 🔄 Continuous execution until user exits

---

## 📂 Project Structure

```text
mini-calculator/
│
├── calculator.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your system.

```bash
python --version
```

or

```bash
python3 --version
```

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mini-calculator.git
```

### 2. Navigate to the Project Folder

```bash
cd mini-calculator
```

### 3. Run the Program

```bash
python calculator.py
```

or

```bash
python3 calculator.py
```

---

## 📖 Usage

When the program starts, you'll see a loading animation:

```text
Loading Calculator.....
```

Then enter two numbers:

```text
Enter First Number: 10
Enter Second Number: 5
```

Choose an operation:

```text
1 - Addition
2 - Substraction
3 - Multiplication
4 - Division
5 - Exit
```

Example:

```text
Choose a Number to Proceed: 1
Answer: 15
```

---

## 🧾 Example Output

```text
Loading Calculator.....

Welcome to Mini Calculator!

Enter First Number: 20
Enter Second Number: 4

1 - Addition
2 - Substraction
3 - Multiplication
4 - Division
5 - Exit

Choose a Number to Proceed: 4

Answer: 5.0

======================================== Coded by : Basant Jangra ========================================
```

---

## ⚠️ Error Handling

### Invalid Input

If the user enters anything other than numbers:

```text
Only Number are Allowed.
```

### Division by Zero

```text
Division by Zero is Not Possible.
```

### Keyboard Interrupt

Press:

```text
Ctrl + C
```

Output:

```text
Program Closed By User.
```

---

## 🛠 Built With

* Python 3
* Built-in `time` module

---

## 🔧 Future Improvements

Possible enhancements:

* Support decimal numbers (`float`)
* Add modulus operation (`%`)
* Add exponent operation (`**`)
* Add calculation history
* Create a GUI version using Tkinter
* Improve menu navigation
* Add unit tests

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Basant Jangra**

Python Developer | Software Engineer

If you found this project useful, consider giving it a ⭐ on GitHub.
