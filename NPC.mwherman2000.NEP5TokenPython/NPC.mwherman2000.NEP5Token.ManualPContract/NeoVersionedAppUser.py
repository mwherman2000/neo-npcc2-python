from NeoTrace import NeoTraceRuntime
from NeoEntityModel import NeoEntityModel
from boa.interop.Neo.Storage import GetContext, Get, Put, Delete
from boa.interop.BigInteger import FromBytes, ToByteArray
from boa.code.builtins import concat

class NeoVersionedAppUser(NeoTraceRuntime):
    __app = None
    __major = None
    __minor = None
    __build = None
    __userScriptHash = None
    __state = None

    def SetAppName(vau: NeoVersionedAppUser, value: bytes):
        vau.__app = value
        vau.__state = NeoEntityModel.SET

    def GetAppNameAsByteArray(vau: NeoVersionedAppUser):
        return vau.__app

    def SetAppName(vau: NeoVersionedAppUser, value: str):
        vau.__app = ToByteArray(value)
        vau.__state = NeoEntityModel.SET

    def GetAppNameAsString(vau: NeoVersionedAppUser):
        return FromBytes(vau.__app)

    def SetMajor(vau: NeoVersionedAppUser, value: int):
        vau.__major = value
        vau.__state = NeoEntityModel.SET
    
    def GetMajor(vau: NeoVersionedAppUser):
        return vau.__major

    def SetMinor(vau: NeoVersionedAppUser, value: int):
        vau.__minor = value
        vau.__state = NeoEntityModel.SET
    
    def GetMinor(vau: NeoVersionedAppUser):
        return vau.__minor

    def SetBuild(vau: NeoVersionedAppUser, value: int):
        vau.__build = value
        vau.__state = NeoEntityModel.SET

    def GetBuild(vau: NeoVersionedAppUser):
        return vau.__build

    def SetUserScriptHash(vau: NeoVersionedAppUser, value: bytes):
        vau.__userScriptHash = value
        vau.__state = NeoEntityModel.SET

    def GetUserScriptHash(vau: NeoVersionedAppUser):
        return vau.__userScriptHash

    def Set(vau: NeoVersionedAppUser, app: str, major: int, minor: int, build: int, userScriptHash: bytes):
        vau.__app = ToByteArray(app)
        vau.__major = major
        vau.__minor = minor
        vau.__build = build
        vau.__userScriptHash = userScriptHash
        vau.__state = NeoEntityModel.SET

    def Set(vau: NeoVersionedAppUser, app: bytes, major: int, minor: int, build: int, userScriptHash: bytes):
        vau.__app = app
        vau.__major = major
        vau.__minor = minor
        vau.__build = build
        vau.__userScriptHash = userScriptHash
        vau.__state = NeoEntityModel.SET

    def __Initialize(vau: NeoVersionedAppUser):
        vau.__app = NeoEntityModel.NullByteArray
        vau.__major = 0
        vau.__minor = 0
        vau.__build = 0
        vau.__state = NeoEntityModel.NULL
        if NeoTrace.RUNTIME:
            LogExt("__Initialize(vau).vau", vau)
        return vau

    def New():
        vau = NeoVersionedAppUser
        __Initialize(vau)
        if NeoTrace.RUNTIME:
            LogExt("New().vau", vau)
        return vau

    def New(app: bytes, major: int, minor: int, build: int, userScriptHash: bytes):
        vau = NeoVersionedAppUser()
        vau.__app = app
        vau.__major = major
        vau.__minor = minor
        vau.__build = build
        vau.__userScriptHash = userScriptHash
        vau.__state = NeoEntityModel.INIT
        if NeoTrace.RUNTIME:
            LogExt("New(ba,m,m,b,u).vau", vau)
        return vau

    def New(app: str, major: int, minor: int, build: int, userScriptHash: bytes):
        vau = NeoVersionedAppUser()
        vau.__app = ToByteArray(app)
        vau.__major = major
        vau.__minor = minor
        vau.__build = build
        vau.__userScriptHash = userScriptHash
        vau.__state = NeoEntityModel.INIT
        if NeoTrace.RUNTIME:
            LogExt("New(ba,m,m,b,u).vau", vau)
        return vau

    def Null():
        vau = NeoVersionedAppUser()
        __Initialize(vau)
        if NeoTrace.RUNTIME:
            LogExt("Null().vau", vau)
        return vau

    def IsNull(vau: NeoVersionedAppUser):
        return vau.__state == NeoEntityModel.NULL

    def Log(label: str, vau: NeoVersionedAppUser):
        NeoTraceRuntime.TraceRuntime(label, vau.__app, vau.__major, vau.__minor, vau.__build, vau.__userScriptHash)

    def LogExt(label: str, vau: NeoVersionedAppUser):
        NeoTraceRuntime.TraceRuntime(label, vau.__app, vau.__major, vau.__minor, vau.__build, vau.__userScriptHash, vau._state)