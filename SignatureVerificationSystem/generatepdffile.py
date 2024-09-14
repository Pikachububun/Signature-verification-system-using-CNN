from fpdf import FPDF


def generatepdf(path, result1,maxresult_1col_list, maxresult_pos_1col_list,chart_img_paths,i):
        
    # Create instance of FPDF class
    pdf = FPDF()
    pdf.l_margin=5
    pdf.r_margin=0
    pdf.t_margin=5
    pdf.b_margin=0
    # Add a page
    pdf.add_page()

    # Set font for the entire document
    pdf.set_font("Arial", size=25,style='B')

    # Add a cell
    # pdf.cell(200, 10, txt="", ln=True, align='C',border=0)
    pdf.cell(200, 15, txt="SVS", ln=True, align='C',border=0)


    pdf.set_font("Arial", size=12,style='B')

    # Add another cell
    pdf.cell(200, 10, txt="Signature Verification System", ln=True, align='C',border=1)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="", ln=True, align='C',border=0)
    pdf.cell(200, 10, txt="", ln=True, align='C',border=0)

    
    
    pdf.image(path[i][0], x = 10, y = 40, w = 30)
    pdf.image(path[i][1], x = 50, y = 40, w = 30)
    pdf.image(path[i][2], x = 90, y = 40, w = 30)
    pdf.image(path[i][3], x = 130, y = 40, w = 30)
    pdf.image(path[i][4], x = 170, y = 40, w = 30)
       
    pdf.cell(200, 20, txt="", ln=True, align='C',border=0)
    pdf.cell(40, 10, txt="ORIGINAL", ln=False, align='C',border=0)
    pdf.cell(40, 10, txt="SITTING", ln=False, align='C',border=0)
    pdf.cell(40, 10, txt="STANDING", ln=False, align='C',border=0)
    pdf.cell(40, 10, txt="SLEEPING", ln=False, align='C',border=0)
    pdf.cell(40, 10, txt="WALKING", ln=True, align='C',border=0)

    pdf.cell(40, 10, txt="100", ln=False, align='C',border=0)
    pdf.cell(40, 10, txt=str(result1[i][0]), ln=False, align='C',border=0)
    pdf.cell(40, 10, txt=str(result1[i][1]), ln=False, align='C',border=0)
    pdf.cell(40, 10, txt=str(result1[i][2]), ln=False, align='C',border=0)
    pdf.cell(40, 10, txt=str(result1[i][3]), ln=True, align='C',border=0)
    pdf.cell(200, 10, txt="", ln=True, align='C',border=0)
    pdf.cell(200, 10, txt="original signature "+str(maxresult_1col_list[i]) +"% matched with signature in "+str(maxresult_pos_1col_list[i])+" position", ln=True, align='L',border=1)
    pdf.cell(200, 2, txt="", ln=True, align='C',border=0)
    pdf.cell(200, 1, txt="", ln=True, align='C',border=1)

    pdf.image(chart_img_paths[i][0], x = 30, y = 120, w = 160)


    pdf.output(f"C:/Users/arunk/OneDrive/Desktop/SVSSystem/SignatureVerificationSystem/pdfs/Result{i}.pdf")

