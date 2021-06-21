from .TransactionNode import Node
from typing import List

class HeapManip:
    def __init__(self, txn_heap) -> None:
        self.txn_heap = txn_heap

    def checkParentPresentInHeap(self, parent_list: List):
        for parent in parent_list:
            response = self.txn_heap.find(parent)
            if not response:
                return False
        return True

    def addParentsToNonRemovableList(self, parent_list: List):
        for parent in parent_list:
            self.txn_heap.nonremovable_parent_list.append(parent)

    def checkIfHeapTopInNonRemovableList(self, txid: str):
        for parent_txid in self.txn_heap.nonremovable_parent_list:
            if(parent_txid == txid):
                return True
        return False

    def checkParentEqualsHeapTop(self, parent_txid: str):
        heap_top = self.txn_heap.get_top()
        if(parent_txid == heap_top.txid):
            return True
        return False

    def heapPush(self, txn: Node):
        new_heap_node = Node(txn.txid, txn.fee, txn.weight)
        if(txn.parent_list[0] != ''):
            self.addParentsToNonRemovableList(txn.parent_list)
        self.txn_heap.push(new_heap_node)

    def heapPopAndPush(self, txn: Node):
        heap_top = self.txn_heap.get_top()

        response = self.checkIfHeapTopInNonRemovableList(heap_top.txid)
        response2 = self.checkParentEqualsHeapTop(heap_top.txid)
        if not response and not response2:
            self.txn_heap.pop()
            self.heapPush(txn)