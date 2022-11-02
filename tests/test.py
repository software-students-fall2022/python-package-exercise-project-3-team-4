
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
     
     def test_animal_exists_cowsay(self): 
          """
          Testing if correct animal exists in cowsay function output. 
          """
          text = "some string"
          result = pyfarmsay.cowsay(text)
          exists = False
          if all(result.find(part) > -1 for part in animals.COW):
               exists = True

          assert exists == True

     def test_animal_exists_pigsay(self): 
          """
          Testing if correct animal exists in cowsay function output. 
          """
          text = "some string"
          result = pyfarmsay.pigsay(text)
          exists = False
          if all(result.find(part) > -1 for part in animals.PIG):
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
          
