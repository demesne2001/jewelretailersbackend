from Entity.DTO.WsInput import CardandChartInput,StockToSalesInput 
from Entity.DTO.WsInput import MinSubitemDeatil,GetByID,AddEditChartOption,ChartWiseImageInput
from DBConnection import SQLManager
from Entity.DTO import WsInput
from Entity.DTO.WsResponse import CommanChartFilterResult


def GetCommanChart(input:CardandChartInput):
    result=CommanChartFilterResult()   
    if(len(result.Message)==0):
        try:
            param=""
            param=SQLManager.CommonParam(input)
            if(len(param)>0):  
                param+=f",@Grouping='{input.Grouping}'"
            else:
                param+=f"@Grouping='{input.Grouping}'"
            param+=f",@SortBy='{input.SortBy}'"
            if(input.SortByLabel !=''):
                param+=f",@SortByLabel='{input.SortByLabel}'"
            if(input.Unity !=''):
                param+=f",@Unity='{input.Unity}'"
            print('param',param)
            # result.lstResult=SQLManager.ExecuteDataReader(param,'Wr_BIrpt_Sales_GetChart',"GetCommanChart")
            result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_BIrpt_Sales_GetChart","GetCommanChart",False)
        except  Exception as E:
            # CommanScript.ErrorLog("GetCommanChart",SQLManager.spParam(input),"Wr_BIrpt_Sales_GetChart",E)
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result 


def GetDetailCommanChart(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""  
        param=SQLManager.CommonParam(input) 
        param+=f",@Grouping='{input.Grouping}'"
       
        result.lstResult=SQLManager.ExecuteDataReader(param,"WR_DetailWise_Chart","GetDetailCommanChart",False)
    except  Exception as E:
        # CommanScript.ErrorLog("GetDetailCommanChart",SQLManager.spParam(input),"WR_DetailWise_Chart",E)
        result.HasError=True
        result.Message.append(str(E))
    return result 

def GetCardValue(input:CardandChartInput):
    print('Service')
    result=CommanChartFilterResult()
    try:
        param=""
        print('input',input)
        param=SQLManager.CommonParam(input)
        if(len(param)>0):
            param+=f",@Grouping='{input.Grouping}'"
        else:
            param+=f"@Grouping='{input.Grouping}'"
        print('param',param)
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_Dashboard_GetCard","GetCardValue",False)
    except  Exception as E:        
        # CommanScript.ErrorLog("GetCardValue",SQLManager.spParam(input),"Wr_Dashboard_GetCard",E)
        result.HasError=True
        result.Message.append(str(E))
    return result


def GetStockToSalesChart(input:StockToSalesInput):
    result=CommanChartFilterResult()
    if(input.FromDate == ""):
        result.Message.append("Required Field From Date")
    elif(input.Mode <=0):\
        result.Message.append("Required Field Mode")
    elif(input.Mode ==1):
        if(input.MonthType == ""):
            result.Message.append("Required Field MonthType")
    if(len(result.Message)==0):        
        try:
            param=""
            param=SQLManager.spParam(input)
            result.lstResult=SQLManager.ExecuteDataReader(param,"WR_BI_rpt_StockAgainSales_GetChartData","GetStockToSalesChart",False)
        except  Exception as E:
            print(E)
            result.HasError=True
            result.Message.append(E)
    else:
        result.HasError=True
    return result 

def GetMinStockChart(input:StockToSalesInput):
    result=CommanChartFilterResult()
    if(input.FromDate == ""):
        result.Message.append("Required Field From Date")
    elif(input.Mode <=0):\
        result.Message.append("Required Field Mode")
    elif(input.Mode ==1):
        if(input.MonthType == ""):
            result.Message.append("Required Field MonthType")
    if(len(result.Message)==0):        
        try:
            param=""
            param=SQLManager.spParam(input)
            result.lstResult=SQLManager.ExecuteDataReader(param,"WR_mstMinMaxStock_Getchart","GetMinStockChart",False)
        except  Exception as E:
            print(E)
            result.HasError=True
            result.Message.append(E)
    else:
        result.HasError=True
    return result 

def GetMinStockDeatilChart(input:MinSubitemDeatil):
    result=CommanChartFilterResult()
    if(input.FromDate == ""):
        result.Message.append("Required Field From Date")
    elif(input.SubItemID <=0):\
        result.Message.append("Required Field Sub  Item")
    elif(input.ToDate ==""):
         result.Message.append("Required Field To  Date")
    if(len(result.Message)==0):        
        try:
            param=""
            param=SQLManager.spParam(input)
            result.lstResult=SQLManager.ExecuteDataReader(param,"WR_Bi_MstMinStock_GetDetailchart","GetMinStockDeatilChart",False)
        except  Exception as E:
            print(E)
            result.HasError=True
            result.Message.append(E)
    else:
        result.HasError=True
    return result 

def GetChartOptionByID(input:GetByID):
    result=CommanChartFilterResult()
    try:
        print(input.ID)
        result.lstResult=SQLManager.ExecuteDataReader(f"@ID={input.ID}","WR_mstChartOption_GetByID","GetChartOptionByID",False)
    except  Exception as E:
        # CommanScript.ErrorLog("GetChartOptionByID",f"@ID={input.ID}","WR_mstChartOption_GetByID",E)
        result.HasError=True
        result.Message.append(str(E))
    return result

def ChartOptionAddEdit(input:AddEditChartOption):
    result=CommanChartFilterResult()
    if(input.ChartOption==''):
        result.Message.append("ChartOption Required")
    elif(input.ChartID<=0):
        result.Message.append("ChartID Required")
    if(len(result.Message)==0): 
        try:
            ID=0
            print('serviec')
            ID=SQLManager.ExecuteNonQuery(input,"WR_mstChartOption_AddEdit","ChartOptionAddEdit",False)
            if(ID>0):
                result.Message.append("Chart Option Updated Sucessfully")
            elif(ID == -1):
                result.Message.append("Already Have it...!")
            elif(ID ==-5):
                result.Message.append("Contact To Backend Developer")
                result.HasError=True
            
        except  Exception as E:
            # CommanScript.ErrorLog("ChartOptionAddEdit",SQLManager.spParam(input),"WR_mstChartOption_AddEdit",E)
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

def GetChartGroupByID(input:GetByID):
    result=CommanChartFilterResult()
    try:
        print(input.ID)
        result.lstResult=SQLManager.ExecuteDataReader(f"@ID={input.ID}","WR_mstChartGroup_GetByID","GetChartGroupByID",False)
    except  Exception as E:
        # CommanScript.ErrorLog("GetChartGroupByID",f"@ID={input.ID}","WR_mstChartGroup_GetByID",E)
        result.HasError=True
        result.Message.append(E)
    return result

def ChartGroupAddEdit(input:WsInput.AddEditChartGroup):
    result=CommanChartFilterResult()
    if(input.ChartGroup==''):
        result.Message.append("ChartGroup Required")
    elif(input.ChartID<=0):
        result.Message.append("ChartID Required")
    if(len(result.Message)==0):
        try:
            ID=0
            print('serviec')
            ID=SQLManager.ExecuteNonQuery(input,"WR_mstChartGroup_AddEdit","ChartGroupAddEdit",False)
            if(ID>0):
                result.Message.append("Chart Group Updated Sucessfully")
            elif(ID == -1):
                result.Message.append("Already Have it...!")
            elif(ID ==-5):
                result.Message.append("Contact To Backend Developer")
                result.HasError=True
            
        except  Exception as E:
            # CommanScript.ErrorLog("ChartGroupAddEdit",SQLManager.spParam(input),"WR_mstChartGroup_AddEdit",E)
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result

def GetDetailChartImage(input:ChartWiseImageInput):
    result=CommanChartFilterResult() 
    if(len(result.Message)==0):
        try:
            param=""
            param=SQLManager.spParam(input)
            result.lstResult=SQLManager.ExecuteDataReader(param,"WR_GetBarcodeImage_GetByID","GetDetailChartImage",False)
        except  Exception as E:
            # CommanScript.ErrorLog("GetCommanChart",DBConfig.spParam(input),"Wr_BIrpt_Sales_GetChart",E)
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result     

def GetDefaultScreenData():
    result=CommanChartFilterResult()
    try:
        param=""        
        result.lstResult=SQLManager.ExecuteDataReader(param,"WR_DefaultScreen_GetData","GetDayBook",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 