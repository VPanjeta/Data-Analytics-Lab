import os

def getPOs():
	return [
	            "Engineering knowledge: Apply the knowledge of mathematics, science, engineering fundamentals, and an engineering specialization to the solution of complex engineering problems.",
	            "Problem analysis: Identify, formulate, review research literature, and analyze complex engineering problems reaching substantiated conclusions using first principles of mathematics, natural sciences, and engineering sciences.",
	            "Design/development of solutions: Design solutions for complex engineering problems and design system components or processes that meet the specified needs with appropriate consideration for the public health and safety, and the cultural, societal, and environmental considerations. ",
	            "Conduct investigations of complex problems: Use research-based knowledge and research methods including design of experiments, analysis and interpretation of data, and synthesis of the information to provide valid conclusions.",
	            "Modern tool usage: Create, select, and apply appropriate techniques, resources, and modern engineering and IT tools including prediction and modeling to complex engineering activities with an understanding of the limitations.",
	            "The engineer and society: Apply reasoning informed by the contextual knowledge to assess societal, health, safety, legal and cultural issues and the consequent responsibilities relevant to the professional engineering practice.",
	            "Environment and sustainability: Understand the impact of the professional engineering solutions in societal and environmental contexts, and demonstrate the knowledge of, and need for sustainable development.",
	            "Ethics: Apply ethical principles and commit to professional ethics and responsibilities and norms of the engineering practice.",
	            "Individual and team work: Function effectively as an individual, and as a member or leader in diverse teams, and in multidisciplinary settings.",
	            "Communication: Communicate effectively on complex engineering activities with the engineering community and with society at large, such as, being able to comprehend and write effective reports and design documentation, make effective presentations, and give and receive clear instructions.",
	            "Project management and finance: Demonstrate knowledge and understanding of the engineering and management principles and apply these to one's own work, as a member and leader in a team, to manage projects and in multidisciplinary environments.",
	            "Life-long learning: Recognize the need for, and have the preparation and ability to engage independent and life-long learning in the broadest context of technological change."
        	]

def getCOs():
	return {
				"DA" : 	{
						    "Understand the different types of data and its structure" : [2, 3, 5],
						    "Analyse the different types of data pre processing techniques involved in management of data" : [2, 3, 5],
						    "Demonstrate the usage of graphical analysis of data using R" : [1, 2, 3, 5, 12],
						    "Demonstrate the different classes of analytical techniques (basic and advanced statistics) using R" : [1, 2, 3, 5],
						    "Recognize the need for data analytical applications" : [2, 3, 5]    
						},
				"PMEE" :
						{
							"Describe the basic concepts of engineering economics and Time Value Equivalence of money":  [1, 2, 3, 4, 11, 12],
							"Calculate present worth, future worth and equivalent annual worth of investment and compare investment alternatives": [1,5,7,9,12],
							"Identify the various rates of returns" : [3,4,5,7,9,10,12],
							"Estimate the time,scope and cost of a software project" : [1, 3, 5, 6, 8, 9, 10, 11, 12],
							"Identify  various quality issues, communication issues and risks in a software project.": [3,4,6,7,9,10,11,12]
						},
				"EIPR" :
						{
							"Identify the importance of entrepreneurship" : [1, 9],
							"Identify and select the right marketing communication plan and financial plan" : [7, 8, 9, 11, 12],
							"Exemplify the basic principles of IP laws like patents" : [6, 8, 9, 11],
							"Recognize the characteristics and Infringement of Copyright" : [6, 7, 8, 9, 11],
							"Explain  the  importance  of  Trade  Marks,  Industrial  Design  and its infringement" : [6, 8, 9, 11],
						}
			} 