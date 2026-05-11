import tkinter as tk
from tkinter import messagebox, ttk
import os

# --- MATEMATİKSEL FONKSİYONLAR ---
def asal_mi(n):
    """Bir sayının asal olup olmadığını kontrol eder."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def obeb(a, b):
    """En Büyük Ortak Bölen hesaplar."""
    while b:
        a, b = b, a % b
    return a

def mod_tersi(e, phi):
    """Genişletilmiş Öklid Algoritması ile modüler ters hesaplar."""
    m0 = phi
    y, x = 0, 1
    if phi == 1:
        return 0
    while e > 1:
        q = e // phi
        t = phi
        phi = e % phi
        e = t
        t = y
        y = x - q * y
        x = t
    if x < 0:
        x = x + m0
    return x

# --- UYGULAMA SINIFI ---
class KriptoCuzdanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sayı Teorisi Kripto-Cüzdan Simülasyonu")
        self.root.geometry("650x750")

        # Cüzdan Anahtar Hafızası
        self.cuzdan_A = {}
        self.cuzdan_B = {}

        self.create_widgets()

    def create_widgets(self):
        # Başlık
        lbl_baslik = tk.Label(self.root, text="Sayı Teorisi Kripto-Cüzdan Simülasyonu", font=("Arial", 14, "bold"))
        lbl_baslik.pack(pady=10)

        # Rehber Not
        lbl_not = tk.Label(self.root, text="Öneri Küçük Asallar: (11, 13), (17, 19), (61, 53)", font=("Arial", 9, "italic"), fg="gray")
        lbl_not.pack()

        # --- 1. ADIM: ANAHTAR ÜRETİMİ ---
        frame_anahtar = tk.LabelFrame(self.root, text=" Adım 1: Cüzdan Anahtar Çifti Üretimi ", padx=10, pady=10)
        frame_anahtar.pack(fill="x", padx=15, pady=5)

        tk.Label(frame_anahtar, text="Asal Sayı p:").grid(row=0, column=0, sticky="w")
        self.ent_p = tk.Entry(frame_anahtar, width=8)
        self.ent_p.grid(row=0, column=1, padx=5)

        tk.Label(frame_anahtar, text="Asal Sayı q:").grid(row=0, column=2, sticky="w")
        self.ent_q = tk.Entry(frame_anahtar, width=8)
        self.ent_q.grid(row=0, column=3, padx=5)

        btn_uret = tk.Button(frame_anahtar, text="Anahtarları Hesapla", command=self.anahtar_hesapla, bg="#4CAF50", fg="white")
        btn_uret.grid(row=0, column=4, padx=10)

        # --- İŞLEM LOGU ---
        frame_log = tk.LabelFrame(self.root, text=" Matematiksel İşlem Adımları ", padx=10, pady=5)
        frame_log.pack(fill="x", padx=15, pady=5)

        self.txt_log = tk.Text(frame_log, height=10, width=70, font=("Courier", 9))
        self.txt_log.pack()

        # --- 2. ADIM: İŞLEM GÖNDERİMİ ---
        frame_islem = tk.LabelFrame(self.root, text=" Adım 2: Dijital İmza ve Gönderim ", padx=10, pady=10)
        frame_islem.pack(fill="x", padx=15, pady=5)

        tk.Label(frame_islem, text="Sayısal Veri (M):").grid(row=0, column=0, sticky="w")
        self.ent_mesaj = tk.Entry(frame_islem, width=15)
        self.ent_mesaj.grid(row=0, column=1, padx=5, pady=5)

        btn_gonder = tk.Button(frame_islem, text="İmzala ve Gönder", command=self.islem_gonder, bg="#2196F3", fg="white")
        btn_gonder.grid(row=0, column=2, padx=5)

        # --- 3. ADIM: DOĞRULAMA ---
        frame_ekran = tk.LabelFrame(self.root, text=" Adım 3: Alıcı Cüzdan Doğrulaması ", padx=10, pady=10)
        frame_ekran.pack(fill="both", expand=True, padx=15, pady=10)

        self.lbl_gonderilen = tk.Label(frame_ekran, text="Gönderilen Ham Veri: -", font=("Arial", 10))
        self.lbl_gonderilen.pack(anchor="w")

        self.lbl_imza = tk.Label(frame_ekran, text="Dijital İmza (S): -", font=("Arial", 10, "bold"), fg="darkblue")
        self.lbl_imza.pack(anchor="w", pady=2)

        self.lbl_dogrulama = tk.Label(frame_ekran, text="Doğrulama Durumu: Bekleniyor...", font=("Arial", 11, "bold"), fg="orange")
        self.lbl_dogrulama.pack(anchor="w", pady=5)

    def anahtar_hesapla(self):
        try:
            p_val = self.ent_p.get()
            q_val = self.ent_q.get()

            if not p_val.isdigit() or not q_val.isdigit():
                raise ValueError("Lütfen sadece pozitif tam sayılar girin.")

            p, q = int(p_val), int(q_val)

            # --- ASALLIK KONTROLÜ ---
            p_asal = asal_mi(p)
            q_asal = asal_mi(q)

            if not p_asal or not q_asal:
                uyari_msg = ""
                if not p_asal: uyari_msg += f"p={p} asal değil!\n"
                if not q_asal: uyari_msg += f"q={q} asal değil!"
                messagebox.showwarning("Asal Sayı Hatası", uyari_msg + "\n\nLütfen RSA için asal sayılar seçin.")
                return

            if p == q:
                raise ValueError("p ve q değerleri birbirinden farklı olmalıdır.")

            n = p * q
            phi = (p - 1) * (q - 1)

            # e seçimi
            e = 3
            while e < phi:
                if obeb(e, phi) == 1:
                    break
                e += 2

            if e >= phi:
                raise ValueError("Uygun bir 'e' değeri bulunamadı.")

            d = mod_tersi(e, phi)

            # Verileri kaydet
            self.cuzdan_A = {"public": (e, n), "private": (d, n)}
            
            # Log ekranını güncelle
            self.txt_log.delete("1.0", tk.END)
            self.txt_log.insert(tk.END, f"MODÜL (n): {n}\n")
            self.txt_log.insert(tk.END, f"PHI (φ): {phi}\n")
            self.txt_log.insert(tk.END, f"AÇIK ÜS (e): {e}\n")
            self.txt_log.insert(tk.END, f"GİZLİ ÜS (d): {d}\n")
            self.txt_log.insert(tk.END, f"---------------------------\n")
            self.txt_log.insert(tk.END, f"Açık Anahtar: ({e}, {n})\n")
            self.txt_log.insert(tk.END, f"Gizli Anahtar: ({d}, {n})")

            messagebox.showinfo("Başarılı", "Anahtar çifti başarıyla oluşturuldu!")

        except ValueError as err:
            messagebox.showerror("Hata", str(err))

    def islem_gonder(self):
        if not self.cuzdan_A:
            messagebox.showwarning("Uyarı", "Önce anahtarları üretmelisiniz!")
            return

        try:
            mesaj_str = self.ent_mesaj.get()
            if not mesaj_str.isdigit():
                raise ValueError("Lütfen sayısal bir miktar girin.")

            M = int(mesaj_str)
            e, n = self.cuzdan_A["public"]
            d, _ = self.cuzdan_A["private"]

            if M >= n:
                raise ValueError(f"Veri (M), modül n={n} değerinden küçük olmalıdır.")

            # İmzala: S = M^d mod n
            S = pow(M, d, n)
            self.lbl_gonderilen.config(text=f"Gönderilen Ham Veri: {M}")
            self.lbl_imza.config(text=f"Dijital İmza (S = M^d mod n): {S}")

            # Doğrula: M' = S^e mod n
            M_dogrulanan = pow(S, e, n)

            if M_dogrulanan == M:
                self.lbl_dogrulama.config(text="✓ Doğrulama Başarılı! İmza Sahibi Onaylandı.", fg="green")
            else:
                self.lbl_dogrulama.config(text="X Doğrulama Başarısız!", fg="red")

        except ValueError as err:
            messagebox.showerror("Hata", str(err))

if __name__ == "__main__":
    if 'DISPLAY' in os.environ or os.name == 'nt':
        root = tk.Tk()
        app = KriptoCuzdanApp(root)
        root.mainloop()
    else:
        print("Grafik arayüz desteği bulunamadı.")