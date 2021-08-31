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
		solution.append(line)
	elif len(connector_indexes) == 1:
		connector = get_info_exactly_one_connector(line.lower())

		if connector == None:
			return solution, method, dataset
		
		i = line.lower().find(' '+connector+' ')
		subpart_0 = line[0:i]
		subpart_1 = line[i+len(' '+connector+' '):]
		
		if connector == 'using' or connector == 'with' or connector == 'via' or connector == 'by' or connector == 'through':
			if not non_content(subpart_0, subpart_0.lower()):
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_0)
			solution.append(subpart_1)
		else:
			if not non_content(subpart_0, subpart_0.lower()):
				solution.append(subpart_0)
			language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
		
	return solution, research_problem, resource, language, tool, method, dataset
	