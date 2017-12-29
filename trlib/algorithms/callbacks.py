import json
from trlib.utilities.evaluation import evaluate_policy

def save_json_callback(file_name):
    """
    Generates a callback for saving results in JSON format
    
    Parameters
    ----------
    file_name: the file where to save results
    
    Returns
    -------
    A callback for an algorithm to save results
    """
    
    def fun(algorithm):
        with open(file_name,"w") as file:
            json.dump(algorithm._result.__dict__,file)
            
    return fun

def eval_policy_callback(field_name, criterion = 'discounted', n_episodes = 1, initial_states = None, n_threads = 1):
    """
    Generates a callback for evaluating a policy.
    
    Parameters
    ----------
    field_name: name of the field in the algorithm's Result object where to store the evaluation
    others: see evaluation.py
    
    Returns
    -------
    A callback for an algorithm to evaluate performance
    """
    
    def fun(algorithm):
        
        perf = evaluate_policy(algorithm._mdp, algorithm._policy, criterion = criterion, n_episodes = n_episodes, initial_states = initial_states, n_threads = n_threads)
        algorithm._result.steps[algorithm._step][field_name] = perf
    
    return fun