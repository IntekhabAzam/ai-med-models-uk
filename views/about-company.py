import streamlit as st
from utils import get_img_as_base64


clients1 = get_img_as_base64("assets/clients1.png")
clients2 = get_img_as_base64("assets/clients2.png")

# Include Font Awesome for icons
st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)


# Company overview
st.markdown("""
    <div className="company-overview" style="
        background: #fff; 
        padding: 32px; 
        border-radius: 16px; 
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1); 
        margin-bottom: 5rem;">
        <div style=" 
            text-align: center; 
            margin-bottom: 4rem;"
        >
            <div style="font-size: 3rem; font-weight: bold;">AI-MED MODELS LIMITED</div>
            <p style="font-size: 1.3rem;">Transforming Healthcare with Innovative AI</p>
        </div>
        <p style="color: #555; font-size: 1.1rem; margin-bottom: 30px;">
            <b style="color: #0D47A1;">AI-MED MODELS LIMITED</b>, is an Artificial Intelligence technology company based in the United Kingdom, aimed for the development of artificial Intelligence in the field of medical science and other sectors.
            <br><br>
            Through our innovative research and cutting-edge generative AI technology, we enable the early and highly accurate detection of diseases, saving valuable time and millions of dollars.
            <br><br>
            Artificial intelligence is revolutionizing healthcare, becoming a powerful tool that transforms the practice of medicine. Our AI advancements in healthcare outline a roadmap for developing effective, reliable, and safe AI solutions.
        </p>
    </div>
    <style>
        @media (max-width: 600px) {
            .company-overview {
                padding: 32px 20px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Vision Impact Section with Icons for Key Pillars
st.markdown("""
    <div style="text-align: center; margin-bottom: 1rem;">
        <div style="font-size: 2.25rem; color: #0D47A1; font-weight: bold;">Our Vision</div>
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
            
        /* Media Query for smaller devices */
        @media (max-width: 768px) {
            .vision-container {
                grid-template-columns: 1fr;  /* Stack cards into a single column */
            }
        }
    </style>
""", unsafe_allow_html=True)

# Cards inside Grid container
st.markdown("""
    <div class="vision-container">
        <div class="vision-card">
            <i class="fas fa-heartbeat" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>Health Accessibility</h4>
            <p>Enhance population health and improve patient care experiences by ensuring AI-driven healthcare solutions are accessible to all individuals worldwide, regardless of location or socioeconomic status.</p>
        </div>
        <div class="vision-card">
            <i class="fas fa-dollar-sign" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>Reducing Healthcare Costs</h4>
            <p>The increasing costs of healthcare worldwide are creating challenges for authorities, governments, hospitals, regulators, and providers, urging them to innovate and transform healthcare models to ensure the delivery of effective, high-quality care.</p>
        </div>
        <div class="vision-card">
            <i class="fas fa-chart-line" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>Transforming Healthcare Delivery</h4>
            <p>Leveraging real-world data-driven insights to transform care at scale, ensuring healthcare systems are more responsive and efficient.</p>
        </div>
        <div class="vision-card">
            <i class="fas fa-people-carry" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>Workforce Empowerment</h4>
            <p>The pandemic has highlighted workforce shortages and inequities in healthcare access. By addressing these challenges, AI tools assist healthcare workers in delivering timely care while reducing burnout.</p>
        </div>
        <div class="vision-card">
            <i class="fas fa-network-wired" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>Bridging Healthcare Gaps</h4>
            <p>AI helps bridge the gap between the supply and demand for healthcare staff employed by authorities and trusts, aligning workforce resources with the evolving healthcare needs of the global population.</p>
        </div>
        <div class="vision-card">
            <i class="fas fa-robot" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4>AI-Driven Supply and Demand Balance</h4>
            <p>The application of technology and artificial intelligence (AI) in healthcare has the potential to optimize staffing solutions and improve the allocation of resources, effectively addressing supply-and-demand challenges.</p>
        </div>
    </div>
""", unsafe_allow_html=True)


# AI Healthcare Transformation Section
st.markdown("""
    <div class="healthcare-transformation" style="
        background: #fff; 
        padding: 32px; 
        border-radius: 16px; 
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1); 
        margin-bottom: 5rem;">
        <div style="text-align: center; color: #0D47A1; font-weight: bold; font-size: 2.25rem; margin-bottom: 20px;">AI Healthcare Transformation</div>
        <p style="color: #555; font-size: 1.1rem; margin-bottom: 30px;">
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
            medical institutes, and research centers.
            <br><br>
            Many other innovative healthcare AI models are currently in our research and development stages.
        </p>
    </div>
    <style>
        @media (max-width: 600px) {
            .healthcare-transformation {
                padding: 32px 20px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)




# AI Innovations Section with Cards
st.markdown("""
    <div style="text-align: center; margin-bottom: 2.5rem;">
        <div style="font-size: 2.25rem; color: #0D47A1; font-weight: bold;">Our AI Innovations</div>
        <p style="color: #555; font-size: 1rem; margin-bottom: 1.5rem;">
            Explore how our AI-driven solutions will reshape healthcare:
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
            <i class="fas fa-brain" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4 style="color: #0D47A1; margin: 15px 0;">Brain Tumor Detection</h4>
            <p style="color: #555;">Early detection of brain cancer, meningioma, and other tumors using AI-enhanced CT and MRI scans before tumor progression.</p>
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
            <p style="color: #555;">AI-powered scans enable early detection of eye diseases like retinopathy, cataracts, glaucoma, and macular degeneration.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            background: #fff; 
            padding: 20px; 
            border-radius: 16px; 
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
            margin-bottom: 20px;">
                <i class="fas fa-ribbon" style="font-size: 2rem; color: #0D47A1;"></i>
                <h4 style="color: #0D47A1; margin: 15px 0;">Breast Cancer Detection</h4>
                <p style="color: #555;">AI helps detect breast cancer early using mammograms and MRI scans, improving treatment, monitoring, and recovery chances.</p>
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
            <h4 style="color: #0D47A1; margin: 15px 0;">Cardiovascular Disease Detection</h4>
            <p style="color: #555;">AI-powered scans enable early detection of cardiovascular diseases (CVD) through advanced data analysis.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            background: #fff; 
            padding: 20px; 
            border-radius: 16px; 
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
            margin-bottom: 20px;">
            <i class="fas fas fa-head-side-mask" style="font-size: 2rem; color: #0D47A1;"></i>
            <h4 style="color: #0D47A1; margin: 15px 0;">COPD Detection</h4>
            <p style="color: #555;">AI-powered early detection of Chronic Obstructive Pulmonary Disease (COPD) and other lung diseases using data analysis and scans.<br>Many other innovative healthcare AI models under our research and development stages.</p>
        </div>
    """, unsafe_allow_html=True)


# Our Clients Section
st.markdown("""
    <div style="text-align: center; margin-bottom: 2.5rem; margin-top: 4rem;">
        <div style="font-size: 2.25rem; color: #0D47A1; font-weight: bold;">Our Clients</div>
        <p style="color: #555; font-size: 1rem; margin-bottom: 1.5rem;">
            We are proud to work with a diverse group of clients across the healthcare industry:
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div>
        <img src="data:image/png;base64,{clients1}" alt="Client Image 1" style="width: 100%; height: auto; border-radius: 12px; margin-bottom: 20px;">
        <img src="data:image/png;base64,{clients2}" alt="Client Image 2" style="width: 100%; height: auto; border-radius: 12px">
    </div>
""", unsafe_allow_html=True)


# Call to Action Section
# st.markdown("""
#     <div style="
#         text-align: center; 
#         margin-top: 2rem; 
#         padding: 30px; 
#         background: #FFFFFF; 
#         border-radius: 16px; 
#         color: #0D47A1; 
#         box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
#         <h3 style="margin-bottom: 15px; color: #1976D2;">Ready to Revolutionize Healthcare?</h3>
#         <p style="font-size: 1.1rem; margin-bottom: 20px;">Join us in leveraging AI for better health outcomes and sustainable systems.</p>
#         <a href="https://www.aimedmodels.com" target="_blank" style="
#             display: inline-block; 
#             padding: 12px 35px; 
#             background-color: #1976D2; 
#             color: white; 
#             font-size: 1rem; 
#             border-radius: 8px; 
#             text-decoration: none; 
#             box-shadow: 0 3px 6px rgba(0, 0, 0, 0.15); 
#             transition: background-color 0.3s, transform 0.2s;">
#             Visit AI-MED Models
#         </a>
#         <div style="margin-top: 30px; font-size: 1rem; display: grid; grid-template-columns: 1fr 1fr; gap: 20px; width: 100%; max-width: 800px; margin: 30px auto;">
#             <div style="text-align: left; border-right: 2px solid #E3F2FD; padding-right: 20px;">
#                 <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
#                     <i class="fas fa-map-marker-alt" style="margin-right: 8px; color: #1976D2;"></i>
#                     <span><strong>Address</strong></span>
#                 </div>
#                 <p style="margin: 0; line-height: 1.5; text-align: center;">The Technocentre, Coventry University Technology Park, Puma Way, Coventry CV1 2TT, United Kingdom</p>
#             </div>
#             <div style="text-align: center; padding-left: 20px;">
#                 <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
#                     <i class="fas fa-envelope" style="margin-right: 8px; color: #1976D2;"></i>
#                     <span><strong>Email</strong></span>
#                 </div>
#                 <p style="margin: 0; line-height: 1.5;">
#                     <a href="mailto:info@aimedmodels.com" style="color: #0D47A1; text-decoration: none;">
#                         info@aimedmodels.com
#                     </a>
#                 </p>
#             </div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

st.markdown("""
    <div className="footer" style="
        text-align: center; 
        margin-top: 5rem; 
        padding: 32px; 
        background: #212121; 
        border-radius: 16px; 
        color: #E3F2FD; 
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);">
        <div style="font-size: 2.25rem; margin-bottom: 16px; color: #1976D2; font-weight: bold;">Ready to Revolutionize Healthcare?</div>
        <p style="font-size: 1.1rem; margin-bottom: 24px;">Connect with us in leveraging AI for better health outcomes and sustainable systems.</p>
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
        <div style="font-size: 1rem; display: grid; grid-template-columns: 1fr 1fr; gap: 16px; width: 100%; max-width: 800px; margin: 40px auto;">
            <div style="text-align: left; border-right: 2px solid #424242; padding-right: 20px;">
                <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 8px;">
                    <i class="fas fa-map-marker-alt" style="margin-right: 8px; color: #1976D2;"></i>
                    <span><strong>Address</strong></span>
                </div>
                <p style="margin: 0; line-height: 1.5; text-align: center;">The Technocentre, Coventry University Technology Park, Puma Way, Coventry CV1 2TT, United Kingdom</p>
            </div>
            <div style="text-align: center; padding-left: 20px;">
                <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 8px;">
                    <i class="fas fa-envelope" style="margin-right: 8px; color: #1976D2;"></i>
                    <span><strong>Email</strong></span>
                </div>
                <p style="margin: 0; line-height: 1.5;">
                    <a href="mailto:info@aimedmodels.com" style="color: #E3F2FD; text-decoration: none;">
                        info@aimedmodels.com
                    </a>
                </p>
            </div>
        </div>
    </div>
    <style>
        @media (max-width: 600px) {
            .footer {
                padding: 32px 20px !important;
            }
        }
    </style>
""", unsafe_allow_html=True)







