using NPC.Runtime;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// NPC.mwherman2000.NEP5Token.Contract.NEP5LedgerEntry - Level 1 Managed
///
/// Processed:       2018-04-21 10:49:17 PM by npcc - NEO Persistable Classes (NPC) Platform 2.1 Compiler v2.1.0.38328
/// NPC Project:     https://github.com/mwherman2000/neo-npcc2/blob/master/README.md
/// NPC Lead:        Michael Herman (Toronto) (mwherman@parallelspace.net)
/// </summary>

namespace NPC.mwherman2000.NEP5Token.Contract
{
    public partial class NEP5LedgerEntry : NeoTraceRuntime /* Level 1 Managed */
    {
        private NeoEntityModel.EntityState _state;

        // Hidden constructor
        private NEP5LedgerEntry()
        {
        }

        // Accessors

        public static void SetTimestamp(NEP5LedgerEntry e, BigInteger value) // Template: NPCLevel1SetXGetX_cs.txt
                               { e._timestamp = value; e._state = NeoEntityModel.EntityState.SET; }
        public static BigInteger GetTimestamp(NEP5LedgerEntry e) { return e._timestamp; }
        public static void SetDecription(NEP5LedgerEntry e, string value) // Template: NPCLevel1SetXGetX_cs.txt
                               { e._decription = value; e._state = NeoEntityModel.EntityState.SET; }
        public static string GetDecription(NEP5LedgerEntry e) { return e._decription; }
        public static void SetDebitCreditAmount(NEP5LedgerEntry e, BigInteger value) // Template: NPCLevel1SetXGetX_cs.txt
                               { e._debitCreditAmount = value; e._state = NeoEntityModel.EntityState.SET; }
        public static BigInteger GetDebitCreditAmount(NEP5LedgerEntry e) { return e._debitCreditAmount; }
        public static void SetBalance(NEP5LedgerEntry e, BigInteger value) // Template: NPCLevel1SetXGetX_cs.txt
                               { e._balance = value; e._state = NeoEntityModel.EntityState.SET; }
        public static BigInteger GetBalance(NEP5LedgerEntry e) { return e._balance; }
        public static void Set(NEP5LedgerEntry e, BigInteger Timestamp, string Decription, BigInteger DebitCreditAmount, BigInteger Balance) // Template: NPCLevel1Set_cs.txt
                                { {e._timestamp = Timestamp; e._decription = Decription; e._debitCreditAmount = DebitCreditAmount; e._balance = Balance;  e._state = NeoEntityModel.EntityState.SET;} }        
        // Factory methods // Template: NPCLevel1Part2_cs.txt
        private static NEP5LedgerEntry _Initialize(NEP5LedgerEntry e)
        {
            e._timestamp = 0; e._decription = ""; e._debitCreditAmount = 0; e._balance = 0; 
            e._state = NeoEntityModel.EntityState.NULL;
            if (NeoTrace.RUNTIME) LogExt("_Initialize(e).NEP5LedgerEntry", e);
            return e;
        }
        public static NEP5LedgerEntry New()
        {
            NEP5LedgerEntry e = new NEP5LedgerEntry();
            _Initialize(e);
            if (NeoTrace.RUNTIME) LogExt("New().NEP5LedgerEntry", e);
            return e;
        }
        public static NEP5LedgerEntry New(BigInteger Timestamp, string Decription, BigInteger DebitCreditAmount, BigInteger Balance)
        {
            NEP5LedgerEntry e = new NEP5LedgerEntry();
            e._timestamp = Timestamp; e._decription = Decription; e._debitCreditAmount = DebitCreditAmount; e._balance = Balance; 
            e._state = NeoEntityModel.EntityState.INIT;
            if (NeoTrace.RUNTIME) LogExt("New(.,.).NEP5LedgerEntry", e);
            return e;
        }
        public static NEP5LedgerEntry Null()
        {
            NEP5LedgerEntry e = new NEP5LedgerEntry();
            _Initialize(e);
            if (NeoTrace.RUNTIME) LogExt("Null().NEP5LedgerEntry", e);
            return e;
        }

        // EntityState wrapper methods
        public static bool IsNull(NEP5LedgerEntry e)
        {
            return (e._state == NeoEntityModel.EntityState.NULL);
        }

        // Log/trace methods
        public static void Log(string label, NEP5LedgerEntry e)
        {
            TraceRuntime(label, e._timestamp, e._decription, e._debitCreditAmount, e._balance);
        }
        public static void LogExt(string label, NEP5LedgerEntry e)
        {
            TraceRuntime(label, e._timestamp, e._decription, e._debitCreditAmount, e._balance, e._state);
        }
    }
}