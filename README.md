# HR Employee Attrition Analysis & Prediction

Proyek analisis data HR end-to-end yang berfokus pada pemahaman pola **employee attrition**, identifikasi faktor yang berkaitan dengan turnover karyawan, pembangunan model prediksi attrition, serta penyajian insight melalui dashboard interaktif menggunakan Tableau.

## Project Overview

Employee attrition dapat menimbulkan biaya operasional yang signifikan bagi perusahaan melalui proses rekrutmen, onboarding, dan pelatihan karyawan. Proyek ini menganalisis data karyawan untuk memahami pola attrition dan mengidentifikasi faktor-faktor yang berkaitan dengan karyawan yang meninggalkan perusahaan.

Proyek ini mencakup:

* Exploratory Data Analysis (EDA)
* Data cleaning dan data preparation
* Machine Learning classification
* Model evaluation dan feature importance
* Employee attrition prediction
* Tableau Business Intelligence dashboard

Tujuan akhir proyek adalah memberikan hasil analisis dan dashboard yang dapat membantu stakeholder HR dalam memantau serta memahami pola employee attrition.

## Business Questions

Proyek ini berfokus pada tiga pertanyaan utama:

1. Faktor apa saja yang paling berkaitan dengan employee attrition?
2. Apakah employee attrition dapat diprediksi berdasarkan karakteristik karyawan yang tersedia?
3. Bagaimana pola attrition dapat disajikan melalui dashboard interaktif untuk mendukung monitoring dan pengambilan keputusan HR?

## Dataset

Proyek ini menggunakan dataset **Employee Jaya Jaya Maju** yang disediakan oleh Dicoding.

Dataset berisi informasi tingkat karyawan yang mencakup karakteristik demografis, kompensasi, pekerjaan, dan status pekerjaan.

Dataset terdiri dari:

* **1.470 records**
* **35 columns**

Variabel target `Attrition` tersedia untuk **1.058 records**, yang digunakan untuk analisis attrition dan predictive modeling.

Sumber:

[Employee Jaya Jaya Maju Dataset](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/employee/employee_data.csv)

## Project Workflow

```text
Raw Employee Data
        │
        ▼
Data Cleaning & Preparation
        │
        ▼
Exploratory Data Analysis
        │
        ├───────────────┐
        ▼               ▼
Attrition Analysis   Class Imbalance
        │
        ▼
Machine Learning
        │
        ├── Random Forest
        └── Gradient Boosting
        │
        ▼
Hyperparameter Tuning
        │
        ▼
Model Evaluation
        │
        ▼
Feature Importance
        │
        ├───────────────┐
        ▼               ▼
Prediction Script   Tableau Dashboard
        │               │
        └───────┬───────┘
                ▼
        Business Insights
```

## Data Preparation

Tahapan data preparation yang dilakukan meliputi:

* Menangani missing value pada variabel target.
* Memisahkan data yang memiliki label `Attrition` dan data yang tidak memiliki label.
* Menghapus fitur yang dianggap tidak relevan untuk analisis.
* Mempersiapkan fitur numerik dan kategorikal untuk kebutuhan Machine Learning.
* Menerapkan `StandardScaler` pada variabel numerik.
* Menerapkan One-Hot Encoding pada variabel kategorikal.

Kolom berikut dihapus pada tahap data preparation:

* `EmployeeId`
* `EmployeeCount`
* `StandardHours`
* `Over18`

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) dilakukan untuk memahami:

* Distribusi attrition
* Class imbalance
* Karakteristik demografis karyawan
* Pola kompensasi
* Pola overtime
* Hubungan antara karakteristik karyawan dan attrition

Analisis secara khusus mencakup beberapa faktor berikut:

* Monthly Income
* Age
* Stock Option Level
* OverTime
* Job Role
* Department
* Gender

## Machine Learning

Dua algoritma klasifikasi berbasis tree dibandingkan dalam proyek ini:

* Random Forest
* Gradient Boosting

Kedua model diimplementasikan menggunakan preprocessing pipeline dan dievaluasi menggunakan metrik yang sesuai untuk permasalahan klasifikasi dengan class imbalance.

Hyperparameter tuning dilakukan menggunakan `GridSearchCV`.

### Model Evaluation

Gradient Boosting menghasilkan performa terbaik berdasarkan hasil evaluasi yang diperoleh:

| Metric                   | Gradient Boosting |
| ------------------------ | ----------------: |
| Cross-Validation ROC-AUC |            0.7858 |
| Test ROC-AUC             |            0.8046 |
| Test PR-AUC              |            0.5737 |

Model kemudian dipilih berdasarkan performa ROC-AUC.

> Catatan: Performa model merepresentasikan kemampuan prediksi pada data pengujian yang tersedia dan tidak dapat diartikan sebagai bukti bahwa variabel yang teridentifikasi secara kausal menyebabkan employee attrition.

## Feature Importance

Model mengidentifikasi beberapa variabel sebagai fitur yang memiliki tingkat kepentingan tinggi dalam prediksi:

1. `MonthlyIncome`
2. `Age`
3. `StockOptionLevel`
4. `OverTime`

Faktor-faktor tersebut kemudian menjadi bagian dari analisis bisnis dan dashboard.

## Tableau Business Dashboard

Dashboard interaktif dikembangkan menggunakan Tableau Public untuk membantu stakeholder HR memantau pola employee attrition.

### Dashboard KPIs

| KPI              |  Value |
| ---------------- | -----: |
| Total Employees  |  1,058 |
| Active Employees |    879 |
| Attrition Count  |    179 |
| Attrition Rate   | 16.92% |
| Average Age      |     37 |

### Dashboard Analysis

Dashboard menyediakan beberapa perspektif analisis employee attrition:

* Job Role Attrition
* Salary Gap by Role
* OverTime Impact
* Stock Option Impact
* Attrition by Age
* Attrition by Department
* Attrition by Gender

### Dashboard Preview

![HR Attrition Dashboard](dashboard/HR%20Attrition%20Dashboard.png)

### Live Dashboard

[View Interactive Tableau Dashboard](https://public.tableau.com/app/profile/azzam.mujahid/viz/HRAttrition_17721994843030/Dashboard1)

## Key Insights

Analisis menghasilkan beberapa pola utama yang perlu diperhatikan.

### 1. Attrition terjadi pada sebagian kecil dari total karyawan

Dari 1.058 karyawan yang memiliki label `Attrition`, terdapat **179 karyawan yang mengalami attrition**, dengan attrition rate sebesar **16,92%**.

### 2. Overtime berkaitan dengan tingkat attrition yang lebih tinggi

Karyawan yang bekerja overtime menunjukkan tingkat attrition yang lebih tinggi dibandingkan karyawan yang tidak bekerja overtime.

Oleh karena itu, overtime menjadi salah satu aspek yang penting untuk dimonitor dalam analisis employee retention.

### 3. Kompensasi merupakan salah satu faktor penting dalam analisis

`MonthlyIncome` merupakan salah satu fitur dengan tingkat importance yang tinggi dalam model prediksi.

Analisis juga menunjukkan adanya perbedaan rata-rata MonthlyIncome antara karyawan yang mengalami attrition dan karyawan yang tetap bekerja.

### 4. Age merupakan salah satu fitur penting

`Age` termasuk salah satu fitur dengan tingkat importance yang tinggi dalam model prediksi. Dashboard juga memberikan perspektif tambahan mengenai distribusi attrition berdasarkan usia karyawan.

### 5. Stock Option Level relevan dalam model prediksi

`StockOptionLevel` juga termasuk dalam fitur dengan tingkat importance yang tinggi. Hal ini menjadikan employee benefits dan incentive program sebagai salah satu aspek yang relevan untuk dipertimbangkan dalam analisis retention.

## Business Recommendations

Berdasarkan pola yang ditemukan, beberapa area dapat menjadi pertimbangan bagi tim HR.

### Review Overtime dan Workload

Menganalisis distribusi workload dan pola overtime berdasarkan department dan job role. Karyawan dengan tingkat overtime yang konsisten tinggi dapat menjadi salah satu kelompok yang diprioritaskan untuk evaluasi workload dan retention.

### Review Compensation

Melakukan evaluasi terhadap perbedaan kompensasi antar job role dan kelompok karyawan, terutama pada kelompok yang menunjukkan tingkat attrition lebih tinggi dan tingkat income yang lebih rendah.

### Evaluate Employee Benefits

Mengevaluasi hubungan antara `StockOptionLevel` dan employee retention untuk memahami apakah program incentive yang diberikan sudah selaras dengan tujuan mempertahankan karyawan.

### Strengthen Early Retention Programs

Kelompok karyawan yang lebih muda atau kelompok lain yang menunjukkan pola attrition lebih tinggi dapat dipertimbangkan untuk mendapatkan program career development, mentorship, dan retention yang lebih terarah.

Rekomendasi di atas didasarkan pada pola yang diamati dalam data dan feature importance dari model. Validasi lebih lanjut dengan konteks bisnis dan informasi HR diperlukan sebelum hasil tersebut digunakan sebagai dasar untuk menyimpulkan hubungan sebab-akibat atau menetapkan kebijakan.

## Project Structure

```text
hr-attrition-analytics/
│
├── dashboard/
│   └── HR Attrition Dashboard.png
│
├── notebook.ipynb
├── prediction.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Tools & Technologies

### Programming & Analysis

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Tableau Public

### Machine Learning

* Scikit-learn
* Random Forest
* Gradient Boosting
* GridSearchCV
* ROC-AUC
* PR-AUC

### Model Deployment / Inference

* Joblib
* Python prediction script

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/azaams/hr-attrition-analytics.git
cd hr-attrition-analytics
```

### 2. Install Dependencies

Python 3.9 atau versi yang lebih baru direkomendasikan.

```bash
pip install -r requirements.txt
```

### 3. Run Analysis

Buka file:

```text
notebook.ipynb
```

Kemudian jalankan notebook secara berurutan.

### 4. Run Prediction Script

Setelah model selesai dilatih:

```bash
python prediction.py
```

## Repository

[GitHub Repository](https://github.com/azaams/hr-attrition-analytics)

## Dashboard

[Tableau Public — HR Attrition Dashboard](https://public.tableau.com/app/profile/azzam.mujahid/viz/HRAttrition_17721994843030/Dashboard1)

## Author

**Azzam Mujahid**

S1 Teknik Informatika

Interested in Data Analytics and Data Science
