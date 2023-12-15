"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import tkinter as tk

window = tk.Tk()
window.title("Factoring Trinomials")
window.geometry("400x200")

instruction_label = tk.Label(window, text="Enter the coefficients for b and c in the trinomial x^2 + bx + c")
instruction_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

b_label = tk.Label(window, text="b:")
b_label.grid(row=1, column=0, padx=10, pady=10)
b_entry = tk.Entry(window)
b_entry.grid(row=1, column=1, padx=10, pady=10)
c_label = tk.Label(window, text="c:")
c_label.grid(row=1, column=2, padx=10, pady=10)
c_entry = tk.Entry(window)
c_entry.grid(row=1, column=3, padx=10, pady=10)

factored_label = tk.Label(window, text="Factored form:")
factored_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
factored_entry = tk.Entry(window,width=30)
factored_entry.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

def validate_inputs():
    try:
        b = int(b_entry.get())
        c = int(c_entry.get())
        return True
    except ValueError:
        factored_entry.delete(0, tk.END)
        factored_entry.insert(0, "Invalid inputs. Please enter integers.")
        b_entry.delete(0, tk.END)
        c_entry.delete(0, tk.END)
        return False

def factor_trinomial():
    if validate_inputs():
        b = int(b_entry.get())
        c = int(c_entry.get())
        for i in range(-abs(c), abs(c) + 1):
            if i != 0 and c % i == 0:
                j = c // i
                if i + j == b:
                    factored_form = f"(x + {i})(x + {j})"
                    factored_entry.delete(0, tk.END)
                    factored_entry.insert(0, factored_form)
                    break
        else:
            factored_entry.delete(0, tk.END)
            factored_entry.insert(0, "The trinomial is not factorable.")
            b_entry.delete(0, tk.END)
            c_entry.delete(0, tk.END)

factor_button = tk.Button(window, text="Factor", command=factor_trinomial)
factor_button.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

window.mainloop()

