class protect:
    def __init__(self, name_colums:list, values:list):
        self.dict_values: dict = self._dict_values(name_colums, values)
        self.keys_str: list = self._keys_str(self.dict_values)
    
    def _dict_values(self, name_colums:list, values:list) -> dict:
        dict_values = {}

        for i in range(len(name_colums)):
            dict_values[name_colums[i]] = values[i]

        return dict_values
    
    def _keys_str(self, dict_values: dict) -> str:
        keys_list = []

        for i in list(dict_values.keys()):
            keys_list.append(f"%({i})s")

        keys_str = ",".join(keys_list)
        
        return keys_str
