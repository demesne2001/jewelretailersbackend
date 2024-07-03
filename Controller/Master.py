from fastapi import APIRouter,Body,Depends
from Services import MasterSevice
from Entity.DTO.WsInput import CardandChartInput,GetByID,AddEditFilterGrid,GetSalesValueInput
Filter=APIRouter()

@Filter.post('/GetBranch')
def GetBranch(input:CardandChartInput):
    return MasterSevice.GetBranch(input)

@Filter.post('/GetState')
def GetState(input:CardandChartInput):
    return MasterSevice.GetState(input)

@Filter.post('/GetCity')
def GetCity(input:CardandChartInput):
    return MasterSevice.GetCity(input)


@Filter.post('/GetRegion')
def GetRegion(input:CardandChartInput):
    return MasterSevice.GetRegion(input)


@Filter.post('/GetItem')
def GetItem(input:CardandChartInput):
    return MasterSevice.GetItem(input)

@Filter.post('/GetSubItem')
def GetSubItem(input:CardandChartInput):
    return MasterSevice.GetSubItem(input)

@Filter.post('/GetItemGroup')
def GetItemGroup(input:CardandChartInput):
    return MasterSevice.GetItemGroup(input)

@Filter.post('/GetItemWithSubitem')
def GetItemWithSubitem(input:CardandChartInput):
    return MasterSevice.GetItemWithSubitem(input)

@Filter.post('/GetPurchaseParty')
def GetPurchaseParty(input:CardandChartInput):
    return MasterSevice.Getdesigncode(input)

@Filter.post('/Getdesigncode')
def Getdesigncode(input:CardandChartInput):
    return MasterSevice.Getdesigncode(input)

@Filter.post('/GetSalesParty')
def GetSalesParty(input:CardandChartInput):
    return MasterSevice.GetSalesParty(input)


@Filter.post('/GetSaleman')
def GetSaleman(input:CardandChartInput):
    return MasterSevice.GetSaleman(input)

@Filter.post('/GetProduct')
def GetProduct(input:CardandChartInput):
    return MasterSevice.GetProduct(input)

@Filter.post('/GetDesignCatalogue')
def GetDesignCatalogue(input:CardandChartInput):
    return MasterSevice.GetDesignCatalogue(input)

@Filter.post('/GetDayBook')
def GetDayBook(input:CardandChartInput):
    return MasterSevice.GetDayBook(input)

@Filter.post('/GetMetalType')
def GetMetalType(input:CardandChartInput):
    return MasterSevice.GetMetalType(input)

@Filter.post('/GetSalesAging')
def GetSalesAging(input:CardandChartInput):
    return MasterSevice.GetSalesAging(input)

@Filter.post('/GetFilterGridByID')
def GetFilterGridByID(input:GetByID):
    return MasterSevice.GetFilterGridByID(input)

@Filter.post('/GetSalesValue')
def GetSalesValue(input:GetSalesValueInput):
    return MasterSevice.GetSalesValue(input)


@Filter.post('/FilterGridAddEdit')
def FilterGridAddEdit(input:AddEditFilterGrid):
    return MasterSevice.FilterGridAddEdit(input)


@Filter.post('/GetMonth')
def GetMonth(input:CardandChartInput):
    return MasterSevice.GetMonth(input)