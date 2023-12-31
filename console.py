import pdb
from models.member import Member
from models.court import Court
from models.booking import Booking
from datetime import datetime, time, date


import repositories.member_repository as member_repository
import repositories.court_repository as court_repository
import repositories.booking_repository as booking_repository


member_repository.delete_all()
court_repository.delete_all()
booking_repository.delete_all()

member1 = Member("Gillian Roberts", "34 Kilnside Road, Glasgow", "G45 8JN", "07883552756", "gilrob@outlook.com", "14/8/78", True, 1, 0)
member_repository.save(member1)

member2 = Member("Louise Reid", "45 The Best Street, Glasgow", "G34 1LK", "07886443554", "loureid@gg.com", "10/10/81", False, 1, 4)
member_repository.save(member2)

member3 = Member("Carmen Roberts", "34 Kilnside Road, Glasgow", "G45 8JN", "07883552226", "carmrob@outlook.com", "10/9/17", True, 3, 1)
member_repository.save(member3)


court1 = Court(1, "Grass")
court_repository.save(court1)

court2 = Court(2, "Clay")
court_repository.save(court2)

# start_time1 = datetime.combine(date(2023, 8, 28), time(11, 0, 0))  
# end_time1 = datetime.combine(date(2023, 8, 28), time(12, 0, 0))    
# slot1 = Slot(court1, start_time1, end_time1)
# slot_repository.save(slot1)

# start_time2 = datetime.combine(date(2023, 8, 28), time(12, 0, 0))  
# end_time2 = datetime.combine(date(2023, 8, 28), time(13, 0, 0))    
# slot2 = Slot(court1, start_time2, end_time2)
# slot_repository.save(slot2)





booking1 = Booking(member1, court1)
booking_repository.save(booking1)

booking2 = Booking(member2, court2)
booking_repository.save(booking2)




courts = court_repository.court_for_member(member1)
for court in courts:
    print (court.__dict__)




members = member_repository.members_for_court(court1)

pdb.set_trace()
