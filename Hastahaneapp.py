from tkinter import Tk, Label, Entry, Button, Listbox, END, Toplevel, messagebox, StringVar
import sqlite3

# Veritabanı bağlantısı
def connect_db():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        ailment TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        patient_id INTEGER NOT NULL,
                        doctor_name TEXT NOT NULL,
                        appointment_date TEXT NOT NULL,
                        FOREIGN KEY(patient_id) REFERENCES patients(id)
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS doctors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        specialty TEXT NOT NULL
                    )''')
    conn.commit()
    return conn, cursor

conn, cursor = connect_db()

# Hasta ekleme işlemi
def add_patient():
    name = entry_name.get()
    age = entry_age.get()
    ailment = entry_ailment.get()

    if name and age and ailment:
        cursor.execute("INSERT INTO patients (name, age, ailment) VALUES (?, ?, ?)", (name, age, ailment))
        conn.commit()
        entry_name.delete(0, END)
        entry_age.delete(0, END)
        entry_ailment.delete(0, END)
        status_label.config(text="Hasta başarıyla eklendi!", fg="green")
    else:
        status_label.config(text="Tüm alanları doldurun!", fg="red")

# Hastaları listeleme işlemi
def list_patients():
    list_window = Toplevel(root)
    list_window.title("Hastalar Listesi")
    list_window.configure(bg="#557a99")
    
    listbox = Listbox(list_window, width=50, height=20, bg="#cce0f5", fg="#002b5e")
    listbox.pack()

    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()

    for patient in patients:
        listbox.insert(END, f"ID: {patient[0]}, İsim: {patient[1]}, Yaş: {patient[2]}, Hastalık: {patient[3]}")

# Randevu ekleme işlemi
def add_appointment():
    patient_id = entry_patient_id.get()
    doctor_name = entry_doctor.get()
    appointment_date = entry_date.get()

    if patient_id and doctor_name and appointment_date:
        cursor.execute("INSERT INTO appointments (patient_id, doctor_name, appointment_date) VALUES (?, ?, ?)",
                       (patient_id, doctor_name, appointment_date))
        conn.commit()
        entry_patient_id.delete(0, END)
        entry_doctor.delete(0, END)
        entry_date.delete(0, END)
        status_label.config(text="Randevu başarıyla eklendi!", fg="green")
    else:
        status_label.config(text="Tüm alanları doldurun!", fg="red")

# Doktor ekleme işlemi
def add_doctor():
    doctor_name = entry_doctor_name.get()
    specialty = entry_specialty.get()

    if doctor_name and specialty:
        cursor.execute("INSERT INTO doctors (name, specialty) VALUES (?, ?)", (doctor_name, specialty))
        conn.commit()
        entry_doctor_name.delete(0, END)
        entry_specialty.delete(0, END)
        status_label.config(text="Doktor başarıyla eklendi!", fg="green")
    else:
        status_label.config(text="Tüm alanları doldurun!", fg="red")

# Doktorları listeleme
def list_doctors():
    list_window = Toplevel(root)
    list_window.title("Doktorlar Listesi")
    list_window.configure(bg="#557a99")

    listbox = Listbox(list_window, width=50, height=20, bg="#cce0f5", fg="#002b5e")
    listbox.pack()

    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()

    for doctor in doctors:
        listbox.insert(END, f"ID: {doctor[0]}, İsim: {doctor[1]}, Uzmanlık: {doctor[2]}")

# Ana pencere
def main_window():
    global root, entry_name, entry_age, entry_ailment, entry_patient_id, entry_doctor, entry_date
    global entry_doctor_name, entry_specialty, status_label

    root = Tk()
    root.title("Hastane Yönetim Sistemi")
    root.configure(bg="#6699cc")

    # Hasta ekleme formu
    Label(root, text="Hasta Adı:", bg="#6699cc", fg="#ffffff").grid(row=0, column=0, padx=10, pady=5)
    entry_name = Entry(root, bg="#cce0f5", fg="#002b5e")
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    Label(root, text="Hasta Yaşı:", bg="#6699cc", fg="#ffffff").grid(row=1, column=0, padx=10, pady=5)
    entry_age = Entry(root, bg="#cce0f5", fg="#002b5e")
    entry_age.grid(row=1, column=1, padx=10, pady=5)

    Label(root, text="Hastalık:", bg="#6699cc", fg="#ffffff").grid(row=2, column=0, padx=10, pady=5)
    entry_ailment = Entry(root, bg="#cce0f5", fg="#002b5e")
    entry_ailment.grid(row=2, column=1, padx=10, pady=5)

    Button(root, text="Hasta Ekle", bg="#004080", fg="white", command=add_patient).grid(row=3, column=0, pady=10)
    Button(root, text="Hastaları Listele", bg="#003366", fg="white", command=list_patients).grid(row=3, column=1, pady=10)

    # Randevu ekleme formu
    Label(root, text="Hasta ID:", bg="#6699cc", fg="#ffffff").grid(row=4, column=0, padx=10, pady=5)
    entry_patient_id = Entry(root, bg="#cce0f5", fg="#002b5e")
    entry_patient_id.grid(row=4, column=1, padx=10, pady=5)

    Label(root, text="Doktor Adı:", bg="#6699cc", fg="#ffffff").grid(row=5, column=0, padx=10, pady=5)
    entry_doctor = Entry(root, bg="#cce0f5", fg="#002b5e")
    entry_doctor.grid(row=5, column=1, padx=10, pady=5)

    Label(root, text="Randevu Tarihi:", bg="#6699cc", fg="#ffffff").grid(row=6, column=0, padx=10, pady=5)
    entry_date = Entry(root, bg="#cce0f5", fg="#002b5e")
    entry_date.grid(row=6, column=1, padx=10, pady=5)

    Button(root, text="Randevu Ekle", bg="#004080", fg="white", command=add_appointment).grid(row=7, column=0, pady=10)
    Button(root, text="Randevuları Listele", bg="#003366", fg="white").grid(row=7, column=1, pady=10)

    # Doktor ekleme formu
    Label(root, text="Doktor Adı:", bg="#6699cc", fg="#ffffff").grid(row=8, column=0, padx=10, pady=5)
    entry_doctor_name = Entry(root, bg="#cce0f5", fg="#002b5e")
    entry_doctor_name.grid(row=8, column=1, padx=10, pady=5)

    Label(root, text="Uzmanlık Alanı:", bg="#6699cc", fg="#ffffff").grid(row=9, column=0, padx=10, pady=5)
    entry_specialty = Entry(root, bg="#cce0f5", fg="#002b5e")
    entry_specialty.grid(row=9, column=1, padx=10, pady=5)

    Button(root, text="Doktor Ekle", bg="#004080", fg="white", command=add_doctor).grid(row=10, column=0, pady=10)
    Button(root, text="Doktorları Listele", bg="#003366", fg="white", command=list_doctors).grid(row=10, column=1, pady=10)

    # Durum mesajı
    status_label = Label(root, text="", bg="#6699cc")
    status_label.grid(row=11, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_window()
