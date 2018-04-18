from boa.blockchain.vm.Neo.Runtime import CheckWitness, Notify

class NeoTrace():
    TRACEON = True
    SPLASH = True
    ARGSRESULT = True
    RUNTIME = False
    ERROR = True
    WARNING = True
    INFO = True
    VERBOSE = False
    TESTING = False

    def LogExt():
        Notify("TRACEON", self.TRACEON)
        Notify("SPLASH", self.SPLASH)
        Notify("ARGSRESULT", self.ARGSRESULT)
        Notify("RUNTIME", self.RUNTIME)
        Notify("ERROR", self.ERROR)
        Notify("WARNING", self.WARNING)
        Notify("INFO", self.INFO)
        Notify("VERBOSE", self.VERBOSE)
        Notify("TESTING", self.TESTING)

    def Trace(args):
        if self.TRACEON:
            Notify(args)

class NeoTraceRuntime():

    def TraceRuntime(args):
        if self.TRACEON:
            Notify(args)

