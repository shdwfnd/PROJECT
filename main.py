start GUI development
import math
import tkinter as tk

LARGE_FONT_STYLE = ("Cambria", 30, "bold")
SMALL_FONT_STYLE = ("Cambria", 16)
DEFAULT_FONT_STYLE = ("Cambria", 20)
sin, cos, tan = math.sin, math.cos, math.tan
sqrt = math.sqrt
power = math.pow
π = math.pi
abs = math.fabs
log = math.log10
ln = math.log
e = math.exp


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("370x590")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.prev_ans = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {
            7: (3, 1), 8: (3, 2), 9: (3, 3),
            4: (4, 1), 5: (4, 2), 6: (4, 3),
            1: (5, 1), 2: (5, 2), 3: (5, 3),
            ".": (6, 2), 0: (6, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.operations1 = {"*": "\u00D7", "+": "+"}
        self.operations2 = {"/": "\u00F7", "-": "-"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        # BASIC BUTTONS
        self.create_digit_buttons()
        self.create_operator1_buttons()
        self.create_operator2_buttons()
        self.create_delete_button()
        self.create_equals_button()
        self.create_clear_button()
        self.create_additional_buttons()
        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("c", lambda event: self.clear())
        self.window.bind("<BackSpace>", lambda event: self.delete())
        self.window.bind("<Tab>", lambda event: self.exit())
        self.window.bind("E", lambda event: self.add_to_expression('E'))
        self.window.bind("e", lambda event: self.add_to_expression('e(' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt(' )
                           else '*e(' ))
        self.window.bind("P", lambda event: self.add_to_expression('P'))
        self.window.bind("C", lambda event: self.add_to_expression('C'))
        self.window.bind('(', lambda event: self.add_to_expression('(' if (not self.current_expression or
                           self.current_expression == "+" or self.current_expression == '-' or self.current_expression == '*' or
                           self.current_expression == "/")
                           else '*('))
        self.window.bind(")", lambda event: self.add_to_expression(')'))
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_additional_buttons(self):
        self.create_square_button()
        self.create_sqrt_button()
        self.create_cube_button()
        self.create_exp_button()
        self.create_right_parenthesis_button()
        self.create_left_parenthesis_button()
        self.create_ans_button()
        self.create_tan_button()
        self.create_sin_button()
        self.create_cos_button()
        self.create_pi_button()
        self.create_log_button()
        self.create_ln_button()
        self.create_abs_button()
        self.create_e_button()
        self.create_permutation_button()
        self.create_combination_button()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    # row 0

    def create_pi_button(self):
        button = tk.Button(self.buttons_frame, text="π", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('π' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt(' or
                           self.current_expression == 'abs(')
                           else '*π' ))
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_log_button(self):
        button = tk.Button(self.buttons_frame, text="log", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('log(' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt('or
                           self.current_expression == 'abs(')
                           else '*log(' ))
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_ln_button(self):
        button = tk.Button(self.buttons_frame, text="ln", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('ln(' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt(' or
                           self.current_expression == 'abs(')
                           else '*ln('))
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_abs_button(self):
        button = tk.Button(self.buttons_frame, text="abs", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('abs(' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt(' or
                           self.current_expression == 'abs(' or self.current_expression == 'e(')
                           else '*abs('))
        button.grid(row=0, column=4, sticky=tk.NSEW)

    def create_e_button(self):
        button = tk.Button(self.buttons_frame, text="e", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('e(' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt(' or
                           self.current_expression == 'abs(')
                           else '*e(' ))
        button.grid(row=0, column=5, sticky=tk.NSEW)

    # row 1
    def create_sin_button(self):
        button = tk.Button(self.buttons_frame, text="sin", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('sin(' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt('or
                           self.current_expression == 'abs(')
                           else '*sin('))
        button.grid(row=1, column=1, sticky=tk.NSEW)

    def create_cos_button(self):
        button = tk.Button(self.buttons_frame, text="cos", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('cos(' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt('or
                           self.current_expression == 'abs(')
                           else '*cos(' ))
        button.grid(row=1, column=2, sticky=tk.NSEW)

    def create_tan_button(self):
        button = tk.Button(self.buttons_frame, text="tan", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('tan(' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt('or
                           self.current_expression == 'abs(')
                           else '*tan('))
        button.grid(row=1, column=3, sticky=tk.NSEW)

    def create_left_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text="(", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('(' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt('or
                           self.current_expression == 'abs(' or self.current_expression == 'e('  or self.current_expression == '(')
                           else '*('))
        button.grid(row=1, column=4, sticky=tk.NSEW)

    def create_right_parenthesis_button(self):
        button = tk.Button(self.buttons_frame, text=")", bg="gray10", fg="ghost white",
                           font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression(')'))
        button.grid(row=1, column=5, sticky=tk.NSEW)

    # row 2
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('²'))
        button.grid(row=2, column=1, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('sqrt(' if (not self.current_expression or
                           self.current_expression == 'ln(' or self.current_expression == 'log(' or self.current_expression == 'tan(' or
                           self.current_expression == 'cos(' or self.current_expression == 'sin(' or self.current_expression == 'sqrt(')
                           else '*sqrt('))
        button.grid(row=2, column=2, sticky=tk.NSEW)

    def create_cube_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b3", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('³'))
        button.grid(row=2, column=3, sticky=tk.NSEW)

    def create_permutation_button(self):
        button = tk.Button(self.buttons_frame, text="nPr", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('P'))
        button.grid(row=2, column=4, sticky=tk.NSEW)

    def create_combination_button(self):
        button = tk.Button(self.buttons_frame, text="nCr", bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('C'))
        button.grid(row=2, column=5, sticky=tk.NSEW)

    # row 3
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="gray6", fg="ghost white", font=SMALL_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="AC", bg="firebrick3", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=3, column=4, sticky=tk.NSEW)

    def delete(self):
        self.current_expression = str(self.current_expression[:-1])
        self.update_label()

    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text="del", bg="firebrick3", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.delete)
        button.grid(row=3, column=5, sticky=tk.NSEW)

    # row 4 and 5
    def create_operator1_buttons(self):
        i = 4
        for operator, symbol in self.operations1.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_operator2_buttons(self):
        i = 4
        for operator, symbol in self.operations2.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="gray10", fg="ghost white", font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=5, sticky=tk.NSEW)
            i += 1

    # row 6
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="chocolate1", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=6, column=5, sticky=tk.NSEW)

    def answer(self):
        self.current_expression = self.current_expression + "Ans"
        self.update_label()
        self.update_total_label()

    def create_ans_button(self):
        button = tk.Button(self.buttons_frame, text="Ans", bg="gray6", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.answer)
        button.grid(row=6, column=4, sticky=tk.NSEW)

    def create_exp_button(self):
        button = tk.Button(self.buttons_frame, text="EXP", bg="gray6", fg="ghost white", font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=lambda: self.add_to_expression('E'))
        button.grid(row=6, column=3, sticky=tk.NSEW)

    # other functions
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        x = self.total_expression

        try:
            if '²' in x or '³' in x or 'E' in x or 'P' in x or 'C' in x or 'Ans' in x:
                x = x.replace('²', '**2').replace('³', '**3').replace('E','*10**').replace('Ans',f'{self.prev_ans}')
                pc = []
                operands = ['+', '-', '*', '/']
                for i in range(len(x)):
                    if x[i] == 'P' or x[i] == 'C':
                        term = ''
                        y = z = i
                        while y > -1 and x[y] not in operands:
                            term = x[y] + term
                            y -= 1
                        while (z+1) < len(x) and x[z+1] not in operands:
                            term += x[z+1]
                            z += 1
                        pc.append(term)
                for term in pc:
                    if 'P' in term:
                        n,r = term.split('P')
                        n,r = int(n), int(r)
                        if 0 <= r <= n: 
                            x = x.replace(term, f'math.factorial({n})' + '//' + f'math.factorial({n}-{r})')
                    elif 'C' in term:
                        n,r = term.split('C')
                        n,r = int(n), int(r)
                        if 0 <= r <= n:
                            x = x.replace(term, f'math.factorial({n})' + '//' + f'math.factorial({r})' + '//' + f'math.factorial({n}-{r})' )
            self.current_expression = str(eval(x))

        except Exception:
            self.current_expression = "Math Error"   

        self.prev_ans = self.current_expression[:]
        self.total_expression = ""
        self.update_label()
        return self.current_expression

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="gray37",
                               fg="lavender", padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="gray37",
                         fg="lavender", padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, )
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations1.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:13])

    def exit(self):
        exit()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
