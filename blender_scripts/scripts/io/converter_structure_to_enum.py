# <pep8-80 compliant>
import os
import sys
import json
current_directory = os.getcwd()
if current_directory not in sys.path:
        sys.path.append(current_directory)
from enum_comandos import Comandos

class ConverterStructureToEnum:
    estrutura = [[{"name":30}]]
    
    #defining constructor  
    def __init__(self, instructions):
         self.preencher_estrutura(instructions)
          
    #defining class methods  
    def preencher_estrutura(self, instructions):
         comando_list_counter = 0
         for instruction in instructions:
            print("comando_list_counter=", comando_list_counter)
            print(instruction)
            print('Comandos[list(instruction.keys())[0]].value=')
            print(Comandos[list(instruction.keys())[0]].value)
            self.estrutura[comando_list_counter][0] = Comandos[list(instruction.keys())[0]].value
            print('self.estrutura[comando_list_counter][0]=')
            print(self.estrutura[comando_list_counter][0])
            print('instruction.get(list(instruction.keys())[0])=')
            print(instruction.get(list(instruction.keys())[0]))
            print(type(instruction.get(list(instruction.keys())[0])))
            self.estrutura[comando_list_counter].append(instruction.get(list(instruction.keys())[0]))
            print('self.estrutura[comando_list_counter][1]=')
            print(self.estrutura[comando_list_counter][1])
            comando_list_counter = int(comando_list_counter)
            comando_list_counter+=1
            

    def get_estrutura():
         return self.estrutura

if __name__ == "__main__":
    # register()
    t_json_structure = {}
    with open('./input_planta_structure.json') as json_data_file:
            t_json_structure = json.load(json_data_file)
    input = ConverterStructureToEnum(t_json_structure['comandos'])
    print(input.get_estrutura())
