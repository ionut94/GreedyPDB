domains = [
{'description': 'The scenario is the following: There is a building with N+1 floors, numbered from 0 to N. The building can be separated in blocks of size M+1, where M divides N. Adjacent blocks have a common floor. For example, suppose N=12 and M=4, then we have 13 floors in total (ranging from 0 to 12), which form 3 blocks of 5 floors each, being 0 to 4, 4 to 8 and 8 to 12. The building has K fast (accelarating) elevators that stop only in floors that are multiple of M/2 (so M has to be an even number). Each fast elevator has a capacity of X persons. Furthermore, within each block, there are L slow elevators, that stop at every floor of the block. Each slow elevator has a capacity of Y persons (usually Y<X). There are costs associated with each elavator starting/stoping and moving. In particular, fast (accelarating) elevators have negligible cost of starting/stoping but have significant cost while moving. On the other hand, slow (constant speed) elevators have significant cost when starting/stoping and negligible cost while moving. Travelling times between floors are given for any type of elevator, taking into account the constant speed of the slow elevators and the constant acceleration of the fast elevators. There are several passengers, for which their current location (i.e. the floor they are) and their destination are given. The planning problem is to find a plan that moves the passengers to their destinations while minimizing the total cost of moving the passengers to their destinations . The total cost is increased each time an elevator starts/stops or moves.',
 'ipc': '2000',
 'name': 'elevators',
 'problems': [('elevators-00-adl/domain.pddl',
               'elevators-00-adl/m10-strips.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s1-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s1-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s1-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s1-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s1-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s10-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s10-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s10-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s10-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s10-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s11-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s11-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s11-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s11-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s11-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s12-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s12-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s12-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s12-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s12-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s13-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s13-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s13-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s13-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s13-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s14-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s14-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s14-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s14-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s14-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s15-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s15-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s15-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s15-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s15-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s16-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s16-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s16-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s16-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s16-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s17-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s17-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s17-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s17-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s17-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s18-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s18-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s18-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s18-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s18-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s19-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s19-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s19-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s19-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s19-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s2-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s2-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s2-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s2-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s2-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s20-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s20-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s20-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s20-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s20-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s21-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s21-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s21-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s21-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s21-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s22-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s22-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s22-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s22-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s22-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s23-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s23-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s23-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s23-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s23-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s24-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s24-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s24-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s24-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s24-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s25-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s25-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s25-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s25-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s25-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s26-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s26-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s26-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s26-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s26-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s27-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s27-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s27-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s27-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s27-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s28-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s28-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s28-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s28-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s28-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s29-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s29-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s29-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s29-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s29-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s3-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s3-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s3-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s3-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s3-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s30-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s30-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s30-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s30-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s30-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s4-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s4-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s4-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s4-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s4-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s5-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s5-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s5-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s5-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s5-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s6-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s6-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s6-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s6-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s6-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s7-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s7-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s7-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s7-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s7-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s8-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s8-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s8-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s8-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s8-4.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s9-0.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s9-1.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s9-2.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s9-3.pddl'),
              ('elevators-00-adl/domain.pddl', 'elevators-00-adl/s9-4.pddl')]}
]