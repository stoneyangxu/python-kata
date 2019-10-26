import datetime

last_id = 0


class Note:
    """Represent a note in notebook"""

    def __init__(self, memo, tags=''):
        """initialize a note with memo and optional space-separated tags
        Automatically set the note's creation date and a unique id"""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        self.id = ++last_id

    def match(self, filter_str):
        """Determine if this note matchs the filter"""
        return filter_str in self.memo or filter_str in self.tags


class NoteBook:
    """Represent a collection of notes"""

    def __init__(self):
        """initialize a notebook with an empty list"""
        self.notes = []

    def new_note(self, memo, tags=''):
        """create a new note"""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """Find a note with a given id and change its memo"""
        note = self._find_node(note_id)
        if note:
            note.memo = memo

    def modify_tags(self, note_id, tags):
        """Find a note with a given id and change its tags"""
        note = self._find_node(note_id)
        if note:
            note.tags = tags

    def search(self, filter_str):
        """Find all notes that match the given filter"""
        return [note for note in self.notes if note.match(filter_str)]

    def _find_node(self, node_id):
        """Find a note with a given id"""
        for note in self.notes:
            if str(note.id) == str(node_id):
                return note
        return None
