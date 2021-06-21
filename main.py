from utilities.TransactionHeap import TransactionHeap
from utilities.MempoolTransactions import MempoolTransaction, parse_mempool_csv
from utilities.HeapManipulator import HeapManip


def filterTransactionForBlock(txn_heap: TransactionHeap, txn: MempoolTransaction):

    max_weight = txn_heap.max_weight
    free_weight = max_weight - txn_heap.curr_weight

    """ Creating Object of HeapManip Class for further use in this function"""
    heap = HeapManip(txn_heap)  

    """ 
        Check if the transaction has any parent transactions.
        Also check if parent transaction is in heap.
    """
    if(txn.parent_list[0] != ''):
        response = heap.checkParentPresentInHeap(txn.parent_list)
        if not response:
            return

    """  If current transaction weight < available weight, add transaction to heap. 
         Else process further
    """
    if(txn.weight <= free_weight):
        heap.heapPush(txn)

    
    elif(txn.weight > free_weight):
        heap_top = txn_heap.get_top()
        if(txn.fee > heap_top.fee and txn.weight <= heap_top.weight + free_weight):
            heap.heapPopAndPush(txn)

        elif(txn.fee == heap_top.fee):
            if(txn.weight < heap_top.weight):
                heap.heapPopAndPush(txn)

        
# Driver Function

if __name__ == "__main__":
    # Parse Mempool Transactions
    mempool_transactions = parse_mempool_csv()

    # Create new Heap
    min_heap = TransactionHeap()

    # Filter Mempool Transactions for including in Block
    for txn in mempool_transactions:
        filterTransactionForBlock(min_heap, txn)

    # Include the Filtered Transactions in the block
    heap = min_heap.get_heap()
    with open('block.txt',"w+") as ptr:
        for txn in heap:
            ptr.write(f"{txn.txid}\n")