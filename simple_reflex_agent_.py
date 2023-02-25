# A simplex reflex agent takes actions based on current situational experiences.
A='A'
B='B'
enviroment={A:'dirty',B:'dirty','current':A}

def sensors():
    loc=enviroment['current']
    status=enviroment[loc]
    return(loc,status)

rule_action={1:'suck',2:'right',3:'left',4:'noop'}
rules={(A,'dirty'):1,(B,'dirty'):1,(A,'clean'):2,(B,'clean'):3,(A,B,'clean'):4}

def rule_match(state,rules):
    rule=rules.get(tuple(state))
    return rule

def simple_reflex_agent(loc,status):
    state=(loc,status)
    rule=rule_match(state,rules)
    action=rule_action[rule]
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
    print('current\t\t\tnew')
    for i in range(n):
        if enviroment[A] == 'clean' and enviroment[B] == 'clean':
            rule = rules[(A, B, 'clean')]
            action = rule_action[rule]
            print('(A,B, clean)\t', action)
            break
        (loc1, stat1) = sensors()
        action = simple_reflex_agent(loc1, stat1)
        acctuators(action)
        (loc2, stat2) = sensors()
        print((loc1, stat1), '\t', action, '\t', (loc2, stat2))

run(10)
