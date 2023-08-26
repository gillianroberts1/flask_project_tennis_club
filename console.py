import pdb
from models.member import Member
from models.court import Court


import repositories.member_repository as member_repository
import repositories.court_repository as court_repository



member_repository.delete_all()
court_repository.delete_all()

member1 = Member("Gillian Roberts", True)
member_repository.save(member1)

member2 = Member("Louise Reid", False)
member_repository.save(member2)

member3 = Member("Carmen Roberts", True)
member_repository.save(member3)


court1 = Court(1, "Lawn")
court_repository.save(court1)

court2 = Court(2, "Clay")
court_repository.save(court2)


# courts = court_repository.court_for_member(member1)

# members = member_repository.member_for_court(court1)

# pdb.set_trace()
