print("=" * 50)
print("Selamat datang di program kesehatan!")
print("Menghitung Indeks Massa Tubuh (#BMI)")
print   ("-----------------------------------") 
nama = input("Masukkan nama: ")
gender = input("Masukkan gender (L/P): ")
umur = int(input("Masukkan umur: "))

berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))
bmi = berat / (tinggi ** 2)
print("=" * 50)
print(f"BMI Anda: {bmi:.2f}")
print("=" * 50)
if bmi < 18.5:
    status = "Underweight (Kurus)"
elif 18.5 <= bmi < 24.9:
    status = "Normal (Ideal)"
elif 25.0 <= bmi < 29.9:
    status = "Overweight (Gemuk)"
else:
    status = "Obese (Sangat Gemuk)"
print(f"Status BMI Anda: {status}")
print("\n--- Saran Kesehatan ---")
print("=" * 50)
if bmi < 18.5:
    print("Pola Makan: Tingkatkan asupan kalori dengan makanan bergizi seimbang")
    print("Aktivitas: Lakukan latihan beban untuk membangun massa otot")
    print("Olahraga: Kombinasikan cardio ringan dengan strength training 3-4x seminggu")
    print("Saran Lain: Konsultasikan dengan ahli gizi untuk program nutrisi khusus")
elif 18.5 <= bmi < 24.9:
    print("Pola Makan: Pertahankan pola makan sehat dan seimbang")
    print("Aktivitas: Lanjutkan aktivitas fisik rutin untuk menjaga kesehatan")
    print("Olahraga: Olahraga 150 menit per minggu (walking, jogging, cycling)")
    print("Saran Lain: Terus jaga berat badan ideal dan gaya hidup sehat")
elif 25.0 <= bmi < 29.9:
    print("Pola Makan: Kurangi makanan tinggi lemak dan gula, perbanyak sayur-buahan")
    print("Aktivitas: Tingkatkan aktivitas harian seperti berjalan kaki")
    print("Olahraga: Lakukan olahraga rutin 30 menit sehari, 5 hari seminggu")
    print("Saran Lain: Kontrol porsi makan dan hindari makanan cepat saji")
else:
    print("Pola Makan: Ikuti diet ketat dengan supervisor ahli gizi profesional")
    print("Aktivitas: Mulai dengan aktivitas ringan dan tingkatkan secara bertahap")
    print("Olahraga: Konsultasikan dengan dokter sebelum memulai program olahraga")
    print("Saran Lain: Segera periksakan diri ke dokter untuk evaluasi kesehatan menyeluruh")

print("=" * 50)