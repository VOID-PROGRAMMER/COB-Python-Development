import tkinter as tk
from tkinter import ttk
import pyshorteners
import webbrowser

def shortenurl(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

# open link directly on webbrowser
def open_url(event):
    webbrowser.open(result_label.cget("text"))

def on_button_click():
    entered_text = entry.get()
    shortened_url = shortenurl(entered_text)
    print(f'Original URL: {entered_text}')
    print(f'Shortened URL: {shortened_url}')
    
    # Update the label with the shortened URL
    result_label.config(text=f'{shortened_url}')

# Create the main window
root = tk.Tk()
root.title("Task 1")
root.configure(bg='Dark Blue')
result_label = ttk.Label(root, text="Python Internship Phase 1", font=('Helvetica', 12), foreground="White",background='Dark Blue')
result_label.pack(pady=10)

# Style configuration
style = ttk.Style()
style.configure('TButton', padding=(10, 5), font=('Helvetica', 12))

# Textbox
entry = ttk.Entry(root, width=50, font=('Helvetica', 12))
entry.pack(pady=10)

# Button
button = ttk.Button(root, text="Shorten URL",command=on_button_click)
button.pack()

# Result Label
result_label = ttk.Label(root, text="", font=('Helvetica', 12), foreground="White",background='Dark Blue' ,cursor="hand2")
result_label.pack(pady=10)

# Url 
result_label.bind("<Button-1>", open_url)

# Start the Tkinter event loop
root.mainloop()










# import pyshorteners

# # url = input('Enter the url: ')


# # def shortenurl(url):
# #     s = pyshorteners.Shortener()
# #     print(s.tinyurl.short(url))

# # shortenurl(url)

# import tkinter as tk
# from tkinter import ttk



# def on_button_click():
#     entered_text = entry.get()
#     shorty = shortenurl(entered_text)
#     print(f'Text entered: {shorty}')
#     entry2.set(shorty)

# # url = input('Enter the url: ')


# def shortenurl(entered_text):
#     s = pyshorteners.Shortener()
#     print(s.tinyurl.short(entered_text))



# # Create the main window
# root = tk.Tk()
# root.title("Styled GUI")

# # Style configuration
# style = ttk.Style()
# style.configure('TButton', padding=(10, 5), font=('Helvetica', 12))

# # Create an Entry widget (input field)
# entry = ttk.Entry(root, width=30, font=('Helvetica', 12))
# entry.pack(pady=10)

# # Create a Button widget
# button = ttk.Button(root, text="Click Me", command=on_button_click)
# button.pack()

# # Create an Entry widget (input field)
# entry2 = ttk.Entry(root, width=30, font=('Helvetica', 12))
# entry2.pack(pady=10)

# # Start the Tkinter event loop
# root.mainloop()
