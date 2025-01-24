import os
import streamlit as st
import random

# Print current working directory
print("Current working directory:", os.getcwd())

# Print absolute path of the script
print("Script location:", os.path.abspath(__file__))

# Cek lokasi file
current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current directory: {current_dir}")

# Dictionary untuk menyimpan masalah kulit dan responnya
skin_problems = {
    "kulit kering": {
        "keywords": ["kering", "pecah-pecah", "bersisik", "kasar", "ketarik"],
        "analisis": "Dari gejala yang Anda sebutkan, sepertinya Anda mengalami masalah kulit kering. Kulit kering bisa disebabkan oleh berbagai faktor seperti cuaca, penggunaan produk yang terlalu keras, atau dehidrasi.",
        "solusi": [
            "1. Gunakan cleanser yang lembut dan non-foaming",
            "2. Aplikasikan toner yang mengandung humectant seperti glycerin",
            "3. Gunakan serum atau moisturizer dengan kandungan hyaluronic acid",
            "4. Lindungi kulit dengan sunscreen di siang hari",
            "5. Pertimbangkan untuk menggunakan facial oil di malam hari"
        ],
        "tips": "Pastikan untuk minum cukup air dan hindari mandi dengan air terlalu panas karena bisa memperparah kulit kering. Hyaluronic acid dapat membantu menjaga kelembapan kulit dan mencegah tanda-tanda penuaan."
    },
    "kulit berminyak": {
        "keywords": ["berminyak", "mengkilap", "kilap", "minyak", "mengkilat"],
        "analisis": "Berdasarkan keluhan Anda, tampaknya Anda memiliki tipe kulit berminyak. Kondisi ini biasanya disebabkan oleh produksi sebum yang berlebihan.",
        "solusi": [
            "1. Gunakan cleanser dengan kandungan salicylic acid",
            "2. Pilih toner yang mengandung niacinamide atau witch hazel",
            "3. Aplikasikan moisturizer berbasis gel yang oil-free",
            "4. Gunakan sunscreen yang ringan dan non-comedogenic",
            "5. Pertimbangkan penggunaan clay mask 1-2 kali seminggu"
        ],
        "tips": "Hindari produk yang terlalu rich atau creamy, dan jangan lupa double cleansing di malam hari. Ceramide dapat menjadi pilihan anda yang dapat membantu menjaga kesehatan kulit berminyak."
    },
    "kulit sensitif": {
        "keywords": ["sensitif", "merah", "iritasi", "gatal", "perih"],
        "analisis": "Dari gejala yang Anda sebutkan, tampaknya Anda memiliki kulit sensitif. Kulit sensitif membutuhkan perhatian khusus dan produk yang gentle.",
        "solusi": [
            "1. Gunakan cleanser yang sangat lembut dan fragrance-free",
            "2. Pilih produk dengan kandungan menenangkan seperti aloe vera",
            "3. Hindari produk yang mengandung alkohol dan parfum",
            "4. Gunakan moisturizer yang minimal ingredients",
            "5. Pakai sunscreen mineral/physical (zinc oxide/titanium dioxide)"
        ],
        "tips": "Selalu patch test produk baru dan hindari eksfoliasi yang terlalu keras. Nicotinamide dapat membantu meredakan kemerahan dan iritasi pada kulit sensitif."
    },
    "jerawat": {
        "keywords": ["jerawat", "berjerawat", "bruntusan", "acne", "komedo"],
        "analisis": "Dari keluhan Anda, sepertinya Anda mengalami masalah jerawat. Jerawat bisa disebabkan oleh berbagai faktor seperti hormonal, bakteri, atau penggunaan produk yang tidak sesuai.",
        "solusi": [
            "1. Gunakan cleanser dengan salicylic acid atau benzoyl peroxide",
            "2. Aplikasikan spot treatment yang mengandung tea tree oil",
            "3. Pilih moisturizer non-comedogenic",
            "4. Jangan lupa gunakan sunscreen setiap hari",
            "5. Pertimbangkan penggunaan produk dengan niacinamide"
        ],
        "tips": "Hindari memencet jerawat dan jaga kebersihan wajah serta barang-barang yang bersentuhan dengan wajah seperti handuk dan sarung bantal. Salicylic acid bekerja dengan cara mengangkat sel-sel kulit mati yang menyumbat pori-pori."
    }
}

# Tambahkan dictionary responses di bagian atas file, setelah skin_problems
yes_responses = [
    "Baik, apa yang ingin Anda tanyakan mengenai kulit Anda?",
    "Tentu, silakan tanyakan apa yang ingin Anda ketahui tentang perawatan kulit Anda.",
    "Saya siap membantu Anda lagi. Apa yang ingin Anda konsultasikan?"
]

no_responses = [
    "Baiklah, terima kasih telah berkonsultasi! 😊",
    "Senang bisa membantu Anda. Semoga harimu menyenangkan! ✨",
    "Terima kasih telah menggunakan Beauty Helper. Jaga kesehatan kulitmu ya! 💖"
]

def get_skin_problem_response(user_input):
    user_input = user_input.lower()
    
    # Cek untuk respons iya/tidak
    if user_input in ["iya", "ya", "y"]:
        return {
            "type": "follow_up",
            "content": random.choice(yes_responses)
        }
    elif user_input in ["tidak", "nggak", "gak", "engga", "enggak", "no", "n"]:
        return {
            "type": "follow_up",
            "content": random.choice(no_responses)
        }
    
    # Logika existing untuk skin problems
    for problem, data in skin_problems.items():
        if any(keyword in user_input for keyword in data["keywords"]):
            return {
                "type": "skin_problem",
                "analisis": data["analisis"],
                "solusi": data["solusi"],
                "tips": data["tips"]
            }
    
    return None

def main():
    st.set_page_config(page_title="Beauty Helper", page_icon="💄", layout="wide")
    
    # Custom CSS untuk meniru tampilan HTML/CSS original
    st.markdown("""
        <style>
        /* Main layout */
        .stApp {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #ffd1dc 0%, #ff69b4 100%);
        }
        
        /* App container */
        .main > div {
            display: flex;
            padding: 2rem;
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: rgba(255, 255, 255, 0.95);
            padding: 20px;
            border-radius: 20px 0 0 20px;
            box-shadow: -5px 0 15px rgba(0, 0, 0, 0.1);
            background-image: linear-gradient(45deg, #ffe6ea 25%, #fff1f4 25%, #fff1f4 50%, #ffe6ea 50%, #ffe6ea 75%, #fff1f4 75%, #fff1f4 100%);
            background-size: 20px 20px;
        }
        
        /* Main chat container */
        .css-1d391kg {
            flex: 1;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
            padding: 30px;
            margin: 20px;
        }
        
        /* Chat messages styling yang baru */
        .user-message {
            background: linear-gradient(135deg, #ff69b4, #ff1493);
            color: white;
            margin-left: auto;
            margin-right: 20px;
            padding: 15px 20px;
            border-radius: 20px 20px 0 20px;
            max-width: 70%;
            position: relative;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(255, 20, 147, 0.2);
            animation: fadeIn 0.5s ease-in-out;
        }
        
        .user-message::after {
            content: '';
            position: absolute;
            right: -10px;
            bottom: 0;
            width: 20px;
            height: 20px;
            background: linear-gradient(135deg, #ff69b4, #ff1493);
            border-bottom-left-radius: 15px;
            transform: skew(-15deg);
        }
        
        .bot-message {
            background: linear-gradient(135deg, #fff, #f0f0f0);
            color: #333;
            margin-right: auto;
            margin-left: 20px;
            padding: 15px 20px;
            border-radius: 20px 20px 20px 0;
            max-width: 70%;
            position: relative;
            margin-bottom: 20px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            animation: fadeIn 0.5s ease-in-out;
        }
        
        .bot-message::after {
            content: '';
            position: absolute;
            left: -10px;
            bottom: 0;
            width: 20px;
            height: 20px;
            background: linear-gradient(135deg, #fff, #f0f0f0);
            border-bottom-right-radius: 15px;
            transform: skew(15deg);
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .message-container {
            display: flex;
            flex-direction: column;
            gap: 15px;
            padding: 10px;
        }
        
        .message-header {
            font-size: 0.9em;
            margin-bottom: 5px;
            opacity: 0.8;
        }
        
        .message-time {
            font-size: 0.8em;
            opacity: 0.6;
            margin-top: 5px;
        }
        
        .bot-content {
            margin-top: 10px;
            line-height: 1.5;
        }
        
        /* Solution styling dalam bubble */
        .bot-message .solution-section {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 15px;
            padding: 15px;
            margin-top: 15px;
        }
        
        .bot-message .step-item {
            background: rgba(255, 192, 203, 0.1);
            border-left: 3px solid #ff69b4;
            padding: 10px 15px;
            margin: 8px 0;
            border-radius: 0 10px 10px 0;
            transition: all 0.3s ease;
        }
        
        .bot-message .step-item:hover {
            transform: translateX(5px);
            background: rgba(255, 192, 203, 0.2);
        }
        
        .bot-message .tips-section {
            background: rgba(255, 20, 147, 0.05);
            border-radius: 10px;
            padding: 12px 15px;
            margin-top: 15px;
            border-left: 3px solid #ff1493;
        }
        
        /* Input field styling */
        .stTextInput input {
            flex: 1;
            padding: 15px;
            border: 1px solid rgba(255, 20, 147, 0.2);
            border-radius: 10px;
            font-size: 1em;
        }
        
        .stTextInput input:focus {
            outline: none;
            border-color: #ff1493;
            box-shadow: 0 0 5px rgba(255, 20, 147, 0.3);
        }
        
        /* Button styling */
        .stButton button {
            padding: 15px 30px;
            background: linear-gradient(135deg, #ff69b4, #ff1493);
            border: none;
            border-radius: 10px;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 20, 147, 0.4);
        }
        
        /* Solution sections */
        .solution-section {
            margin: 15px 0;
            padding-left: 20px;
        }
        
        .solution-title {
            font-weight: 600;
            color: #ff1493;
            margin-bottom: 10px;
        }
        
        .step-item {
            margin: 8px 0;
            padding: 8px 15px;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 8px;
            border-left: 3px solid #ff69b4;
        }
        
        .tips-section {
            margin-top: 15px;
            padding: 12px 15px;
            background: rgba(255, 105, 180, 0.1);
            border-left: 3px solid #ff1493;
            border-radius: 4px;
            color: #ff1493;
        }
        
        /* Logo styling */
        h1 {
            color: #ff1493;
            font-size: 28px;
            text-align: center;
            margin-top: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        /* Form container */
        form {
            display: flex;
            gap: 15px;
            margin-top: 15px;
            background: transparent;
            border: none;
            box-shadow: none;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .main > div {
                flex-direction: column;
            }
            
            .stButton button {
                width: 100%;
            }
        }
        
        /* Follow-up question styling */
        .follow-up-question {
            margin-top: 20px;
            padding: 10px 15px;
            background: linear-gradient(135deg, #ffe6ea, #ffd1dc);
            border-radius: 10px;
            font-weight: 500;
            color: #ff1493;
            text-align: center;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.02);
            }
            100% {
                transform: scale(1);
            }
        }
        
        /* Sidebar title styling */
        .sidebar-title {
            background: linear-gradient(135deg, #ff69b4, #ff1493);
            padding: 15px 20px;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: bold;
            font-size: 24px;
            animation: glow 2s ease-in-out infinite;
        }
        
        @keyframes glow {
            0% {
                box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
            }
            50% {
                box-shadow: 0 4px 25px rgba(255, 105, 180, 0.5);
            }
            100% {
                box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown('<div class="sidebar-title">Beauty Helper</div>', unsafe_allow_html=True)

    # Main chat container
    container = st.container()
    with container:
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Halo! 👋 Saya dapat membantu anda untuk memberi informasi permasalahan kulit seperti kulit kering, kulit berminyak, kulit berjerawat dan kulit sensitif. Apa keluhan Anda?"}
            ]

        # Display chat messages
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.markdown(f"""
                    <div class="message-container">
                        <div class="user-message">
                            <div class="message-header">Anda</div>
                            {message['content']}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="message-container">
                        <div class="bot-message">
                            <div class="message-header">Beauty Helper</div>
                            <div class="bot-content">{message['content']}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

        # Chat input form
        with st.form(key='chat_form', clear_on_submit=True):
            cols = st.columns([4, 1])
            with cols[0]:
                user_input = st.text_input("Tulis permasalahan wajah yang kamu alami...", 
                                         key="user_input")
            with cols[1]:
                submit_button = st.form_submit_button("Kirim")

            if submit_button and user_input:
                st.session_state.messages.append({"role": "user", "content": user_input})
                response = get_skin_problem_response(user_input)
                
                if response:
                    if response["type"] == "follow_up":
                        response_text = response["content"]
                    else:
                        response_text = f"""**Analisis:**
{response['analisis']}

**Solusi:**
{chr(10).join(response['solusi'])}

**Tips:**
{response['tips']}

💭 *Apakah ada yang ingin ditanyakan lagi?*"""
                else:
                    response_text = """Maaf, saya tidak memahami masalah kulit yang Anda sebutkan. 
Mohon jelaskan lebih detail tentang kondisi kulit Anda, misalnya apakah:
• Kulit kering
• Kulit berminyak
• Kulit sensitif
• Berjerawat"""

                st.session_state.messages.append({"role": "assistant", "content": response_text})
                st.rerun()

if __name__ == "__main__":
    main()
