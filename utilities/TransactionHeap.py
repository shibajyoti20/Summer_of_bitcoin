from heapq import heapify, heappop, heappush
from .TransactionNode import Node

class TransactionHeap:
    def __init__(self) -> None:
        self.heap = []
        self.nonremovable_parent_list = []
        self.max_weight = 4000000
        self.curr_weight = 0
        heapify(self.heap)

    def push(self, element) -> None:
        heappush(self.heap, element)
        self.curr_weight += element.weight

    def pop(self) -> Node:
        element = heappop(self.heap)
        self.curr_weight -= element.weight
        return element

    def get_top(self) -> Node:
        return self.heap[0]

    def get_heap(self):
        return self.heap

    def find(self, txid) -> bool:
        for parent_txid in self.heap:
            if(parent_txid.txid == txid):
                return parent_txid
        return False