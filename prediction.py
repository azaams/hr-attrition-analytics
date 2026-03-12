import os
import logging
import joblib
import pandas as pd
from typing import Dict, Any, Tuple

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Konfigurasi path
MODEL_PATH = "model/attrition_model_pipeline.joblib"

def load_model(path: str) -> Any:
    """
    Memuat model Machine Learning dari file yang telah disimpan.
    
    Args:
        path (str): Lokasi path file model.
        
    Returns:
        Any: Objek model/pipeline yang telah dimuat.
        
    Raises:
        FileNotFoundError: Jika file model tidak ditemukan.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File model tidak ditemukan di path: {path}")
    
    logging.info(f"Model berhasil dimuat dari {path}")
    return joblib.load(path)

def predict_attrition(model: Any, employee_data: Dict[str, Any]) -> Tuple[int, float]:
    """
    Melakukan prediksi attrition karyawan berdasarkan data input.
    
    Args:
        model (Any): Model Machine Learning yang sudah dilatih (Pipeline).
        employee_data (Dict[str, Any]): Data karyawan dalam bentuk dictionary.
        
    Returns:
        Tuple[int, float]: Hasil prediksi (1 untuk keluar, 0 untuk bertahan) 
                           dan probabilitas kelas 1.
    """
    df_input = pd.DataFrame([employee_data])
    
    prediction = model.predict(df_input)[0]
    prediction_proba = model.predict_proba(df_input)[0][1]
    
    return int(prediction), float(prediction_proba)

def main():
    """
    Fungsi utama untuk menjalankan eksekusi prediksi.
    """
    sample_employee = {
        "Age": 35,
        "BusinessTravel": "Travel_Rarely",
        "DailyRate": 400,
        "Department": "Research & Development",
        "DistanceFromHome": 5,
        "Education": 2,
        "EducationField": "Medical",
        "EnvironmentSatisfaction": 4,
        "Gender": "Female",
        "HourlyRate": 45,
        "JobInvolvement": 2,
        "JobLevel": 1,
        "JobRole": "Laboratory Technician",
        "JobSatisfaction": 2,
        "MaritalStatus": "Single",
        "MonthlyIncome": 6500,
        "MonthlyRate": 12000,
        "NumCompaniesWorked": 3,
        "OverTime": "No",
        "PercentSalaryHike": 12,
        "PerformanceRating": 3,
        "RelationshipSatisfaction": 2,
        "StockOptionLevel": 0,
        "TotalWorkingYears": 4,
        "TrainingTimesLastYear": 2,
        "WorkLifeBalance": 2,
        "YearsAtCompany": 2,
        "YearsInCurrentRole": 2,
        "YearsSinceLastPromotion": 1,
        "YearsWithCurrManager": 2
    }
    
    try:
        model = load_model(MODEL_PATH)
        
        logging.info("Memulai proses prediksi data karyawan.")
        prediction, probability = predict_attrition(model, sample_employee)
        
        status = "Yes" if prediction == 1 else "No"
        
        logging.info(f"Prediksi Attrition  : {status}")
        logging.info(f"Probabilitas Keluar : {probability:.2f}")
        
    except Exception as e:
        logging.error(f"Terjadi kesalahan saat melakukan inferensi: {e}")

if __name__ == "__main__":
    main()