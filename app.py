import streamlit as st
import pickle
import numpy as np

# --- Page Configuration ---
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Premium Look ---
st.markdown("""
<style>
    /* Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Hero Header */
    .hero-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
    }
    .hero-header h1 {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6C63FF, #3B82F6, #8B5CF6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
    }
    .hero-header p {
        color: #8892B0;
        font-size: 1.1rem;
        font-weight: 300;
    }

    /* Divider line */
    .gradient-divider {
        height: 3px;
        background: linear-gradient(90deg, transparent, #6C63FF, #3B82F6, #8B5CF6, transparent);
        border: none;
        margin: 1rem 0 2rem 0;
        border-radius: 2px;
    }

    /* Section headers */
    .section-header {
        font-size: 1.2rem;
        font-weight: 600;
        color: #CCD6F6;
        margin: 1.5rem 0 0.8rem 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Card style containers */
    .stSelectbox, .stNumberInput, .stSlider {
        background: transparent;
    }

    /* Selectbox & input styling */
    .stSelectbox > div > div,
    .stNumberInput > div > div > input {
        border-radius: 10px !important;
        border: 1px solid #2D3748 !important;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .stSelectbox > div > div:hover,
    .stNumberInput > div > div > input:hover {
        border-color: #6C63FF !important;
        box-shadow: 0 0 0 1px #6C63FF33 !important;
    }

    /* Button styling */
    .stButton > button {
        width: 100%;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg, #6C63FF, #3B82F6);
        color: white;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(108, 99, 255, 0.3);
        letter-spacing: 0.5px;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(108, 99, 255, 0.5);
        background: linear-gradient(135deg, #7C73FF, #4B92FF);
    }
    .stButton > button:active {
        transform: translateY(0px);
    }

    /* Price result card */
    .price-card {
        text-align: center;
        padding: 2rem;
        margin: 1.5rem 0;
        border-radius: 16px;
        background: linear-gradient(135deg, #1A1F2E, #252D3D);
        border: 1px solid #6C63FF44;
        box-shadow: 0 8px 32px rgba(108, 99, 255, 0.15);
        animation: fadeInUp 0.6s ease-out;
    }
    .price-card .label {
        font-size: 1rem;
        color: #8892B0;
        font-weight: 400;
        margin-bottom: 0.5rem;
    }
    .price-card .price {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6C63FF, #3B82F6, #10B981);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .price-card .subtitle {
        font-size: 0.9rem;
        color: #64748B;
        margin-top: 0.5rem;
    }

    /* Badge for price range */
    .price-badge {
        display: inline-block;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 0.8rem;
    }
    .badge-budget {
        background: #10B98122;
        color: #10B981;
        border: 1px solid #10B98144;
    }
    .badge-mid {
        background: #3B82F622;
        color: #3B82F6;
        border: 1px solid #3B82F644;
    }
    .badge-premium {
        background: #8B5CF622;
        color: #8B5CF6;
        border: 1px solid #8B5CF644;
    }
    .badge-luxury {
        background: #F59E0B22;
        color: #F59E0B;
        border: 1px solid #F59E0B44;
    }

    /* Fade in animation */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Slider styling */
    .stSlider > div > div > div > div {
        background: #6C63FF !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #4A5568;
        font-size: 0.85rem;
    }
    .footer a {
        color: #6C63FF;
        text-decoration: none;
    }

    /* Hide default streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- Load Model ---
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

# --- Hero Header ---
st.markdown("""
<div class="hero-header">
    <h1>💻 Laptop Price Predictor</h1>
    <p>Predict laptop prices instantly using Machine Learning</p>
</div>
<div class="gradient-divider"></div>
""", unsafe_allow_html=True)

# --- Form Layout ---
st.markdown('<div class="section-header">🏢 Brand & Type</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    company = st.selectbox('Brand', df['Company'].unique())
with col2:
    type = st.selectbox('Type', df['TypeName'].unique())

st.markdown('<div class="section-header">⚙️ Hardware Specifications</div>', unsafe_allow_html=True)
col3, col4, col5 = st.columns(3)
with col3:
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
with col4:
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
with col5:
    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

col6, col7 = st.columns(2)
with col6:
    cpu = st.selectbox('CPU', df['Cpu brand'].unique())
with col7:
    gpu = st.selectbox('GPU', df['Gpu brand'].unique())

st.markdown('<div class="section-header">🖥️ Display & Build</div>', unsafe_allow_html=True)
col8, col9 = st.columns(2)
with col8:
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
with col9:
    ips = st.selectbox('IPS Display', ['No', 'Yes'])

screen_size = st.slider('Screen Size (inches)', 10.0, 18.0, 13.0, step=0.1)

resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160',
    '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
])

st.markdown('<div class="section-header">📦 Other Details</div>', unsafe_allow_html=True)
col10, col11 = st.columns(2)
with col10:
    weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=2.0, step=0.1)
with col11:
    os = st.selectbox('Operating System', df['os'].unique())

# --- Predict Button ---
st.markdown("<br>", unsafe_allow_html=True)
if st.button('🔮 Predict Price'):
    # Process inputs
    touchscreen = 1 if touchscreen == 'Yes' else 0
    ips = 1 if ips == 'Yes' else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # The saved model was trained with the extra synthetic Sales feature.
    sales = int(df['Sales'].median())

    query = np.array([[company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os, sales]])
    predicted_price = int(np.exp(pipe.predict(query)[0]))

    # Determine price range
    if predicted_price < 30000:
        badge_class = "badge-budget"
        badge_text = "💚 Budget Friendly"
    elif predicted_price < 60000:
        badge_class = "badge-mid"
        badge_text = "💙 Mid Range"
    elif predicted_price < 100000:
        badge_class = "badge-premium"
        badge_text = "💜 Premium"
    else:
        badge_class = "badge-luxury"
        badge_text = "💛 Luxury"

    # Display result
    st.markdown(f"""
    <div class="price-card">
        <div class="label">Estimated Laptop Price</div>
        <div class="price">₹ {predicted_price:,}</div>
        <div class="subtitle">Based on your selected configuration</div>
        <div class="price-badge {badge_class}">{badge_text}</div>
    </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    Built with ❤️ by <a href="https://github.com/ArpanChaudhari" target="_blank">Arpan Chaudhari</a> | 
    Powered by Streamlit & scikit-learn
</div>
""", unsafe_allow_html=True)