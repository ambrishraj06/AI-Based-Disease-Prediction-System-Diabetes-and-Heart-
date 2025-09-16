import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import time

# Set page configuration
st.set_page_config(
    page_title="🧬 HealthAI Pro - Medical Intelligence Platform",
    layout="wide",
    page_icon="🧬",
    initial_sidebar_state="expanded"
)

# Initialize session state for holding validation errors
if 'errors' not in st.session_state:
    st.session_state.errors = {}

# --- REFINED CSS FOR A POLISHED & USER-FRIENDLY UI ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@100;200;300;400;500;600;700;800;900&family=SF+Pro+Text:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'SF Pro Display', 'SF Pro Text', -apple-system, BlinkMacSystemFont, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

.stApp {
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
    color: #ffffff;
}

/* Main content centered and medium-sized */
.main .block-container {
    max-width: 1200px;
    padding: 2rem 2rem 6rem 2rem;
}

/* --- IMPROVED INPUT FIELDS --- */
.stTextInput > div > div > input, .stSelectbox > div > div > div {
    background: rgba(255, 255, 255, 0.95) !important;
    border: 2px solid rgba(59, 130, 246, 0.2) !important;
    border-radius: 16px !important;
    padding: 16px 20px !important;
    font-weight: 500 !important;
    font-size: 16px !important;
    color: #1a202c !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08) !important;
    backdrop-filter: blur(10px) !important;
}

.stTextInput > div > div > input:focus {
    border-color: #3b82f6 !important;
    background: rgba(255, 255, 255, 1) !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1), 0 6px 20px rgba(0, 0, 0, 0.1) !importanT;
    transform: translateY(-1px) !important;
    outline: none !important;
}

.stTextInput > div > div > input::placeholder { color: rgba(107, 114, 128, 0.6) !important; font-weight: 400 !important; }

/* --- AGGRESSIVE FIX FOR SELECTBOX TEXT VISIBILITY --- */
/* This targets the text of the selected option in the main box */
div[data-baseweb="select"] div[class*="singleValue"] {
    color: #000000 !important;
}

/* This targets the options in the dropdown list */
div[data-baseweb="popover"] li {
    color: #000000 !important;
}

/* This is a fallback to ensure the container itself has the right color */
.stSelectbox > div > div > div {
    color: #000000 !important;
}

/* Clear & Visible Labels */
.stTextInput label, .stSelectbox label {
    color: rgba(255, 255, 255, 0.95) !important;
    font-weight: 600 !important;
    font-size: 17px !important;
    margin-bottom: 8px !important;
    display: block !important;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.3) !important;
}

/* --- SMALLER, PATIENT-FRIENDLY INFO BOXES --- */
.info-box {
    background: rgba(59, 130, 246, 0.1) !important;
    border-left: 3px solid #3b82f6 !important;
    border-radius: 8px !important;
    padding: 6px 12px !important;
    margin-top: 5px !important;
    margin-bottom: 18px !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
    backdrop-filter: blur(10px) !important;
}

.info-box p {
    color: rgba(255, 255, 255, 0.8) !important;
    font-size: 12px !important;
    margin: 0 !important;
    line-height: 1.4;
}
.info-box strong {
    color: #a5c3f5 !important;
    font-weight: 600;
}

/* Premium buttons */
.stButton > button {
    background: linear-gradient(135deg, #3b82f6 0%, #2563eb 50%, #1d4ed8 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 18px !important;
    padding: 18px 36px !important;
    font-weight: 600 !important;
    font-size: 17px !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    width: 100% !important;
    box-shadow: 0 12px 24px rgba(59, 130, 246, 0.25), 0 4px 12px rgba(59, 130, 246, 0.15) !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 18px 36px rgba(59, 130, 246, 0.4), 0 6px 18px rgba(59, 130, 246, 0.3) !important;
}

h1, h2, h3 {
    color: #ffffff !important;
    font-weight: 700 !important;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3) !important;
}

.glass-card {
    background: rgba(255, 255, 255, 0.06) !important;
    backdrop-filter: blur(30px) !important;
    border-radius: 24px !important;
    padding: 35px !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    margin-bottom: 30px !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* --- ENHANCED HOVER ANIMATION --- */
.glass-card:hover {
    transform: translateY(-6px) scale(1.01) !important;
    box-shadow: 0 30px 60px rgba(0, 0, 0, 0.25), 0 15px 30px rgba(0,0,0,0.2) !important;
    background: rgba(255, 255, 255, 0.08) !important;
}

.header-container {
    padding: 45px 35px !important;
    margin-bottom: 40px !important;
    text-align: center !important;
    animation: fadeIn 1s ease-out !important;
}

.header-title {
    background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 50%, #dbeafe 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    font-size: 3.5rem !important;
    font-weight: 800 !important;
}

.header-subtitle {
    color: rgba(255, 255, 255, 0.9) !important;
    font-size: 1.3rem !important;
    font-weight: 400 !important;
}

/* --- CLEAN & CLEAR RESULT CARDS --- */
.result-card {
    background: rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(30px) !important;
    border-radius: 20px !important;
    padding: 30px !important;
    margin-top: 25px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2) !important;
    animation: fadeInResult 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}
.result-card-high-risk { border-left: 6px solid #ef4444 !important; }
.result-card-low-risk { border-left: 6px solid #10b981 !important; }

.result-title {
    font-size: 1.8rem !important;
    font-weight: 700 !important;
    margin-bottom: 10px !important;
    display: flex;
    align-items: center;
}
.result-title-high-risk { color: #f87171 !important; }
.result-title-low-risk { color: #34d399 !important; }

.result-summary {
    color: rgba(255, 255, 255, 0.9) !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
    margin-bottom: 20px !important;
}

.result-recommendations h4 {
    color: #81a9f1 !important;
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    margin-top: 20px;
    margin-bottom: 10px;
    border-bottom: 1px solid rgba(255,255,255,0.15);
    padding-bottom: 5px;
}

.result-recommendations ul { list-style-type: none; padding-left: 0; }
.result-recommendations li {
    color: rgba(255, 255, 255, 0.85) !important;
    font-size: 15px; margin-bottom: 10px; display: flex; align-items: flex-start;
}
.result-recommendations li::before {
    content: '✓'; color: #3b82f6; font-weight: bold; margin-right: 12px; margin-top: 2px;
}

/* Premium animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeInResult {
    from { opacity: 0; transform: translateY(20px) scale(0.98); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

.stWarning {
    background: rgba(245, 158, 11, 0.15) !important;
    backdrop-filter: blur(15px) !important;
    border-radius: 10px !important;
    border: 1px solid rgba(245, 158, 11, 0.3) !important;
    border-left: 4px solid #f59e0b !important;
    padding: 10px 15px !important;
    margin-top: -8px !important;
    margin-bottom: 10px !important;
}

/* --- SIDEBAR STATUS --- */
.sidebar-status {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    padding: 15px;
    margin-top: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.sidebar-status h4 {
    color: #3b82f6;
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 12px;
    text-align: center;
}

.status-item {
    display: flex;
    align-items: center;
    font-size: 12px;
    color: rgba(255, 255, 255, 0.8);
    margin-bottom: 8px;
}
.status-item span {
    margin-right: 8px;
    font-size: 14px;
}
.status-item strong {
    color: #10b981;
    font-weight: 600;
    margin-left: auto;
}
</style>
""", unsafe_allow_html=True)

# Model loading
@st.cache_resource
def load_models():
    try:
        # IMPORTANT: Make sure these file paths are correct for your system.
        diabetes_model = pickle.load(open('trained_model_diabetics.sav', 'rb'))
        heart_disease_model = pickle.load(open('trained_model_heart.sav', 'rb'))
        return diabetes_model, heart_disease_model
    except FileNotFoundError:
        st.error("⚠️ **Model Files Not Found:** Could not find `trained_model_diabetics.sav` or `trained_model_heart.sav`. Please ensure these files are in the same directory as the script.")
        st.stop()
    except Exception as e:
        st.error(f"❌ **Error Loading Models:** An unexpected error occurred: {e}")
        st.stop()

diabetes_model, heart_disease_model = load_models()

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 25px 0 20px;">
        <div style="font-size: 3rem; margin-bottom: 12px; filter: drop-shadow(0 4px 8px rgba(59, 130, 246, 0.3));">🧬</div>
        <h1 style="color: #3b82f6; margin: 0; font-size: 1.8rem; font-weight: 800;">HealthAI Pro</h1>
        <p style="color: rgba(255, 255, 255, 0.8); font-size: 14px; margin-top: 6px;">Medical Intelligence Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    selected = option_menu(
        'Medical Analysis',
        ['🩸 Diabetes Assessment', '❤️ Cardiovascular Analysis'],
        menu_icon='hospital',
        icons=['droplet-half', 'heart-pulse'],
        default_index=0,
        styles={
            "container": {"padding": "10px", "background": "rgba(255, 255, 255, 0.05)", "border-radius": "16px"},
            "icon": {"color": "#3b82f6", "font-size": "18px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin": "4px 0", "color": "rgba(255, 255, 255, 0.9)", "--hover-color": "rgba(59, 130, 246, 0.2)"},
            "nav-link-selected": {"background": "linear-gradient(135deg, #3b82f6, #2563eb)", "color": "white"},
        }
    )

    st.markdown("""
    <div class="sidebar-status">
        <h4>System Status</h4>
        <div class="status-item"><span>🤖</span> AI Models <strong>Ready</strong></div>
        <div class="status-item"><span>⚡️</span> Response Time <strong>Fast</strong></div>
        <div class="status-item"><span>🔒</span> Security <strong>Active</strong></div>
    </div>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container glass-card">
    <div class="header-title">HealthAI Pro</div>
    <div class="header-subtitle">Your Personal Health Risk Assessment Tool</div>
</div>
""", unsafe_allow_html=True)

# PROMINENT DISCLAIMER
st.markdown("""
<div class="glass-card" style="border-left: 5px solid #f59e0b; animation: fadeIn 1.2s ease-out;">
    <h3 style="color: #f59e0b; margin-top: 0; font-size: 1.3rem;">⚕️ Important Medical Notice</h3>
    <p style="color: rgba(255, 255, 255, 0.9); line-height: 1.6; font-size: 15px;">
    This tool provides AI-driven predictions for informational purposes only. <strong>It is not a substitute for professional medical advice, diagnosis, or treatment.</strong> Always consult with a qualified healthcare provider regarding any medical concerns or before making any health decisions.
    </p>
</div>
""", unsafe_allow_html=True)

# --- HELPER FUNCTION FOR VALIDATION ---
def validate_input(value, min_val, max_val, name):
    """Checks if an input value is a valid float and within the specified range."""
    if not value or value == 'Select':
        return f"Please provide a value for {name}."
    try:
        val_float = float(value)
        if not (min_val <= val_float <= max_val):
            return f"{name} must be between {min_val} and {max_val}."
    except ValueError:
        return f"Please enter a valid number for {name}."
    return None

# --- DIABETES PAGE ---
if selected == '🩸 Diabetes Assessment':

    st.markdown("<h1>Diabetes Risk Assessment</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', placeholder="e.g., 2", key="db_preg")
        if st.session_state.errors.get("Pregnancies"): st.warning(f"⚠️ {st.session_state.errors['Pregnancies']}")
        st.markdown('<div class="info-box"><p>Total past pregnancies. <strong>Valid range: 0-20</strong>.</p></div>', unsafe_allow_html=True)
        
        Glucose = st.text_input('Blood Glucose Level (mg/dL)', placeholder="e.g., 120", key="db_glucose")
        if st.session_state.errors.get("Glucose"): st.warning(f"⚠️ {st.session_state.errors['Glucose']}")
        st.markdown('<div class="info-box"><p>Your blood sugar level. <strong>Valid range: 40-300</strong>.</p></div>', unsafe_allow_html=True)

        BloodPressure = st.text_input('Blood Pressure (Diastolic, mmHg)', placeholder="e.g., 80", key="db_bp")
        if st.session_state.errors.get("BloodPressure"): st.warning(f"⚠️ {st.session_state.errors['BloodPressure']}")
        st.markdown('<div class="info-box"><p>Lower number in BP reading. <strong>Valid range: 30-140</strong>.</p></div>', unsafe_allow_html=True)

        SkinThickness = st.text_input('Skin Thickness (mm)', placeholder="e.g., 20", key="db_skin")
        if st.session_state.errors.get("SkinThickness"): st.warning(f"⚠️ {st.session_state.errors['SkinThickness']}")
        st.markdown('<div class="info-box"><p>Triceps skinfold thickness. <strong>Valid range: 0-100</strong>.</p></div>', unsafe_allow_html=True)

    with col2:
        Insulin = st.text_input('Insulin Level (mu U/ml)', placeholder="e.g., 80", key="db_insulin")
        if st.session_state.errors.get("Insulin"): st.warning(f"⚠️ {st.session_state.errors['Insulin']}")
        st.markdown('<div class="info-box"><p>2-Hour serum insulin. <strong>Valid range: 0-900</strong>.</p></div>', unsafe_allow_html=True)
        
        BMI = st.text_input('Body Mass Index (BMI)', placeholder="e.g., 25.5", key="db_bmi")
        if st.session_state.errors.get("BMI"): st.warning(f"⚠️ {st.session_state.errors['BMI']}")
        st.markdown('<div class="info-box"><p>Your Body Mass Index. <strong>Valid range: 10-70</strong>.</p></div>', unsafe_allow_html=True)
        
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function', placeholder="e.g., 0.5", key="db_dpf")
        if st.session_state.errors.get("DiabetesPedigreeFunction"): st.warning(f"⚠️ {st.session_state.errors['DiabetesPedigreeFunction']}")
        st.markdown('<div class="info-box"><p>Family history score. <strong>Valid range: 0.0-2.5</strong>.</p></div>', unsafe_allow_html=True)
        
        Age = st.text_input('Age (Years)', placeholder="e.g., 35", key="db_age")
        if st.session_state.errors.get("Age"): st.warning(f"⚠️ {st.session_state.errors['Age']}")
        st.markdown('<div class="info-box"><p>Your current age. <strong>Valid range: 1-120</strong>.</p></div>', unsafe_allow_html=True)

    if st.button('🔍 Analyze Diabetes Risk'):
        st.session_state.errors = {} # Reset errors on button click
        validations = {
            "Pregnancies": validate_input(Pregnancies, 0, 20, "Pregnancies"), "Glucose": validate_input(Glucose, 40, 300, "Glucose"),
            "BloodPressure": validate_input(BloodPressure, 30, 140, "Blood Pressure"), "SkinThickness": validate_input(SkinThickness, 0, 100, "Skin Thickness"),
            "Insulin": validate_input(Insulin, 0, 900, "Insulin"), "BMI": validate_input(BMI, 10, 70, "BMI"),
            "DiabetesPedigreeFunction": validate_input(DiabetesPedigreeFunction, 0.0, 2.5, "Diabetes Pedigree"), "Age": validate_input(Age, 1, 120, "Age")
        }
        
        for key, msg in validations.items():
            if msg: st.session_state.errors[key] = msg
        
        if not st.session_state.errors:
            with st.spinner('🧠 Analyzing Health Data... This may take a moment.'):
                time.sleep(1.5)
                user_input = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
                prediction = diabetes_model.predict([user_input])
                
                if prediction[0] == 1:
                    st.markdown("""
                    <div class="result-card result-card-high-risk">
                        <h2 class="result-title result-title-high-risk">🚨 WARNING: Elevated Diabetes Risk Detected</h2>
                        <p class="result-summary">
                            <b>This is a significant warning sign.</b> Our AI analysis indicates that your health metrics align with patterns commonly seen in individuals at a higher risk for developing Type 2 diabetes. This requires prompt attention.
                        </p>
                        <div class="result-recommendations">
                            <h4>Recommended Immediate Actions</h4>
                            <ul>
                                <li><b>Consult a Doctor:</b> Schedule an appointment with your healthcare provider or an endocrinologist for a definitive diagnosis.</li>
                                <li><b>Request Specific Tests:</b> Discuss getting comprehensive tests like an HbA1c, Fasting Plasma Glucose, or an Oral Glucose Tolerance Test.</li>
                                <li><b>Do Not Ignore Symptoms:</b> Be aware of symptoms like increased thirst, frequent urination, unexplained weight loss, or fatigue.</li>
                            </ul>
                            <h4>Tips for Prevention & Management to Discuss with Your Doctor</h4>
                            <ul>
                                <li><b>Dietary Changes:</b> Focus on a diet rich in fiber, lean proteins, and non-starchy vegetables. Reduce intake of sugary drinks and processed foods.</li>
                                <li><b>Consistent Physical Activity:</b> Aim for at least 150 minutes of moderate exercise (like brisk walking) per week.</li>
                                <li><b>Weight Management:</b> Even a small amount of weight loss (5-7% of body weight) can significantly lower your risk.</li>
                                <li><b>Monitor Blood Sugar:</b> Your doctor may advise you to start monitoring your blood sugar levels at home.</li>
                            </ul>
                        </div>
                    </div>""", unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="result-card result-card-low-risk">
                        <h2 class="result-title result-title-low-risk">✅ PROACTIVE HEALTH: Lower Diabetes Risk Profile</h2>
                        <p class="result-summary">
                           <b>Excellent news!</b> Your health data suggests a lower statistical risk of developing diabetes at this time. This indicates good metabolic health and is a great foundation to build upon.
                        </p>
                         <div class="result-recommendations">
                            <h4>How to Maintain Your Low-Risk Status</h4>
                            <ul>
                                <li><b>Stay Active:</b> Continue with regular physical activity. Consistency is more important than intensity.</li>
                                <li><b>Balanced Nutrition:</b> Maintain a diet rich in whole foods. Prioritize whole grains, fruits, vegetables, and lean protein sources.</li>
                                <li><b>Limit Sugars:</b> Be mindful of hidden sugars in drinks and processed snacks. Water is always the best choice for hydration.</li>
                                <li><b>Regular Check-ups:</b> A low-risk profile is not permanent. Attend yearly health check-ups to monitor your key health markers and stay ahead of any potential issues.</li>
                            </ul>
                            <h4>A Gentle Warning</h4>
                            <p class="result-summary" style="margin-bottom: 0;">While your current risk is low, it's important to remember that lifestyle choices and genetics play an ongoing role. Remaining proactive with healthy habits is the best way to prevent future health problems.</p>
                        </div>
                    </div>""", unsafe_allow_html=True)

# --- HEART DISEASE PAGE ---
elif selected == '❤️ Cardiovascular Analysis':

    st.markdown("<h1>Cardiovascular Risk Assessment</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        age = st.text_input('Age', placeholder="e.g., 45", key="hd_age")
        if st.session_state.errors.get("age"): st.warning(f"⚠️ {st.session_state.errors['age']}")
        st.markdown('<div class="info-box"><p>Current age. <strong>Range: 1-120</strong>.</p></div>', unsafe_allow_html=True)

        sex = st.selectbox('Sex', ['Select', 'Male', 'Female'], key="hd_sex")
        if st.session_state.errors.get("sex"): st.warning(f"⚠️ {st.session_state.errors['sex']}")
        st.markdown('<div class="info-box"><p>Your biological sex.</p></div>', unsafe_allow_html=True)

        cp = st.selectbox('Chest Pain Type', ['Select', 'Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'], key="hd_cp")
        if st.session_state.errors.get("cp"): st.warning(f"⚠️ {st.session_state.errors['cp']}")
        st.markdown('<div class="info-box"><p>Type of chest pain experienced.</p></div>', unsafe_allow_html=True)

        trestbps = st.text_input('Resting Blood Pressure (mm Hg)', placeholder="e.g., 120", key="hd_trestbps")
        if st.session_state.errors.get("trestbps"): st.warning(f"⚠️ {st.session_state.errors['trestbps']}")
        st.markdown('<div class="info-box"><p>Systolic pressure at rest. <strong>Range: 80-220</strong>.</p></div>', unsafe_allow_html=True)

    with col2:
        chol = st.text_input('Serum Cholestoral (mg/dL)', placeholder="e.g., 200", key="hd_chol")
        if st.session_state.errors.get("chol"): st.warning(f"⚠️ {st.session_state.errors['chol']}")
        st.markdown('<div class="info-box"><p>Total cholesterol level. <strong>Range: 100-600</strong>.</p></div>', unsafe_allow_html=True)

        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', ['Select', 'Yes', 'No'], key="hd_fbs")
        if st.session_state.errors.get("fbs"): st.warning(f"⚠️ {st.session_state.errors['fbs']}")
        st.markdown('<div class="info-box"><p>Is your fasting sugar high?</p></div>', unsafe_allow_html=True)
        
        restecg = st.selectbox('Resting ECG Results', ['Select', 'Normal', 'ST-T Wave Abnormality', 'LV Hypertrophy'], key="hd_restecg")
        if st.session_state.errors.get("restecg"): st.warning(f"⚠️ {st.session_state.errors['restecg']}")
        st.markdown('<div class="info-box"><p>Results from an ECG test.</p></div>', unsafe_allow_html=True)
        
        thalach = st.text_input('Maximum Heart Rate Achieved', placeholder="e.g., 150 bpm", key="hd_thalach")
        if st.session_state.errors.get("thalach"): st.warning(f"⚠️ {st.session_state.errors['thalach']}")
        st.markdown('<div class="info-box"><p>Peak heart rate during exercise. <strong>Range: 60-220</strong>.</p></div>', unsafe_allow_html=True)
    
    with col3:
        exang = st.selectbox('Exercise Induced Angina', ['Select', 'Yes', 'No'], key="hd_exang")
        if st.session_state.errors.get("exang"): st.warning(f"⚠️ {st.session_state.errors['exang']}")
        st.markdown('<div class="info-box"><p>Did exercise cause chest pain?</p></div>', unsafe_allow_html=True)

        oldpeak = st.text_input('ST depression (exercise-induced)', placeholder="e.g., 1.0", key="hd_oldpeak")
        if st.session_state.errors.get("oldpeak"): st.warning(f"⚠️ {st.session_state.errors['oldpeak']}")
        st.markdown('<div class="info-box"><p>Result from stress test. <strong>Range: 0-7</strong>.</p></div>', unsafe_allow_html=True)
        
        slope = st.selectbox('Peak exercise ST slope', ['Select', 'Upsloping', 'Flat', 'Downsloping'], key="hd_slope")
        if st.session_state.errors.get("slope"): st.warning(f"⚠️ {st.session_state.errors['slope']}")
        st.markdown('<div class="info-box"><p>The ST slope pattern.</p></div>', unsafe_allow_html=True)

        ca = st.selectbox('Major vessels colored by flourosopy', ['Select', '0', '1', '2', '3', '4'], key="hd_ca")
        if st.session_state.errors.get("ca"): st.warning(f"⚠️ {st.session_state.errors['ca']}")
        st.markdown('<div class="info-box"><p>Number of blocked vessels. <strong>Range: 0-4</strong>.</p></div>', unsafe_allow_html=True)

        thal = st.selectbox('Thalassemia', ['Select', 'Normal', 'Fixed Defect', 'Reversible Defect'], key="hd_thal")
        if st.session_state.errors.get("thal"): st.warning(f"⚠️ {st.session_state.errors['thal']}")
        st.markdown('<div class="info-box"><p>A blood disorder status.</p></div>', unsafe_allow_html=True)
        st.markdown("""
<style>
/* Force selectbox displayed text to be black and visible */
div[data-baseweb="select"] > div > div {
    color: #000000 !important; /* Black text */
    font-weight: 600 !important;
    font-size: 15px !important;
    background-color: rgba(255, 255, 255, 0.95) !important; /* Light background */
}
/* Dropdown menu items visible with white background and black text */
div[role="listbox"] {
    background-color: rgba(255, 255, 255, 0.99) !important;
    border-radius: 10px !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.2) !important;
}
/* Dropdown options visible on hover */
div[role="option"] {
    color: #000000 !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    padding: 10px 14px !important;
}
div[role="option"]:hover {
    background-color: #2563eb !important; /* Blue hover */
    color: white !important;
}
/* Also ensure the inner input box text gets styled */
div[data-baseweb="input"] > input {
    color: #000000 !important;
    background-color: transparent !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}
/* Smaller adjustments to height and padding for better alignment */
div[data-baseweb="select"] > div > div {
    min-height: 62px !important;
    padding-left: 14px !important;
}
</style>
""", unsafe_allow_html=True)

    if st.button('🔍 Analyze Cardiovascular Risk'):
        st.session_state.errors = {} # Reset errors
        
        # Consolidate checks and validation
        fields_to_validate = {
            "age": (age, 1, 120), "trestbps": (trestbps, 80, 220), "chol": (chol, 100, 600),
            "thalach": (thalach, 60, 220), "oldpeak": (oldpeak, 0, 7), "ca": (ca, 0, 4)
        }
        select_fields = {"sex": sex, "cp": cp, "fbs": fbs, "restecg": restecg, "exang": exang, "slope": slope, "thal": thal}

        for name, (val, min_v, max_v) in fields_to_validate.items():
            error = validate_input(val, min_v, max_v, name.capitalize())
            if error: st.session_state.errors[name] = error

        for name, val in select_fields.items():
            if val == 'Select': st.session_state.errors[name] = f"Please make a selection for {name.capitalize()}."

        if not st.session_state.errors:
            with st.spinner('🧠 Analyzing Cardiovascular Data...'):
                time.sleep(1.5)
                sex_val = 1 if sex == 'Male' else 0
                cp_map = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
                fbs_val = 1 if fbs == 'Yes' else 0
                restecg_map = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'LV Hypertrophy': 2}
                exang_val = 1 if exang == 'Yes' else 0
                slope_map = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
                thal_map = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}
                
                user_input = [float(age), sex_val, cp_map[cp], float(trestbps), float(chol), fbs_val, restecg_map[restecg], float(thalach), exang_val, float(oldpeak), slope_map[slope], float(ca), thal_map[thal]]
                prediction = heart_disease_model.predict([user_input])

                if prediction[0] == 1:
                    st.markdown("""
                    <div class="result-card result-card-high-risk">
                        <h2 class="result-title result-title-high-risk">🚨 URGENT: High Cardiovascular Risk Identified</h2>
                        <p class="result-summary">
                           <b>Warning: These results indicate a serious potential for cardiovascular disease.</b> The data you provided matches patterns strongly associated with heart conditions. It is crucial that you seek professional medical evaluation without delay.
                        </p>
                        <div class="result-recommendations">
                            <h4>Immediate Medical Recommendations</h4>
                            <ul>
                                <li><b>See a Cardiologist:</b> Schedule an appointment with a heart specialist as soon as possible.</li>
                                <li><b>Undergo Diagnostic Tests:</b> Your doctor will likely recommend tests like an ECG, stress test, echocardiogram, or blood work.</li>
                                <li><b>Do Not Ignore Symptoms:</b> Pay close attention to any chest pain, shortness of breath, dizziness, or pain in your arms/jaw. Seek emergency care if these occur.</li>
                            </ul>
                            <h4>Critical Lifestyle Tips to Avoid Heart Disease</h4>
                            <ul>
                                <li><b>Adopt a Heart-Healthy Diet:</b> Focus on the Mediterranean or DASH diet, which are rich in vegetables, fruits, whole grains, and healthy fats while being low in sodium and saturated fats.</li>
                                <li><b>Quit Smoking:</b> If you smoke, quitting is the single most effective action you can take to protect your heart.</li>
                                <li><b>Control Blood Pressure:</b> Work with your doctor to manage your blood pressure through diet, exercise, and medication if needed.</li>
                                <li><b>Manage Cholesterol:</b> Follow medical advice to lower your LDL ('bad') cholesterol and raise your HDL ('good') cholesterol.</li>
                            </ul>
                        </div>
                    </div>""", unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="result-card result-card-low-risk">
                        <h2 class="result-title result-title-low-risk">✅ POSITIVE OUTLOOK: Lower Cardiovascular Risk Profile</h2>
                        <p class="result-summary">
                            <b>Fantastic!</b> Your cardiovascular analysis shows a lower statistical risk for heart disease. Your current health parameters appear to be in a heart-healthy range, which is an excellent achievement.
                        </p>
                        <div class="result-recommendations">
                            <h4>Tips to Protect Your Heart for the Long Term</h4>
                            <ul>
                                <li><b>Prioritize Aerobic Exercise:</b> Engage in activities like brisk walking, cycling, swimming, or jogging for at least 150 minutes per week.</li>
                                <li><b>Eat for Heart Health:</b> Incorporate sources of healthy fats like avocados, nuts, and olive oil. Limit processed foods and reduce sodium intake to help maintain healthy blood pressure.</li>
                                <li><b>Manage Stress:</b> Chronic stress can impact heart health. Practice stress-reduction techniques like mindfulness, yoga, or hobbies you enjoy.</li>
                                <li><b>Ensure Quality Sleep:</b> Aim for 7-9 hours of quality sleep per night, as it's vital for cardiovascular recovery and health.</li>
                            </ul>
                            <h4>Important Reminder</h4>
                             <p class="result-summary" style="margin-bottom: 0;">A low-risk profile is something to be proud of, but heart health requires continuous effort. Regular check-ups and a consistent healthy lifestyle are the best combination to prevent future cardiovascular issues.</p>
                        </div>
                    </div>""", unsafe_allow_html=True)