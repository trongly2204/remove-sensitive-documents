SENSITIVE TEXT REDACTION API - SETUP & USAGE GUIDE
==================================================

REQUIREMENTS FOR PYTHON INSTALLING
----------------------------------
Install the following Python libraries and tools:

- spacy
- en_core_web_trf (SpaCy transformer model)
- requests
- flask
- transformers
- torch>=1.10.0
- pandas

REQUIREMENTS FOR PYTHON IMPORTS
-------------------------------
Ensure your scripts include these imports:

import re
import requests
import spacy
import pandas as pd
from flask import Flask, request, jsonify

HOW TO INSTALL
--------------
1. Install all required libraries using:

   pip install -r requirements.txt

2. Download the SpaCy transformer model using:

   python -m spacy download en_core_web_trf

HOW TO RUN THE PROJECT
----------------------
1. Ensure you are in the folder that contains app.py

2. Start the Flask API server:
   > python app.py

3. Open a new terminal or command prompt and run the main script:
   > python main.py

4. When prompted, input the name of your text file (e.g., input.txt)

5. The program will:
   - Read and display the original text with sensitive data
   - Sanitize and print the cleaned version
   - Save the sanitized version to 'output.txt'

FILES EXPECTED IN PROJECT DIRECTORY
-----------------------------------
- app.py               -> Hosts the Flask API
- main.py              -> Sends request to the API
- regex_detector.py    -> Contains regex_method
- ner_detector.py      -> Contains ner_method
- input.txt            -> Your input text file
- output.txt           -> Auto-generated sanitized result
- requirements.txt     -> Python package dependencies
- README.txt           -> This instruction file
