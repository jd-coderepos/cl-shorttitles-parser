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
		if ' and ' in line:
			language, dataset, tool, method, resource, research_problem = and_heuristics(line)
		elif ending(line_lower, 'problem') or ending(line_lower, 'problems'):
			research_problem.append(line)
		elif is_research_problem(line) or is_method(line) or is_tool(line):
			solution.append(line)
	elif len(connector_indexes) == 1:	
		connector = get_info_exactly_one_connector(line.lower())

		if connector == None:
			return solution, research_problem, resource, language, tool, method, dataset
		
		i = line.lower().find(' '+connector+' ')
		subpart_0 = line[0:i]
		subpart_1 = line[i+len(' '+connector+' '):]		

		if 'learning' in subpart_0.lower():
		
			if ending(subpart_1.lower(), 'problem') or ending(subpart_1.lower(), 'problems'):
				solution.append(subpart_0)
				research_problem.append(subpart_1)
			elif ending(subpart_0.lower(), 'problem') or ending(subpart_0.lower(), 'problems'):
				solution.append(subpart_1)
				research_problem.append(subpart_0)
			elif is_language(subpart_1):
				solution.append(subpart_0)
				language.append(subpart_1)
			elif len(subpart_1.split(' ')) == 1:
				solution.append(subpart_0)
				tool.append(subpart_1)
			elif len(subpart_0.split(' ')) < 4:
				if 'with' == connector or 'via' == connector or 'using' == connector:
					method.append(subpart_0)
					solution.append(subpart_1)
				else:
					method.append(subpart_0)
					language, dataset, tool, meth, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
					if len(meth) > 0:
						method.append(meth[0])
			else:
				solution.append(subpart_0)
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
				
		else:
			if len(subpart_1.split(' ')) < 4:
				if not non_content(subpart_0, subpart_0.lower()):
					solution.append(subpart_0)
				if 'with' == connector or 'via' == connector or 'using' == connector:
					method.append(subpart_1)
				else:
					language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
			elif connector == 'for' and (is_research_problem(subpart_0) or is_method(subpart_0) or is_tool(subpart_0)):
				solution.append(subpart_0)
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_1)
			else:	
				language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(subpart_0)
				solution.append(subpart_1)
		
	return solution, research_problem, resource, language, tool, method, dataset
