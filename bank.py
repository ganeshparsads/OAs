

import heapq

class Account:
    def __init__(self, accountId, timeStamp):
        self.accountId = accountId
        self.timeStamp = timeStamp
        self.amount = 0
        self.transactions = []
        self.out_trans = 0
        self.cashback_heap = []
        
class Bank:
    def __init__(self):
        self.accounts = {}
payment_id = 0
payments = {}
account_heap = []

def solution(queries):
    nonlocal payment_id
    bank = Bank()
    # bank.accounts([])
    
    result = []

    for query in queries:
        if query[0] == "CREATE_ACCOUNT":
            timeStamp = query[1]
            accountId = query[2]
            
            # aid = int(re.findall(r'\b\d+\b', accountId)[0])
            if accountId not in bank.accounts:
                account_obj = Account(accountId, timeStamp)
                bank.accounts[accountId] = account_obj
                result.append("true")
                heapq.heappush(account_heap, (-0, accountId))
            else:
                result.append("false")
        
        elif query[0] == "DEPOSIT":
            timeStamp = query[1]
            accountId = query[2]
            amt = int(query[3])
            
            if accountId in bank.accounts:
                account_obj = bank.accounts[accountId]
                account_obj.amount += amt
                result.append(str(account_obj.amount))
            else:
                result.append("")
        elif query[0] == "TRANSFER":
            timeStamp = query[1]
            src_accnt = query[2]
            # aid = int(src_accnt)
            target_accnt = query[3]
            amt = int(query[4])            
            
            if src_accnt not in bank.accounts or target_accnt not in bank.accounts:
               result.append("")
            
            elif src_accnt == target_accnt:
                result.append("")
            else:
                src_obj = bank.accounts[src_accnt]
                target_obj = bank.accounts[target_accnt]
                while src_obj.cashback_heap and src_obj.cashback_heap[0] > timeStamp:
                    timestamp, cashamt = heapq.heappop(src_obj.cashback_heap)
                    src_obj.amount += cashamt

                if src_obj.amount < amt:
                    result.append("")
                else:
                    target_obj.amount += amt
                    src_obj.amount -= amt
                    
                    result.append(str(src_obj.amount))
                    src_obj.transactions.append(amt)
                    src_obj.out_trans += amt
                    heapq.heappush(account_heap, (-src_obj.out_trans, src_accnt))
                    bank.accounts[src_accnt] = src_obj
                    bank.accounts[target_accnt] = target_obj
        elif query[0] == "TOP_SPENDERS":
            topN = int(query[2])
            backup = []
            popped_acnt = set()
            result_str = []
            accounts = 0
            while accounts < topN and account_heap:
                amt, aid = heapq.heappop(account_heap)
                backup.append((amt, aid))
                if aid not in popped_acnt:
                    popped_acnt.add(aid)
                    # account_obj = bank.accounts["account" + aid]
                    account_obj = bank.accounts[aid]

                    result_str.append(account_obj.accountId + "(" + str(account_obj.out_trans) +  ")")
                    accounts += 1
            
            for (amt, aid) in backup:
                heapq.heappush(account_heap, (amt, aid))
            
            result.append(", ".join(result_str))
        elif query[0] == "PAY":
            timeStamp = int(query[1])
            accountId = query[2]
            amt = int(query[3])
            
            if accountId not in bank.accounts:
                result.append("")
                continue
            else:
                account_obj = bank.accounts[accountId]

                if account_obj.amount < amt:
                    result.append("")
                    continue
                
                account_obj.out_trans += amt
                heapq.heappush(self.account_obj.cashback_heap, (timeStamp + 86400000, int(0.02 * amt)))
                heapq.heappush(account_heap, (-account_obj.out_trans, accountId))
                payment_id += 1
                payment_iid = "payment" + payment_id
                payments[payment_iid] = accountId
                result.append(payment_iid)
        elif query[0] == "GET_PAYMENT_STATUS":
            timeStamp = int(query[1])
            accountId = query[2]
            amt = int(query[3])
            payid = query[4]
            account_obj = bank.accounts[accountId]
            if account_obj.cashback_heap and account_obj.cashback_heap[0] > timeStamp:
                result.append("IN_PROGRESS")
            else:
                result.append("COMPLETED")
            pass
            
            

    return result
                        

