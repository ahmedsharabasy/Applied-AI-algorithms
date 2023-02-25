A='A'
B='B'
percepts=[]
table={
((A,'clean'),):'right',((B,'clean'),):'right',
((A,'dirty'),):'suck',((B,'dirty'),):'suck',
((A,'clean'),(A,'clean')):'right',
((A,'clean'),(A,'dirty')):'suck',
((A,'clean'),(B,'clean')):'left',
((A,'clean'),(B,'dirty')):'suck',
((B,'clean'),(B,'clean')):'left',
((B,'clean'),(B,'dirty')):'suck',
((B,'clean'),(A,'clean')):'right',
((B,'clean'),(A,'dirty')):'suck',
((A,'clean'),(B,'clean'),(B,'dirty')):'suck'
}

# def lookUp(percepts,table):
#     action=table.get(tuple(percepts))
#     return action

# def table_driven_agent(percept):
#     percepts.append(percept)
#     action=lookUp(percepts,table)
#     return action

#بدل الاتنين فانكشن الى فوق
def table_driven_agent(percept):
    percepts.append(percept)
    action=table.get(tuple(percepts))
    return action

def run():
    print('action \t percept')
    print(table_driven_agent((A,'clean'),),'\t',percepts)
    print(table_driven_agent((B,'clean'),),'\t',percepts)
    print(table_driven_agent((B,'dirty')),'\t',percepts)

run()   