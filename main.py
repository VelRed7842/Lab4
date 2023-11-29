import tkinter as tk

class NewtonInterpolation:
    def __init__(self):
        self.x = []
        self.y = []
        self.n = 0
        self.coefficients = []

    def calculate_coefficients(self):
        self.n = len(self.x)
        self.coefficients = [self.y]

        for i in range(1, self.n):
            next_row = []
            for j in range(self.n - i):
                delta_y = self.coefficients[i - 1][j + 1] - self.coefficients[i - 1][j]
                delta_x = self.x[j + i] - self.x[j]
                next_row.append(delta_y / delta_x)
            self.coefficients.append(next_row)

    def interpolate(self, x_value):
        result = self.coefficients[0][0]
        for i in range(1, self.n):
            term = self.coefficients[i][0]
            for j in range(i):
                term *= (x_value - self.x[j])
            result += term
        return result

    def clear_data(self):
        self.x = []
        self.y = []
        self.n = 0
        self.coefficients = []

def calculate():
    x_values = list(map(float, x_entry.get().split()))
    y_values = list(map(float, y_entry.get().split()))
    x_interpolate = float(x_interpolate_entry.get())

    newton_interpolation.clear_data()
    newton_interpolation.x = x_values
    newton_interpolation.y = y_values
    newton_interpolation.calculate_coefficients()
    result = newton_interpolation.interpolate(x_interpolate)

    result_label.config(text=f"Вологость ґрунту о {x_interpolate} годині: {result}")

app = tk.Tk()
app.title("Newton Interpolation Calculator")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

x_label = tk.Label(frame, text="Години вимірювань (через пробіл):")
x_label.pack()
x_entry = tk.Entry(frame)
x_entry.pack()

y_label = tk.Label(frame, text="Відсоток вологості (через пробіл):")
y_label.pack()
y_entry = tk.Entry(frame)
y_entry.pack()

x_interpolate_label = tk.Label(frame, text="Година для інтерполяції:")
x_interpolate_label.pack()
x_interpolate_entry = tk.Entry(frame)
x_interpolate_entry.pack()

calculate_button = tk.Button(frame, text="Розрахувати", command=calculate)
calculate_button.pack()

result_label = tk.Label(frame, text="")
result_label.pack()

newton_interpolation = NewtonInterpolation()

app.mainloop()