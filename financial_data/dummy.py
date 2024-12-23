class Dummy():
    @property
    def get_data(self)->list:
        return [1,2,3]
    
if __name__ == "__main__":
    d = Dummy()
    print(d.get_data)