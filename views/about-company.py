import streamlit as st

# Include Font Awesome for icons
st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)


# Company overview
st.markdown("""
    <div style="
        background: #fff; 
        padding: 40px; 
        border-radius: 16px; 
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1); 
        margin-bottom: 5rem;">
        <div style=" 
            text-align: center; 
            margin-bottom: 4rem;"
        >
            <h1 style="font-size: 3rem; font-weight: bold;">AI-MED MODELS LIMITED</h1>
            <p style="font-size: 1.3rem;">Transforming Healthcare with Innovative AI</p>
        </div>
        <p style="text-align: justify; color: #555; font-size: 1.1rem; margin-bottom: 30px;">
            <b style="color: #0D47A1;">AI-MED MODELS LIMITED</b>, is an Artificial Intelligence technology company based in the United Kingdom, aimed for the development of artificial Intelligence in the field of medical science and other sectors.
            <br><br>
            Through our innovative research and cutting-edge generative AI technology, we enable the early and highly accurate detection of diseases, saving valuable time and millions of dollars. Artificial intelligence is revolutionizing healthcare, becoming a powerful tool that transforms the practice of medicine.
        </p>
    </div>
""", unsafe_allow_html=True)

# Vision Impact Section with Icons for Key Pillars
st.markdown("""
    <div style="text-align: center; margin-bottom: 1rem;">
        <h2 style="color: #0D47A1; font-weight: bold;">Our Vision</h2>
        <p style="color: #555; font-size: 1rem; margin-bottom: 1.5rem;">
            These core principles guide our mission and shape our innovative approach to transforming healthcare:
        </p>
    </div>
""", unsafe_allow_html=True)

# Create a card-like layout using Streamlit columns for Vision Pillars
st.markdown("""
    <style>
        .vision-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            align-items: stretch;
            margin-bottom: 6rem;
        }
        .vision-card {
            background: #fff;
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .vision-card h4 {
            color: #0D47A1;
            margin: 15px 0;
        }
        .vision-card p {
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

# Cards inside Grid container
st.markdown("""
    <div class="vision-container">
        <div class="vision-card">
            <i class="fas fa-heartbeat" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>Health Accessibility</h4>
            <p>Ensuring that AI-driven healthcare solutions are accessible to all individuals globally, regardless of location or socioeconomic status.</p>
        </div>
        <div class="vision-card">
            <i class="fas fa-dollar-sign" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>Reducing Healthcare Costs</h4>
            <p>AI innovations help reduce the rising costs of healthcare globally by optimizing resource utilization and improving efficiency in healthcare delivery.</p>
        </div>
        <div class="vision-card">
            <i class="fas fa-chart-line" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>Transforming Healthcare Delivery</h4>
            <p>Leveraging real-world data-driven insights to transform care at scale, ensuring healthcare systems are more responsive and efficient.</p>
        </div>
        <div class="vision-card">
            <i class="fas fa-people-carry" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>Workforce Empowerment</h4>
            <p>Addressing workforce shortages and inequities in healthcare access, AI tools help support healthcare workers in providing timely care while reducing burnout.</p>
        </div>
        <div class="vision-card">
            <i class="fas fa-network-wired" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>Bridging Healthcare Gaps</h4>
            <p>AI addresses the growing gap between supply and demand for healthcare staff, helping to match workforce resources with the healthcare needs of global populations.</p>
        </div>
        <div class="vision-card">
            <i class="fas fa-robot" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>AI-Driven Supply and Demand Balance</h4>
            <p>The application of AI in healthcare optimizes staffing solutions and improves the allocation of healthcare resources, ensuring a better balance between supply and demand.</p>
        </div>
    </div>
""", unsafe_allow_html=True)


# AI Healthcare Transformation Section
st.markdown("""
    <div style="
        background: #fff; 
        padding: 40px; 
        border-radius: 16px; 
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1); 
        margin-bottom: 5rem;">
        <h2 style="text-align: center; color: #0D47A1; font-weight: bold; font-size: 2rem; margin-bottom: 20px;">AI Healthcare Transformation</h2>
        <p style="text-align: justify; color: #555; font-size: 1.1rem; margin-bottom: 30px;">
            The increasing availability of multi-modal data, including genomics, economic, demographic, clinical, and phenotypic data, 
            coupled with advancements in technology such as mobile, internet, computing power, and data security, marks a moment 
            of convergence between healthcare and technology. This convergence has the potential to fundamentally transform 
            healthcare delivery models.
            <br><br>
            AI in healthcare excels in its ability to learn and recognize patterns from large, multi-dimensional, and multi-modal 
            datasets. This capability is key to enabling more accurate predictions, faster diagnoses, and better patient outcomes.
            <br><br>
            Our innovative AI models are already being developed and are suitable for deployment in government hospitals, 
            health ministries, and medical research institutions. These entities, with their massive healthcare budgets, are 
            well-positioned to leverage the power of AI technologies, accelerating the adoption of these advancements in hospitals, 
            institutes of medical science, and research centers.
            <br><br>
            Many other innovative healthcare AI models under our research and development stages.
        </p>
    </div>
""", unsafe_allow_html=True)




# AI Innovations Section with Cards
st.markdown("""
    <div style="text-align: center; margin-bottom: 2.5rem;">
        <h2 style="color: #0D47A1; font-weight: bold;">Our AI Innovations</h2>
        <p style="color: #555; font-size: 1rem; margin-bottom: 1.5rem;">
            Explore how our AI-driven solutions are reshaping healthcare:
        </p>
    </div>
""", unsafe_allow_html=True)

# Create a card-like layout using Streamlit columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div style="
            background: #fff; 
            padding: 20px; 
            border-radius: 16px; 
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
            margin-bottom: 20px;">
            <i class="fas fa-lungs" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4 style="color: #0D47A1; margin: 15px 0;">Lung Cancer Detection</h4>
            <p style="color: #555;">Early detection of carcinoma and malignant tumors ensures timely, life-saving treatment.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            background: #fff; 
            padding: 20px; 
            border-radius: 16px; 
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
            margin-bottom: 20px;">
            <i class="fas fa-heart" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4 style="color: #0D47A1; margin: 15px 0;">Cardiovascular Disease</h4>
            <p style="color: #555;">Proactively detect heart conditions using AI-driven data analysis and imaging.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style="
            background: #fff; 
            padding: 20px; 
            border-radius: 16px; 
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
            margin-bottom: 20px;">
            <i class="fas fa-brain" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4 style="color: #0D47A1; margin: 15px 0;">Brain Tumor Detection</h4>
            <p style="color: #555;">AI-integrated scans enable precise diagnosis of brain tumors before progression.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            background: #fff; 
            padding: 20px; 
            border-radius: 16px; 
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
            margin-bottom: 20px;">
            <i class="fas fa-eye" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4 style="color: #0D47A1; margin: 15px 0;">Eye Disease Detection</h4>
            <p style="color: #555;">Detect retinopathy, glaucoma, and cataracts early with AI-powered analysis.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style="
        background: #fff; 
        padding: 20px; 
        border-radius: 16px; 
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
        text-align: center;
        margin: 0 auto 5rem; width: 100%; max-width: 600px;">
        <i class="fas fa-ribbon" style="font-size: 2rem; color: #0D47A1;"></i>
        <h4 style="color: #0D47A1; margin: 15px 0;">Breast Cancer Detection</h4>
        <p style="color: #555;">AI helps detect breast cancer early using mammograms and MRI scans, improving treatment success.</p>
    </div>
""", unsafe_allow_html=True)

# Call to Action Section
st.markdown("""
    <div style="
        text-align: center; 
        margin-top: 2rem; 
        padding: 30px; 
        background: #FFFFFF; 
        border-radius: 16px; 
        color: #0D47A1; 
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
        <h3 style="margin-bottom: 15px; color: #1976D2;">Ready to Revolutionize Healthcare?</h3>
        <p style="font-size: 1.1rem; margin-bottom: 20px;">Join us in leveraging AI for better health outcomes and sustainable systems.</p>
        <a href="https://www.aimedmodels.com" target="_blank" style="
            display: inline-block; 
            padding: 12px 35px; 
            background-color: #1976D2; 
            color: white; 
            font-size: 1rem; 
            border-radius: 8px; 
            text-decoration: none; 
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15); 
            transition: background-color 0.3s, transform 0.2s;">
            Visit AI-MED Models
        </a>
        <div style="margin-top: 30px; font-size: 1rem; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; width: 100%; max-width: 800px; margin: 30px auto;">
            <div style="text-align: left; border-right: 2px solid #E3F2FD; padding-right: 20px;">
                <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
                    <i class="fas fa-map-marker-alt" style="margin-right: 8px; color: #1976D2;"></i>
                    <span><strong>Address</strong></span>
                </div>
                <p style="margin: 0; line-height: 1.5; text-align: center;">The Technocentre, Coventry University Technology Park, Puma Way, Coventry CV1 2TT, United Kingdom</p>
            </div>
            <div style="text-align: center; padding-left: 20px;">
                <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
                    <i class="fas fa-envelope" style="margin-right: 8px; color: #1976D2;"></i>
                    <span><strong>Email</strong></span>
                </div>
                <p style="margin: 0; line-height: 1.5;">
                    <a href="mailto:info@aimedmodels.com" style="color: #0D47A1; text-decoration: none;">
                        info@aimedmodels.com
                    </a>
                </p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)





