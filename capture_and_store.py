from pathlib import Path
import json

path = Path('data.json')


def get_stored_info():

    if path.exists():

        contents = path.read_text()
        info = json.loads(contents)
        return info
    else:    
        return None

def get_new_info():        
   
    info = {
           'nome': input('Qual é o seu nome?: '),
           'localização': input('Qual sua localização?: '),
           'idade': input('Qual a sua idade?')
            }

    contents = json.dumps(info)
    path.write_text(contents)
    return info

def greet_user():        

    info = get_stored_info()
    if info:
       
        verification = input(f'Are you {info['nome']}? Answer with yes or no: ')
        while verification.lower() != 'yes' and verification.lower() != 'no':
            print('Invalid answer. Respond with either yes or no')
            verification = input(f'Are you {info['nome']}? Answer with yes or no: ')

        if verification.lower() == 'no':
            info = get_new_info()
            print(f'We will remember you when you come back, {info['nome']}')
        elif verification.lower() == 'yes':    
            print(f'Welcome back, {info['nome']}')
        
    else:    
        info = get_new_info()
        print(f'Welcome back, {info['nome']}')
        
        

def show_info():        

    info = get_stored_info()
    
    print(f'Nome: {info['nome']}')
    print(f'Localização: {info['localização']}')
    print(f'Idade: {info['idade']}')


greet_user()
show_info()

 