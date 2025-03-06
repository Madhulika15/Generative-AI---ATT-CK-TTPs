
!pip install transformers datasets gradio scikit-learn nltk
import os

print(os.listdir("/content"))


!pip install pandas openpyxl
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from google.colab import files
files.download("detected_results.csv")
!pip install gradio
import gradio as gr
