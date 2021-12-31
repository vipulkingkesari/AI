from durable.lang import *

with ruleset('run'):
    # will be triggered by 'run' facts
    @when_all((m.interests == 'ML') & (m.grade == '9') & (m.demand == 'theory'))
    def ai(c):
        c.assert_fact('required_skills', { 'flag': 'probability' })
        c.assert_fact({ 'subject': 'Take elective ML course.' })
        c.assert_fact('preference', { 'type': 'ML theory'})

    @when_all((m.interests == 'DL') & (m.grade == '9') &(m.demand=='theory'))
    def ai(c):
        c.assert_fact('required_skills', { 'flag': 'probability' })
        c.assert_fact({ 'subject': 'Take DL course.' })

    @when_all((m.interests == 'Developement') & (m.grade == '9') & (m.demand == 'practical'))
    def ai(c):
        c.assert_fact('required_skills', { 'flag': 'Coding' })
        c.assert_fact({ 'subject': 'Take elective SDOS course.' })
        c.assert_fact('preference', { 'type': 'Developement'})

    @when_all((m.interests=='Network_security') & (m.grade=='8') & (m.demand=='practical'))
    def ai(c):
        c.assert_fact('required_skills',{'flag':'scripting'})
        c.assert_fact({'subject':'Take os course.'})
        c.assert_fact('preference',{'type':'Network_security'})

    @when_all((m.interests=='CV') & (m.grade=='7') &(m.demand=='theory'))
    def ai(c):
        c.assert_fact('required_skills',{'flag':'programming'})
        c.assert_fact({'subject':'Take Math100 course.'})
        c.assert_fact('preference',{'type':'CV'})

    @when_all((m.interests =='IBC') & (m.grade=='9') &(m.demand=='theory'))
    def ai(c):
        c.assert_fact('required_skills' ,{'flag':'program'})
        c.assert_fact({'subject':'Take IBC course.'})
        c.assert_fact('preference',{'type':'IBC'})

    @when_all((m.interests =='AI') & (m.grade=='9') & (m.demand=='theory'))
    def ai(c):
        c.assert_fact('required_skills',{'flag':'prog'})
        c.assert_fact({'subject':'Take AI course'})
        c.assert_fact('preference',{'type':'AI'})

    @when_all((m.interests =='Compilers') & (m.grade=='7') & (m.demand=='theory'))
    def ai(c):
        c.assert_fact('required_skills',{'flag':'math'})
        c.assert_fact({'subject':'Take Compilers course and Digital circuits course'})
        c.assert_fact('preference',{'type':'Compilers'})

    @when_all((m.interests=='CN') & (m.grade=='7') & (m.demand=='practical'))
    def ai(c):
        c.assert_fact('required_skills',{'flag':'pro'})
        c.assert_fact({'subject':'Take DSA course.'})
        c.assert_fact('preference',{'type':'CN'})



    @when_all(+m.subject)
    def output(c):
        print('Fact: {0}'.format(c.m.subject))


with ruleset('required_skills'):
    @when_all((m.flag == 'probability'))
    def facts(d):
        d.assert_fact({ 'subject': 'Take Probability and Statistics course' })

    @when_all((m.flag == 'Coding'))
    def facts(d):
        d.assert_fact({ 'subject': 'Take AP course' })

    @when_all((m.flag=='scripting'))
    def facts(d):
        d.assert_fact({'subject':'Take Computer organiztion and OS course. '})

    @when_all((m.flag=='programming'))
    def facts(d):
        d.assert_fact({'subject':'Take AP course.'})

    @when_all((m.flag=='math'))
    def facts(d):
        d.assert_fact({'subject':'Take Maths100 and DM courses.'})

    @when_all((m.flag=='pro'))
    def facts(d):
        d.assert_fact({'subject':'Take AP course.'})

    @when_all((m.flag=='prog'))
    def facts(d):
        d.assert_fact({'subject':'Take AP course.'})

    @when_all((m.flag=='program'))
    def facts(d):
        d.assert_fact({'subject':'Take AP course.'})





    @when_all(+m.subject)
    def output(d):
        print('Fact: {0}'.format(d.m.subject))

with ruleset('preference'):
    @when_all((m.type == 'ML theory'))
    def do(e):
        e.assert_fact({ 'subject': 'Take Advanced ML theory course'})

    @when_all((m.type == 'Developement'))
    def do(e):
        e.assert_fact({ 'subject': 'Do an internship'})

    @when_all((m.type == 'Network_security'))
    def do(e):
        e.assert_fact({'subject':'Do Foundation of Computer security course.'})

    @when_all((m.type =='CV'))
    def do(e):
        e.assert_fact({'subject':'Do Discrete mathematics.'})

    @when_all((m.type=='IBC'))
    def do(e):
        e.assert_fact({'subject':'Do Applied cryptography course.'})

    @when_all((m.type=='AI'))
    def do(e):
        e.assert_fact({'subject':'Do electives of AI courses.'})


    @when_all((m.type=='Compilers'))
    def do(e):
        e.assert_fact({'subject':'Do DSA and DBMS courses.'})

    @when_all((m.type=='CN'))
    def do(e):
        e.assert_fact({'subject':'Do OS and ADA courses.'})



    @when_all(+m.subject)
    def output(c):
        print('Fact: {0}'.format(c.m.subject))

l = [{ 'interests': 'ML', 'grade': '9', 'demand':'theory' }, { 'interests': 'Developement', 'grade': '9', 'demand':'practical' },{'interests':'Network_security','grade':'8','demand':'practical'},{'interests':'CV','grade':'7','demand':'theory'},{'interests':'IBC','grade':'9','demand':'theory'},{'interests':'DL','grade':'9','demand':'theory'},{'interests':'AI','grade':'9','demand':'theory'},{'interests':'Compilers','grade':'7','demand':'theory'},{'interests':'CN','grade':'7','demand':'practical'}]
for i in l:
    print('For interest: '+i['interests']+' grade: '+i['grade']+' preference: '+i['demand'])
    assert_fact('run',i)
    print()