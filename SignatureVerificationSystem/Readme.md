# SIGNATURE VERIFICATION SYSTEM

### About

find matches between original and sample signautures that wether the signatures are same or not
or weather check the signature with different type of position

### Requirements

from tkinter import \*
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import font
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import result_type
from signature3 import match1
from signature2 import match2
from generatepdffile import generatepdf
from \_path_config import xlsx_path
from \_path_config import chart_img_excel_file_path
from tkinter import filedialog
from fpdf import FPDF
import cv2
from skimage.metrics import structural_similarity as ssim
import statistics

### how output will work or how to use

- first take the input in the field as image
  (browse the image path or put the image path in field)

- images should be in jpg, png, jpeg format

1. while run it will show the first ui inter face with 2 text input fields i.e. original signature field and sample signature field (that what we want to know the signaure is genuin or furgery) and also there are 2 buttons named 'compare' and 'experimental compare'.

2. on clicking compare button it will match the original and smpale signature field images and show output in a message box wehter signatures are similar or not.

3. if we want to test some experimental values then we take it by clicking experimental button.

4. on clicking the experimental button it will show some additional fields to take input signatures in different positions like sitting, standing, sleeping, walking. also 2 buttons named 'store excel' and 'compare'.

5. here our main purpose is that to find which candidate would have maximum similarity in original signature with the samples taken in deifferent positions, so we find the position in which the signature is having maximum similarity with original.

6. when ever user give input to fields then he should use store excel button to store the data in a dataset named 'inputs.xlsx'. after storing several signatures of different candidates then after one can use the compare button.

7. onclicking the compare button it will check the signatures and match original with with each signatures in different positions and it shows the maximum similarity holding signature position in messesge box . and one more thing wether the signatures matched or not . (if result_value > THERESOLD VLAUE then matched otherwise not ; THERESOLD IS 83%)

8. then it will show the indivisual candidates chart graph of similarity matching. and at last all candidates average chart is shown.

9. also it will generate PDF files for all the candidates in dataset , and show the particular results of cadidates in PDF FORMAT.

### how the code works

- important files and folders

  - main.py
  - signature2.py
  - signature3.py
  - generatepdffile.py
  - \_path_config.py
  - inputs.xlsx
  - chart_imgs.xlsx

- folders
  - chartfolder
  - sign
  - pdfs

1. firstly open main.py and run it (program execution starts from here.)
2. while run it on first ui interface by clicking 'compare' button it will call the 'checksimilarity2()' function. after that in this function it will call the match2() in 'signature2.py file'. and after that it will show the output for first 2 input fields.

3. then when click on 'experimental compare' it willl call the 'show_additional_fields()' function and it will show the rest of fields and 2 buttons.

4. after that user can take all inputs and then when click on 'store_excel' button it will call the 'store_to_excel()' function. it will store the 5 signatures of cadidate (original, sitting , standing, sleeping, walking). from this function it will call to the 'write_to_excel()' function. and in this function it will write to the 'inputs.xlsx' file.

5. after storing of several candidates, now use the 'compare' button. it will call the 'read_excelfile()' function. this reads the excel dataset. from here it will call the 'checksimilarity()' function. from here it wll call te 'match1()' funciton in 'signature3.py' file.

6. after compilation of 'signature3.py' file, from 'match1()' it will call the 'avg_ssim()' function then at last the 'match1()' returns the value to 'checksimilarity()' in 'main.py'. then it calculates 2 max values in 2d list for each candidate. from that again find one max value.

7. after that it will plot match graphs for each candidate in dataset and store that data in 'chartfolder'. from there it will put all graphs in 'chart_imgs.xlsx' file.

8. after that it will show a avg graph of all candidates. and then show a messagebox in which it show results for all students.

9. after that it will generate pdf file all student. it will call the 'generatepdf()' in 'generatepdffile.py'.

10. after that if we want then clear the whole data of 'inputs.xlsx' by clicking 'clear excel' button.

### About developers

- ARUN KUMAR SAHU
  E-MAIL: aurnkumarsahu634@gmail.com
  INSTAGRAM: **arunsahu_98**
- BISWAJEET PATTNAYAK
  E-MAIL: biswajeetpattnayak123@gmail.com
  INSTAGRAM: **biswajeet_76**
