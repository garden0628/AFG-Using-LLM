from AFG_system.src.dataset import Dataset
from AFG_system.src.tester import Tester
from AFG_system.src.locator import Locator
from AFG_system.src.validator import Validator
from AFG_system.info import api_key, generate_apr_messages, generate_afg_messages
import openai


Dataset.init_glob_vars()

def run_AFG_system():
    patch_program, feedback = None, None
    
    description = Dataset.description
    wrong_program = Dataset.wrong_prog
    test_cases = Dataset.testcases
        
    tester = Tester(test_cases)
    locator = Locator(tester)
    validator = Validator(tester)

    openai.api_key = api_key
    temperature_value = [0, 0.9, 0.9, 0.9, 0.9, 0.9]
    temperature_idx = 0

    passed = False
    failed_tcs, faults = locator.run(wrong_program)
    
    while not passed and temperature_idx < len(temperature_value):
        apr_messages = generate_apr_messages(description, wrong_program, failed_tcs, faults)
        completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=apr_messages,
                    temperature=temperature_value[temperature_idx]
        )
        response = completion.choices[0].message.content
        passed, patch_program = validator.run(response)
        
        '''Current State : validator doesn't work now
        if not passed:
            temperature_idx += 1
            patch_program = None
        else:
            afg_messages = generate_afg_messages(wrong_program, patch_program)
            completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=afg_messages,
                    temperature=0
            )
            response = completion.choices[0].message.content
            feedback = str(response)
        '''
        
        # Do not valid check and go to feedback generation system
        afg_messages = generate_afg_messages(wrong_program, patch_program)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=afg_messages,
            temperature=0
        )
        response = completion.choices[0].message.content
        feedback = str(response)
            
        return patch_program, feedback