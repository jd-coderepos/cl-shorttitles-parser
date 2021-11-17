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
			if 'their applications' in line.lower() or 'its applications' in line.lower() or 'and applications' in line.lower():
				solution.append(line)
			else:
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

		if 'for' == connector:	
			solution.append(subpart_0)
			language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
		elif 'of' == connector:
			if 'application' == subpart_0.lower() or 'applications' == subpart_0.lower():
				method.append(subpart_1)
			elif 'application' in subpart_0.lower():
				if 'construction and applications' in subpart_0.lower() or 'performance analysis and application' in subpart_0.lower() or 'applications and challenges' == subpart_0.lower() or \
				'systems applications' in subpart_0.lower() or 'some applications' in subpart_0.lower() or 'theory and applications' in subpart_0.lower() or 'Recent implementations applications and extensions' == subpart_0 or \
				'some new applications' in subpart_0.lower() or 'application-level studies' == subpart_0.lower() or 'complexity and applications' == subpart_0.lower() or 'techniques and applications' == subpart_0.lower() or \
				'design and application' == subpart_0.lower() or 'study representation and applications' in subpart_0.lower() or 'model-driven applications' in subpart_0.lower():
					language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
				else:
					solution.append(subpart_0)
					language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
			else:
				if non_content(subpart_0, subpart_0.lower()):
					solution.append(subpart_0)
				tool.append(subpart_1)
		elif 'to' == connector:
			if not non_content(subpart_0, subpart_0.lower()):
				solution.append(subpart_0)
			language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
		elif 'using' == connector or 'with' == connector or 'by' == connector or 'from' == connector:
			solution.append(subpart_0)
			if 'applications' != subpart_1.lower():
				if is_tool(subpart_1):
					tool.append(subpart_1)
				else:
					language, dataset, method, resource, research_problem = language_or_dataset_or_method_or_resource_or_rp(subpart_1)
		else:
			if not non_content(subpart_0, subpart_0.lower()):
				solution.append(subpart_0)
			language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
			
	return solution, research_problem, resource, language, tool, method, dataset
