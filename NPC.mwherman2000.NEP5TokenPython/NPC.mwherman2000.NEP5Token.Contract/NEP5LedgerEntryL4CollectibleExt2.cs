using NPC.Runtime;
using Neo.SmartContract.Framework;
using System; // Template: NPCLevel4Part1Ext2_cs.txt
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// NPC.mwherman2000.NEP5Token.Contract.NEP5LedgerEntry - Level 4 Collectible (Extended)
///
/// Processed:      2018-04-21 10:49:17 PM by npcc - NEO Persistable Classes (NPC) Platform 2.1 Compiler v2.1.0.38328
/// NPC Project:    https://github.com/mwherman2000/neo-npcc2/blob/master/README.md
/// NPC Lead:       Michael Herman (Toronto) (mwherman@parallelspace.net)
/// </summary>

namespace NPC.mwherman2000.NEP5Token.Contract
{
    public partial class NEP5LedgerEntry : NeoTraceRuntime /* Level 4 Collectible */
    {
        /// <summary>
        /// Collectible methods (NPC Level 4)
        /// </summary>
        /// <param name="e">e</param>
        /// <param name="vau">vau</param>
        /// <param name="index">index</param>
        /// <returns>bool</returns>
        public static bool PutElement(NEP5LedgerEntry e, NeoVersionedAppUser vau, byte[] domain, byte[] bindex)
        {
            if (NeoVersionedAppUser.IsNull(vau)) return false;

            Neo.SmartContract.Framework.Services.Neo.StorageContext ctx = Neo.SmartContract.Framework.Services.Neo.Storage.CurrentContext;
            NeoStorageKey nsk = NeoStorageKey.New(vau, domain, _bClassName);

            // no readonly fields byte[] bsta = Neo.SmartContract.Framework.Services.Neo.Storage.Get(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bSTA));
            // no readonly fields if (NeoTrace.RUNTIME) TraceRuntime("Get(bkey).NEP5LedgerEntry.bsta", bsta.Length, bsta);
            // no readonly fields bool isMissing = false; if (bsta.Length == 0) isMissing = true;

            //byte[] bkey;
            e._state = NeoEntityModel.EntityState.PUTTED;
            Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bSTA), e._state.AsBigInteger());
 
            Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bTimestamp), e._timestamp); // Template: NPCLevel4APutElementExt2_cs.txt

            Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bDecription), e._decription); // Template: NPCLevel4APutElementExt2_cs.txt

            Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bDebitCreditAmount), e._debitCreditAmount); // Template: NPCLevel4APutElementExt2_cs.txt

            Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bBalance), e._balance); // Template: NPCLevel4APutElementExt2_cs.txt

            if (NeoTrace.RUNTIME) LogExt("PutElement(vau,i).NEP5LedgerEntry", e); // Template: NPCLevel4BGetElement_cs.txt
            return true;
        }

        /// <summary>
        /// Get an element of an array of entities from Storage based on a NeoStorageKey (NPC Level 4)
        /// </summary>
        /// <param name="vau">vau</param>
        /// <param name="index">index</param>
        /// <returns>NEP5LedgerEntry</returns>
        public static NEP5LedgerEntry GetElement(NeoVersionedAppUser vau, byte[] domain, byte[] bindex)
        {
            if (NeoVersionedAppUser.IsNull(vau)) return Null();

            Neo.SmartContract.Framework.Services.Neo.StorageContext ctx = Neo.SmartContract.Framework.Services.Neo.Storage.CurrentContext;
            NeoStorageKey nsk = NeoStorageKey.New(vau, domain, _bClassName);

            NEP5LedgerEntry e;
            //byte[] bkey;
            byte[] bsta = Neo.SmartContract.Framework.Services.Neo.Storage.Get(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bSTA));
            if (NeoTrace.RUNTIME) TraceRuntime("Get(bkey).NEP5LedgerEntry.bsta", bsta.Length, bsta);
            if (bsta.Length == 0)
            {
                e = NEP5LedgerEntry.Missing();
            }
            else // not MISSING
            {
                int ista = (int)bsta.AsBigInteger();
                NeoEntityModel.EntityState sta = (NeoEntityModel.EntityState)ista;
                if (sta == NeoEntityModel.EntityState.TOMBSTONED)
                {
                    e = NEP5LedgerEntry.Tombstone();
                }
                else // not MISSING && not TOMBSTONED
                {
                    e = new NEP5LedgerEntry();
                    BigInteger Timestamp = Neo.SmartContract.Framework.Services.Neo.Storage.Get(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bTimestamp)).AsBigInteger(); // Template: NPCLevel4CGetElement_cs.txt

                    string Decription = Neo.SmartContract.Framework.Services.Neo.Storage.Get(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bDecription)).AsString(); // Template: NPCLevel4CGetElement_cs.txt

                    BigInteger DebitCreditAmount = Neo.SmartContract.Framework.Services.Neo.Storage.Get(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bDebitCreditAmount)).AsBigInteger(); // Template: NPCLevel4CGetElement_cs.txt

                    BigInteger Balance = Neo.SmartContract.Framework.Services.Neo.Storage.Get(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bBalance)).AsBigInteger(); // Template: NPCLevel4CGetElement_cs.txt

                    e._timestamp = Timestamp; e._decription = Decription; e._debitCreditAmount = DebitCreditAmount; e._balance = Balance;  // NPCLevel4DBuryElement_cs.txt
                    e._state = sta;
                    e._state = NeoEntityModel.EntityState.GETTED; /* OVERRIDE */
                }
            }
            if (NeoTrace.RUNTIME) LogExt("Get(bkey).NEP5LedgerEntry.e", e);
            return e;
        }

        /// <summary>
        /// Bury an element of an array of entities in Storage based on a NeoStorageKey (NPC Level 4)
        /// </summary>
        /// <param name="vau">vau</param>
        /// <param name="index">index</param>
        /// <returns>NEP5LedgerEntry</returns>
        public static NEP5LedgerEntry BuryElement(NeoVersionedAppUser vau, byte[] domain, byte[] bindex)
        {
            if (NeoVersionedAppUser.IsNull(vau)) // TODO - create NeoEntityModel.EntityState.BADKEY?
            {
                return NEP5LedgerEntry.Null();
            }

            Neo.SmartContract.Framework.Services.Neo.StorageContext ctx = Neo.SmartContract.Framework.Services.Neo.Storage.CurrentContext;
            NeoStorageKey nsk = NeoStorageKey.New(vau, domain, _bClassName);

            //byte[] bkey;
            NEP5LedgerEntry e;
            byte[] bsta = Neo.SmartContract.Framework.Services.Neo.Storage.Get(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bSTA));
            if (NeoTrace.RUNTIME) TraceRuntime("Bury(vau,index).NEP5LedgerEntry.bsta", bsta.Length, bsta);
            if (bsta.Length == 0)
            {
                e = NEP5LedgerEntry.Missing();
            }
            else // not MISSING - bury it
            {
                e = NEP5LedgerEntry.Tombstone(); // TODO - should Bury() preserve the exist field values or re-initialize them? Preserve is cheaper but not as private
                Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bSTA), e._state.AsBigInteger());

                Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bTimestamp), e._timestamp); // NPCLevel4EBuryElement_cs.txt

                Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bDecription), e._decription); // NPCLevel4EBuryElement_cs.txt

                Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bDebitCreditAmount), e._debitCreditAmount); // NPCLevel4EBuryElement_cs.txt

                Neo.SmartContract.Framework.Services.Neo.Storage.Put(ctx, NeoStorageKey.StorageKey(nsk, bindex, _bBalance), e._balance); // NPCLevel4EBuryElement_cs.txt

            } // Template: NPCLevel4Part2_cs.txt
            if (NeoTrace.RUNTIME) LogExt("Bury(vau,i).NEP5LedgerEntry", e);
            return e;
        }
    }
}