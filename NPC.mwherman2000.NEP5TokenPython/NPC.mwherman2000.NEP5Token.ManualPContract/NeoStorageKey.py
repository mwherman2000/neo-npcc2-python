from aenum import Enum
from NeoTrace import NeoTraceRuntime, NeoTrace
from NeoEntityModel import NeoEntityModel
from boa.interop.Neo.Storage import GetContext, Get, Put, Delete
from boa.interop.BigInteger import FromBytes, ToByteArray
from boa.code.builtins import concat
from NeoVersionedAppUser import NeoVersionedAppUser

class ContractParameterTypeLocal(Enum):
    Signature = 0
    Boolean = 1
    Integer = 2
    Hash160 = 3
    Hash256 = 4
    ByteArray = 5
    PublicKey = 6
    String = 7
    Array = 16
    InteropInterface = 240
    Void = 255

class NeoStorageKey(NeoTraceRuntime):
    __app = None
    __major = None
    __minor = None
    __build = None
    __userScriptHash = None
    __state = None
    __domain = None
    __className = None
    __index = None
    __fieldName = None
    __state = None

    def SetAppName(nsk: NeoStorageKey, value: bytes):
        nsk.__app = value
        nsk.__state = NeoEntityModel.SET

    def GetAppNameAsByteArray(nsk: NeoStorageKey):
        return nsk.__app

    def SetAppName(nsk: NeoStorageKey, value: str):
        nsk.__app = ToByteArray(value)
        nsk.__state = NeoEntityModel.SET

    def GetAppNameAsString(nsk: NeoStorageKey):
        return FromBytes(nsk.__app)

    def SetMajor(nsk: NeoStorageKey, value: int):
        nsk.__major = value
        nsk.__state = NeoEntityModel.SET
    
    def GetMajor(nsk: NeoStorageKey):
        return nsk.__major

    def SetMinor(nsk: NeoStorageKey, value: int):
        nsk.__minor = value
        nsk.__state = NeoEntityModel.SET
    
    def GetMinor(nsk: NeoStorageKey):
        return nsk.__minor

    def SetBuild(nsk: NeoStorageKey, value: int):
        nsk.__build = value
        nsk.__state = NeoEntityModel.SET

    def GetBuild(nsk: NeoStorageKey):
        return nsk.__build

    def SetUserScriptHash(nsk: NeoStorageKey, value: bytes):
        nsk.__userScriptHash = value
        nsk.__state = NeoEntityModel.SET

    def GetUserScriptHash(nsk: NeoStorageKey):
        return nsk.__userScriptHash

    def SetDomain(nsk: NeoStorageKey, value: bytes):
        nsk.__app = value
        nsk.__state = NeoEntityModel.SET

    def GetDomainAsByteArray(nsk: NeoStorageKey):
        return nsk.__app

    def SetDomain(nsk: NeoStorageKey, value: str):
        nsk.__app = ToByteArray(value)
        nsk.__state = NeoEntityModel.SET

    def GetDomainAsString(nsk: NeoStorageKey):
        return FromBytes(nsk.__app)

    def SetClassName(nsk: NeoStorageKey, value: bytes):
        nsk.__app = value
        nsk.__state = NeoEntityModel.SET

    def GetClassNameAsByteArray(nsk: NeoStorageKey):
        return nsk.__app

    def SetIndex(nsk: NeoStorageKey, value: str):
        nsk.__app = ToByteArray(value)
        nsk.__state = NeoEntityModel.SET

    def GetIndex(nsk: NeoStorageKey):
        return FromBytes(nsk.__app)

    def SetFieldName(nsk: NeoStorageKey, value: str):
        nsk.__app = ToByteArray(value)
        nsk.__state = NeoEntityModel.SET

    def GetFieldName(nsk: NeoStorageKey):
        return FromBytes(nsk.__app)

    def Set(nsk: NeoStorageKey, app: bytes, major: int, minor: int, build: int, userScriptHash: bytes, domain: bytes, className: bytes, index: int, fieldName: bytes):
        nsk.__app = app
        nsk.__major = major
        nsk.__minor = minor
        nsk.__build = build
        nsk.__userScriptHash = userScriptHash
        nsk.__domain = domain
        nsk.__className = className
        nsk.__index = index
        nsk.__fieldName = fieldName
        nsk.__state = NeoEntityModel.SET

    def Set(nsk: NeoStorageKey, app: str, major: int, minor: int, build: int, userScriptHash: bytes, domain: str, className: str, index: int, fieldName: bytes):
        nsk.__app = ToByteArray(app)
        nsk.__major = major
        nsk.__minor = minor
        nsk.__build = build
        nsk.__userScriptHash = userScriptHash
        nsk.__domain = ToByteArray(domain)
        nsk.__className = ToByteArray(className)
        nsk.__index = index
        nsk.__fieldName = fieldName
        nsk.__state = NeoEntityModel.SET

    def Set(nsk: NeoStorageKey, vau: NeoVersionedAppUser, userScriptHash: bytes, domain: bytes, className: bytes, index: int, fieldName: bytes):
        nsk.__major = NeoVersionedAppUser.GetMajor(vau)
        nsk.__minor = NeoVersionedAppUser.GetMinor(vau)
        nsk.__build = NeoVersionedAppUser.GetBuild(vau)
        nsk.__userScriptHash = NeoVersionedAppUser.GetUserScriptHash(vau)
        nsk.__domain = domain
        nsk.__className = className
        nsk.__index = index 
        nsk.__fieldName = fieldName
        nsk.__state = NeoEntityModel.SET
        
    def Set(nsk: NeoStorageKey, vau: NeoVersionedAppUser, userScriptHash: bytes, domain: str, className: str, index: int, fieldName: bytes):
        nsk.__major = NeoVersionedAppUser.GetMajor(vau)
        nsk.__minor = NeoVersionedAppUser.GetMinor(vau)
        nsk.__build = NeoVersionedAppUser.GetBuild(vau)
        nsk.__userScriptHash = NeoVersionedAppUser.GetUserScriptHash(vau)
        nsk.__domain = ToByteArray(domain)
        nsk.__className = ToByteArray(className)
        nsk.__index = index 
        nsk.__fieldName = fieldName
        nsk.__state = NeoEntityModel.SET

    def __Initialize(nsk: NeoStorageKey):
        nsk.__app = NeoEntityModel.NullByteArray
        nsk.__major = 0
        nsk.__minor = 0
        nsk.__build = 0
        nsk.__userScriptHash = NeoEntityModel.NullScriptHash
        nsk.__domain = NeoEntityModel.NullByteArray
        nsk.__className = NeoEntityModel.NullByteArray
        nsk.__index = 0 
        nsk.__fieldName = NeoEntityModel.NullByteArray
        nsk.__state = NeoEntityModel.NULL
        if NeoTrace.RUNTIME:
            LogExt("__Initialize(nsk).nsk", nsk)
        return nsk

    def New():
        nsk = NeoStorageKey()
        __Initialize(nsk)
        if NeoTrace.RUNTIME:
            LogExt("New().nsk", nsk)
        return nsk

    def New(app: bytes, major: int, minor: int, build: int, userScriptHash: bytes, domain: bytes, className: bytes, index: int, fieldName: bytes):
        nsk = NeoStorageKey()
        nsk.__app = app
        nsk.__major = major
        nsk.__minor = minor
        nsk.__build = build
        nsk.__userScriptHash = userScriptHash
        nsk.__domain = domain
        nsk.__className = className
        nsk.__index = index 
        nsk.__fieldName = fieldName
        nsk.__state = NeoEntityModel.INIT
        if NeoTrace.RUNTIME:
            LogExt("New(ab,m,m,b,u,cb,i,f,s).nsk", nsk)
        return nsk

    def New(vau: NeoVersionedAppUser, domain: bytes, className: bytes):
        if NeoVersionedAppUser.IsNull(vau):
            return NeoStorageKey.Null()
        nsk = NeoStorageKey()
        nsk.__app = NeoVersionedAppUser.GetAppNameAsByteArray(vau)
        nsk.__major = NeoVersionedAppUser.GetMajor(vau)
        nsk.__minor = NeoVersionedAppUser.GetMinor(vau)
        nsk.__build = NeoVersionAppUser.GetBuild(vau)
        nsk.__userScriptHash = NeoVersionedAppUser.GetUserScriptHash(vau)
        nsk.__domain = domain
        nsk.__className = className
        nsk.__state = NeoEntityModel.INIT
        if NeoTrace.RUNTIME:
            LogExt("New(vau, bc)", nsk)
        return nsk

    def Null():
        nsk = NeoStorageKey()
        __Initialize(nsk)
        if NeoTrace.RUNTIME:
            LogExt("Null().nsk", nsk)
        return nsk

    def IsNull(nsk: NeoStorageKey):
        return nsk.__state == NeoEntityModel.NULL

    def Log(label: str, nsk: NeoStorageKey):
        NeoTraceRuntime.TraceRuntime(label, nsk.__app, nsk.__major, nsk.__minor, nsk.__build, nsk.__domain, nsk.__className, nsk.__userScriptHash)

    def LogExt(label: str, nsk: NeoStorageKey):
        NeoTraceRuntime.TraceRuntime(label, nsk.__app, nsk.__major, nsk.__minor, nsk.__build, nsk.__domain, nsk.__className, nsk.__userScriptHash, nsk._state)

    __bLeftBrace = ToByteArray("{")
    __bRightBrace = ToByteArray("}")
    __bColon = ToByteArray(":")
    __bEquals = ToByteArray("=")
    __bSemiColon = ToByteArray(";")
    __ba = ToByteArray("a") 
    __bM = ToByteArray("M")
    __bm = ToByteArray("m")
    __bb = ToByteArray("b")
    __bu = ToByteArray("u")
    __bd = ToByteArray("d")
    __bc = ToByteArray("c")
    __bf = ToByteArray("f")
    __bStringType = ToByteArray(ContractParameterTypeLocal.String)
    __bBigIntegerType = ToByteArray(ContractParameterTypeLocal.Integer)
    __bByteArrayType = ToByteArray(ContractParameterTypeLocal.ByteArray)
    __bUserScriptHashType = ToByteArray(ContractParameterTypeLocal.ByteArray)

    def StorageKey(nsk: NeoStorageKey, index: int, fieldName: bytes):

        if NeoTrace.RUNTIME:
            LogExt("StorageKey(nsk,bi,bf).nsk", nsk)

        if NeoTrace.RUNTIME:
            TraceRuntime("StorageKey(nsk,bi,bf).nsk", index, fieldName)

        bkey = concat(nsk.__bLeftBrace, nsk.__ba)#app
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bStringType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__app)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bM)#major
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__major) #BigInteger
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bm)#minor
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__minor) #BigInteger
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bb)#build
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__build) #BigInteger
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bu) #userScriptHash
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__userScriptHash)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bd) #domain
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__domain)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bc) #class
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__className)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bi) #index
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, bindex)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bf) #fieldName
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, fieldName)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, __bRightBrace)

        if NeoTrace.RUNTIME:
            TraceRuntime("StorageKey(nsk,bi,bf).bkey$BSK", bkey)

        return bkey

    def StorageKey(nsk: NeoStorageKey, index: bytes, fieldName: bytes):

        if NeoTrace.RUNTIME:
            LogExt("StorageKey(nsk,i,bf).nsk", nsk)

        if NeoTrace.RUNTIME:
            TraceRuntime("StorageKey(nsk,i,bf).nsk", bindex, fieldName)

        bkey = concat(nsk.__bLeftBrace, nsk.__ba)#app
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bStringType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__app)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bM)#major
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__major) #BigInteger
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bm)#minor
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__minor) #BigInteger
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bb)#build
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__build) #BigInteger
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bu) #userScriptHash
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__userScriptHash)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bd) #domain
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__domain)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bc) #class
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, nsk.__className)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bi) #index
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, index) #BigInteger
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, nsk.__bf) #fieldName
        bkey = concat(bkey, nsk.__bColon)
        bkey = concat(bkey, nsk.__bBigIntegerType)
        bkey = concat(bkey, nsk.__bEquals)
        bkey = concat(bkey, fieldName)
        bkey = concat(bkey, nsk.__bSemiColon)
        bkey = concat(bkey, __bRightBrace)

        if NeoTrace.RUNTIME:
            TraceRuntime("StorageKey(nsk,i,bf).bkey$BSK", bkey)

        return bkey