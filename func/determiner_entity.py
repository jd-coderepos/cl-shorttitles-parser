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
	
	line = line.split(':')[0].strip()
	line_lower = line.lower()
	
	connector_indexes = get_list_of_connector_indexes(line_lower, connectors_rx)
	connector_indexes.sort()

	if len(connector_indexes) == 0:
		if is_research_problem(line):
			research_problem.append(line)
		elif len(line.split(' ')) < 11:
			solution.append(line)
		else:
			token = has_ing_connector(line)
			if '' != token:
				i = line.find(token)
				part_0 = line[0:i].strip()
				part_0 = remove_and_ending(part_0).strip()				
				part_1 = line[i+len(token)+1:].lstrip().strip()
				
				if is_research_problem(part_0) or is_method(part_0) or is_tool(part_0.lower()):
					solution.append(part_0)
			
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(part_1)
				
	elif len(connector_indexes) == 1:
		sol, research_problem, resource, language, tool, method, dataset = one_connector_heuristics_titled_solution(line, line_lower)
		
		# if 'A MAP-Based Layered Detection Algorithm and Outage Analysis over MIMO Channels' in line:
			# print(line)
			# #print(subparts_1)
			# print(str(research_problem))
			# print(str(resource))			
			# print(str(language))
			# print(str(tool))
			# print(str(method))		
			# print(str(dataset)+'\n')
		
		if len(sol) > 0:
			solution.extend(sol)
						
	return solution, research_problem, resource, language, tool, method, dataset