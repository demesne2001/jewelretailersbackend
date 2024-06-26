from Entity.DTO.WsInput import CardandChartInput,GetByID,AddEditFilterGrid,GetSalesValueInput
from DBConnection import SQLManager
from Entity.DTO.WsResponse import CommanChartFilterResult
from Services import jwtBearer


def GetBranch(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"
        if(input.strCompanyID!=''):
            param +=f" @strCompanyID='{input.strCompanyID}',"     
        param +=f" @Search='{input.Search}'"        
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_MstBranch_GetForHelp","",False)
    except  Exception as E:
        # CommanScript.ErrorLog("GetCommanChart",SQLManager.spParam(input),"Wr_BIrpt_Sales_GetChart",E)
        print(str(E))
        result.HasError=True
        result.Message.append(str(E))
    return result 

def GetState(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"    
        param +=f" @Search='{input.Search}'"
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_mstState_GetForHelp","",False)
    except  Exception as E:
        # CommanScript.ErrorLog("GetCommanChart",SQLManager.spParam(input),"Wr_BIrpt_Sales_GetChart",E)
        result.HasError=True
        result.Message.append(str(E))
    return result 


def GetCity(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""    
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"
        if(input.strState!=''):
            param +=f" @StrStateID='{input.StrStateID}',"     
        if(input.strRegionID!=''):
            param +=f" @strRegionID='{input.strRegionID}',"                     
        param +=f" @Search='{input.Search}'"    
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_mstCity_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 



def GetRegion(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"    
        param +=f" @Search='{input.Search}'"
        # param=SQLManager.CommonParam(input)
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_RegionName_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 



def GetItem(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"    
        param +=f" @Search='{input.Search}',"
        
        param +=f" @strItemGroupID='{input.strItemGroup}',"      
        param +=f" @strProductID='{input.strProduct}'"
   
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_mstitem_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 


def GetSubItem(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""    
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"    
        param +=f" @Search='{input.Search}'"    
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_mstSubItem_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 


def GetItemGroup(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"    
        param +=f" @Search='{input.Search}'"
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_mstItemGroup_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 


def GetItemWithSubitem(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"            
        if(input.strItem!=''):
            param +=f" @strItemID='{input.strItem}',"
        if(input.strSubItem!=''):
            param +=f" @strSubItemID='{input.strSubItem}',"      
        if(input.strItemGroup!=''):
            param +=f" @strItemGroupID='{input.strItemGroup}'," 
        if(input.strProduct!=''):
            param +=f" @strProductID='{input.strProduct}',"       
        param +=f" @Search='{input.Search}'"
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_mstItemSub_GetForHelp","",False)
    except  Exception as E:
        # CommanScript.ErrorLog("GetItemWithSubitem",SQLManager.spParam(input),"Wr_mstItemSub_GetForHelp",E)
        result.HasError=True
        result.Message.append(str(E))
    return result 


def Getdesigncode(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"          
        param +=f" @Search='{input.Search}'"
                
        result.lstResult=SQLManager.ExecuteDataReader(param,"WR_mstdesigncode_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 



def GetSalesParty(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"
        if(input.strRegionID!=''):
            param +=f" @strRegionID='{input.strRegionID}',"   
        if(input.strDayBook!=''):
            param +=f" @strDayBookID='{input.strDayBook}',"   
        param +=f" @Search='{input.Search}'"
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_SalesParty_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 



def GetSaleman(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""   
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"    
        param +=f" @Search='{input.Search}'"   
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_mstSalesman_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 


def GetProduct(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"    
        param +=f" @Search='{input.Search}'"
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_MstProduct_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 


def GetDesignCatalogue(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        if(input.PageNo>0):
            param +=f" @PageNo={input.PageNo},"
        if(input.PageSize>0):
            param +=f" @PageSize={input.PageSize},"            
        if(input.strItem!=''):
            param +=f" @strItemID='{input.strItem}',"
        if(input.strItemSubitem!=''):
            param +=f" @strItemSubitemID='{input.strItemSubitem}',"            
        param +=f" @Search='{input.Search}'"
        
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_mstDesignCatalog_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 


def GetDayBook(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""        
        result.lstResult=SQLManager.ExecuteDataReader(param,"WR_Daybook_GetForHelp","GetDayBook",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 

def GetMetalType(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""
        # param=SQLManager.CommonParam(input)
      
        result.lstResult=SQLManager.ExecuteDataReader(param,"WR_mstMetalType_GetForHelp","GetMetalType",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 

def GetSalesAging(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""        
        result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_SalesAging_GetForHelp","",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result 

def GetFilterGridByID(input:GetByID):
    result=CommanChartFilterResult()
    try:
        print(input.ID)
        result.lstResult=SQLManager.ExecuteDataReader(f"@ID={input.ID}","WR_mstFilterGrid_GetBYID","GetFilterGridByID",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result

def GetSalesValue(input:GetSalesValueInput):
    result=CommanChartFilterResult()
    try:
        param=""
        param=SQLManager.spParam(input)        
        result.lstResult=SQLManager.ExecuteDataReader(param,"WR_trnSales_GetData","GetFilterGridByID",False)
    except  Exception as E:
        result.HasError=True
        result.Message.append(str(E))
    return result

def FilterGridAddEdit(input:AddEditFilterGrid):
    result=CommanChartFilterResult()
    if(input.FilterGrid==''):
        result.Message.append("FilterGrid Required")
    elif(input.FilterID<=0):
        result.Message.append("FilterID Required")
    if(len(result.Message)==0):
        try:
            ID=0
            print('serviec')
            ID=SQLManager.ExecuteNonQuery(input,"WR_mstFilterGrid_AddEdit","FilterGridAddEdit",False)
            if(ID>0):
                result.Message.append("FilterGrid Updated Sucessfully")
            elif(ID == -1):
                result.Message.append("Already Have it...!")
            elif(ID ==-5):
                result.Message.append("Contact To Backend Developer")
                result.HasError=True
            
        except  Exception as E:
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result