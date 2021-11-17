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

	if len(connector_indexes) == 1:
		connector = get_info_exactly_one_connector(line.lower())
		
		if connector == None:
			return solution, research_problem, resource, language, tool, method, dataset
		
		i = line.lower().find(' '+connector+' ')
		subpart_0 = line[0:i]
		subpart_1 = line[i+len(' '+connector+' '):]
		
		if len(subpart_0.split(' ')) == 2:
			tokens = subpart_0.split(' ')
			if not non_content(tokens[1], tokens[1].lower()):
				solution.append(subpart_0)
			language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
		else:
			solution.append(subpart_0)
			language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
			
		if len(language) == 0 and len(dataset) == 0 and len(tool) == 0 and len(method) == 0 and len(resource) == 0 and len(research_problem) == 0:
			tool.append(subpart_1)
		
	return solution, research_problem, resource, language, tool, method, dataset