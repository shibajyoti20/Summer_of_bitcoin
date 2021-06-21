class Node:
    def __init__(self, txid, fee, weight) -> None:
        self.txid = txid
        self.fee = fee
        self.weight = weight

    def __eq__(self, other):
        if self.fee == other.fee:
            return self.weight < other.weight

    def __lt__(self, other):
        return self.fee < other.fee