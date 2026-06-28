from random import sample

# LINKED LISTS FOR STORING CASE BY ARRIVAL TIME
class ListNode:
    def __init__(self, case_info):
        self.data = case_info
        self.next = None
 
class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, case_info): # add a value to the linked list
        if self.head == None:
            self.head = ListNode(case_info) # head is the value if head is None
            return "First case Added!!"
        
        else:
            current = self.head 
            while current.next != None:
                current = current.next
            current.next = ListNode(case_info) # appends to the next if head is not == None

    def display(self): # prints all the values in the linked list by arrival order
        current = self.head 
        elements = []

        while current != None:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(str(e) for e in elements))

    def delete(self, case_id):
        if self.head == None:
            return "No cases to show"
        
        elif self.head.data["case_id"] == case_id:
            self.head = self.head.next
            return f"Case: {case_id} has been deleted"
        
        else:
            previous = self.head
            current = self.head.next

            while current != None:
                if current.data["case_id"] == case_id:
                    previous.next = current.next
                    return f"Case: {current.data['case_name']} | ID {current.data['case_id']} deleted"
                previous = current
                current = current.next


# BINARY SEARCH TREE FOR CASE PRIORITY ORDER
class TreeNode:
    def __init__(self, case_info): # node constains whole case
        self.case_info = case_info
        self.left = None
        self.right = None

class BST:
    def __init__(self): # BST with empty root
        self.root = None

    def insert(self, node, case_info): # inserting into BST

        if node is None:
            return TreeNode(case_info) # if node is None, case_info becomes root
        
        elif case_info["priority"] > node.case_info["priority"]: # if root is not empty, check if priority is greater or less that root
            node.right = self.insert(node.right, case_info) # go left if it's greater than till root is None
        else:
            node.left = self.insert(node.left, case_info) # right if less than till root is None

        return node 

    def HightoLow(self, node): # in order traversal
        if node is None:
            return # return nothing if root is None
        else:
            self.HightoLow(node.right) # traverse rightmost
            print(node.case_info, end=", ") # seperate with ", " after each value
            self.HightoLow(node.left) # traverse leftmost


# HASH TABLE FOR CASE SEARCHING (even closed cases can be accessed)
class HashTable:

    def __init__(self):
        self.hash_table = [[] for _ in range(100)] # values stored in a list with 100 lists (making sure we have enough room)

    def hashFunction(self, case_info):
        case = case_info["case_id"] # extracts case ID from dict to use as key
        sum = 0
        for char in case:
            sum += ord(char) # converts char to unicode and sumns up the char
        return sum % 100 # modulus of the sum by the number of places we have in our hashtable
    
    def add(self, case_info): 
        index = self.hashFunction(case_info)
        self.hash_table[index].append(case_info)
        return f"Case: {case_info["case_name"]} added successfully to database!"

    def search(self, case_id):
        index = self.hashFunction({"case_id": case_id})
        for i in self.hash_table[index]:
            if  case_id == i["case_id"]:
                return f"Searched Case: {case_id} -> match found -> Name: {i["case_name"]}, Case ID: {i["case_id"]}, Priority: {i["priority"]}"
            else:
                return f"Case {case_id} not found. Check your search"

            
# INSERTION SORT for sorted list of cases
class InsertionSort:
    def sort(self, ht):
        all_cases = [] # to store all cases from hash table
        for bucket in ht.hash_table:
            for case in bucket: # get case from every list in the hash table
                all_cases.append(case) # put all cases in 'all_cases' lol

        for i in range(1, len(all_cases)):
            key = all_cases[i] # current case
            j = i - 1 # j is one step behind i, is the second pointer
            while j >= 0 and key["priority"] < all_cases[j]["priority"]: 
                all_cases[j + 1] = all_cases[j] # shifts larger lement one postition to the right
                j -= 1 
            all_cases[j + 1] = key # places key after right spot is found
        return all_cases

## DUMMY DATA FOR DEMO
def demo(ll, bst, ht, sorter):

    ll = Linkedlist()
    bst = BST()
    ht = HashTable()
    sorter = InsertionSort() 

    demo_cases = [
        {"case_id": "C001", "case_name": "State vs Mwale", "priority": 3},
        {"case_id": "C002", "case_name": "Banda vs Banda", "priority": 1},
        {"case_id": "C003", "case_name": "State vs Phiri", "priority": 5},
        {"case_id": "C004", "case_name": "Mutale vs City Council", "priority": 2},
        {"case_id": "C005", "case_name": "State vs Tembo", "priority": 4},
    ]
    for case in demo_cases:
        ll.append(case)
        bst.root = bst.insert(bst.root, case)
        ht.add(case)

    print("\n--- DEMO: INSERTION SORT ---")
    print("Sorting cases by priority (low to high)...\n")
    sorted_cases = sorter.sort(ht)
    for case in sorted_cases:
        print(f"  Priority {case['priority']} | {case['case_id']} | {case['case_name']}")

    print("\n--- DEMO: BST TRAVERSAL (High to Low Priority) ---")
    print("Traversing binary search tree by priority...\n")
    bst.HightoLow(bst.root)

    print("\n\n--- DEMO: HASH SEARCH vs LINEAR SEARCH ---")
    print("Searching for case C003...\n")
    
    # hash search
    import time
    start = time.time()
    result = ht.search("C003")
    hash_time = time.time() - start
    print(f"  Hash Search result: {result}")
    print(f"  Hash Search time: {hash_time:.10f} seconds")

    # linear search
    all_cases = []
    for bucket in ht.hash_table:
        for case in bucket:
            all_cases.append(case)
    
    start = time.time()
    for case in all_cases:
        if case["case_id"] == "C003":
            linear_result = case
            break
    linear_time = time.time() - start
    print(f"\n  Linear Search result: {linear_result}")
    print(f"  Linear Search time: {linear_time:.10f} seconds")
    print("\n  Hash search jumps directly to the case.")
    print("  Linear search scans every case until it finds a match.")
    
 

# MENU
# DICTIONARY input FORMAT WILL BE ------------> {"case_id", "case_name", "priority"}
def main():
    ll = Linkedlist()
    bst = BST()
    ht = HashTable()
    sorter = InsertionSort() 

    print("""
╔══════════════════════════════════════════════╗
║         CASE TRACKING SYSTEM                 ║
║         DSA Group Project — 2025             ║
╚══════════════════════════════════════════════╝
""")

    print("""
┌──────────────────────────────────────────────┐
│                   MAIN MENU                  │
├──────────────────────────────────────────────┤
│  1. Add Case                                 │
│  2. View Cases by Arrival Order              │
│  3. View Cases by Priority Order             │
│  4. Search Case                              │
│  5. View Sorted Cases                        │
│  6. Algorithm Demo                           │
│  0. Exit                                     │
└──────────────────────────────────────────────┘
    """)

    while True:
        option = int(input("Enter an option: "))

        if option == 1:
            case_id = input("Enter Case ID: ")
            case_name = input("Enter Case Name: ")
            priority = int(input("Enter Case Priority (number 0 - 20): "))

            case_info = {"case_id": case_id, "case_name": case_name, "priority": priority}

            ll.append(case_info)
            bst.root = bst.insert(bst.root, case_info)
            ht.add(case_info)

        elif option == 2:
            ll.display()
        
        elif option == 3:
            bst.HightoLow(bst.root)

        elif option == 4:
            search = input("Please enter Case ID: ")
            print(ht.search(search))

        elif option == 5:
            sorted_Cases = sorter.sort(ht)
            print(sorted_Cases)

        elif option == 6:
            demo(ll, bst, sorter, ht)

        elif option == 0:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()