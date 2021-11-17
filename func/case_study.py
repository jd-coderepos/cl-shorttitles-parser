import re
import func.titled_solution
from utils import *
from core_func import *

#... : a case study
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
	
	connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
	connector_indexes.sort()

	if len(connector_indexes) == 0:	
		language, dataset, tool, method, resource = language_or_dataset_or_tool_or_method_or_resource(line)
	elif len(connector_indexes) == 1:
		solution, research_problem, resource, language, tool, method, dataset = one_connector_heuristics_titled_solution(line, line.lower())
		solution, research_problem, resource, language, tool, method, dataset = one_connector_heuristics_postprocess(solution, research_problem, resource, language, tool, method, dataset)
						
	return solution, research_problem, resource, language, tool, method, dataset


	