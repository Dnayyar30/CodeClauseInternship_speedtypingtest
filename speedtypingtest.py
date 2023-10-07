import random
import time
import tkinter as tk

# Sample text passages
text_passages = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a versatile and powerful programming language.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Programming is fun and challenging at the same time."
]

def start_typing_test():
    global start_time
    start_time = time.time()
    random.shuffle(text_passages)
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text_passages[0])
    text_area.config(state=tk.DISABLED)
    start_button.config(state=tk.DISABLED)
    end_button.config(state=tk.NORMAL)
    user_input_area.config(state=tk.NORMAL)  # Enable user input

def end_typing_test():
    end_time = time.time()
    text = text_area.get(1.0, tk.END)
    user_input = user_input_area.get(1.0, tk.END)
    
    words = text.split()
    user_words = user_input.split()
    
    correct_words = sum(1 for w1, w2 in zip(words, user_words) if w1 == w2)
    
    total_time = end_time - start_time
    words_per_minute = int((correct_words / total_time) * 60) if total_time > 0 else 0
    
    result_label.config(text=f"Words per minute: {words_per_minute}")
    
    start_button.config(state=tk.NORMAL)
    end_button.config(state=tk.DISABLED)
    user_input_area.config(state=tk.DISABLED)  # Disable user input

# Create the main window
root = tk.Tk()
root.title("Speed Typing Test")

text_area = tk.Text(root, wrap=tk.WORD, height=5, width=40, state=tk.DISABLED)
user_input_area = tk.Text(root, wrap=tk.WORD, height=5, width=40, state=tk.DISABLED)
start_button = tk.Button(root, text="Start Typing Test", command=start_typing_test)
end_button = tk.Button(root, text="End Typing Test", command=end_typing_test, state=tk.DISABLED)
result_label = tk.Label(root, text="")

text_area.pack(pady=10)
user_input_area.pack()
start_button.pack(pady=5)
end_button.pack(pady=5)
result_label.pack(pady=10)

root.mainloop()

