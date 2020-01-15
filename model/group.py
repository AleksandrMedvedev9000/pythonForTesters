from sys import maxsize

class Group:

    def __init__(self, table_name=None, table_header=None, table_footer=None, table_id=None):
        self.table_name = table_name
        self.table_header = table_header
        self.table_footer = table_footer
        self.table_id = table_id

    def __repr__(self):
        return "%s: %s" % (self.table_id, self.table_name)

    def __eq__(self, other):
        return (self.table_id is None or other.table_id is None or self.table_id == other.table_id) and self.table_name == other.table_name

    def id_or_max(self):
        if self.table_id:
            return int(self.table_id)
        else:
            return maxsize
