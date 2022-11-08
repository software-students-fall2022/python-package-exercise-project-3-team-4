
from multiprocessing.sharedctypes import Value
import pytest
import src.pyfarmsay.pyfarmsay as pyfarmsay
import src.pyfarmsay.animals as animals
import src.pyfarmsay.__main__ as main
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

     def test_improper_input_cowsay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for cowsay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.cowsay("")

     def test_improper_input_pigsay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for pigsay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.pigsay("")
     
     def test_improper_input_chickensay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for chickensay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.chickensay("")

     def test_improper_input_sheepsay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for sheepsay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.sheepsay("")
     
     def test_improper_input_dogsay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for dogsay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.dogsay("")

     def test_improper_input_penguinsay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for penguinsay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.penguinsay("")


     def test_improper_input_cli(self):
          """
          Testing if error is flagged when an unknown animal is inputted
          """
          animal = "unknown"
          message = "some message"
          result = main.main(animal, message)
          assert result == "animal not in farm :(!"

     def test_proper_cow_detection_cli(self):
          """
          Testing if cow is displayed from the command line if the argument "cow" is displayed
          """
          animal = "cow"
          message = "some message"
          result = main.main(animal, message)
          expected = pyfarmsay.cowsay(message)

          assert result == expected

     def test_proper_dog_detection_cli(self):
          """
          Testing if cow is displayed from the command line if the argument "cow" is displayed
          """
          animal = "dog"
          message = "some message"
          result = main.main(animal,message)
          expected = pyfarmsay.dogsay(message)

          assert result == expected

     def test_proper_pig_detection_cli(self):
          """
          Testing if cow is displayed from the command line if the argument "cow" is displayed
          """
          animal = "pig"
          message = "some message"
          result = main.main(animal, message)
          expected = pyfarmsay.pigsay(message)

          assert result == expected
   
     def test_proper_penguin_detection_cli(self):
          """
          Testing if cow is displayed from the command line if the argument "cow" is displayed
          """
          animal = "penguin"
          message = "some message"
          result = main.main(animal, message)
          expected = pyfarmsay.penguinsay(message)

          assert result == expected

     def test_proper_chicken_detection_cli(self):
          """
          Testing if cow is displayed from the command line if the argument "cow" is displayed
          """
          animal = "chicken"
          message = "some message"
          result = main.main(animal, message)
          expected = pyfarmsay.chickensay(message)

          assert result == expected

     def test_proper_sheep_detection_cli(self):
          """
          Testing if cow is displayed from the command line if the argument "cow" is displayed
          """
          animal = "sheep"
          message = "some message"
          result = main.main(animal, message)
          expected = pyfarmsay.sheepsay(message)

          assert result == expected


          
