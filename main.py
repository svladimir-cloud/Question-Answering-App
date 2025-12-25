import ML_model
import streamlit_app

if __name__ == "__main__":
    pipe = ML_model.pipe
    streamlit_app.start_app(pipe)
