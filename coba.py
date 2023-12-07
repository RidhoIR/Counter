import tkinter as tk
from redis import StrictRedis

# Inisialisasi koneksi Redis
redis_conn = StrictRedis(host='localhost', port=6379, db=0)

class CounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Counter App")

        # Mendapatkan nilai awal dari Redis atau menggunakan nilai default 0
        initial_count = int(redis_conn.get("counter") or 0)

        # Menggunakan Tkinter IntVar untuk menyimpan nilai Counter
        self.counter_var = tk.IntVar(value=initial_count)

        # Membuat label dan tombol di GUI
        self.label = tk.Label(master, textvariable=self.counter_var, font=('Arial', 24))
        self.label.pack(pady=20)

        self.increment_button = tk.Button(master, text="Increment", command=self.increment_counter)
        self.increment_button.pack(pady=10)

        self.decrement_button = tk.Button(master, text="Decrement", command=self.decrement_counter)
        self.decrement_button.pack(pady=10)

        # Menyimpan nilai Counter ke Redis setiap kali nilai berubah
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def increment_counter(self):
        self.counter_var.set(self.counter_var.get() + 1)
        self.update_redis_counter()

    def decrement_counter(self):
        self.counter_var.set(self.counter_var.get() - 1)
        self.update_redis_counter()

    def update_redis_counter(self):
        redis_conn.set("counter", self.counter_var.get())

    def on_closing(self):
        # Menyimpan nilai Counter ke Redis sebelum menutup aplikasi
        self.update_redis_counter()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
