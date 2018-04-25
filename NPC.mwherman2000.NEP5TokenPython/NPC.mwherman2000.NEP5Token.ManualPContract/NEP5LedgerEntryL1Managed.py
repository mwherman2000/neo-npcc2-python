from NeoTrace import NeoTraceRuntime
from NeoEntityModel import NeoEntityModel

class NEP5LedgerEntry(NeoTraceRuntime):
    __state = NeoEntityModel.NULL

    def SetTimestamp(e: NEP5LedgerEntry, value: int):
        e.__timestamp = value
        e.__state = NeoEntityModel.SET 

    def GetTimestamp(e: NEP5LedgerEntry):
        return e.__timestamp

    def SetDecription(e: NEP5LedgerEntry, value: str):
        e.__decription = value
        e.__state = NeoEntityModel.SET

    def GetDecription(e:NEP5LedgerEntry):
        return e.__decription

    def SetDebitCreditAmount(e: NEP5LedgerEntry, value: int):
        e.__debitCreditAmount = value
        e.__state = NeoEntityModel.SET
    
    def GetDebitCreditAmount(e: NEP5LedgerEntry):
        return e.__debitCreditAmount

    def SetBalance(e: NEP5LedgerEntry, value: int):
        e.__balance = value
        e.__state = NeoEntityModel.SET

    def GetBalance(e: NEP5LedgerEntry):
        return e.__balance

    def Set(e: NEP5LedgerEntry, Timestamp: int, Decription: str, 
        DebitCreditAmount: int, Balance: int):
        e.__timestamp = Timestamp
        e.__decription = Decription
        e.__debitCreditAmount = DebitCreditAmount
        e.__balance = Balance

    def __Initialize(NEP5LedgerEntry e, timestamp, decription, debitCreditAmount, balance):
        e.__timestamp = 0
        e.__decription = ""
        e.__debitCreditAmount = 0
        e.__balance = 0
        e.__state = NeoEntityModel.NULL
        if (NeoTrace.RUNTIME):
            LogExt("Null().NEP5LedgerEntry", e)
        return e

    def __init__(Timestamp=0, Decription="", DebitCreditAmount=0, Balance=0):
        e = NEP5LedgerEntry()
        __Initialize(e, Timestamp, Decription, DebitCreditAmount, Balance)
        if (NeoTrace.RUNTIME):
            LogExt("Null().NEP5LedgerEntry", e)
        return e

    def Null():
        e = NEP5LedgerEntry()
        __Initialize(e)
        if (NeoTrace.RUNTIME):
            LogExt("Null().NEP5LedgerEntry", e)
        return e

    def IsNull(NEP5LedgerEntry e):
        return e.__state == NeoEntityModel.NULL 

    def Log(label: str, e: NEP5LedgerEntry):
        TraceRuntime(label, e.__timestamp, e.__decription, e.__debitCreditAmount, e.__balance)

    def LogExt(label: str, e: NEP5LedgerEntry):
        TraceRuntime(label, e.__timestamp, e.__decription, e.__debitCreditAmount, e.__balance, e.__state)


