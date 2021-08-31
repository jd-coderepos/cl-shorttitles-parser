import re
from utils import *
from core_func import *

def computer_science(part_0, part_1):
	solution = []
	research_problem = []
	resource = []
	language = []
	tool = []
	method = []
	dataset = []
	
	if '' != part_0:
		connector_indexes = get_list_of_connector_indexes(part_0.lower(), connectors_rx)
		connector_indexes.sort()	
		
		if not non_content(part_0, part_0.lower()):		
			if len(connector_indexes) == 0 and ((' ' in part_0 and is_method(part_0.lower())) or (len(part_0.split(' ')) < 4 and (is_tool(part_0) or is_resource(part_0.lower())))):
				solution.append(part_0)								
			else:
				if len(connector_indexes) == 0:
					language, dataset, tool, method, resource = language_or_dataset_or_tool_or_method_or_resource(part_0)
				elif len(connector_indexes) == 1:				
					solution, research_problem, resource, language, tool, method, dataset = one_connector_heuristics_titled_solution(part_0, part_0.lower())					
					
	if not non_content(part_1, part_1.lower()) and (len(solution) > 0 or len(research_problem) > 0 or len(resource) > 0 or len(language) > 0 or len(tool) > 0 or len(method) > 0 or len(dataset) > 0):
		part_1_lower = part_1.lower()
		connector_indexes = get_list_of_connector_indexes(part_1_lower, connectors_rx)
		connector_indexes.sort()
		
		sol = []
		rp = [] 
		res = [] 
		lang = [] 
		t = [] 
		meth = [] 
		data = []
		
		if len(connector_indexes) == 0:	
			if is_dataset(part_1_lower):
				data.append(part_1)
			elif ending(part_1_lower, '(task)'):
				rp.append(part_1)
			elif not ending(part_1_lower, '(results)') and not begins_phrase('(toward)', part_1_lower):
				sol.append(part_1)
		elif len(connector_indexes) == 1:
			sol, rp, res, lang, t, meth, data = one_connector_heuristics_titled_solution(part_1, part_1_lower)
			
		if len(sol) > 0 or len(rp) > 0 or len(res) > 0 or len(lang) > 0 or len(t) > 0 or len(meth) > 0 or len(data) > 0:
			solution, research_problem, resource, language, tool, method, dataset = extend_lists_seven(solution, sol, research_problem, rp, resource, res, language, lang, tool, t, method, meth, dataset, data)
		else:
			solution = []
			research_problem = []
			resource = []
			language = []
			tool = []
			method = []
			dataset = []		
						
	return solution, research_problem, resource, language, tool, method, dataset
				
		