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
		if ' and ' in line.lower():
			language, dataset, tool, method, resource, research_problem = and_heuristics(line)
		else:
			solution.append(line)
	elif len(connector_indexes) == 1:
		connector = get_info_exactly_one_connector(line.lower())
		
		if connector == None:
			return solution, research_problem, resource, language, tool, method, dataset
		
		i = line.lower().find(' '+connector+' ')
		subpart_0 = line[0:i]
		subpart_1 = line[i+len(' '+connector+' '):]
		
		if 'by' == connector or 'using' == connector or 'with' == connector or 'via' == connector or 'from' == connector or 'through' == connector:
			if 'protocol' in subpart_1.lower() or 'rule' in subpart_1.lower() or 'method' in subpart_1.lower():
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_0)
				solution.append(subpart_1)
			else:
				solution.append(subpart_0)
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
		elif 'for' == connector:
			solution.append(subpart_0)
			language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
		elif 'of' == connector:
			if 'protocol' in subpart_1.lower() or 'rule' in subpart_1.lower() or 'method' in subpart_1.lower():
				method.append(subpart_1)
			else:
				solution.append(subpart_0)
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
		else:
			if 'protocol' in subpart_1.lower() or 'rule' in subpart_1.lower() or 'method' in subpart_1.lower():
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_0)
				lang, data, t, meth, res, rp = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
				language, dataset, tool, method, resource, research_problem = extend_lists_all(language, lang, dataset, data, tool, t, method, meth, resource, res, research_problem, rp)
			else:
				solution.append(subpart_0)			
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)				
			
	return solution, research_problem, resource, language, tool, method, dataset
