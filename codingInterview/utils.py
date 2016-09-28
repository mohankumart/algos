def filterNestedJson(test):
    for detail in test:
        for mylist in detail['y']:
            for key in mylist.keys():
                if mylist[key] == 'mohan':
                    # del mylist[key]
                    break
            detail['y'].remove(mylist)
    print test

test = [
            {'y':[{'name':'mohan','hello':'testing'},{'name':'kumar'}]},
            {'y':[{'name':'test'}, {'name':'count'}]}
       ]


filterNestedJson(test)












