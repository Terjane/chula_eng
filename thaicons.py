import tkinter as tk
import random

# Thai consonants with their pronunciation
thai_consonants = [
    ("ก", "gor kai (ไก่)"),
    ("ข", "kho khai (ไข่)"),
    ("ค", "kho khwai (ควาย)"),
    ("ง", "ngor ngu (งู)"),
    ("จ", "jor jaan (จาน)"),
    ("ฉ", "chor ching (ฉิ่ง)"),
    ("ช", "chor chang (ช้าง)"),
    ("ซ", "sor so (โซ่)"),
    ("ญ", "yor ying (หญิง)"),
    ("ฎ", "dor cha-da (ชฎา)"),
    ("ฏ", "tor pa-tak (ปฏัก)"),
    ("ฐ", "thor than (ฐาน)"),
    ("ณ", "nor nen (เณร)"),
    ("ด", "dor dek (เด็ก)"),
    ("ต", "tor tao (เต่า)"),
    ("บ", "bor bai-mai (ใบไม้)"),
    ("ป", "por pla (ปลา)"),
    ("ผ", "phor phueng (ผึ้ง)"),
    ("ฝ", "for fa (ฝา)"),
    ("พ", "phor phan (พาน)"),
    ("ฟ", "for fan (ฟัน)"),
    ("ม", "mor ma (ม้า)"),
    ("ย", "yor yak (ยักษ์)"),
    ("ร", "ror ruea (เรือ)"),
    ("ล", "lor ling (ลิง)"),
    ("ว", "wor waen (แหวน)"),
    ("ศ", "sor sala (ศาลา)"),
    ("ส", "sor suea (เสือ)"),
    ("ห", "hor hip (หีบ)"),
    ("อ", "or ang (อ่าง)"),
    ("ฮ", "hor nok-huk (นกฮูก)")
]

# Shuffle the consonants for random order
random.shuffle(thai_consonants)
current_index = 0
flipped = False

# Functions
def flip_card():
    global flipped
    if flipped:
        card_label.config(text=thai_consonants[current_index][0])  # Show Thai consonant
    else:
        card_label.config(text=thai_consonants[current_index][1])  # Show pronunciation
    flipped = not flipped

def next_card():
    global current_index, flipped
    current_index = (current_index + 1) % len(thai_consonants)
    card_label.config(text=thai_consonants[current_index][0])
    flipped = False

# GUI Setup
root = tk.Tk()
root.title("Thai Consonant Flashcards")

# Flashcard display
card_label = tk.Label(root, text=thai_consonants[current_index][0], font=("Arial", 40), width=12, height=3, relief="solid")
card_label.pack(pady=20)

# Buttons
flip_button = tk.Button(root, text="Flip", font=("Arial", 14), command=flip_card)
flip_button.pack(side="left", padx=20, pady=10)

next_button = tk.Button(root, text="Next", font=("Arial", 14), command=next_card)
next_button.pack(side="right", padx=20, pady=10)

# Start the Tkinter loop
root.mainloop()
