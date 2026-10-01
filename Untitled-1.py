def alpha_beta(node,alpha,beta,is_max):

    if isinstance(node,int):
        print("Evaluated:",node)
        return node

    if is_max:
        value=float('-inf')
        for child in node:
            value=max(value,alpha_beta(child,alpha,beta,False))
            alpha=max(alpha,value)

            if alpha>=beta:
                print("Pruning remaining branch")
                break
        return value
    else:
        value=float('inf')
        for child in node:
            value=min(value,alpha_beta(child,alpha,beta,True))
            beta=min(beta,value)

            if alpha>=beta:
                print("pruning remaining branch")
                break
        return value

tree=[[[4,2],[8,1]],[[5,3],[9,7]]]

result=alpha_beta(tree,float('-inf'),float('inf'),True)

print("\n Optimal Value:",result)