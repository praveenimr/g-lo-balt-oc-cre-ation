import os

os.system("pip install -r requirements.txt")
os.system("streamlit run app.py --server.port=8501 --server.address=0.0.0.0")
