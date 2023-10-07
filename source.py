import PyPDF2
file=input()
result=0

# this part read information from pdf file and place 
# split pdf file in to two pages and extraxt page content to text variables
if file!="":        
    row=[]
    pdf_file=PyPDF2.PdfReader(open(file,"rb"))
    number_of_pages=len(pdf_file.pages)
    page1=pdf_file.pages[0]
    page2=pdf_file.pages[1]
    text1=page1.extract_text()
    text2=page2.extract_text()
 
 # this part
    with open("nordpool.csv","r") as f:
        next(f)
        


print(result)


