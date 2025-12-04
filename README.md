# Image to Text Converter (OCR Tool) 📝

A professional, modern desktop application built with Python that converts handwritten or printed text from images into editable digital text files. This tool utilizes **Google Tesseract OCR** for text recognition and **OpenCV** for image preprocessing, ensuring high accuracy.

Designed with a clean, modern User Interface using `CustomTkinter`.

## 🚀 Key Features
* **Modern UI:** Clean, professional interface with a "Light Mode" design.
* **Image Preprocessing:** Automatically handles noise removal and thresholding to improve accuracy.
* **Format Support:** Supports JPG, PNG, and BMP image formats.
* **Save to File:** One-click option to save extracted text as `.txt` files.
* **Developer Branding:** Developed by **SahanST19**.

---

## ⚠️ Important Prerequisites (Read First)
To run this application, **Tesseract-OCR** must be installed on your computer.

### 📥 How to Install Tesseract OCR
1.  Download the Tesseract installer for Windows (64-bit) from this link:
    * [Download Tesseract at UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
2.  Run the installer.
3.  **IMPORTANT:** During installation, ensure the destination folder is exactly:
    > `C:\Program Files\Tesseract-OCR`
    
    *(If you install it elsewhere, the application will not be able to find the OCR engine).*

---

## 🛠️ Installation & Setup (Source Code)

If you want to run the source code directly:

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/SahanST19/Image-to-Text-OCR.git](https://github.com/SahanST19/Image-to-Text-OCR.git)
    cd Image-to-Text-OCR
    ```

2.  **Install Required Libraries**
    Open your terminal/command prompt and run:
    ```bash
    pip install customtkinter pytesseract opencv-python pillow packaging
    ```

3.  **Run the Application**
    ```bash
    python main.py
    ```

---

## 💿 Creating the Executable (.exe)
To build this project into a standalone software file:

1.  Install PyInstaller:
    ```bash
    pip install pyinstaller
    ```
2.  Run the build command:
    ```bash
    python -m PyInstaller --noconsole --onefile --collect-all customtkinter main.py
    ```
3.  Check the `dist` folder for the `main.exe` file.

---

## 👨‍💻 Developer
**SahanST19**
* GitHub: [SahanST19](https://github.com/SahanST19)
* Email: sahan.github19@gmail.com

---
*Created for  Project | 2025*