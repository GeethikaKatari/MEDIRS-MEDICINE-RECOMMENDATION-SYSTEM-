import streamlit as st
import base64

# Dummy credentials for login
USERNAME = "admin"
PASSWORD = "password"

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'agreed' not in st.session_state:
    st.session_state['agreed'] = False

# Login function
def login(username, password):
    if username == USERNAME and password == PASSWORD:
        st.session_state['logged_in'] = True
    else:
        st.error("Incorrect username or password")

# Logout function
def logout():
    st.session_state['logged_in'] = False
    st.session_state['agreed'] = False

# Medicine recommendation function (dummy function)
def recommend_medicine(symptoms):
    # Placeholder function - replace with your actual model/prediction logic
    
    # Define recognized symptoms and corresponding responses
    symptom_responses = {
        "itching": (
            "Eczema",
            "A skin condition that causes dry, itchy, inflamed skin.",
            ["Moisturize regularly", "Avoid scratching", "Use mild soap"],
            ["Hydrocortisone cream", "Antihistamines"],
            ["Yoga", "Meditation"],
            ["Omega-3 fatty acids", "Vitamin E supplements"]
        ),
        "sleeping": (
            "Insomnia",
            "A common sleep disorder characterized by difficulty falling asleep or staying asleep.",
            ["Establish a bedtime routine", "Limit caffeine intake", "Exercise regularly"],
            ["Melatonin supplements", "Prescription sleep medications"],
            ["Tai chi", "Deep breathing exercises"],
            ["Avoid heavy meals before bedtime", "Limit exposure to screens before sleep"]
        ),
        "aching": (
            "Muscle Strain",
            "An injury to a muscle or tendon, resulting in pain and inflammation.",
            ["Rest the affected muscle", "Apply ice packs", "Use compression bandages"],
            ["Over-the-counter pain relievers", "Muscle relaxants"],
            ["Gentle stretching", "Swimming"],
            ["Stay hydrated", "Include protein-rich foods in your diet"]
        ),
        "fever": (
            "Flu",
            "A viral infection that affects the respiratory system, causing fever, chills, and body aches.",
            ["Get plenty of rest", "Stay hydrated", "Use a humidifier"],
            ["Antiviral medications (e.g., Oseltamivir)", "Over-the-counter pain relievers"],
            ["Light exercise (if tolerated)", "Yoga or Pilates"],
            ["Consume clear fluids", "Eat easily digestible foods like soup"]
        ),
        "headache": (
            "Migraine",
            "A type of headache characterized by throbbing pain, often accompanied by nausea and sensitivity to light and sound.",
            ["Rest in a quiet, dark room", "Apply cold compresses to the head", "Try relaxation techniques"],
            ["Triptans", "Over-the-counter pain relievers (e.g., ibuprofen)"],
            ["Gentle stretching", "Walking"],
            ["Avoid trigger foods (e.g., caffeine, alcohol)", "Stay hydrated"]
        ),
        "stomach pain": (
            "Gastritis",
            "Inflammation of the lining of the stomach, causing abdominal pain and discomfort.",
            ["Avoid irritating foods (e.g., spicy or acidic foods)", "Eat smaller, more frequent meals", "Avoid alcohol and caffeine"],
            ["Antacids", "Proton pump inhibitors (e.g., omeprazole)"],
            ["Gentle yoga", "Walking"],
            ["Eat a bland diet (e.g., bananas, rice, applesauce, toast)", "Drink herbal teas (e.g., ginger tea)"]
        ),
        "hormone imbalance": (
            "Hormonal Imbalance",
            "An imbalance in hormone levels, which can cause a variety of symptoms depending on the specific hormones involved.",
            ["Consult with a healthcare professional for personalized treatment", "Maintain a healthy lifestyle (e.g., balanced diet, regular exercise)"],
            ["Hormone replacement therapy (if necessary)", "Birth control pills (for certain hormonal imbalances)"],
            ["Cardio exercises", "Strength training"],
            ["Eat a balanced diet with plenty of fruits, vegetables, and whole grains", "Limit processed foods and refined sugars"]
        ),
        "loss of appetite": (
            "Anorexia",
            "A decrease in appetite or lack of desire to eat, often associated with medical or psychological conditions.",
            ["Eat small, frequent meals", "Choose nutrient-dense foods", "Consider nutritional supplements"],
            ["Appetite stimulants (e.g., Megestrol)", "Medications to address underlying conditions (if applicable)"],
            ["Light aerobic exercises", "Yoga or meditation"],
            ["Focus on consuming high-calorie, high-protein foods", "Drink smoothies or shakes with added protein"]
        ),
        "nausea": (
            "Gastroenteritis",
            "Inflammation of the stomach and intestines, typically caused by a viral or bacterial infection, leading to nausea, vomiting, and diarrhea.",
            ["Stay hydrated with clear fluids", "Eat bland, easy-to-digest foods", "Rest and avoid strenuous activity"],
            ["Antiemetic medications (e.g., Ondansetron)", "Over-the-counter nausea relief (e.g., Pepto-Bismol)"],
            ["Gentle walks or light activity (as tolerated)", "Deep breathing exercises"],
            ["Avoid spicy, greasy, or heavy foods", "Consume clear liquids like ginger ale or broth"]
        ),
        "skin rash": (
            "Dermatitis",
            "An allergic reaction or irritation of the skin caused by contact with a specific substance.",
            ["Identify and avoid the triggering substance", "Apply soothing lotions or creams", "Use cool compresses to reduce itching"],
            ["Topical corticosteroids", "Antihistamines (for itching)"],
            ["Gentle swimming", "Low-impact exercises like cycling"],
            ["Take lukewarm baths with colloidal oatmeal", "Apply calamine lotion to affected areas"]
        ),
        "cough": (
            "Bronchitis",
            "Inflammation of the bronchial tubes, causing coughing, chest discomfort, and difficulty breathing.",
            ["Get plenty of rest", "Stay hydrated", "Use a humidifier"],
            ["Cough suppressants (e.g., Dextromethorphan)", "Expectorants"],
            ["Gentle walks or light exercise (as tolerated)", "Deep breathing exercises"],
            ["Stay hydrated with warm fluids", "Avoid irritants like smoke or pollutants"]
        ),
        "breathlessness": (
            "Asthma",
            "A chronic respiratory condition characterized by inflammation and narrowing of the airways, leading to difficulty breathing.",
            ["Use a rescue inhaler (e.g., Albuterol) as needed", "Avoid triggers (e.g., allergens, smoke)"],
            ["Inhaled corticosteroids", "Bronchodilators (e.g., Salbutamol)"],
            ["Yoga or breathing exercises", "Low-impact activities like swimming"],
            ["Identify and avoid triggers", "Consider allergy testing if applicable"]
        ),
        "chest pain": (
            "Angina",
            "Chest pain or discomfort caused by reduced blood flow to the heart muscles.",
            ["Rest", "Take nitroglycerin as prescribed", "Seek emergency medical attention if severe or persistent"],
            ["Aspirin", "Nitroglycerin tablets or spray"],
            ["Avoid strenuous activities", "Light walking or stretching"],
            ["Maintain a heart-healthy diet", "Monitor blood pressure and cholesterol levels"]
        ),
        "neck pain": (
            "Muscle Strain",
            "Injury to the muscles or ligaments in the neck, often caused by sudden movements or poor posture.",
            ["Apply ice or heat packs", "Take over-the-counter pain relievers", "Use a neck brace if recommended by a healthcare professional"],
            ["Muscle relaxants", "Pain medications (e.g., ibuprofen)"],
            ["Gentle neck stretches", "Low-impact exercises like swimming or cycling"],
            ["Practice good posture", "Use ergonomic pillows or support devices"]
        ),
        "dizziness": (
            "Vertigo",
            "A sensation of spinning or imbalance, often caused by problems in the inner ear or the brain.",
            ["Sit or lie down until the dizziness passes", "Stay hydrated", "Avoid sudden movements"],
            ["Antihistamines (e.g., Meclizine)", "Anti-nausea medications"],
            ["Balance exercises", "Tai chi or yoga"],
            ["Avoid caffeine and alcohol", "Get plenty of sleep"]
        ),
        "joint pain": (
            "Arthritis",
            "Inflammation of the joints, causing pain, stiffness, and reduced range of motion.",
            ["Stay physically active", "Apply hot or cold packs", "Consider physical therapy"],
            ["Nonsteroidal anti-inflammatory drugs (NSAIDs)", "Disease-modifying antirheumatic drugs (DMARDs)"],
            ["Low-impact exercises like swimming or cycling", "Yoga or Pilates"],
            ["Maintain a healthy weight", "Eat a balanced diet rich in omega-3 fatty acids"]
        ),
        "continuous sneezing": (
            "Allergic Rhinitis",
            "Inflammation of the nasal passages due to allergens, causing sneezing, congestion, and itching.",
            ["Avoid allergens (e.g., pollen, dust mites)", "Use air purifiers or filters", "Keep windows closed during peak pollen seasons"],
            ["Antihistamines (e.g., Loratadine)", "Nasal corticosteroids"],
            ["Indoor exercises on high-pollen days", "Yoga or stretching"],
            ["Keep indoor air clean and dry", "Regularly clean bedding and carpets"]
        ),
         "vomiting": (
            "Gastroenteritis",
            "Inflammation of the stomach and intestines, typically caused by a viral or bacterial infection, leading to nausea, vomiting, and diarrhea.",
            ["Stay hydrated with clear fluids", "Eat bland, easy-to-digest foods", "Rest and avoid strenuous activity"],
            ["Antiemetic medications (e.g., Ondansetron)", "Over-the-counter nausea relief (e.g., Pepto-Bismol)"],
            ["Gentle walks or light activity (as tolerated)", "Deep breathing exercises"],
            ["Avoid spicy, greasy, or heavy foods", "Consume clear liquids like ginger ale or broth"]
        ),
        "indigestion": (
            "Gastritis",
            "Inflammation of the lining of the stomach, causing abdominal pain and discomfort.",
            ["Avoid irritating foods (e.g., spicy or acidic foods)", "Eat smaller, more frequent meals", "Avoid alcohol and caffeine"],
            ["Antacids", "Proton pump inhibitors (e.g., omeprazole)"],
            ["Gentle yoga", "Walking"],
            ["Eat a bland diet (e.g., bananas, rice, applesauce, toast)", "Drink herbal teas (e.g., ginger tea)"]
        ),
       
        "patches in throat": (
            "Pharyngitis (Sore Throat)",
            "Inflammation of the throat, typically due to a viral or bacterial infection.",
            ["Get plenty of rest", "Drink warm liquids (e.g., tea with honey)", "Gargle with salt water"],
            ["Pain relievers (e.g., ibuprofen, acetaminophen)", "Throat lozenges or sprays"],
            ["Avoid irritants like smoke or pollutants", "Use a humidifier"],
            ["Stay hydrated", "Consume soothing foods like soup or broth"]
        ),
        "restlessness": (
            "Anxiety",
            "A mental health condition characterized by feelings of worry, nervousness, or unease.",
            ["Practice relaxation techniques (e.g., deep breathing, meditation)", "Engage in physical activity", "Seek support from friends, family, or a therapist"],
            ["Selective serotonin reuptake inhibitors (SSRIs)", "Benzodiazepines (for short-term relief of severe anxiety)"],
            ["Yoga or tai chi", "Aerobic exercises like jogging or cycling"],
            ["Limit caffeine intake", "Maintain a regular sleep schedule"]
        ),
        "weight loss": (
            "Hyperthyroidism",
            "An overactive thyroid gland, leading to an increase in metabolism and unintended weight loss.",
            ["Eat regular, balanced meals", "Increase calorie intake with healthy snacks", "Consult with a healthcare professional for personalized dietary advice"],
            ["Antithyroid medications (e.g., Methimazole)", "Radioactive iodine therapy (for long-term management)"],
            ["Resistance training to build muscle", "Aerobic exercises like walking or swimming"],
            ["Include nutrient-dense foods in your diet", "Monitor weight regularly"]
        ),
        "dehydration": (
            "Dehydration",
            "A condition where the body loses more fluid than it takes in, leading to symptoms like thirst, dry mouth, and fatigue.",
            ["Drink plenty of fluids (water, oral rehydration solutions)", "Rest in a cool, shaded area", "Avoid strenuous activity"],
            ["Oral rehydration salts (ORS)", "Intravenous (IV) fluids for severe cases"],
            ["Sip water or electrolyte drinks regularly", "Use cool compresses to reduce body temperature"],
            ["Avoid sugary or caffeinated beverages", "Monitor urine color for hydration status"]
        ),
        "watering from eyes": (
            "Allergic Conjunctivitis (Eye Allergies)",
            "Inflammation of the conjunctiva (the tissue lining the inside of the eyelids and covering the white part of the eye) due to allergens.",
            ["Avoid allergens (e.g., pollen, dust)", "Use cool compresses to soothe the eyes", "Avoid rubbing the eyes"],
            ["Antihistamine eye drops", "Mast cell stabilizers"],
            ["Indoor activities on high-pollen days", "Wear sunglasses outdoors to protect against pollen"],
            ["Regularly clean bedding and upholstery", "Use air purifiers or filters indoors"]
        ),
        
    }
    

    
    # Check if any recognized symptoms are present
    recognized_symptoms = [symptom.lower() for symptom in symptoms.split(",")]
    for symptom in recognized_symptoms:
        if symptom in symptom_responses:
            predicted_disease, dis_des, my_precautions, medications, my_workouts, my_diets = symptom_responses[symptom]
            return predicted_disease, dis_des, my_precautions, medications, my_workouts, my_diets
    
    # If no recognized symptoms are present, return unknown
    return "Unknown", "Symptom is not recognized. Please enter valid symptoms.", [], [], [], []

# Login page with background image
def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(username, password)

# Agreement page
def agreement_page():
    st.title("Agreement Page")
    st.write("Please read and agree to the instructions below before proceeding.")
    
    # Instructions
    st.write("""
    **Instructions for Using the Medicine Recommendation System Application:**
    
    1. **Login**: Enter your username and password on the login page. Click the 'Login' button to proceed.
    
    2. **Agreement**: Read the instructions carefully. Check the box indicating your agreement to the instructions.
    
    3. **Enter Symptoms**: On the medicine recommendation page, enter your symptoms in the provided text box. 
       - Example: `itching, sleeping, aching`
    
    4. **Predict**: Click the 'Predict' button to receive recommendations.
    
    5. **View Results**: The application will display:
       - **Predicted Disease**: The likely condition based on your symptoms.
       - **Description**: Details about the predicted disease.
       - **Precautions**: Suggested precautions to manage or prevent the condition.
       - **Medications**: Recommended medications.
       - **Workouts**: Suitable exercises or physical activities.
       - **Diets**: Dietary recommendations.
    
    6. **Logout**: Click the 'Logout' button to log out of the application.
    
    **Disclaimer**: This application provides recommendations based on general medical information. 
    Consult a healthcare professional for personalized medical advice.
    """)

    agree = st.checkbox("I agree to the instructions")
    if agree and st.button("OK"):
        st.session_state['agreed'] = True

# Medicine recommendation page
def recommendation_page():
    st.title("Medicine Recommendation System")
    
    # Base64 encoded image
    image_base64 = base64.b64encode(open("C:\\Users\\Prudhvi\\OneDrive\\Desktop\\java ad-30\\MEDIRS\\download.jpeg", "rb").read()).decode()

    background_css = f"background-image: url(data:image/jpg;base64,{image_base64}); background-size: cover;"
    st.markdown(f"""
        <style>
        .reportview-container {{
            {background_css}
        }}
        </style>
    """, unsafe_allow_html=True)
    
    # Input symptoms
    symptoms = st.text_input("Enter Symptoms", placeholder="e.g., itching, sleeping, aching")

    if st.button("Predict"):
        if symptoms:
            predicted_disease, dis_des, my_precautions, medications, my_workouts, my_diets = recommend_medicine(symptoms)
            
            # Display results
            st.subheader("Predicted Disease")
            st.write(predicted_disease)

            st.subheader("Description")
            st.write(dis_des)

            st.subheader("Precautions")
            st.write(", ".join(my_precautions))

            st.subheader("Medications")
            st.write(", ".join(medications))

            st.subheader("Workouts")
            st.write(", ".join(my_workouts))

            st.subheader("Diets")
            st.write(", ".join(my_diets))
        else:
            st.error("Please enter symptoms")

    if st.button("Logout"):
        logout()

# Main application logic
if st.session_state['logged_in']:
    if st.session_state['agreed']:
        recommendation_page()
    else:
        agreement_page()
else:
    login_page()
