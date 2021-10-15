#Mehmet Akif Selbi
#Turkce bir metni Turkceye ozgu karakterleri noktasiz benzerleriyle degistirme
import tkinter as tk

window = tk.Tk()
window.minsize(600,400)
window.resizable(0, 0)

def clickMe():
    kaynak = "şçöğüıŞÇÖĞÜİ"
    hedef = "scoguiSCOGUI"
    ceviri = str.maketrans(kaynak,hedef)
    message = entry.get()
    text_box.configure(state = "normal")
    text_box.delete("1.0", tk.END)
    text_box.insert("1.0", message.translate(ceviri))
    text_box.configure(state = "disabled")


inp_ = tk.Label(text="input").grid(row=0)
out_ = tk.Label(text="output").grid(row=2)

entry = tk.Entry(window,width=100)
entry.grid(row = 1)

text_box = tk.Text()
text_box.grid(row=3)
text_box.configure(state = "disabled")

button = tk.Button(window, text = "Kelimeyi_Cevir", command = clickMe,bd=5).grid(row = 5)

bos = tk.Label().grid(row=6)
bos = tk.Label().grid(row=4)

window.mainloop()