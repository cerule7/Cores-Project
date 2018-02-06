class Course:

    def __init__(self, name, number, cores):
        self.name = name
        self.number = number
        self.cores = cores

    def __repr__(self):
		# What we'll see if we call print(course) or str(course)
        return f'<{self.number}: {self.name}>'
