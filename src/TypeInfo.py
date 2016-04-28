class TypeInfo:
	def __init__(self, rvalue, basetype=, indirections=0, const=[False], isArray=False):
		self.rvalue = rvalue
		self.basetype
		self.indirections = indirections
		self.const = const
		self.isArray = isArray