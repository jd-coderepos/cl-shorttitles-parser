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
	
	line_lower = line.lower()
	
	connector_indexes = get_list_of_connector_indexes(line.lower(), connectors_rx)
	connector_indexes.sort()
	
	if len(connector_indexes) == 0:
		if ending(line.lower(), 'prediction') or ending(line.lower(), 'predictions'):
			solution.append(line)
	elif len(connector_indexes) == 1:	
		connector = get_info_exactly_one_connector(line.lower())
		
		if connector == None:
			return solution, research_problem, resource, language, tool, method, dataset
		
		i = line.lower().find(' '+connector+' ')
		subpart_0 = line[0:i]
		subpart_1 = line[i+len(' '+connector+' '):]
		
		if 'prediction' in subpart_0.lower():
			if len(subpart_0.split(' ')) < 3:
				if 'with' == connector or 'using' == connector:
					if not non_content(subpart_0, subpart_0.lower()):				
						research_problem.append(subpart_0)
						
					if is_dataset(subpart_1.lower()):
						dataset.append(subpart_1)
					else:
						solution.append(subpart_1)
				else:
					if not non_content(subpart_0, subpart_0.lower()):				
						research_problem.append(subpart_0)
					language, dataset, tool, method, resource, rp = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
					
					if len(rp) > 0:
						research_problem.append(rp[0])
			else:	
				solution.append(subpart_0)
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
		else:
			if connector == 'with' or connector == 'via' or connector == 'using' or connector == 'by' or connector == 'for':
				if not non_content(subpart_0, subpart_0.lower()):
					solution.append(subpart_0)
				if not non_content(subpart_1, subpart_1.lower()):
					if ' and ' in subpart_1.lower():
						language, dataset, tool, method, resource, research_problem = and_heuristics(subpart_1)
					else:
						language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
			else:
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_0)
				lang, data, t, meth, res, rp = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
				language, dataset, tool, method, resource, research_problem = extend_lists_all(language, lang, dataset, data, tool, t, method, meth, resource, res, research_problem, rp)
				#print(line)
				#print(connector)
				#print(subpart_0)
				#print(subpart_1+'\n')
			
	
	return solution, research_problem, resource, language, tool, method, dataset
	