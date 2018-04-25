from NeoTrace import NeoTraceRuntime
from NeoEntityModel import NeoEntityModel
from boa.interop.Neo.Storage import GetContext, Get, Put, Delete
from boa.interop.BigInteger import FromBytes, ToByteArray
from boa.code.builtins import concat

class NEP5LedgerEntry(NeoTraceRuntime):

    def IsBuried(e: NEP5LedgerEntry):
        return (e.__state == NeoEntityModel.TOMBSTONED)

    def Tombstone():
        e = NEP5LedgerEntry()
        e.__timestamp = 0
        e.__decription = ""
        e.__debitCreditAmount = 0
        e.__balance = 0
        e.__state = NeoEntityModel.TOMBSTONED
        if NeoTrace.RUNTIME:
            LogExt("Tombstone().NEP5LedgerEntry", e)
        return e

    def Bury(key: bytes):
        if len(key) == 0:
            return None
        ctx = GetContext()
        __bkeyTag = concat(key, self.__bclassKeyTag)
        bsta = Get(ctx, concat(__bkeyTag, __bSTA)) #__bSTA is from a partial
        if NeoTrace.RUNTIME:
            NeoTraceRuntime.TraceRuntime("Bury(bkey).bsta", len(bsta), bsta)
        if len(bsta) == 0:
            e = NEP5LedgerEntry.Missing()
        else:
            e = NEP5LedgerEntry.Tombstone()
            Put(ctx, concat(__bkeyTag, self.__bSTA), e.__state)
        if NeoTrace.RUNTIME:
            LogExt("Bury(bkey).NEP5LedgerEntry", e)
        return e

    def Bury(key: str):
        if len(key) == 0:
            return None
        ctx = GetContext()
        __skeyTag = concat(key, self.__classKeyTag)
        bsta = Get(ctx, concat(__skeyTag, __sSTA)) #__bSTA is from a partial
        if NeoTrace.RUNTIME:
            NeoTraceRuntime.TraceRuntime("Bury(skey).NEP5LedgerEntry.bsta", len(bsta), bsta)
        if len(bsta) == 0:
            e = NEP5LedgerEntry.Missing()
        else:
            e = NEP5LedgerEntry.Tombstone()
            Put(ctx, concat(__skeyTag, self.__sSTA), e.__state)
        if NeoTrace.RUNTIME:
            LogExt("Bury(skey).NEP5LedgerEntry", e)
        return e