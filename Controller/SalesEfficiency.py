from fastapi import APIRouter,Body,Depends
from Services import SalesEfficiencyService
from Entity.DTO.WsInput import CardandChartInput,StockToSalesInput,MinSubitemDeatil,GetByID,AddEditChartOption,AddEditChartGroup
Chart=APIRouter()



@Chart.post('/GetCommanChart')
def GetCommanChart(input:CardandChartInput):
    return SalesEfficiencyService.GetCommanChart(input)

@Chart.post('/GetDetailCommanChart')
def GetDetailCommanChart(input:CardandChartInput):
    return SalesEfficiencyService.GetDetailCommanChart(input)

@Chart.post('/GetCardValue')
def GetCardValue(input:CardandChartInput):
    return SalesEfficiencyService.GetCardValue(input)


@Chart.post('/GetStockToSalesChart')
def GetStockToSalesChart(input:StockToSalesInput):
    return SalesEfficiencyService.GetStockToSalesChart(input)


@Chart.post('/GetMinStockChartDeatil')
def GetMinStockChartDeatil(input:MinSubitemDeatil):
    return SalesEfficiencyService.GetMinStockDeatilChart(input)


@Chart.post('/GetChartOptionByID')
def GetChartOptionByID(input:GetByID):
    return SalesEfficiencyService.GetChartOptionByID(input)

@Chart.post('/ChartOptionAddEdit')
def ChartOptionAddEdit(input:AddEditChartOption):
    return SalesEfficiencyService.ChartOptionAddEdit(input)

@Chart.post('/GetChartGroupByID')
def GetChartGroupByID(input:GetByID):
    return SalesEfficiencyService.GetChartGroupByID(input)

@Chart.post('/ChartGroupAddEdit')
def ChartGroupAddEdit(input:AddEditChartGroup):
    return SalesEfficiencyService.ChartGroupAddEdit(input)
