
from multiprocessing.sharedctypes import Value
import pytest
import src.pyfarmsay.pyfarmsay as pyfarmsay
import src.pyfarmsay.animals as animals

# Tests: 1. test that input exists in function return message
#        2. test that the correct aninmal exists in function return message
#        3. test that invalid function parametes are handled correctly
class Tests: 
     def test_sanity_check(self):
          """
          Test debugging... seeing how building a test works 
          """
          expected = True
          actual = True
          assert expected == actual
     
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

     def improper_input_cowsay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for cowsay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.cowsay("")

     def improper_input_pigsay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for pigsay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.pigsay("")
     
     def improper_input_chickensay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for chickensay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.chickensay("")

     def improper_input_sheepsay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for sheepsay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.sheepsay("")
     
     def improper_input_dogsay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for dogsay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.dogsay("")

     def improper_input_penguinsay(self):
          """
          Testing if error is raised with invalid empty string as parameter
          for penguinsay function. 
          """
          with pytest.raises(TypeError) as errorInfo:
               pyfarmsay.penguinsay("")
          
