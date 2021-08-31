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

	i = line.find(' ')
	word = line[0:i]
	line = line[i+1:]
	line_lower = line.lower()
	
	if begins_phrase('and', line_lower):
		return solution, research_problem, resource, language, tool, method, dataset
	
	connector_indexes = get_list_of_connector_indexes(line_lower, connectors_rx)
	connector_indexes.sort()

	if matches('explaining|rediscovering|dissecting|relating|observing|accomplishing|dealing|demonstrating|preserving|limiting|explaining|ascribing|overcoming|recognising|minimising|uncovering|preparing|changing|untangling|decreasing|equipping|maintaining|managing|monitoring|realizing|transforming|representing|forecasting|representing|routing|handling|addressing|coordinating|measuring|calculating|measuring|combating|listing|advancing|validating|capturing|stabilizing|elaborating|decrypting|augmenting|decoding|enhancing|verifying|reducing|counting|clustering|minimizing|maximizing|testing|denoising|evaluating|checking|assessing|examining|benchmarking|caching|approximating|quantifying|solving|classifying|exploiting|improving|updating|applying|detecting|translating|revisiting|distinguishing|parsing|locating|understanding|separating|combining|interpreting|incorporating|connecting|matching|integrating|adapting|tracking|utilizing|revealing|combining|merging|mapping|characterising|decomposing|increasing', word.lower()):
		if len(connector_indexes) == 0:
			language, dataset, tool, method, resource, research_problem = language_or_dataset_or_tool_or_method_or_resource_or_rp(line)
		elif len(connector_indexes) == 1:
			solution, research_problem, resource, language, tool, method, dataset = one_connector_heuristics_titled_solution(line, line_lower)			
			solution, research_problem, resource, language, tool, method, dataset = one_connector_heuristics_postprocess(solution, research_problem, resource, language, tool, method, dataset)
	elif matches('unveiling|relating|presenting|performing|emulating|explaining|bringing|betting|revising|specifying|upgrading|reviving|justifying|rethinking|furthering|adding|defining|harnessing|optimising|promoting|sustaining|assembling|putting|adopting|employing|determining|deciding|creating|impacting|making|rewriting|serving|selecting|choosing|executing|reconfiguring|enabling|describing|illustrating|synthesizing|composing|drawing|obtaining|providing|outlining|proposing|producing|designing|recovering|robustifying|simulating|approaching|supporting|recovering|enumerating|estimating|acquiring|developing|recognizing|deploying|scheduling|proving|controlling|investigating|discovering|mining|accelerating|deriving|modelling|training|teaching|extending|compiling|factorising|engineering|formalizing|implementing|constructing|leveraging|exploring|building|learning|modeling|computing|achieving|generating|inferring|predicting|analyzing|analysing|resolving|comparing|extracting|studying|visualizing|visualising|identifying|optimizing|finding|aggregating|introducing|forming|automating|establishing|unifying|joining|characterizing|reconstructing', word.lower()):
		if len(connector_indexes) == 0:
			solution.append(line)
		elif len(connector_indexes) == 1:
			solution, research_problem, resource, language, tool, method, dataset = one_connector_heuristics_titled_solution(line, line_lower)
	else:
		if len(connector_indexes) == 0:
			solution.append(line)
		elif len(connector_indexes) == 1:
			solution, research_problem, resource, language, tool, method, dataset = one_connector_heuristics_titled_solution(line, line_lower)			
	#else:
		#print(word+' '+line)
		
	return solution, research_problem, resource, language, tool, method, dataset
