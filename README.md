# zero-divisor_semigroup

do the following on the command line
> download or git clone https://github.com/Paulcappaert/zero-divisor_semigroup.git
> cd zero-divisor_semigroup
> python3

>>from zdg.zdg import ZeroDivisorGraph as ZDG

Define a zero divisor graph from edges
>> graph = ZDG((1,2),(2,3),(3,4),zero=0)

Get a list of possible semigroups and save it in a variable
>> semigroups = graph.get_semigroups()

Get the number of semigrups
>>print(len(semigroups))

print all of the caley table of the possible semigroups
>>for s in semigroups:
    print(s.caley_table)
