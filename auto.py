
# import streamlit as st
# import cv2
# import numpy as np
# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor
# import os
# import tempfile
# from sklearn.model_selection import train_test_split
# import uuid  

# model = None
# results_file = "results.csv"


# def train_model():
#     global model
#     df = pd.read_csv('nm RGB.csv') 

#     x = df.drop(columns=['nm'], axis=1)
#     y = df['nm']
#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) 

#     model = RandomForestRegressor(n_estimators=100, random_state=42)
#     model.fit(x_train, y_train)


# def get_average_color(video_file_path):
#     cap = cv2.VideoCapture(video_file_path)
#     if not cap.isOpened():
#         return {'error': 'Unable to open video'}
    
#     ret, frame = cap.read()
#     if not ret:
#         return {'error': 'Unable to read the first frame'}
    
#     point1 = (846, 577)
#     point2 = (850, 577)
#     point3 = (845, 619)
#     point4 = (860, 633)

#     x_values = [point1[0], point2[0], point3[0], point4[0]]
#     y_values = [point1[1], point2[1], point3[1], point4[1]]
#     x_min, x_max = min(x_values), max(x_values)
#     y_min, y_max = min(y_values), max(y_values)

#     cropped = frame[y_min:y_max, x_min:x_max]
#     resized = cv2.resize(cropped, (1, 1), interpolation=cv2.INTER_AREA)
#     average_color = resized[0, 0].tolist()  

#     cap.release()
#     return average_color


# def predict_nm_from_rgb(rgb_color):
#     predicted_nm = model.predict([rgb_color])
#     return predicted_nm[0]


# def save_result(unique_id, rgb_color, nm_value):
#     if not os.path.exists(results_file):

#         with open(results_file, 'w') as f:
#             f.write("ID,Red,Green,Blue,Predicted Wavelength\n")
    
#     with open(results_file, 'a') as f:
#         f.write(f"{unique_id},{rgb_color[0]},{rgb_color[1]},{rgb_color[2]},{nm_value}\n")


# def main():
#     st.set_page_config(page_title="Predict Wavelength from Video", page_icon=":movie_camera:", layout="centered")
    
#     train_model()
#     st.title("Predict Wavelength from Video")
#     uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])
    
#     if uploaded_file is not None:
#         st.video(uploaded_file)
#         st.write("Processing your video...")

#         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
#             tmp_file.write(uploaded_file.getbuffer())
#             temp_file_path = tmp_file.name

#         average_color = get_average_color(temp_file_path)
#         os.remove(temp_file_path)
#         if 'error' in average_color:
#             st.error(average_color['error'])
#         else:
#             nm_value = predict_nm_from_rgb(average_color)
#             unique_id = str(uuid.uuid4())
#             save_result(unique_id, average_color, nm_value)  
            
#             st.subheader("Predicted Results:")
#             st.write(f"ID: {unique_id}")
#             st.write(f"Predicted Wavelength (nm): {nm_value}")
#             st.write(f"RGB Color: {average_color}")
 
#     if st.button("Return to Home"):
#         st.markdown(
#             f'<a href="index.html" target="_self"><button>Go to Home Page</button></a>',
#             unsafe_allow_html=True
#         )

# if __name__ == "__main__":
#     main()
import streamlit as st
import pandas as pd
import os
import cv2
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import uuid
import tempfile

# File Paths
results_file = "results.csv"
model = None

def train_model():
    global model
    df = pd.read_csv('nm RGB.csv') 

    x = df.drop(columns=['nm'], axis=1)
    y = df['nm']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) 

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

def get_average_color(video_file_path):
    cap = cv2.VideoCapture(video_file_path)
    if not cap.isOpened():
        return {'error': 'Unable to open video'}
    
    ret, frame = cap.read()
    if not ret:
        return {'error': 'Unable to read the first frame'}
    
    point1 = (846, 577)
    point2 = (850, 577)
    point3 = (845, 619)
    point4 = (860, 633)

    x_values = [point1[0], point2[0], point3[0], point4[0]]
    y_values = [point1[1], point2[1], point3[1], point4[1]]
    x_min, x_max = min(x_values), max(x_values)
    y_min, y_max = min(y_values), max(y_values)

    cropped = frame[y_min:y_max, x_min:x_max]
    resized = cv2.resize(cropped, (1, 1), interpolation=cv2.INTER_AREA)
    average_color = resized[0, 0].tolist()  

    cap.release()
    return average_color

def predict_nm_from_rgb(rgb_color):
    predicted_nm = model.predict([rgb_color])
    return predicted_nm[0]

def save_result(unique_id, rgb_color, nm_value):
    if not os.path.exists(results_file):
        with open(results_file, 'w') as f:
            f.write("ID,Red,Green,Blue,Predicted Wavelength\n")
    
    with open(results_file, 'a') as f:
        f.write(f"{unique_id},{rgb_color[0]},{rgb_color[1]},{rgb_color[2]},{nm_value}\n")

def view_results():
    st.title("Results Viewer")
    
    if os.path.exists(results_file):
        df = pd.read_csv(results_file)
        st.write("Here are the details of your results:")
        st.dataframe(df)
    else:
        st.warning("No results found. Please run predictions first.")

def main():
 
    st.set_page_config(page_title="Predict Wavelength from Video", page_icon=":movie_camera:", layout="centered")
    
    train_model()
    
  
    menu = ["Predict Wavelength from Video", "View Previous Results"]
    choice = st.sidebar.selectbox("Select Option", menu)
    
    if choice == "Predict Wavelength from Video":
        uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])
        
        if uploaded_file is not None:
            st.video(uploaded_file)
            st.write("Processing your video...")

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
                tmp_file.write(uploaded_file.getbuffer())
                temp_file_path = tmp_file.name

            average_color = get_average_color(temp_file_path)
            os.remove(temp_file_path)
            
            if 'error' in average_color:
                st.error(average_color['error'])
            else:
                nm_value = predict_nm_from_rgb(average_color)
                unique_id = str(uuid.uuid4())
                save_result(unique_id, average_color, nm_value)  
                
                st.subheader("Predicted Results:")
                st.write(f"ID: {unique_id}")
                st.write(f"Predicted Wavelength (nm): {nm_value}")
                st.write(f"RGB Color: {average_color}")

    elif choice == "View Previous Results":
        view_results()

if __name__ == "__main__":
    main()

