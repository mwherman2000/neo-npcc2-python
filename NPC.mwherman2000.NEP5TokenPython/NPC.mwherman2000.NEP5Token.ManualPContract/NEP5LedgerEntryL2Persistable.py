from NeoTrace import NeoTraceRuntime
from NeoEntityModel import NeoEntityModel
from boa.interop.Neo.Storage import GetContext, Get, Put, Delete
from boa.interop.BigInteger import FromBytes, ToByteArray
from boa.code.builtins import concat

class NEP5LedgerEntry(NeoTraceRuntime):

    __className = "NEP5LedgerEntry"
    __bClassName = bytes(__className)
    __sTimestamp = "Timestamp"
    __bTimestamp = bytes(__sTimestamp)
    __sDecription = "Decription"
    __bDecription = bytes(__sDecription)
    __sDebitCreditAmount = "DebitCreditAmount"
    __bDebitCreditAmount = bytes(__sDebitCreditAmount)
    __sBalance = "Balance"
    __bBalance = bytes(__sBalance)
    __sSTA = "_STA"
    __bSTA = bytes(__sSTA)
    __sEXT = "_EXT"
    __bEXT = bytes(__sEXT)
    __classKeyTag = concat(concat("/#", __className),".")
    __bclassKeyTag = bytes(__classKeyTag)

    def IsMissing(e: NEP5LedgerEntry):
        return (e.__state == NeoEntityModel.MISSING)

    def Missing():
        e.__timestamp = 0
        e.__decription = ""
        e.__debitCreditAmount = 0
        e.__balance = 0
        e.__state = NeoEntityModel.MISSING
        if NeoTrace.RUNTIME:
            TraceRuntime("Missing().NEP5LedgerEntry", e)
        return e

    def Put(e: NEP5LedgerEntry, key: bytes):
        if len(key) == 0:
            return False
        ctx = GetContext()
        __bkeyTag = concat(key, self.__bclassKeyTag)

        e.__state = NeoEntityModel.PUTTED
        Put(ctx, concat(__bkeyTag, self.__bSTA), e.__state)
        Put(ctx, concat(__bkeyTag, self.__bTimestamp), e.__timestamp)
        Put(ctx, concat(__bkeyTag, self.__bDecription), e.__decription)
        Put(ctx, concat(__bkeyTag, self.__bDebitCreditAmount), e.__debitCreditAmount)
        Put(ctx, concat(__bkeyTag, self.__bBalance), e.__balance)
        if NeoTrace.RUNTIME:
            LogExt("Put(bkey).NEP5LedgerEntry", e)
        return True

    def Put(e: NEP5LedgerEntry, key: str):
        if len(key) == 0:
            return False
        if NeoTrace.RUNTIME:
            LogExt("Put(skey).NEP5LedgerEntry", e)
        ctx = GetContext()
        __skeyTag = concat(key, self.__classKeyTag)
        if NeoTrace.RUNTIME:
            TraceRuntime("Put(skey).__skeyTag", __skeyTag)
        e.__state = NeoEntityModel.PUTTED
        if NeoTrace.RUNTIME:
            TraceRuntime("Put(skey).bis", e.__state)
        Put(ctx, concat(__skeyTag, self.__sSTA), e.__state)
        Put(ctx, concat(__skeyTag, self.__sTimestamp), e.__timestamp)
        Put(ctx, concat(__skeyTag, self.__sDecription), e.__decription)
        Put(ctx, concat(__skeyTag, self.__sDebitCreditAmount), e.__debitCreditAmount)
        Put(ctx, concat(__skeyTag, self.__sBalance), e.__balance)
        if NeoTrace.RUNTIME:
            LogExt("Put(bkey).NEP5LedgerEntry", e)
        return True

    def Get(key: bytes):
        if len(key) == 0:
            return None
        ctx = GetContext()
        __bkeyTag = concat(key, self.__bclassKeyTag)
        bsta = Get(ctx, concat(__bkeyTag, __bSTA))
        if NeoTrace.RUNTIME:
            TraceRuntime("Get(bkey).bsta", len(bsta), bsta)
        if len(bsta) == 0:
            e = NEP5LedgerEntry.Missing()
        else:
            ista = FromBytes(bsta)
            e = NEP5LedgerEntry()
            e.__timestamp = Get(ctx, concat(__bkeyTag, self.__bTimestamp))
            e.__decription = Get(ctx, concat(__bkeyTag, self.__bDecription))
            e.__debitCreditAmount = Get(ctx, concat(__bkeyTag, self.__bDebitCreditAmount))
            e.__balance = Get(ctx, concat(__bkeyTag, self.__bBalance))
            e.__state = NeoEntityModel.GETTED
        if NeoTrace.RUNTIME:
            LogExt("Get(bkey).NEP5LedgerEntry", e)

    def Get(key: str):
        if len(key) == 0:
            return None
        ctx = GetContext()
        __skeyTag = concat(key, self.__classKeyTag)
        bsta = Get(ctx, concat(__skeyTag, __sSTA))
        if NeoTrace.RUNTIME:
            TraceRuntime("Get(bkey).bsta", len(bsta), bsta)
        if len(bsta) == 0:
            e = NEP5LedgerEntry.Missing()
        else:
            ista = FromBytes(bsta)
            e = NEP5LedgerEntry()
            e.__timestamp = Get(ctx, concat(__skeyTag, self.__sTimestamp))
            e.__decription = Get(ctx, concat(__skeyTag, self.__sDecription))
            e.__debitCreditAmount = Get(ctx, concat(__skeyTag, self.__sDebitCreditAmount))
            e.__balance = Get(ctx, concat(__skeyTag, self.__sBalance))
            e.__state = NeoEntityModel.GETTED
        if NeoTrace.RUNTIME:
            LogExt("Get(bkey).NEP5LedgerEntry", e)
        return e