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
		
		if connector != None:
			i = line.lower().find(' '+connector+' ')
			subpart_0 = line[0:i]
			subpart_1 = line[i+len(' '+connector+' '):]
			
			if connector == 'using' or connector == 'with' or connector == 'via' or connector == 'by' or connector == 'through':
				if not non_content(subpart_0, subpart_0.lower()):
					if is_research_problem(subpart_0) or is_method(subpart_0):
						research_problem.append(subpart_0)
					elif is_tool(subpart_0) or is_resource(subpart_0):
						tool.append(subpart_0)
					else:
						research_problem.append(subpart_0)
				solution.append(subpart_1)
			elif connector == 'for' or connector == 'of':
				if is_research_problem(subpart_0) or is_method(subpart_0):
					if not non_content(subpart_0, subpart_0.lower()):
						research_problem.append(subpart_0)
					solution.append(subpart_1)
				else:
					if not non_content(subpart_0, subpart_0.lower()):				
						solution.append(subpart_0)			
					tool.append(subpart_1)
			elif connector == 'in' or connector == 'on' or connector == 'as' or connector == 'under' or connector == 'over' or connector == 'against' or connector == 'within':
				solution.append(subpart_0)					
				tool.append(subpart_1)
			elif connector == 'from':
				if not non_content(subpart_0, subpart_0.lower()):
					solution, language, dataset, tool, method, resource, research_problem = from_connector(line)
					solution, research_problem, resource, language, tool, method, dataset = one_connector_heuristics_postprocess(solution, research_problem, resource, language, tool, method, dataset)
				else:
					language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(phrase)
			elif connector == 'to':			
				if begins_phrase('From', line):
					i = subpart_0.find(' ')+1
					subpart_0 = subpart_0[i:]
					if is_tool(subpart_0) or is_resource(subpart_0):
						tool.append(subpart_0)
					else:
						method.append(subpart_0)
					solution.append(subpart_1)
				else:
					if is_language(subpart_0):
						if not non_content(subpart_0, subpart_0.lower()):			
							language.append(subpart_0)
						solution.append(subpart_1)
					else:
						if not non_content(subpart_0, subpart_0.lower()):					
							solution.append(subpart_0)
						if is_tool(subpart_1):
							tool.append(subpart_1)
						elif is_resource(subpart_1):
							resource.append(subpart_1)
						elif is_research_problem(subpart_1):
							research_problem.append(subpart_1)
						elif is_method(subpart_1):
							method.append(subpart_1)
						else:
							tool.append(subpart_1)
			else:
				if not non_content(subpart_0, subpart_0.lower()):
					method.append(subpart_0)
				tool.append(subpart_1)
			
	return solution, research_problem, resource, language, tool, method, dataset