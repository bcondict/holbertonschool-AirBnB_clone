# 0x00. AirBnB clone - The console

## Details

For this project, students are expected to look at these concepts:

* [Python packages](https://intranet.hbtn.io/concepts/66) 

* [AirBnB clone](https://intranet.hbtn.io/concepts/74) 

 <br>

<h1 align="center"><img src="https://imgur.com/OilEsXV.png" width='400'></h1>

<br>

## Background Context

### Welcome to the AirBnB clone project!

Before starting, please read the  [AirBnB](https://intranet.hbtn.io/rltoken/bw70gxOl1RHBKFAWAR2Y3w) 
  concept page.

#### First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the  AirBnB clone .This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… 
Each task is linked and will help you to:

* put in place a parent class (called  ` BaseModel ` ) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB ( ` User ` ,  ` State ` ,  ` City ` ,  ` Place ` …) that inherit from  ` BaseModel ` 
* create the first abstracted storage engine of the project: File storage. 
* create all unittests to validate all our classes and storage engine

### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Resources

Read or watch :

* [Python abstract classes](https://intranet.hbtn.io/rltoken/5Dv7z90qa94hYqtPRCe_wA)
* [cmd module](https://intranet.hbtn.io/rltoken/7dj8WbEE01SwPY2Qxy_Ixg)
* Packages concept page
* [uuid module](https://intranet.hbtn.io/rltoken/xJhjt-mMAchNu5WOb2X6DQ)
* [datetime](https://intranet.hbtn.io/rltoken/aEuCrtCn7p5xaYbNRM8ccQ)
* [unittest module](https://intranet.hbtn.io/rltoken/XfOae8zIhTiKYFMTF98qLg)
* [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg)
* [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A)

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/YeIzIx-J9Sd9WgiVerOpdQ) 
 ,  without the help of Google :

### General

* How to create a Python package
* How to create a command interpreter in Python using the  ` cmd `  module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage  ` datetime ` 
* What is an  ` UUID ` 
* What is  ` *args `  and how to use it
* What is  ` **kwargs `  and how to use it
* How to handle named arguments in a function

## Requirements

### Python Scripts

* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using  ` wc ` 
* All your modules should have a documentation ( ` python3 -c 'print(__import__("my_module").__doc__)' ` )
* All your classes should have a documentation ( ` python3 -c 'print(__import__("my_module").MyClass.__doc__)' ` )
* All your functions (inside and outside a class) should have a documentation ( ` python3 -c 'print(__import__("my_module").my_function.__doc__)' `  and  ` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ` )
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files should end with a new line
* All your test files should be inside a folder  ` tests ` 
* You have to use the [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g) 

* All your test files should be python files (extension:  ` .py ` )
* All your test files and folders should start by  ` test_ ` 
* Your file organization in the tests folder should be the same as your project
* e.g., For  ` models/base_model.py ` , unit tests must be in:  ` tests/test_models/test_base_model.py ` 
* e.g., For  ` models/user.py ` , unit tests must be in:  ` tests/test_models/test_user.py ` 
* All your tests should be executed by using this command:  ` python3 -m unittest discover tests ` 
* You can also test file by file by using this command:  ` python3 -m unittest tests/test_models/test_base_model.py ` 
* All your modules should have a documentation ( ` python3 -c 'print(__import__("my_module").__doc__)' ` )
* All your classes should have a documentation ( ` python3 -c 'print(__import__("my_module").MyClass.__doc__)' ` )
* All your functions (inside and outside a class) should have a documentation ( ` python3 -c 'print(__import__("my_module").my_function.__doc__)' `  and  ` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ` )
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### GitHub

There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.

## More Info

### Execution

Your shell should work like this in interactive mode:
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode:   ` $ echo "python3 -m unittest discover tests" | bash `

### 3. BaseModel 
* Public instance attributes: *  ` id ` : string - assign with an  ` uuid `  when an instance is created:* you can use  ` uuid.uuid4() `  to generate unique  ` id `  but don’t forget to convert to a string
* the goal is to have unique  ` id `  for each  ` BaseModel ` 

*  ` created_at ` : datetime - assign with the current datetime when an instance is created
*  ` updated_at ` : datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object

*  ` __str__ ` : should print:  ` [<class name>] (<self.id>) <self.__dict__> ` 
* Public instance methods:*  ` save(self) ` : updates the public instance attribute  ` updated_at `  with the current datetime
*  ` to_dict(self) ` : returns a dictionary containing all keys/values of  ` __dict__ `  of the instance:* by using  ` self.__dict__ ` , only instance attributes set will be returned
* a key  ` __class__ `  must be added to this dictionary with the class name of the object
*  ` created_at `  and  ` updated_at `  must be converted to string object in ISO format:* format:  ` %Y-%m-%dT%H:%M:%S.%f `  (ex:  ` 2017-06-14T22:31:03.285259 ` ) 
* you can use  ` isoformat() `  of  ` datetime `  object

* This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our  ` BaseModel ` 


```bash
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - My First Model
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427
guillaume@ubuntu:~/AirBnB$ 
```
 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* File:  ` models/base_model.py, models/__init__.py, tests/ ` 
 Self-paced manual review  Panel footer - Controls 

### 4. Create BaseModel from dictionary
 ` <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
 ` Update   ` models/base_model.py `  :
*  ` __init__(self, *args, **kwargs) ` : * you will use  ` *args, **kwargs `  arguments for the constructor of a  ` BaseModel ` . (more information inside the AirBnB clone concept page)
*  ` *args `  won’t be used
* if  ` kwargs `  is not empty:* each key of this dictionary is an attribute name (Note ` __class__ `  from  ` kwargs `  is the only one that should not be added as an attribute. See the example output, below)
* each value of this dictionary is the value of this attribute name
* Warning:  ` created_at `  and  ` updated_at `  are strings in this dictionary, but inside your  ` BaseModel `  instance is working with  ` datetime `  object. You have to convert these strings into  ` datetime `  object. Tip: you know the string format of these datetime
* otherwise:* create  ` id `  and  ` created_at `  as you did previously (new instance)
```bash
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))
print("--")
print(my_model is my_new_model)
guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
False
guillaume@ubuntu:~/AirBnB$ 
```
 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* File:  ` models/base_model.py, tests/ ` 
 Self-paced manual review  Panel footer - Controls

### 5. Store first object
 ` It’s great but it’s still not persistent: every time you launch the program, you don’t restore all objects created before… The first way you will see here is to save these objects to a file.
Writing the dictionary representation to a file won’t be relevant:
* Python doesn’t know how to convert a string to a dictionary (easily)
* It’s not human readable
* Using this file with another program in Python or other language will be hard.
So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.
Now the flow of serialization-deserialization will be:
```bash
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```
Magic right?
Terms:
* simple Python data structure: Dictionaries, arrays, number and string. ex:  ` { '12': { 'numbers': [1, 2, 3], 'name': "John" } } ` 
* JSON string representation: String representing a simple data structure in JSON format. ex:  ` '{ "12": { "numbers": [1, 2, 3], "name": "John" } }' ` 
Write a class   ` FileStorage `   that serializes instances to a JSON file and deserializes JSON file to instances:
*  ` models/engine/file_storage.py ` 
* Private class attributes:*  ` __file_path ` : string - path to the JSON file (ex:  ` file.json ` )
*  ` __objects ` : dictionary - empty but will store all objects by  ` <class name>.id `  (ex: to store a  ` BaseModel `  object with  ` id=12121212 ` , the key will be  ` BaseModel.12121212 ` )
* Public instance methods:*  ` all(self) ` : returns the dictionary  ` __objects ` 
*  ` new(self, obj) ` : sets in  ` __objects `  the  ` obj `  with key  ` <obj class name>.id ` 
*  ` save(self) ` : serializes  ` __objects `  to the JSON file (path:  ` __file_path ` )
*  ` reload(self) ` : deserializes the JSON file to  ` __objects `  (only if the JSON file ( ` __file_path ` ) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
Update   ` models/__init__.py `  : to create a unique   ` FileStorage `   instance for your application
* import  ` file_storage.py ` 
* create the variable  ` storage ` , an instance of  ` FileStorage ` 
* call  ` reload() `  method on this variable
Update   ` models/base_model.py `  : to link your   ` BaseModel `   to   ` FileStorage `   by using the variable   ` storage ` 
* import the variable  ` storage ` 
* in the method  ` save(self) ` :* call  ` save(self) `  method of  ` storage ` 
*  ` __init__(self, *args, **kwargs) ` : * if it’s a new instance (not from a dictionary representation), add a call to the method  ` new(self) `  on  ` storage ` 
```bash
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$ 
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$ 
```
 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* File: ```bash
models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/
```
 Self-paced manual review  Panel footer - Controls
