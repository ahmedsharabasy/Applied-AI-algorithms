A='A'
B='B'
enviroment={A:'dirty',B:'dirty','current':A}
global state   #معرفة فى كل الفانكشنز
def sensors():
    loc=enviroment['current']
    status=enviroment[loc]
    return(loc,status)
rule_action={1:'suck',2:'right',3:'left',4:'noop'}
rules={(A,'dirty'):1,(B,'dirty'):1,(A,'clean'):2,(B,'clean'):3,(A,B,'clean'):4}
state={}    #بنحط فيها الاكشنز والاحالات عشان تبق history مرجعلهاش تانى
action=None
model={A:None,B:None}

def rule_match(state,rules):     #بتجيبلى الروول عشان اخده واطلع الاكشن
    rule=rules.get(tuple(state))
    return rule
def update_state(state,action,percept):   #بيشيل القديم من الmodel ويحط الجديد
    (location,status)=percept
    state=percept
    if model[A]==model[B]=='clean':
        state=(A,B,'clean')
    model[location]=status
    return state

def reflex_agent_state(percept):
     global state, action      #ممكن نشيل جلوبال احنا كاتبينها فوق

     state = update_state(state, action, percept)
     rule = rule_match(state, rules)
     action = rule_action[rule]
     return action

def acctuators(action):
     loc = enviroment['current']
     if action == 'suck':
         enviroment[loc] = 'clean'
     elif action == 'right':
         enviroment['current'] = B
     elif action == 'left':
         enviroment['current'] = A

def run(n):
     global state
     print('current\t\t\tnew')
     print('( loc,status)\taction\t(loc,status)')
     for i in range(n):
         (loc1, stat1) = sensors()
         percept = (loc1, stat1)
         action = reflex_agent_state(percept)
         acctuators(action)
         (loc2, stat2) = sensors()
         state = update_state(state, action, percept)
         print((loc1, stat1), '\t', action, '\t', state)
run(12)
