# Love Percentage Calculator

This is a simple Flask web application that calculates the love percentage between two names using a custom algorithm.

## Project Structure
```
project-folder/
│── app.py
│── requirements.txt
│── README.md
│── static/
│   ├── (CSS, Images, etc.)
│── templates/
│   ├── index.html
```

## Features
- Takes two names as input and calculates a "love percentage."
- Uses a custom function `sum_limit()` to generate a final percentage.
- Simple web UI built with HTML and Flask.

## Prerequisites
Make sure you have Python installed (Python 3.x recommended).

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd project-folder
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask app:
   ```sh
   python3 app.py
   ```
2. Open your web browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Explanation of the Algorithm
The `love_percentage` function:
- Converts both names to lowercase and concatenates them with the word "love."
- Counts the occurrences of each character to form a numerical string.
- Removes zeros and applies `sum_limit()` to repeatedly sum mirrored digits until the value is below 107.

## File Overview
- `app.py` - The main Flask application.
- `templates/index.html` - The frontend HTML file.
- `static/` - Folder for static files (CSS, images, etc.).

## License
This project is for educational purposes. You can modify and distribute it as needed.

# UI Representation of the App
## INPUT:
![Love Percentage Calculator - Google Chrome 04-02-2025 12_04_32 PM](https://github.com/user-attachments/assets/baff958e-1c95-484d-9ac2-c54bf1e58883)
![Love Percentage Calculator - Google Chrome 04-02-2025 12_05_00 PM](https://github.com/user-attachments/assets/23736af2-cff1-4c93-b046-94e3c75eb7dd)
## OUTPUT:
![Love Percentage Calculator - Google Chrome 04-02-2025 12_05_09 PM](https://github.com/user-attachments/assets/6bab7017-e534-4f7e-a131-7531dbafd49e)




