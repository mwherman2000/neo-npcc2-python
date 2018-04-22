using NPC.Runtime;
using Neo.SmartContract.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// NPC.mwherman2000.NEP5Token.Contract.NEP5LedgerEntry - Level 3 Deletable
///
/// Processed:      2018-04-21 10:49:17 PM by npcc - NEO Persistable Classes (NPC) Platform 2.1 Compiler v2.1.0.38328
/// NPC Project:    https://github.com/mwherman2000/neo-npcc2/blob/master/README.md
/// NPC Lead:       Michael Herman (Toronto) (mwherman@parallelspace.net)
/// </summary>

namespace NPC.mwherman2000.NEP5Token.Contract
{
    public partial class NEP5LedgerEntry : NeoTraceRuntime /* Level 3 Deletable */
    {
        // Deletable methods
        public static bool IsBuried(NEP5LedgerEntry e)
        {
            return (e._state == NeoEntityModel.EntityState.TOMBSTONED);
        }

        public static NEP5LedgerEntry Tombstone()
        {
            NEP5LedgerEntry e = new NEP5LedgerEntry();
            e._timestamp = 0; e._decription = ""; e._debitCreditAmount = 0; e._balance = 0; 
            e._state = NeoEntityModel.EntityState.TOMBSTONED;
            if (NeoTrace.RUNTIME) LogExt("Tombstone().NEP5LedgerEntry", e);
            return e;
        }

        public static NEP5LedgerEntry Bury(byte[] key)
        {
            if (key.Length == 0) return Null();

            Neo.SmartContract.Framework.Services.Neo.StorageContext ctx = Neo.SmartContract.Framework.Services.Neo.Storage.CurrentContext;
            byte[] _bkeyTag = Helper.Concat(key, _bclassKeyTag);

            NEP5LedgerEntry e;
            byte[] bsta = Neo.SmartContract.Framework.Services.Neo.Storage.Get(ctx, Helper.Concat(_bkeyTag, _bSTA));
            if (NeoTrace.RUNTIME) TraceRuntime("Bury(bkey).bsta", bsta.Length, bsta);
            if (bsta.Length == 0)
            {
                e = NEP5LedgerEntry.Missing();
            }
            else // not MISSING - bury it
            {
                e = NEP5LedgerEntry.Tombstone(); // but don't overwrite existing field values - just tombstone it
                Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, Helper.Concat(_bkeyTag, _bSTA), e._state.AsBigInteger());

                //Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, Helper.Concat(_bkeyTag, _bTimestamp), e._timestamp); // Template: NPCLevel3ABury_cs.txt
                //Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, Helper.Concat(_bkeyTag, _bDecription), e._decription); // Template: NPCLevel3ABury_cs.txt
                //Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, Helper.Concat(_bkeyTag, _bDebitCreditAmount), e._debitCreditAmount); // Template: NPCLevel3ABury_cs.txt
                //Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, Helper.Concat(_bkeyTag, _bBalance), e._balance); // Template: NPCLevel3ABury_cs.txt
            } // Template: NPCLevel3BBury_cs.txt
            if (NeoTrace.RUNTIME) LogExt("Bury(bkey).NEP5LedgerEntry", e); 
            return e; // return Entity e to signal if key is Missing or bad key
        }

        public static NEP5LedgerEntry Bury(string key)
        {
            if (key.Length == 0) return Null(); 

            Neo.SmartContract.Framework.Services.Neo.StorageContext ctx = Neo.SmartContract.Framework.Services.Neo.Storage.CurrentContext;
            string _skeyTag = key + _classKeyTag;

            NEP5LedgerEntry e;
            byte[] bsta = Neo.SmartContract.Framework.Services.Neo.Storage.Get(ctx, _skeyTag + _sSTA);
            if (NeoTrace.RUNTIME) TraceRuntime("Bury(skey).NEP5LedgerEntry.bsta", bsta.Length, bsta);
            if (bsta.Length == 0)
            {
                e = NEP5LedgerEntry.Missing();
            }
            else // not MISSING - bury it
            {
                e = NEP5LedgerEntry.Tombstone(); // but don't overwrite existing field values - just tombstone it
                Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, _skeyTag + _sSTA, e._state.AsBigInteger());

                //Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, _skeyTag + _sTimestamp, e._timestamp); // Template: NPCLevel3CBury_cs.txt
                //Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, _skeyTag + _sDecription, e._decription); // Template: NPCLevel3CBury_cs.txt
                //Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, _skeyTag + _sDebitCreditAmount, e._debitCreditAmount); // Template: NPCLevel3CBury_cs.txt
                //Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, _skeyTag + _sBalance, e._balance); // Template: NPCLevel3CBury_cs.txt
            } // Template: NPCLevel3Part2_cs.txt
            if (NeoTrace.RUNTIME) LogExt("Bury(skey).NEP5LedgerEntry", e);
            return e; // return Entity e to signal if key is Missing or bad key
        }
    }
}