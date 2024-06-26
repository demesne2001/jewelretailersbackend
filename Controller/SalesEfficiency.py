from fastapi import APIRouter,Body,Depends
from Services import SalesEfficiencyService
from Entity.DTO.WsInput import CardandChartInput,StockToSalesInput,MinSubitemDeatil
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