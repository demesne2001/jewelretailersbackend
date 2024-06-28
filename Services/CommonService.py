import os
import cv2 
from fpdf import FPDF
import numpy as np
from PIL import Image
import img2pdf
from Entity.DTO.WsInput import UploadFile,DeleteFile,GetPDfUsingImageInput
from Entity.DTO.WsResponse import CommanChartFilterResult
BaseDirectory="Utility/Image/"
PDFBaseDirectory="Utility/PDF/"

def ImageToDirectPDf(input:GetPDfUsingImageInput):
    result=CommanChartFilterResult()
    
    if(len(input.ImageLst)<=0):
        result.Message.append("Image is Required")
    if(len(result.Message)==0):
        try:
            # pdf = FPDF()
            # for image in input.ImageLst:
            #     pdf.add_page()            
            #     pdf.image(BaseDirectory+image)
            
            # pdf.output(PDFBaseDirectory+input.FileName+'.PDF',"F")
            # Working One More Option below
            
            image = Image.open(BaseDirectory+input.ImageLst[0])
            image2 = Image.open(BaseDirectory+input.ImageLst[1])
            pdf_bytes = img2pdf.convert([image.filename,image2.filename])                
            file = open(PDFBaseDirectory+input.FileName+'.pdf', "wb")                
            file.write(pdf_bytes)                
            image.close()
            image2.close()                
            file.close()
            result.Message.append(input.FileName+'.pdf')                 
            if(os.path.exists(PDFBaseDirectory+input.FileName+'.pdf')):
                for ImageNA in input.ImageLst:
                      if(os.path.exists(BaseDirectory+ImageNA)): 
                            os.remove(BaseDirectory+ImageNA)                
        except Exception as e:
            print("Error",e)
            result.HasError=True
            result.Message.append(str(e))
    else:
        result.HasError=True
    return result