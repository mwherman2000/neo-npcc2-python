using Neo.SmartContract.Framework;
using Neo.SmartContract.Framework.Services.Neo;
using System;
using System.Numerics;
using NPC.Runtime;

namespace NPC.mwherman2000.NEP5Token.Contract
{
    public class Contract1 : SmartContract
    {
        private const string NEOAccount = "ATrzHaicmhRj15C3Vv6e6gLfLqhSD2PtTr";
        private static readonly byte[] _NEOAccountScriptHash = NEOAccount.ToScriptHash(); // .ToScriptHash() // .AsByteArray();
        private static readonly byte[] _NEOAccountScriptHash_Nonexistent = (NEOAccount + "xyz").ToScriptHash();

        public static NEP5LedgerEntry Main()
        {
            // Use case 0
            NEP5LedgerEntry entry0 = NEP5LedgerEntry.New();
            NEP5LedgerEntry.LogExt("entry0", entry0);
            if (NEP5LedgerEntry.IsNull(entry0))
            {
                NeoTrace.Trace("entry0 is null", entry0);
            }
            else
            {
                NeoTrace.Trace("entry0 is not null", entry0);
            }

            // Use case 1
            NEP5LedgerEntry entry1 = NEP5LedgerEntry.New(12345678, "Initial balance", +100, 100);
            NEP5LedgerEntry.LogExt("entry1", entry1);
            if (NEP5LedgerEntry.IsNull(entry1))
            {
                NeoTrace.Trace("entry1 is null", entry1);
            }
            else
            {
                NeoTrace.Trace("entry1 is not null", entry1);
            }

            // Use case 2
            NEP5LedgerEntry.Put(entry1, _NEOAccountScriptHash);

            // Use case 3
            NEP5LedgerEntry entry3 = NEP5LedgerEntry.Get(_NEOAccountScriptHash);
            NEP5LedgerEntry.LogExt("entry3", entry3);
            if (NEP5LedgerEntry.IsMissing(entry3))
            {
                NeoTrace.Trace("entry3 is missing", entry3);
            }
            else
            {
                NeoTrace.Trace("entry3 is not missing", entry3);
            }

            // Use case 4
            NEP5LedgerEntry entry4 = NEP5LedgerEntry.Get(_NEOAccountScriptHash_Nonexistent);
            NEP5LedgerEntry.LogExt("entry4", entry4);
            if (NEP5LedgerEntry.IsMissing(entry4))
            {
                NeoTrace.Trace("entry4 is missing", entry4);
            }
            else
            {
                NeoTrace.Trace("entry4 is not missing", entry4);
            }

            return entry3;
        }
    }
}
