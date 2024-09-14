from tkinter import *
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
from _path_config import xlsx_path
from _path_config import chart_img_excel_file_path

from tkinter import filedialog

# Mach Threshold
THRESHOLD = 83


def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.delete(0, tk.END)
    ent.insert(tk.END, filename)  # add this




# # condition will check true or false

def checkSimilarity2(window, path1, path2):
    result2 = match2(path1,path2)
    if(result2>100):
        result2=100
    else:
        result2=result2+5

    if(result2 <= THRESHOLD):
        messagebox.showerror("Match results",
                             "originaal Signature "+str(result2)+f" % similar with sample siganature !!Failure: Signatures Do Not Match")
    else:

        messagebox.showinfo("Match results","original Signature  "+str(result2)+f" % similar with sample signature!Success: Signatures Match")




def find2maxvalue(list1):
  list1.sort(reverse=True)
  return list1[0], list1[1]



# # condition will check true or false

def checkSimilarity(window, path):
   
    result1 = match1(path)  #sending 2 dimensional data to the signature 3 file
    #here result1 is also a 2d percent list
    print("\n\n result1= ",result1)   #it is the unmodified list that fetchetd from signature3 file  and in natural order
    for i in range(len(result1)):
        for j in range(len(result1[0])):

            if(result1[i][j]>100):
                result1[i][j]=100
            else:
                result1[i][j]=result1[i][j]+5

    #take position 2d list and then manipulate according to that

    pos_natural_1d_list=["Sitting","Standing","Sleeping","Walking"]
    pos_natural_2d_list=[]
    for i in range(len(result1)):
        # for j in range(len(result1[0])):
        pos_natural_2d_list.append(pos_natural_1d_list)

    print("\n\n pos_natural_2d_list =",pos_natural_2d_list)


    
    # fetch the 2 max cols corresponding positions of pos list   according to element of result list
    maxresult_2col_list=[]
    maxresult_pos_2col_list=[]
    for sublist1, sublist2 in zip(result1, pos_natural_2d_list):
        # Find indices of first and second maximum values
        max_indices = sorted(range(len(sublist1)), key=lambda i: sublist1[i], reverse=True)[:2]
        maxresult_2col_list.append([sublist1[max_indices[0]], sublist1[max_indices[1]]])
        maxresult_pos_2col_list.append([sublist2[max_indices[0]], sublist2[max_indices[1]]])

    print("\n\n\n maxresult_2col_list =", maxresult_2col_list)
    print("\n\n maxresult_pos_2col_list =", maxresult_pos_2col_list)


    #fetch the only max col  from max result 2 col list  and accroing corresponding pos max col  here
    maxresult_1col_list=[]
    maxresult_pos_1col_list=[]

    # print(maxresult_1col_list)
    for sublist1, sublist2 in zip(maxresult_2col_list, maxresult_pos_2col_list):
        # Find indices of first and second maximum values
        max_indices = sorted(range(len(sublist1)), key=lambda i: sublist1[i], reverse=True)[:2]
        maxresult_1col_list.append([sublist1[max_indices[0]]])
        maxresult_pos_1col_list.append([sublist2[max_indices[0]]])


    print("\n\n\n maxresult_1col_list =", maxresult_1col_list)
    print("\n\n maxresult_pos_1col_list =", maxresult_pos_1col_list)


    result_avg_list=[]
    k=0
    for i in range(4):
        sum=0
        avg=0
       
        for j in range(len(result1)):

            # for j in range(10):
            sum=sum + result1[j][i]
            
        avg=sum/len(result1)
        result_avg_list.append(round(avg,2))
        k=k+1


    print(result_avg_list)
    # Loop through the data and plot each bar chart on its corresponding figure

    

    # Global list to keep track of all figure windows
    figure_windows = []

    def on_close(event):
        # Close all other windows when one window is closed
        for window in figure_windows[:]:
            if window.number != event.canvas.figure.number:
                plt.close(window)
                figure_windows.remove(window)

    # Create figures and plots
    figs = [plt.figure() for _ in range(len(result1))]
    chart_paths=[]
    for i in range(len(result1)):
        x = pos_natural_2d_list[i]
        y = result1[i]
        plt.figure(figs[i].number)  # Switch to the correct figure
        plt.bar(x, y,  color=['blue', 'green', 'red', 'purple'])
        plt.title(f"Chart {i+1}")
        plt.xlabel("positions")
        plt.ylabel("similarity value of original with positions")
        
        # Connect the close event to the function on_close
        figs[i].canvas.mpl_connect('close_event', on_close)
        # Add the figure to the list of figure windows
        figure_windows.append(figs[i])
        chart_path = f'C:/Users/arunk/OneDrive/Desktop/SVSSystem/SignatureVerificationSystem/chartfolder/chart{i}.png'
        plt.savefig(chart_path)
        chart_paths.append(chart_path)

    # Store chart paths in an Excel file
    df = pd.DataFrame({'Chart Path': chart_paths})

    # Write DataFrame to Excel file
    excel_file = 'C:/Users/arunk/OneDrive/Desktop/SVSSystem/SignatureVerificationSystem/chart_imgs.xlsx'
    df.to_excel(excel_file, index=False)

    # Show all the figures
    plt.show()


    pos_list = ["Sitting", "Standing", "Sleeping", "Walking"]
        # Plot
    plt.figure(figsize=(10, 6))
    colors = ['red', 'green', 'blue', 'orange']
    plt.plot(pos_list, result_avg_list, color='gray')
    for i in range(len(result_avg_list)):
        plt.plot(pos_list[i], result_avg_list[i], marker='o', color=colors[i], linewidth=2, markersize=8)

    # Adding title and labels
    plt.title('Average Result by Position')
    plt.xlabel('Position')
    plt.ylabel('Average Result')

    # Adding grid
    plt.grid(True)

    # Adding annotations  
    for i in range(len(result_avg_list)):
        plt.text(pos_list[i], result_avg_list[i], str(result_avg_list[i]), ha='center', va='bottom')

    # Show plot
    plt.show()


    msgstring_2d_list=[]
    
    for i in range(len(maxresult_1col_list)):
        msgstring_list_per_sample=[]
        strr=""
        if(maxresult_1col_list[i][0] <= THRESHOLD):
            strr="original Signature of candidate"+str(i)+" is "+str(maxresult_1col_list[i][0])+" % similar with siganaure in " +maxresult_pos_1col_list[i][0]+" postion!!  signatures do not match\n"
        else:
            strr="original Signature of candidate"+str(i)+" is "+str(maxresult_1col_list[i][0])+" % similar with siganaure in "+maxresult_pos_1col_list[i][0]+" postion!! signatures are matched\n"

        msgstring_list_per_sample.append(strr)
        msgstring_2d_list.append(msgstring_list_per_sample)
    
    # print(msgstring_2d_list)


    message = ""
    for row in msgstring_2d_list:
        message += ' '.join(map(str, row)) + '\n'
    messagebox.showinfo("Signatures Match result", message)



    # Read the CSV file into a pandas DataFrame
    df1 = pd.read_excel(chart_img_excel_file_path)
    print(df1)

    chart_img_paths = df1.values.tolist()

    # Print the new list
    print(chart_img_paths)


    for i in range(len(path)):
        generatepdf(path, result1, maxresult_1col_list,maxresult_pos_1col_list, chart_img_paths,i)
   

# Function to clear the Excel file
def clear_excel_file():
    file_path = xlsx_path
    if os.path.exists(file_path):
        df = pd.DataFrame()
        df.to_excel(file_path, index=False, engine='openpyxl')
        print("Excel file cleared successfully.")


def show_additional_fields():
    
    # Additional fields
    additional_img_label1 = tk.Label(root, text="Sitting position", font=(font_style, 16), bg=bg_color, fg=label_text_color)
    image2_path_entry = tk.Entry(root, font=(font_style, 14))

    additional_img_label2 = tk.Label(root, text="Standing position", font=(font_style, 16), bg=bg_color, fg=label_text_color)
    image3_path_entry = tk.Entry(root, font=(font_style, 14))

    additional_img_label3 = tk.Label(root, text="Sleeping position", font=(font_style, 16), bg=bg_color, fg=label_text_color)
    image4_path_entry = tk.Entry(root, font=(font_style, 14))

    additional_img_label4 = tk.Label(root, text="Walking position", font=(font_style, 16), bg=bg_color, fg=label_text_color)
    image5_path_entry = tk.Entry(root, font=(font_style, 14))

    additional_browse_button1 = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=image2_path_entry))
    additional_browse_button2 = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=image3_path_entry))
    additional_browse_button3 = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=image4_path_entry))
    additional_browse_button4 = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=image5_path_entry))


    # Show additional fields and browse buttons
    additional_img_label1.place(x=10, y=320)
    image2_path_entry.place(x=300, y=320, width=400, height=30)
    additional_browse_button1.place(x=720, y=320, width=100, height=30)

    additional_img_label2.place(x=10, y=380)
    image3_path_entry.place(x=300, y=380, width=400, height=30)
    additional_browse_button2.place(x=720, y=380, width=100, height=30)

    additional_img_label3.place(x=10, y=440)
    image4_path_entry.place(x=300, y=440, width=400, height=30)
    additional_browse_button3.place(x=720, y=440, width=100, height=30)

    additional_img_label4.place(x=10, y=500)
    image5_path_entry.place(x=300, y=500, width=400, height=30)
    additional_browse_button4.place(x=720, y=500, width=100, height=30)
    
    
    compare_button = tk.Button(root, text="Compare", font=(font_style, 18), bg="#008CBA", fg="white",command=lambda: readexcelfile())
    compare_button.place(x=550, y=570, width=200, height=50)  # Show the Compare button


    store_excel_button = tk.Button(root, text="store excel", font=(font_style, 18), bg=button_bg_color, fg="white",command=lambda: store_to_excel(image2_path_entry.get(),image3_path_entry.get(),image4_path_entry.get(),image5_path_entry.get()))
    store_excel_button.place(x=250, y=570, width=200, height=50)  # Show the Compare button



root = tk.Tk()
root.title("Signature Matching")
root.geometry("1000x700") 

# Styling
bg_color = "#f0f0f0"
button_bg_color = "#4CAF50"
button_text_color = "white"
label_text_color = "black"
font_style = "Helvetica"

root.config(bg=bg_color)

uname_label = tk.Label(root, text="Compare Signatures:", font=(font_style, 24, "bold"), bg=bg_color, fg=label_text_color)
uname_label.place(x=10, y=20)

img1_message = tk.Label(root, text="Original Signature", font=(font_style, 16), bg=bg_color, fg=label_text_color)
img1_message.place(x=10, y=100)
image1_path_entry = tk.Entry(root, font=(font_style, 14))
image1_path_entry.place(x=300, y=100, width=400, height=30)
img1_browse_button = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=image1_path_entry))
img1_browse_button.place(x=720, y=100, width=100, height=30)

img2_message = tk.Label(root, text="sample signatuare", font=(font_style, 16), bg=bg_color, fg=label_text_color)
img2_message.place(x=10, y=170)
sample_img_path = tk.Entry(root, font=(font_style, 14))
sample_img_path.place(x=300, y=170, width=400, height=30)
img2_browse_button = tk.Button(root, text="Browse", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=lambda: browsefunc(ent=sample_img_path))
img2_browse_button.place(x=720, y=170, width=100, height=30)


compare_button = tk.Button(root, text="Compare", font=(font_style, 18), bg="#008CBA", fg="white", command=lambda: checkSimilarity2(window=root,path1=image1_path_entry.get(),path2=sample_img_path.get()))

experimental_compare_button = tk.Button(root, text="Experimental Compare", font=(font_style, 18), bg=button_bg_color, fg=button_text_color, command=show_additional_fields)

compare_button.place(x=400, y=240, width=150, height=45)
experimental_compare_button.place(x=600, y=240, width=300, height=45)

clear_button = tk.Button(root, text="Clear Excel", font=(font_style, 14), bg=button_bg_color, fg=button_text_color, command=clear_excel_file)
clear_button.place(x=800, y=620, width=150, height=30)


#############only read the excel data set and check similarity fucntion call###################
def readexcelfile():
    # Read the CSV file into a pandas DataFrame
    df = pd.read_excel(xlsx_path)
    print(df)

    original_path = df.values.tolist()

    # Print the new list
    print(original_path)
    checkSimilarity(window=root,path=original_path)


##################################from here only excel works##################
def store_to_excel(path2,path3,path4,path5):
    path1 = image1_path_entry.get()
    original_path=[path1,path2,path3,path4,path5]
    write_to_excel(original_path)

def write_to_excel(original_path):
    file_path = xlsx_path

    # Check if the file already exists
    if os.path.exists(file_path):
        # Read existing data
        df = pd.read_excel(file_path)
        # Create a new DataFrame from the original_path
        new_data = pd.DataFrame([original_path])
        # Concatenate the existing DataFrame with the new DataFrame
        df = pd.concat([df, new_data], ignore_index=False)
    else:
        # Create new DataFrame if the file doesn't exist
        df = pd.DataFrame([original_path])
    
    # Write the DataFrame to the Excel file
    df.to_excel(file_path, index=False, engine='openpyxl')
    print("Data stored successfully in '{}'".format(file_path))


root.mainloop()