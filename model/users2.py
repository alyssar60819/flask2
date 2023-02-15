from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
import json
# Start code w/ birthday and age
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

dob = date(2006, 8, 20)
age = calculate_age(dob)
print(age)

class User:    

    def __init__(self, name, uid, password, dob, classOf):
        # variables with self prefix
        self._name = name   
        self._uid = uid
        self.set_password(password)
        self._dob = dob
        self._classOf = classOf
    
    @property
    def name(self):
        return self._name
    
    # setter function
    @name.setter
    def name(self, name):
        self._name = name
    
    # getter method
    @property
    def uid(self):
        return self._uid
    
    # setter function
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    # returns boolean
    def is_uid(self, uid):
        return self._uid == uid
    
    # date is returned as a string
    @property
    def dob(self):
        dob_string = self._dob.strftime('%m-%d-%Y')
        return dob_string
    
    # verification
    @dob.setter
    def dob(self, dob):
        self._dob = dob
        
    # age calculation
    @property
    def age(self):
        today = date.today()
        return today.year - self._dob.year - ((today.month, today.day) < (self._dob.month, self._dob.day))
    
    @property
    def classOf(self):
        return self._classOf
    
    # setter function
    @classOf.setter
    def name(self, classOf):
        self._classOf = classOf
    
    # customized dictionary
    @property
    def dictionary(self):
        dict = {
            "name" : self.name,
            "uid" : self.uid,
            "dob" : self.dob,
            "age" : self.age
        }
        return dict
    
    # setter function
    def set_password(self, password):
        """Create a hashed password."""
        self._password = generate_password_hash(password, method='sha256')

    # password checker
    def is_password(self, password):
        """Check against hashed password."""
        result = check_password_hash(self._password, password)
        return result
    
    # output
    def __str__(self):
        return json.dumps(self.dictionary)
    def __repr__(self):
        return f'User(name={self._name}, uid={self._uid}, password={self._password},dob={self._dob})'
    

if __name__ == "__main__":
    u1 = User(name='Johsua Ringler', uid='joshua', password='5678', dob=date(2011, 2, 15), classOf='2029')
    u2 = User(name='Alyssa Ringler', uid='alyssa', password='1234', dob=date(2006, 8, 20), classOf='2024')
    
    print("JSON ready string:\n", u1, "\n") 
    print("Raw Variables of object:\n", vars(u1), "\n") 
    print("Raw Attributes and Methods of object:\n", dir(u1), "\n")
    print("Representation to Re-Create the object:\n", repr(u1), "\n") 
    
    print("JSON ready string:\n", u2, "\n") 
    print("Raw Variables of object:\n", vars(u2), "\n")
    print("Raw Attributes and Methods of object:\n", dir(u2), "\n")
    print("Representation to Re-Create the object:\n", repr(u2), "\n")