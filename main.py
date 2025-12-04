import customtkinter as ctk
from tkinter import filedialog, messagebox
import pytesseract
import cv2
import os
from PIL import Image

# --- Configuration & Setup ---

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Theme Settings - Light Mode for clean look
ctk.set_appearance_mode("Light")  
ctk.set_default_color_theme("blue")

# Colors
COLOR_HEADER = "#2C3E50"    # Dark Blue/Grey for Top Bar
COLOR_ACCENT = "#D81B60"    # Pink/Red for Upload Box
COLOR_BTN_HOVER = "#C2185B" # Hover color for pink button
COLOR_SUCCESS = "#27AE60"   # Green for success

class OCRApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Handwritten Note Digitizer Pro")
        self.geometry("900x650")
        
        # Grid Layout: 1 Column, 3 Rows (Header, Content, Footer)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1) # Main content takes most space
        self.grid_rowconfigure(2, weight=0) # Footer takes little space

        # ==================== 1. Top Header Bar ====================
        self.header_frame = ctk.CTkFrame(self, height=80, corner_radius=0, fg_color=COLOR_HEADER)
        self.header_frame.grid(row=0, column=0, sticky="ew")
        
        # App Title in Header
        self.title_label = ctk.CTkLabel(self.header_frame, text="Image to Text Converter", 
                                        font=ctk.CTkFont(family="Arial", size=28, weight="bold"),
                                        text_color="white")
        self.title_label.place(relx=0.5, rely=0.5, anchor="center") # Completely center text


        # ==================== 2. Upload Screen (Main View) ====================
        
        # Container Frame for the Upload Box (To center it perfectly)
        self.upload_container = ctk.CTkFrame(self, fg_color="transparent")
        self.upload_container.grid(row=1, column=0)

        # The Pink Upload Box (Now smaller as requested)
        self.upload_frame = ctk.CTkFrame(self.upload_container, width=500, height=300, 
                                         fg_color=COLOR_ACCENT, corner_radius=20)
        self.upload_frame.pack(pady=20, padx=20)
        self.upload_frame.grid_propagate(False) # Fix size

        # Center content inside upload frame
        self.upload_frame.grid_columnconfigure(0, weight=1)
        self.upload_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # Plus Icon Button
        self.btn_upload_trigger = ctk.CTkButton(self.upload_frame, text="+", font=ctk.CTkFont(size=50),
                                                 width=100, height=100, corner_radius=50,
                                                 fg_color="white", text_color=COLOR_ACCENT, 
                                                 hover_color="#F0F0F0",
                                                 command=self.open_file)
        self.btn_upload_trigger.grid(row=0, column=0, pady=(40, 10))

        # Main Text
        self.label_upload_text = ctk.CTkLabel(self.upload_frame, text="Upload your Image",
                                              font=ctk.CTkFont(size=20, weight="bold"), text_color="white")
        self.label_upload_text.grid(row=1, column=0, pady=5)


        # ==================== 3. Result Screen (Initially Hidden) ====================
        self.result_frame = ctk.CTkFrame(self, fg_color="transparent")
        
        # Result Heading
        self.result_heading = ctk.CTkLabel(self.result_frame, text="Extraction Successful!", 
                                           font=ctk.CTkFont(size=20, weight="bold"), text_color=COLOR_SUCCESS)
        self.result_heading.pack(pady=(10, 10))

        # Textbox
        self.textbox = ctk.CTkTextbox(self.result_frame, width=700, height=350, 
                                      font=("Consolas", 14), corner_radius=10, border_width=2, border_color="#E0E0E0")
        self.textbox.pack(pady=10)

        # Buttons Frame
        self.btn_frame = ctk.CTkFrame(self.result_frame, fg_color="transparent")
        self.btn_frame.pack(pady=10)

        # Download Button
        self.btn_save = ctk.CTkButton(self.btn_frame, text="💾 Save Text", command=self.save_file,
                                      fg_color=COLOR_SUCCESS, hover_color="#219150", width=180, height=45, 
                                      font=ctk.CTkFont(size=15, weight="bold"))
        self.btn_save.pack(side="left", padx=15)

        # Restart Button
        self.btn_restart = ctk.CTkButton(self.btn_frame, text="🔄 Convert New", command=self.restart_app,
                                         fg_color=COLOR_HEADER, hover_color="#1A252F", width=180, height=45, 
                                         font=ctk.CTkFont(size=15, weight="bold"))
        self.btn_restart.pack(side="left", padx=15)


        # ==================== 4. Footer (Developer Credit) ====================
        self.footer_label = ctk.CTkLabel(self, text="Developed by SahanST19", 
                                         font=ctk.CTkFont(size=12, slant="italic"), text_color="gray")
        self.footer_label.grid(row=2, column=0, pady=(0, 15))


    def preprocess_image(self, image_path):
        """Preprocessing for better OCR"""
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 3)
        threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return threshold_img

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")]
        )
        
        if file_path:
            self.label_upload_text.configure(text="Processing...")
            self.update()

            try:
                processed_img = self.preprocess_image(file_path)
                text = pytesseract.image_to_string(processed_img, config='--psm 6')

                # Update Textbox
                self.textbox.delete("0.0", "end")
                self.textbox.insert("0.0", text)

                # Switch UI
                self.upload_container.grid_forget() # Hide upload
                self.result_frame.grid(row=1, column=0) # Show result

            except Exception as e:
                messagebox.showerror("Error", f"Failed: {e}")
                self.label_upload_text.configure(text="Upload your Image")

    def restart_app(self):
        self.textbox.delete("0.0", "end")
        self.label_upload_text.configure(text="Upload your Image")
        self.result_frame.grid_forget() # Hide result
        self.upload_container.grid(row=1, column=0) # Show upload

    def save_file(self):
        text_content = self.textbox.get("0.0", "end")
        if not text_content.strip():
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text File", "*.txt"), ("Word Document", "*.doc")]
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(text_content)
                messagebox.showinfo("Success", "Saved!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save: {e}")

if __name__ == "__main__":
    app = OCRApp()
    app.mainloop()