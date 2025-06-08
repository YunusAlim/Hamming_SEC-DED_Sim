import tkinter as tk
from tkinter import ttk, messagebox
from hamming_core import HammingCore

class HammingSECDEDSimulator:
    def __init__(self, root):
        # Ana pencere set
        self.root = root
        self.root.title("Hamming SEC-DED Code Simulator - BLM230")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')

        # Hamming core  başlat
        self.hamming = HammingCore()
        self.setup_ui()

    def setup_ui(self):
        # Başlık 
        title_frame = tk.Frame(self.root, bg='#f0f0f0')
        title_frame.pack(pady=10)

        tk.Label(title_frame, text="Hamming SEC-DED Code Simulator",
                 font=('Arial', 16, 'bold'), bg='#f0f0f0').pack()
        tk.Label(title_frame, text="Single-Error-Correcting, Double-Error-Detecting",
                 font=('Arial', 10), bg='#f0f0f0', fg='gray').pack()

        #  boyut seçim 
        size_frame = tk.LabelFrame(self.root, text="Data Size Selection",
                                   font=('Arial', 12, 'bold'), bg='#f0f0f0')
        size_frame.pack(pady=10, padx=20, fill='x')

        self.size_var = tk.IntVar(value=8)
        for size in [8, 16, 32]:
            tk.Radiobutton(size_frame, text=f"{size} bits", variable=self.size_var,
                           value=size, command=self.on_size_change,
                           bg='#f0f0f0', font=('Arial', 10)).pack(side='left', padx=20, pady=10)

        # Veri giriş 
        input_frame = tk.LabelFrame(self.root, text="Data Input",
                                    font=('Arial', 12, 'bold'), bg='#f0f0f0')
        input_frame.pack(pady=10, padx=20, fill='x')

        tk.Label(input_frame, text="Enter binary data:", bg='#f0f0f0').pack(anchor='w', padx=10, pady=5)

        input_sub_frame = tk.Frame(input_frame, bg='#f0f0f0')
        input_sub_frame.pack(fill='x', padx=10, pady=5)

        self.data_entry = tk.Entry(input_sub_frame, font=('Courier', 12), width=40)
        self.data_entry.pack(side='left', padx=(0, 10))

        # Veri giriş butonları
        tk.Button(input_sub_frame, text="Generate Random",
                  command=self.generate_random_data, bg='#e0e0e0').pack(side='left', padx=5)
        tk.Button(input_sub_frame, text="Encode & Store",
                  command=self.encode_and_store, bg='#4CAF50', fg='white').pack(side='left', padx=5)

        # Hata sim 
        error_frame = tk.LabelFrame(self.root, text="📡 Error Simulation & Correction",
                                    font=('Arial', 12, 'bold'), bg='#f0f0f0')
        error_frame.pack(pady=10, padx=20, fill='x')

        error_buttons_frame = tk.Frame(error_frame, bg='#f0f0f0')
        error_buttons_frame.pack(fill='x', padx=5, pady=5)

        # Hata butonları
        tk.Button(error_buttons_frame, text="⚡ Single Bit Error",
                  command=self.introduce_single_error, bg='#FF9800', fg='white',
                  font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(error_buttons_frame, text="💥 Double Bit Error",
                  command=self.introduce_double_error, bg='#F44336', fg='white',
                  font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(error_buttons_frame, text="🔍 Detect & Correct",
                  command=self.detect_and_correct, bg='#9C27B0', fg='white',
                  font=('Arial', 10, 'bold')).pack(side='left', padx=5)

        # Sonuçlar
        results_frame = tk.LabelFrame(self.root, text="📋 Analysis Results",
                                      font=('Arial', 12, 'bold'), bg='#f0f0f0')
        results_frame.pack(pady=10, padx=20, fill='x')

        self.results_text = tk.Text(results_frame, height=10, font=('Courier', 10),
                                    bg='#f9f9f9', wrap='word')
        results_scrollbar = tk.Scrollbar(results_frame, orient='vertical', command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=results_scrollbar.set)

        self.results_text.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        results_scrollbar.pack(side='right', fill='y', pady=5)

        # Durum 
        self.status_label = tk.Label(self.root, text="🟢 Ready", font=('Arial', 10),
                                     bg='#f0f0f0', fg='green')
        self.status_label.pack(pady=5)

    def update_status(self, status, color='green'):
        # Durum  güncelle
        self.status_label.config(text=f"🟢 {status}", fg=color)

    def on_size_change(self):
        #  boyut değiştiğinde hafızayı temizle
        self.hamming.set_size(self.size_var.get())
        self.data_entry.delete(0, tk.END)
        self.update_display()

    def generate_random_data(self):
        # Rastgele binary veri 
        size = self.size_var.get()
        random_data = self.hamming.generate_random_data(size)
        self.data_entry.delete(0, tk.END)
        self.data_entry.insert(0, random_data)

    def encode_and_store(self):
        # Veriyi kodla kaydet
        data = self.data_entry.get().strip()
        success, message = self.hamming.encode_and_store(data)
        
        if not success:
            messagebox.showerror("Error", message)
            return

        self.update_display()
        self.update_status("Data encoded successfully", 'green')

    def update_display(self):
        # Ekranı güncelle
        self.results_text.delete('1.0', tk.END)
        
        current_code = self.hamming.get_current_code()
        if not current_code:
            self.results_text.insert('1.0', "No data encoded yet.\nPlease enter binary data and click 'Encode & Store'.")
            return

        # Mevcut kod durum
        result = "📊 CURRENT CODE STATUS\n"
        result += "=" * 40 + "\n\n"
        result += f"Original Data: {current_code['original']}\n"
        result += f"Encoded Data:  {current_code['encoded']}\n"
        result += f"Current Data:  {current_code['current']}\n\n"

        if current_code['current'] != current_code['encoded']:
            result += "⚠️ Status: DATA MODIFIED (Possible errors)\n"
        else:
            result += "✅ Status: DATA INTACT (No errors)\n"

        self.results_text.insert('1.0', result)

    def introduce_single_error(self):
        # Tek bit hata 
        success, message = self.hamming.introduce_single_error()
        if not success:
            messagebox.showwarning("Warning", message)
            return

        self.update_display()
        self.update_status(message, 'orange')

    def introduce_double_error(self):
        # Çift bit hata 
        success, message = self.hamming.introduce_double_error()
        if not success:
            messagebox.showwarning("Warning", message)
            return

        self.update_display()
        self.update_status(message, 'orange')

    def detect_and_correct(self):
        #  tespit et ve düzelt
        success, result = self.hamming.detect_and_correct()
        if not success:
            messagebox.showwarning("Warning", result)
            return

        # Sonuçları göster
        display_result = "🔍 ERROR DETECTION & CORRECTION\n"
        display_result += "=" * 40 + "\n\n"
        display_result += f"Current Data: {result['current_data']}\n"
        display_result += f"Status: {result['status']}\n\n"
        display_result += f"Syndrome: {result['syndrome']} (binary: {bin(result['syndrome'])[2:]})\n\n"

        if "Single error detected" in result['status']:
            display_result += f"Error Position: {result['error_position']}\n"
            display_result += f"Corrected Data: {result['corrected_data']}\n"
            display_result += f"Corrected Decoded: {result['corrected_decoded']}\n"

            if messagebox.askyesno("Apply Correction", "Apply the correction?"):
                success, message = self.hamming.apply_correction()
                if success:
                    self.update_display()
                    self.update_status("Error corrected successfully", 'green')
                    display_result += "\n✅ Correction applied successfully"
                else:
                    display_result += f"\n❌ {message}"
            else:
                display_result += "\n⏸️ Correction not applied (user choice)"
        elif "Double error detected" in result['status']:
            display_result += "❌ Double error detected - cannot be corrected\n"
            display_result += "💡 Suggestion: Request data retransmission"
            self.update_status("Double error detected - uncorrectable", 'red')
        else:
            display_result += "✅ No errors detected"
            self.update_status("No errors detected", 'green')

        self.results_text.delete('1.0', tk.END)
        self.results_text.insert('1.0', display_result)

def main():
    # başlat
    root = tk.Tk()
    app = HammingSECDEDSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
