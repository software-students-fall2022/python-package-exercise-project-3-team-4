
from multiprocessing.sharedctypes import Value
import pytest
import src.pyfarmsay.util as util
import src.pyfarmsay.pyfarmsay as pyfarmsay
import src.pyfarmsay.animals as animals
import src.pyfarmsay.__main__ as main
import sys
# Tests: 1. test that input exists in function return message
#        2. test that the correct aninmal exists in function return message
#        3. test that invalid function parameters are handled correctly
#        4. test that default noises are correct (when parameters are EMPTY string)
class Tests: 
     def test_sanity_check(self):
          """
          Test debugging... seeing how building a test works 
          """
          expected = True
          actual = True
          assert expected == actual

     def test_no_arg_genquotebubble(self):
          """
          Testing if TypeError is raised when helper util.genquotebubble()
          has no arguments. 
          """
          with pytest.raises(TypeError) as err:
               util.genquotebubble()

     def test_line_exists_genquotebubble(self):
          """
          Testing if all characters in non-empty genquotebubble
          argument are present in function output.
          """
          line = list("some string")
          res = util.genquotebubble(line)
          res = "\n".join(res)
          valid = True
          for word in line:
               valid = valid and res.find(word) != -1
          assert valid
     
     def test_empty_line_genquotebubble(self):
          """
          Testing if genquotebubble raises a value error
          when passed an empty list as input 
          """
          with pytest.raises(ValueError) as err:
               util.genquotebubble([])
     
     def test_no_arg_animalsay(self):
          """
          Testing if TypeError is raised when helper util.animalsay()
          has no valid arguments. 
          """
          with pytest.raises(ValueError) as err:
               util.animalsay("")

     def test_default_animalsay(self):
          """
          Testing if default animal sound is returned
          when helper util.animalsay()
          has an valid but empty argument. 
          """
          result = util.animalsay([])
          assert result.find(animals.COW.sound) != -1

     def test_input_animalsay(self):
          """
          Testing if default animal sound is returned
          when helper util.animalsay()
          has an valid and non-empty argument. 
          """
          result = util.animalsay(["hello"])
          assert result.find("hello") != -1
     
     def test_animal_call_animal(self):
          """
          Testing if all expected animals are called using 
          call_animal(ANIMAL, MESSAGE).
          """
          message = "message"
          farm = ["cow", "pig", "chicken", "dog", "penguin", "sheep", 
          "farm"]
          for animal in farm: 
               result = main.call_animal(animal, message)
               if result == "animal not in farm :(!":
                    assert False
          assert True
     
     def test_default_cowsay(self): 
          """
          Testing if default input exists in cowsay function output. 
          """
          expected = "moo"
          actual = pyfarmsay.cowsay("")
          assert actual.find(expected) != -1

     def test_default_pigsay(self): 
          """
          Testing if default input exists in cowsay function output. 
          """
          expected = "oink"
          actual = pyfarmsay.pigsay("")
          assert actual.find(expected) != -1

     def test_default_chickensay(self): 
          """
          Testing if default input exists in chickensay function output. 
          """
          expected = "cluck"
          actual = pyfarmsay.chickensay("")
          assert actual.find(expected) != -1

     def test_default_sheepsay(self): 
          """
          Testing if default input exists in sheepsay function output. 
          """
          expected = "baa"
          actual = pyfarmsay.sheepsay("")
          assert actual.find(expected) != -1

     def test_default_penguinsay(self): 
          """
          Testing if default input exists in penguinsay function output. 
          """
          expected = "noot"
          actual = pyfarmsay.penguinsay("")
          assert actual.find(expected) != -1

     def test_default_dogsay(self): 
          """
          Testing if default input exists in dogsay function output. 
          """
          expected = "woof"
          actual = pyfarmsay.dogsay("")
          assert actual.find(expected) != -1

     def test_default_farmsay(self):
          """
          Testing if default input exists in famray function output.
          """
          expected = ["woof", "baa", "noot", "oink", "moo", "cluck"]
          actual = pyfarmsay.farmsay("")

          valid = True
          for i in range(len(expected)):
               valid = valid and actual.find(expected[i]) != -1

          assert valid
         
     def test_no_input_cowsay(self):
          """
          testing if default animal sound is outputted when pyfarmsay functions
          are called with no arguments.
          """
          expected = "moo"
          actual = pyfarmsay.cowsay()
          assert actual.find(expected) != -1

     def test_no_input_pigsay(self):
          """
          testing if default animal sound is outputted when pyfarmsay functions
          are called with no arguments.
          """
          expected = "oink"
          actual = pyfarmsay.pigsay()
          assert actual.find(expected) != -1
          
     def test_no_input_chickensay(self):
          """
          testing if default animal sound is outputted when pyfarmsay functions
          are called with no arguments.
          """
          expected = "cluck"
          actual = pyfarmsay.chickensay()
          assert actual.find(expected) != -1

          
     def test_no_input_dogsay(self):
          """
          testing if default animal sound is outputted when pyfarmsay functions
          are called with no arguments.
          """
          expected = "woof"
          actual = pyfarmsay.dogsay()
          assert actual.find(expected) != -1

     def test_no_input_penguinsay(self):
          """
          testing if default animal sound is outputted when pyfarmsay functions
          are called with no arguments.
          """
          expected = "noot"
          actual = pyfarmsay.penguinsay()
          assert actual.find(expected) != -1

     def test_no_input_sheepsay(self):
          """
          testing if default animal sound is outputted when pyfarmsay functions
          are called with no arguments.
          """
          expected = "baa"
          actual = pyfarmsay.sheepsay()
          assert actual.find(expected) != -1

     def test_no_input_farmsay(self):
          """
          Testing if default input exists in famray function output.
          """
          expected = ["woof", "baa", "noot", "oink", "moo", "cluck"]
          actual = pyfarmsay.farmsay()

          valid = True
          for i in range(len(expected)):
               valid = valid and actual.find(expected[i]) != -1

          assert valid

     def test_input_recieved_cowsay(self):
          """
          Testing if input exists in cowsay function output. 
          """
          text = "some string"
          actual = pyfarmsay.cowsay(text)
          assert actual.find(text) != -1

     def test_input_recieved_pigsay(self):
          """
          Testing if input exists in pigsay function output. 
          """
          text = "some string"
          actual = pyfarmsay.pigsay(text)
          assert actual.find(text) != -1
     
     def test_input_recieved_chickensay(self):
          """
          Testing if input exists in chickensay function output
          """
          text = "some string"
          actual = pyfarmsay.chickensay(text)
          assert actual.find(text) != 1
     
     def test_input_recieved_sheepsay(self):
          """
          Testing if input exists in sheepsay function output
          """
          text = "some string"
          actual = pyfarmsay.sheepsay(text)
          assert actual.find(text) != 1
     
     def test_input_recieved_penguinsay(self):
          """
          Testing if input exists in penguinsay function output
          """
          text = "some string"
          actual = pyfarmsay.penguinsay(text)
          assert actual.find(text) != 1
     
     def test_input_recieved_dogsay(self):
          """
          Testing if input exists in dogsay function output
          """
          text = "some string"
          actual = pyfarmsay.dogsay(text)
          assert actual.find(text) != 1

     def test_input_recieved_farmsay(self):
          """
          Testing if input exists in farmsay function output
          """
          text = "some string"
          actual = pyfarmsay.farmsay(text)
          assert actual.find(text) != 1

     def test_animal_exists_cowsay(self): 
          """
          Testing if correct animal exists in cowsay function output. 
          """
          text = "some string"
          result = pyfarmsay.cowsay(text)
          exists = False
          if all(result.find(part) > -1 for part in animals.COW.body):
               exists = True

          assert exists == True

     def test_animal_exists_pigsay(self): 
          """
          Testing if correct animal exists in cowsay function output. 
          """
          text = "some string"
          result = pyfarmsay.pigsay(text)
          exists = False
          if all(result.find(part) > -1 for part in animals.PIG.body):
               exists = True

          assert exists == True
     
     def test_animal_exists_chickensay(self):
          """
          Testing if correct animal exists in chickensay function output. 
          """
          text = "some string"
          result = pyfarmsay.chickensay(text)
          exists = False
          if all(result.find(part) > -1 for part in animals.CHICKEN.body):
               exists = True

          assert exists == True
     
     def test_animal_exists_sheepsay(self):
          """
          Testing if correct animal exists in sheepsay function output. 
          """
          text = "some string"
          result = pyfarmsay.sheepsay(text)
          exists = False
          if all(result.find(part) > -1 for part in animals.SHEEP.body):
               exists = True

          assert exists == True
     
     def test_animal_exists_dogsay(self):
          """
          Testing if correct animal exists in dogsay function output. 
          """
          text = "some string"
          result = pyfarmsay.dogsay(text)
          exists = False
          if all(result.find(part) > -1 for part in animals.DOG.body):
               exists = True

          assert exists == True

     def test_animal_exists_penguinsay(self):
          """
          Testing if correct animal exists in penguinsay function output. 
          """
          text = "some string"
          result = pyfarmsay.penguinsay(text)
          exists = False
          if all(result.find(part) > -1 for part in animals.PENGUIN.body):
               exists = True

          assert exists == True

     def test_animals_exist_farmsay(self):
          """
           Testing if all animals exist in farmsay function output.
          """
          text = "some string"
          result = pyfarmsay.farmsay(text)
          exists = False
          if all(result.find(part) > -1 for part in animals.PENGUIN.body) and \
          all(result.find(part) > -1 for part in animals.COW.body) and \
          all(result.find(part) > -1 for part in animals.DOG.body) and \
          all(result.find(part) > -1 for part in animals.SHEEP.body) and \
          all(result.find(part) > -1 for part in animals.CHICKEN.body) and \
          all(result.find(part) > -1 for part in animals.PIG.body):
               exists = True

          assert exists

     def test_improper_input_cli(self):
          """
          Testing if error is flagged when an unknown animal is inputted
          """
          animal = "unknown"
          message = "some message"
          result = main.call_animal(animal, message)
          assert result == "animal not in farm :(!"

     def test_proper_cow_detection_cli(self):
          """
          Testing if cow is displayed from the command line if the argument "cow" is displayed
          """
          animal = "cow"
          message = "some message"
          result = main.call_animal(animal, message)
          expected = pyfarmsay.cowsay(message)

          assert result == expected

     def test_proper_dog_detection_cli(self):
          """
          Testing if dog is displayed from the command line if the argument "dog" is displayed
          """
          animal = "dog"
          message = "some message"
          result = main.call_animal(animal,message)
          expected = pyfarmsay.dogsay(message)

          assert result == expected

     def test_proper_pig_detection_cli(self):
          """
          Testing if pig is displayed from the command line if the argument "pig" is inputted
          """
          animal = "pig"
          message = "some message"
          result = main.call_animal(animal, message)
          expected = pyfarmsay.pigsay(message)

          assert result == expected
   
     def test_proper_penguin_detection_cli(self):
          """
          Testing if penguin is displayed from the command line if the argument "penguin" is inputted
          """
          animal = "penguin"
          message = "some message"
          result = main.call_animal(animal, message)
          expected = pyfarmsay.penguinsay(message)

          assert result == expected

     def test_proper_chicken_detection_cli(self):
          """
          Testing if chicken is displayed from the command line if the argument "chicken" is inputted
          """
          animal = "chicken"
          message = "some message"
          result = main.call_animal(animal, message)
          expected = pyfarmsay.chickensay(message)

          assert result == expected

     def test_proper_sheep_detection_cli(self):
          """
          Testing if sheep is displayed from the command line if the argument "sheep" is inputte
          """
          animal = "sheep"
          message = "some message"
          result = main.call_animal(animal, message)
          expected = pyfarmsay.sheepsay(message)

          assert result == expected


     def test_proper_farm_detection_cli(self):
          """
          Testing if farm animals are displayed from the command line if the argument "farm" is inputted
          """
          animal = "farm"
          message = "some message"
          result = main.call_animal(animal, message)
          expected = pyfarmsay.farmsay(message)

          assert result == expected

     def test_improper_input_main(self):
          """
          Testing if the module will output an error message when the user
          inputs no command line arguments.
          """
          sys.argv = []
          res = main.main()
          assert res == "You have to specify the pyanimal in the pyfarm that you would like to see."

     def test_capitalized_arg_input_cow_main(self):
          """
          Testing if program will still recognize animal arguments capitalized
          as valid input
          """
          sys.argv = ["pyfarmsay","COW"]
          res = main.main()
          expected = pyfarmsay.cowsay("")
          assert res == expected

     def test_capitalized_arg_input_pig_main(self):
          """
          Testing if program will still recognize animal arguments capitalized
          as valid input
          """
          sys.argv = ["pyfarmsay","PIG"]
          res = main.main()
          expected = pyfarmsay.pigsay("")
          assert res == expected

     def test_capitalized_arg_input_chicken_main(self):
          """
          Testing if program will still recognize animal arguments capitalized
          as valid input
          """
          sys.argv = ["pyfarmsay","CHICKEN"]
          res = main.main()
          expected = pyfarmsay.chickensay("")
          assert res == expected

     def test_capitalized_arg_input_dog_main(self):
          """
          Testing if program will still recognize animal arguments capitalized
          as valid input
          """
          sys.argv = ["pyfarmsay","DOG"]
          res = main.main()
          expected = pyfarmsay.dogsay("")
          assert res == expected

     def test_capitalized_arg_input_penguin_main(self):
          """
          Testing if program will still recognize animal arguments capitalized
          as valid input
          """
          sys.argv = ["pyfarmsay","PENGUIN"]
          res = main.main()
          expected = pyfarmsay.penguinsay("")
          assert res == expected

     def test_capitalized_arg_input_sheep_main(self):
          """
          Testing if program will still recognize animal arguments capitalized
          as valid input
          """
          sys.argv = ["pyfarmsay","SHEEP"]
          res = main.main()
          expected = pyfarmsay.sheepsay("")
          assert res == expected

     def test_capitalized_arg_input_farm_main(self):
          """
          Testing if program will still recognize animal arguments capitalized
          as valid input
          """
          sys.argv = ["pyfarmsay", "FARM"]
          res = main.main()
          expected = pyfarmsay.farmsay("")
          assert res == expected
