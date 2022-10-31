
import pyfarmsay
import pytest
import animals

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
          
