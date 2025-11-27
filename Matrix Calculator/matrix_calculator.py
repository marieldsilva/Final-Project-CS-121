#IMPORTING MODULES
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont

class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        self.root.geometry("520x665")
        self.root.resizable(False, False)

        self.logo = PhotoImage(file=r"C:\Users\Mariel De Silva\OneDrive\Documents\Final Project - Advance Computer Programming\Images\icon_photo.png")
        self.root.iconphoto(True, self.logo)

        image_path = r"C:\Users\Mariel De Silva\OneDrive\Documents\Final Project - Advance Computer Programming\Images\background_photo.png"
        self.bg_image = Image.open(image_path).resize((520, 665))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = Canvas(self.root, width=520, height=665, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        self.operation = None
        self.entries_a = []
        self.entries_b = []
        self.result_label = None

        self.show_main_menu()

    def footer(self):
        self.canvas.create_text(260, 615, text="Developed By: Mariel I. De Silva", fill="white", font=("Poppins Medium", 9), anchor="center")
        self.canvas.create_text(260, 630, text="BSIT 2102 - Bachelor of Science in Information and Technology", fill="white", font=("Poppins Medium", 9), anchor="center")
        self.canvas.create_text(260, 645, text="Batangas State University TNEU - Balayan Campus", fill="white", font=("Poppins Medium", 9), anchor="center")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

    # MAIN MENU (1ST PAGE)
    def show_main_menu(self):
        self.clear_canvas()

        self.canvas.create_text(260, 72, text="MATRIX CALCULATOR", fill="white", font=("Poppins Black", 28, "bold"), anchor="center")
        self.canvas.create_text(260, 112, text="Perform basic matrix operations easily!", fill="white", font=("Poppins Medium", 12), anchor="center")

        desc_text = ("This tool helps you calculate:\n"
                     "- Addition and Subtraction of matrices\n"
                     "- Matrix Multiplication\n"
                     "- Determinant of a square matrix\n\n"
                     "Select an operation below to get started:")
        self.canvas.create_text(260, 225, text=desc_text, fill="white", font=("Poppins Medium", 12), width=400, anchor="center")

        y_start = 347
        for op in ["Addition", "Subtraction", "Multiplication", "Determinant"]:
            btn = Button(self.root, text=op, width=20, font=("Poppins Medium", 12), fg = "#213448", 
                         command=lambda o=op: self.select_operation(o))
            self.canvas.create_window(260, y_start, window=btn)
            y_start += 60

        self.footer()

    def select_operation(self, op):
        self.operation = op
        self.show_matrix_size_input()

    # MATRIX SIZE INPUT (2ND PAGE)
    def show_matrix_size_input(self):
        self.clear_canvas()
        self.canvas.create_text(260, 102, text=f"Matrix {self.operation}", fill="white", font=("Poppins Black", 28, "bold"), anchor="center")
        self.canvas.create_text(260, 142, text="Please enter matrix sizes:", fill="white", font=("Poppins Medium", 12), anchor="center")

        frame = Frame(self.root, bg="#547792", padx=20, pady=10)
        self.canvas.create_window(260, 270, window=frame)

        Label(frame, text="Matrix A Rows:", fg="white", font=("Poppins Medium", 12), bg="#547792").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        Label(frame, text="Matrix A Columns:", fg="white", font=("Poppins Medium", 12), bg="#547792").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.a_rows = Entry(frame, width=10, font=("Poppins Medium", 10), fg="#213448")
        self.a_cols = Entry(frame, width=10, font=("Poppins Medium", 10), fg="#213448")
        self.a_rows.grid(row=0, column=1)
        self.a_cols.grid(row=1, column=1)

        if self.operation != "Determinant":
            Label(frame, text="Matrix B Rows:", fg="white", font=("Poppins Medium", 12), bg="#547792").grid(row=2, column=0, padx=5, pady=5, sticky="w")
            Label(frame, text="Matrix B Columns:", fg="white", font=("Poppins Medium", 12), bg="#547792").grid(row=3, column=0, padx=5, pady=5, sticky="w")
            self.b_rows = Entry(frame, width=10, font=("Poppins Medium", 10), fg="#213448")
            self.b_cols = Entry(frame, width=10, font=("Poppins Medium", 10), fg="#213448")
            self.b_rows.grid(row=2, column=1)
            self.b_cols.grid(row=3, column=1)
        else:
            self.b_rows = self.b_cols = None

        next_btn = Button(self.root, text="Next", font=("Poppins Medium", 12), fg = "#213448", width=15, command=self.validate_sizes)
        back_btn = Button(self.root, text="Back", font=("Poppins Medium", 12), fg = "#213448", width=15, command=self.show_main_menu)
        self.canvas.create_window(260, 420, window=next_btn)
        self.canvas.create_window(260, 485, window=back_btn)

        self.footer()

    # ERROR MESSAGES IF SIZES ARE WRONG
    def validate_sizes(self):
        try:
            ar, ac = int(self.a_rows.get()), int(self.a_cols.get())
            if self.operation != "Determinant":
                br, bc = int(self.b_rows.get()), int(self.b_cols.get())
            else:
                br = bc = None
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers.")
            return

        if ar <= 0 or ac <= 0 or (self.operation != "Determinant" and (br <= 0 or bc <= 0)):
            messagebox.showerror("Invalid Input", "Matrix sizes must be positive.")
            return

        if self.operation in ["Addition", "Subtraction"] and (ar != br or ac != bc):
            messagebox.showerror("Error", "For addition/subtraction, matrices must be the same size.")
            return
        elif self.operation == "Multiplication" and ac != br:
            messagebox.showerror("Error", "For multiplication, columns of A must match rows of B.")
            return
        elif self.operation == "Determinant" and ar != ac:
            messagebox.showerror("Error", "Matrix A must be square for determinant.")
            return

        self.show_matrix_input(ar, ac, br, bc)

    # MATRIX VALUE INPUT (3RD PAGE)
    def show_matrix_input(self, ar, ac, br, bc):
        self.clear_canvas()

        self.canvas.create_text(260, 72, text=f"Values for {self.operation}", fill="white", font=("Poppins Black", 28, "bold"), anchor="center")
        if self.operation != "Determinant":
            self.canvas.create_text(260, 102, text=f"Please input the values for Matrix A and Matrix B below:", fill="white", font=("Poppins Medium", 12), anchor="center")
        else:
            self.canvas.create_text(260, 102, text=f"Please input the values of your Matrix below:", fill="white", font=("Poppins Medium", 12), anchor="center")

        container = Frame(self.root, bg="#547792", padx=20, pady=20)
        self.canvas.create_window(260, 220, window=container)

        self.entries_a = []
        self.entries_b = []

        frame_a = LabelFrame(container, text="Matrix A", padx=10, pady=5, bg="#ECEFCA", fg="#213448", font=("Poppins Medium", 10))
        frame_a.grid(row=0, column=0, padx=10)
        for i in range(ar):
            row_entries = []
            for j in range(ac):
                e = Entry(frame_a, width=3, font=("Poppins Medium", 8), fg="#213448")
                e.grid(row=i, column=j, padx=3, pady=3)
                row_entries.append(e)
            self.entries_a.append(row_entries)

        if self.operation != "Determinant":
            frame_b = LabelFrame(container, text="Matrix B", padx=10, pady=5, bg="#ECEFCA", fg="#213448", font=("Poppins Medium", 10))
            frame_b.grid(row=0, column=1, padx=10)
            for i in range(br):
                row_entries = []
                for j in range(bc):
                    e = Entry(frame_b, width=3, font=("Poppins Medium", 8), fg="#213448")
                    e.grid(row=i, column=j, padx=3, pady=3)
                    row_entries.append(e)
                self.entries_b.append(row_entries)

        back_btn = Button(self.root, text="Back", font=("Poppins Medium", 12), fg = "#213448", width=9, command=self.show_matrix_size_input)
        compute_btn = Button(self.root, text="Compute", font=("Poppins Medium", 12), fg = "#213448", width=9, command=lambda: self.compute_result(ar, ac, br, bc))
        home_btn = Button(self.root, text="Home", font=("Poppins Medium", 12), fg = "#213448", width=9, command=self.show_main_menu)
        self.canvas.create_window(115, 540, window=back_btn)
        self.canvas.create_window(260, 540, window=compute_btn)
        self.canvas.create_window(405, 540, window=home_btn)

        self.footer()

    # COMPUTE EACH OPERATIONS
    def compute_result(self, ar, ac, br, bc):
        try:
            A = [[float(e.get()) for e in row] for row in self.entries_a]
            B = [[float(e.get()) for e in row] for row in self.entries_b] if self.operation != "Determinant" else None
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return

        def add(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        def sub(A, B): return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        def mul(A, B):
            result = [[0] * len(B[0]) for _ in range(len(A))]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]
            return result
        def det(M):
            if len(M) == 1:
                return M[0][0]
            if len(M) == 2:
                return M[0][0] * M[1][1] - M[0][1] * M[1][0]
            total = 0
            for i in range(len(M)):
                submatrix = [row[:i] + row[i + 1:] for row in M[1:]]
                total += ((-1) ** i) * M[0][i] * det(submatrix)
            return total

        if self.operation == "Addition":
            result = add(A, B)
        elif self.operation == "Subtraction":
            result = sub(A, B)
        elif self.operation == "Multiplication":
            result = mul(A, B)
        elif self.operation == "Determinant":
            result = det(A)

        if isinstance(result, list):
            result_text = "\n".join(["  ".join(map(str, row)) for row in result])
        else:
            result_text = str(result)

        # SHOW COMPUTED RESULT
        self.result_label = Label(self.root, text=f"Result:\n{result_text}", font=("Poppins Medium", 10), bg="#ECEFCA", fg="#213448", justify="center")
        self.canvas.create_window(260, 400, window=self.result_label)

if __name__ == "__main__":
    root = Tk()
    app = MatrixCalculator(root)
    root.mainloop()