# User roles

# ==============================================================================
# Band
# ==============================================================================
class BandRole():
    "Band role"
    def __init__(self, name):
        self.name = name
        self.musicians = []
            
band_roles = []
band_roles.append(BandRole("Lead"))
band_roles.append(BandRole("Drums"))
band_roles.append(BandRole("Bass"))
band_roles.append(BandRole("Keys"))
band_roles.append(BandRole("Guitar (Acoustic)"))
band_roles.append(BandRole("Guitar (Electric)"))
band_roles.append(BandRole("BV (soprano)"))
band_roles.append(BandRole("BV (alto)"))
band_roles.append(BandRole("BV (tenor/bass)"))
band_roles.append(BandRole("Cello"))


# ==============================================================================
# Members
# ==============================================================================
class MemberRole():
    "Role of a band member"
    def __init__(self, name, min, max):
        self.name = name
        if min <= max:
            self.min = min      # Min playing interval (1 in "min" weeks)
            self.max = max      # Max playing interval (1 in "max" weeks)
        else:
            print("Error: Role min [%d] interval < max [%d]" % (min, max))


class Member():
    "Band member details"
    def __init__(self, name):
        self.name = name
        self.roles = []
        self.events = []      # List of week numbers available

def setAvailability(name, events):
    match = 0
    for member in members:
        if name == member.name:
           member.events = events
           match = 1
    if match == 0:
       print("Error: no match found (setAvailability)")
    return
    
def setRole(m_name, r_name, min, max):
    match = 0
    for member in members:
        if m_name == member.name:
            member.roles.append(MemberRole(r_name, min, max))
            match = 1
    if match == 0:
       print("Error: no match found (setRole)")
    return        
        
        
        
members = []

members.append(Member("PhilH"))
setRole("PhilH", "Lead", 1, 4)
setRole("PhilH", "Guitar (Acoustic)", 4, 4)

members.append(Member("Karen"))
setRole("Karen", "Lead", 1, 4)
setRole("Karen", "Keys", 1, 4)
setRole("Karen", "BV (soprano)", 1, 4)

members.append(Member("Aiden"))
setRole("Aiden", "Lead", 1, 4)
setRole("Aiden", "Guitar (Electric)", 1, 4)
setRole("Aiden", "Bass", 1, 4)

members.append(Member("Cecil"))
setRole("Cecil", "Guitar (Electric)", 1, 4)

members.append(Member("Matt"))
setRole("Matt", "Bass", 1, 4)

members.append(Member("Les"))
setRole("Les", "Bass", 4, 4)
setRole("Les", "BV (tenor/bass)", 4, 4)

members.append(Member("Dan"))
setRole("Dan", "Lead", 4, 4)
setRole("Dan", "Guitar (Acoustic)", 4, 4)

members.append(Member("Amy"))
setRole("Amy", "BV (soprano)", 1, 4)

members.append(Member("Faith"))
setRole("Faith", "BV (soprano)", 1, 4)
setRole("Faith", "Keys", 1, 4)

members.append(Member("Hannah"))
setRole("Hannah", "BV (soprano)", 1, 4)

members.append(Member("HelenT"))
setRole("HelenT", "Lead", 4, 4)
setRole("HelenT", "Guitar (Acoustic)", 4, 4)

members.append(Member("Jamarl"))
setRole("Jamarl", "Lead", 1, 4)
setRole("Jamarl", "Drums", 2, 4)

members.append(Member("Sigrid"))
setRole("Sigrid", "Cello", 1, 4)

# List Members
print("\n ======== Members ========")
for member in members:
    print("%s: " % member.name)
    for m_role in member.roles:
        print("%s, [min:%d, max:%d]" % (m_role.name, m_role.min, m_role.max))


        
        

# Create list of people for each role
print("\n======= Band Roles =============")
for b_role in band_roles:
    for musician in members:
        for m_role in musician.roles:
             if b_role.name == m_role.name:
                b_role.musicians.append(musician)
                 
for b_role in band_roles:
    print("%s: " % b_role.name, end='')
    for musician in b_role.musicians:
        print("%s, " % musician.name, end='')
    print("")
        
        

        
        
# ==============================================================================
# Event
# ==============================================================================
class EventRole():
    "Role with single musician"
    def __init__(self, name, musician):
        self.name = name
        self.musician = musician
        
class Event():
    "Individual session"
    def __init__(self, rota_num, month_num):
        self.rota_num = rota_num        # Number of event in rota
        self.month_num = month_num      # Number of event in month
        self.date = 0  
        self.musicians = []
        self.roles = []
    

        
# ==============================================================================
# Rota (list of events)
# ==============================================================================
rota = []

# Rota configuration:
# Event where role is not required (e.g. 3:bass)
# Event (by week #) where band not required (e.g. 3)
for i in range(0,12):
    rota.append(Event(i, i % 4))
    
    
# Find each member and set availability
setAvailability("PhilH", [0 ,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Karen", [0 ,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Aiden", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Cecil", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Matt", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Les", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Dan", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Amy", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Faith", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Hannah", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("HelenT", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Jamarl", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
setAvailability("Sigrid", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

print("\n ================== Availability ==================")
for member in members:
    print("%s: %s" % (member.name, member.events))


def addToRota(rota, event, member, b_role):
    added = 0
    if member in event.musicians:
        #print("Member already scheduled")
        added = 0 # dummy statement
    elif event.rota_num not in member.events:
        print("Warning: member [%s] not available on week %d" % (member.name, event.rota_num))
    else:
        overworked = 0
        # Determine if member has already been rota'd on too many times.
        for m_role in member.roles:
            if m_role.name == b_role.name:
               min = m_role.min
               max = m_role.max
        for i in range(event.rota_num - (min - 1), event.rota_num):
            for e_role in rota[i].roles:
                if e_role.name == b_role.name:
                    if member == e_role.musician:
                        overworked = 1

        
        
        if overworked == 0:
            # Choose the next member in line.
            event.roles.append(EventRole(b_role.name, member))
            event.musicians.append(member)
                
            # Move the musician to the end to favour others.
            b_role.musicians.remove(member)
            b_role.musicians.append(member)
        
            #print("Add %s to %s on week %d" % (member.name, b_role.name, event.rota_num))
            added = 1
 
    return added
    
    

# Construct Rota.
print("\n============ CONSTRUCT ROTA ===============")
for event in rota:
    #print(event.rota_num, event.month_num)
    for b_role in band_roles:
        #print(b_role.name)
        
        # Determine if any musicians for role will not satisfy max. interval condition.
        added = 0
        critical = []
        for member in b_role.musicians:
            missing = 0
            
            # Find the role information for member.
            for m_role in member.roles:
                if m_role.name == b_role.name:
                   min = m_role.min
                   max = m_role.max
            
            #print("Week: %d, max: %d" % (event.rota_num, max))
            for i in range(event.rota_num+1, event.rota_num + max):
                if i < len(rota):
                    if i not in member.events:
                        missing+=1
            if missing >= (max-1):
                critical.append(member)
        
        if len(critical) > 1:
            print("Error: More than one member can't fulfil minimum rota frequency")
        
        if len(critical):
            print("************ %d ***********************" % len(critical))
            added = addToRota(rota, event, critical[0], b_role)
        
        # Other selection rules here....
        #if selected:
            #added = addToRota(rota, event, "member", b_role)
        
        if added == 0:
            # if none are critical, add the first available member.        
            for member in b_role.musicians:
                #print(member.name)
                # Determine whether the member is selected for role.
                selected = 1
                if selected == 1:
                    added = addToRota(rota, event, member, b_role)
                    if added == 1:
                        break # When member is successfully added to role stop looking
        
        if added == 0:
            print("Error: could not find musician for '%s'" % b_role.name)
        
    #for musician in event.musicians:
        #print("Scheduled: %s" % musician.name)

print("================== ROTA (allocations) ==================")
for event in rota:
    print(event.rota_num)
    for e_role in event.roles:
        print(e_role.name, e_role.musician.name)

# Output rota to CSV.
f = open('rota.csv', 'w')
f.write("Week, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s\n" % \
(band_roles[0].name, band_roles[1].name, band_roles[2].name, band_roles[3].name\
, band_roles[4].name, band_roles[5].name, band_roles[6].name, band_roles[7].name\
, band_roles[8].name, band_roles[9].name))

for event in rota:
    f.write("%d, " % event.rota_num)
    for b_role in band_roles:
        found = 0
        for e_role in event.roles:
            if e_role.name == b_role.name:
                found = 1
                f.write("%s, " % e_role.musician.name)
        if found == 0:
            f.write(", ")
    f.write("\n")            


print("=================== Cumulatives ======================")
for member in members:
    count = 0
    for event in rota:
        for e_role in event.roles:
            if member.name == e_role.musician.name:
                count += 1        
    print("%s: %d" % (member.name, count))    



# New features:
# - Add instrument for leader
# - Group people on certain events (families). Dependency rule
# - Remove some roles for certain weeks (add desired roles to Event)
# - Manual allocation of some roles for special events
