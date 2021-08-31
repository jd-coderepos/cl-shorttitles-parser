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
	
	connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
	connector_indexes.sort()
	
	if len(connector_indexes) == 0:
		if 'and' in line:
			language, dataset, tool, method, resource, research_problem = and_heuristics(line)
		elif ending(line.lower(), 'task|study'):
			research_problem.append(line)		
		elif is_research_problem(line) or is_tool(line):
			solution.append(line)
	elif len(connector_indexes) == 1:
		connector = get_info_exactly_one_connector(line.lower())
		
		if connector == None:
			return solution, research_problem, resource, language, tool, method, dataset
		
		i = line.lower().find(' '+connector+' ')
		subpart_0 = line[0:i]
		subpart_1 = line[i+len(' '+connector+' '):]
		
		if len(subpart_0.split(' ')) < 3 and 'evaluation' in subpart_0.lower():
			if not non_content(subpart_0, subpart_0.lower()):		
				method.append(subpart_0)
				language, dataset, tool, meth, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
				if len(meth) > 0:
					method.append(meth[0])
		else:
			if not non_content(subpart_0, subpart_0.lower()):
				solution.append(subpart_0)
			language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
		
	return solution, research_problem, resource, language, tool, method, dataset
	
	