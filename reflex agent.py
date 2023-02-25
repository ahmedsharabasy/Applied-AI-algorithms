A='A'
B='B'
enviroment={A:'dirty',B:'dirty','current':A}
def sensors():
    loc=enviroment['current']
    status=enviroment[loc]
    return(loc,status)

def reflex_vacuum_agent(loc,status):
    if status=='dirty':
        return'suck'
    elif loc==A:
        return'right'
    elif loc==B:
        return'left'

def acctuators(action):
    loc =enviroment['current']
    if action=='suck':
        enviroment[loc]='clean'
    elif action=='right':
        enviroment['current']=B
    elif action=='left':
        enviroment['current']=A

# def run(n):
#     print('current\t\t\tnew')
#     print('( loc,status)\taction\t(loc,status)')
#     for i in range(n):
#         (loc1,stat1)=sensors()
#         action=reflex_vacuum_agent(loc1,stat1)
#         acctuators(action)
#         (loc2,stat2)=sensors()
#         print((loc1,stat1),'\t',action,'\t',(loc2,stat2))
# run(5)
def run(n):
    print("current \t\t new")
    for i in range(n):       
        (loc1,status1)=sensors()
        action=reflex_vacuum_agent(loc1,status1)
        acctuators(action)
        (loc2,status2)=sensors()
        print((loc1,status1), '\t', action ,'\t', (loc2,status2))

run(5)