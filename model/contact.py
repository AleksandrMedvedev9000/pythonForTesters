from sys import maxsize

class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None, home_phone=None, mobile_phone=None,
                             work_phone=None, fax=None, email=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, address2=None, phone2=None, notes=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s, %s, %s" % (self.first_name, self.last_name, self.id)

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and (self.id == other.id or self.id is None or other.id is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
