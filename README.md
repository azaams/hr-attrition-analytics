# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah sebuah perusahaan berskala nasional yang bergerak di bidang *Edutech*. Walaupun terus berkembang pesat, perusahaan saat ini menghadapi permasalahan serius yaitu tingginya tingkat keluar masuk karyawan (*Attrition Rate*) yang mencapai lebih dari 16%. Fenomena ini merugikan perusahaan karena proses rekrutmen, orientasi, dan pelatihan karyawan baru memakan waktu serta anggaran yang sangat besar, yang pada akhirnya dapat menghambat pertumbuhan dan efisiensi operasional bisnis.

### Permasalahan Bisnis

Berdasarkan latar belakang di atas, permasalahan bisnis yang akan diselesaikan adalah:
1. Apa saja faktor-faktor utama yang menyebabkan karyawan memutuskan untuk keluar (*resign*) dari perusahaan?
2. Bagaimana cara memprediksi karyawan mana yang memiliki risiko tinggi untuk meninggalkan perusahaan di masa depan sehingga tindakan pencegahan dapat dilakukan lebih awal?
3. Bagaimana menyajikan data faktor-faktor *attrition* ini ke dalam sebuah visualisasi yang mudah dipantau oleh manajer HR?

### Cakupan Proyek
Cakupan proyek yang akan dikerjakan meliputi:
1. **Data Pembersihan & Persiapan:** Menangani nilai kosong (*missing values*) pada target variabel dan menghapus fitur yang tidak relevan.
2. **Exploratory Data Analysis (EDA):** Menganalisis distribusi data dan ketidakseimbangan kelas (*class imbalance*).
3. **Membangun Model Machine Learning:** Membuat *Pipeline* klasifikasi menggunakan algoritma *Tree-based* (Random Forest dan Gradient Boosting) serta melakukan *Hyperparameter Tuning* dengan `GridSearchCV`.
4. **Evaluasi Model & Ekstraksi Fitur:** Menggunakan metrik evaluasi yang kebal terhadap *imbalanced data* (ROC-AUC) dan mengekstrak *Feature Importance*.
5. **Pembuatan Script Deployment:** Membangun berkas `prediction.py` untuk inferensi/prediksi data karyawan baru.
6. **Pembuatan Business Dashboard:** Membangun *dashboard* interaktif untuk *monitoring* HR menggunakan Tableau.

### Persiapan

Sumber data: [Dataset Employee Jaya Jaya Maju (CSV)](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/employee/employee_data.csv)

Setup environment:

```
# 1. Pastikan Anda memiliki Python 3.9 atau lebih baru.
# 2. Instal semua library yang dibutuhkan menggunakan pip:
pip install pandas numpy scikit-learn matplotlib seaborn joblib

# 3. Menjalankan skrip prediksi (setelah model dilatih melalui notebook):
python prediction.py
```

## Business Dashboard

Business Dashboard telah dibuat menggunakan Tableau Public untuk memudahkan Manajer HR dalam memantau persebaran attrition karyawan. Dashboard ini menampilkan rasio attrition secara keseluruhan dan menyoroti tiga faktor penyebab utama yang ditemukan oleh model Machine Learning, yaitu: perbandingan rata-rata Gaji Bulanan, distribusi Usia Karyawan, dan pengaruh Jam Lembur (OverTime).

Tautan untuk mengakses dashboard tersebut: [Business Dashboard](https://public.tableau.com/app/profile/azzam.mujahid/viz/HRAttrition_17721994843030/Dashboard1?publish=yes)

## Conclusion

Berdasarkan keseluruhan proyek yang dikerjakan, dapat ditarik kesimpulan sebagai berikut:

1. Model Prediksi: Algoritma Gradient Boosting Classifier terpilih sebagai model terbaik dengan skor evaluasi Cross-Validation ROC-AUC sebesar 0.7858 dan Test ROC-AUC sebesar 0.8046. Model ini sangat andal untuk digunakan perusahaan dalam memprediksi status karyawan.

2. Faktor Utama Attrition: Berdasarkan Feature Importance dari model, 4 faktor yang paling mendominasi keputusan karyawan untuk resign adalah Gaji Bulanan (MonthlyIncome), Usia (Age), Kepemilikan Opsi Saham (StockOptionLevel), dan Intensitas Lembur (OverTime).

3. Wawasan Visual: Dari dashboard terbukti bahwa karyawan yang disuruh lembur memiliki tingkat attrition yang sangat tinggi (mencapai ~32% atau 98 dari 307 karyawan) dibandingkan yang tidak lembur (~10%). Selain itu, rata-rata pendapatan bulanan karyawan yang keluar (~4.873) secara signifikan lebih rendah dari mereka yang bertahan (~6.983).

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

1. Evaluasi dan Kurangi Jam Lembur: Departemen HR harus mengkaji ulang distribusi beban kerja. Mengurangi jam lembur (OverTime) sangat krusial karena data membuktikan lembur menjadi pemicu burnout dan tingginya angka resign.

2. Penyesuaian Kompensasi Finansial: Lakukan riset pasar untuk menyesuaikan standar Gaji Bulanan (Monthly Income), terutama untuk level staf bawah, agar setidaknya mendekati rata-rata gaji karyawan yang bertahan.

3. Pemberian Opsi Saham (Stock Option): Pertimbangkan untuk memberikan paket stock option atau bagi hasil kepada karyawan berprestasi untuk menumbuhkan rasa kepemilikan dan mengikat mereka secara jangka panjang.

4. Program Retensi Karyawan Muda: Karena karyawan di usia muda (20-30 tahun) menunjukkan tingkat attrition terbanyak, buatlah program pengembangan karier atau mentorship khusus agar mereka melihat peluang masa depan yang jelas di perusahaan.