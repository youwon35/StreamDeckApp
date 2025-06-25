import pytesseract
import os
from dotenv import load_dotenv
from PIL import ImageGrab
from PIL import Image
import deepl
import tkinter as tk
from tkinter import Label
import cv2
import numpy as np

load_dotenv()
deepl_api_key = os.getenv('DEEPL_API_KEY')
print(deepl_api_key)
def screenshot_and_translate():
    img = ImageGrab.grab()
    
    img_cv = np.array(img)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    thresh =cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)[1]
    thresh_pil = Image.fromarray(thresh)
    text = pytesseract.image_to_string(thresh_pil, lang='eng', config='--psm 6')
    
    translator = deepl.Translator(deepl_api_key)
    result  = translator.translate_text(text,source_lang = "EN", target_lang = "KO")
    root = tk.Tk()
    root.attributes("-topmost", True)  # 🧲 항상 위에 띄우기
    root.geometry("800x400+900+200")  # 창 크기 및 위치 조절
    root.configure(bg="black")

    label = Label(root, text=result.text, font=("맑은 고딕", 14), wraplength=380, fg="white", bg="black")
    label.pack(expand=True)
    root.attributes("-topmost", True)
    root.mainloop()
screenshot_and_translate()