class Dictionary:
    def __init__(self, dictionary_data):
        self._entries = dictionary_data

    def check_new_entry(self, entry):
        if self._entries.has_key(entry.steno):
            return False

    def entries(self):
        return self._entries
    
    def entries_update(self, new_entries):
        self._entries.update(new_entries)
        # for key in self._entries:
        #     if 
        return self._entries

