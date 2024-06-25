from Entity.DTO.WsInput import CardandChartInput
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
            # result.lstResult=DBConfig.ExecuteDataReader(param,'Wr_BIrpt_Sales_GetChart',"GetCommanChart")
            result.lstResult=SQLManager.ExecuteDataReader(param,"Wr_BIrpt_Sales_GetChart","GetCommanChart",False)
        except  Exception as E:
            # CommanScript.ErrorLog("GetCommanChart",DBConfig.spParam(input),"Wr_BIrpt_Sales_GetChart",E)
            result.HasError=True
            result.Message.append(str(E))
    else:
        result.HasError=True
    return result 


def GetDetailCommanChart(input:CardandChartInput):
    result=CommanChartFilterResult()
    try:
        param=""   
        param+=f"@Grouping='{input.Grouping}'"
       
        result.lstResult=SQLManager.ExecuteDataReader(param,"WR_DetailWise_Chart","GetDetailCommanChart",False)
    except  Exception as E:
        # CommanScript.ErrorLog("GetDetailCommanChart",DBConfig.spParam(input),"WR_DetailWise_Chart",E)
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
        # CommanScript.ErrorLog("GetCardValue",DBConfig.spParam(input),"Wr_Dashboard_GetCard",E)
        result.HasError=True
        result.Message.append(str(E))
    return result
