class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
class node_data:
    def __init__(self,Node,level) -> None:
        self.node=Node
        self.level=level
def right_View(root):
    q=[root]
    q.append(None)
    print(root.value)
    while len(q)>0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                print(q[-1].value)
                q.append(None)
        else:
            # print(curr.value,end=' ')
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)  
if __name__=="__main__":
    root=node(1)

    root.left=node(2)
    root.right=node(3)

    root.left.left=node(4)
    root.left.right=node(5)

    root.right.left=node(6)
    root.right.right=node(7)

    root.left.right.left=node(9)
    root.left.right.right=node(10)

    root.right.right.right=node(11)

    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
    right_View(root)