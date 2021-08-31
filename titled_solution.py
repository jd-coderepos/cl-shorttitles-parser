import re
from utils import *
from core_func import *

def computer_science(line):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	dataset = []
	
	i = line.find(':')
	part_0 = line[0:i]

	part_1 = line[i+1:].lstrip().rstrip()
	part_1_lower = part_1.lower()
	
	connector_indexes = get_list_of_connector_indexes(part_1.lower(), connectors_rx)
	connector_indexes.sort()
	
	if len(connector_indexes) == 0:	
		solution.append(part_0)	
		if is_dataset(part_1_lower):
			dataset.append(part_1)
		elif ending(part_1_lower, '(task)'):
			research_problem.append(part_1)
		elif not ending(part_1_lower, '(results)') and not begins_phrase('(toward)', part_1_lower):
			solution.append(part_1)
	elif len(connector_indexes) == 1:
		solution.append(part_0)	
		sol, research_problem, resource, language, tool, method, dataset = one_connector_heuristics_titled_solution(part_1, part_1_lower)
		
		if len(sol) > 0:
			solution.extend(sol)
				
	return solution, research_problem, resource, language, tool, method, dataset
				
		