import tkinter as tk

# Dictionary to map integers to alphabets
toalpha = {i + 1: e for i, e in enumerate(list(map(chr, range(97, 123))))}

# List representing the key
key = [0, 3, 1, 0, 2, 0, 2, 3]


def manipulate_string(input_string):
    msg = ""
    for idx, x in enumerate(input_string.split()):
        idx %= len(key)
        msg += toalpha[int(x) - key[idx]]
    return msg


def process_input():
    # Function to get input string and display output string
    input_str = input_entry.get()
    output_str = manipulate_string(input_str)
    output_label.config(text=output_str)


# Create GUI window
root = tk.Tk()
root.title("String Manipulation")

# Configure window size and padding
root.geometry("400x200")
root.config(padx=20, pady=20)

# Create input label and entry
input_label = tk.Label(root, text="Input String:", font=("Arial", 14))
input_label.pack()
input_entry = tk.Entry(root, font=("Arial", 14))
input_entry.pack()

# Create output label
output_label = tk.Label(root, text="", font=("Arial", 14))
output_label.pack()

# Create process button
process_button = tk.Button(
    root, text="Process", font=("Arial", 14), command=process_input
)
process_button.pack(pady=10)

# Run the GUI
root.mainloop()
