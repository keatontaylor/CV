"""
	Created by Keaton Taylor. 
	Copyright ™ 2018 - http://keatonstaylor.com
"""

class CV(object):

	class Experience(CV):

		def experienceBuilder():

			class APCON(Experience):
				def getDates():
					return {"startDate": "December 2012", "endDate": "October 2013"}
				def getTitle():
					return "Software Development Intern"
				def getProjects():
					return ['Creation of company-wide continous integration server using jenkins.',
							'Mantainence and up-keep of virtual environment for builds, development and test-beds.',
							'Assisted in release build verifications steps coordinateed by the QA team.',
							'Engineered stanity tests for autoamted builds.',
							'Setup a Subversion mirror at local office for faster check-outs.']
				def getSkills():
					return ['Python', 'Jenkins', 'Continous Integration',
							'ESXi', 'SVN', '...']

			class T-SYSTEM(Experience):
				def getDates():
					return {"startDate": "December 2012", "endDate": "October 2013"}
				def getTitle():
				def getProjects():
				def getSkills():

			class GeekSquad(Experience):
				def getDates():
				def getTitle():
				def getProjects():
				def getSkills():

		experienceBuilder = staticmethod(experienceBuilder)

	class Skills(CV):

		def skillsBuilder():

			class ProfessionalSkills():
				def getSkills():
					# hardcoded for now
					self.skills = ['AWS', 'ESXi', '...']


			class PersonalSkills():
				def getSkills():
					self.skills = ['Home Automation', '...']

		skillsBuilder = staticmethod(skillsBuilder)

	class Projects(CV):




