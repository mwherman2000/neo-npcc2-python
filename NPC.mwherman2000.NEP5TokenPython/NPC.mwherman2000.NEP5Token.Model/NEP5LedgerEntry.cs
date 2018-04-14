using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace NPC.mwherman2000.NEP5Token.Model
{
    public interface NPCLevel0Basic { }
    public interface NPCLevel1Managed { }
    public interface NPCLevel2Persistable { }

    public class NEP5LedgerEntry : NPCLevel0Basic,
                                   NPCLevel1Managed,
                                   NPCLevel2Persistable
    {
        BigInteger Timestamp;
        string Decription;
        BigInteger DebitCreditAmount;
        BigInteger Balance;
    }
}
