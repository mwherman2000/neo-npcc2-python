from boa.blockchain.vm.System.ExecutionEngine import GetScriptContainer, GetExecutingScriptHash
from boa.blockchain.vm.Neo.Transaction import Transaction, GetReferences, GetOutputs,GetUnspentCoins
from boa.blockchain.vm.Neo.Output import GetValue, GetAssetId, GetScriptHash


class NeoEntityModel():

    NULL = 0
    INIT = 1
    SET = 2
    PUTTED = 3
    GETTED = 4
    MISSING = 5
    TOMBSTONED = 6
    NOTAUTHORIZED = 7

    def AsBigInteger(self):
        pass

    def BytesToEntityState(self, bsta):
        pass

    def GetInvokingAddressScriptHash(self):
        """
        """
        tx = GetScriptContainer() 
        references = tx.References

        for r in references:
            return r.ScriptHash

        return b'0x0'