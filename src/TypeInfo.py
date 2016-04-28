import copy

class TypeInfo:
	def __init__(self, rvalue, basetype, indirections=0, const=[False], isArray=False):
		self.rvalue = rvalue
		self.basetype = basetype
		self.indirections = indirections
		self.const = const
		self.isArray = isArray

	def isCompatible(self, other):
		print ("self: " + str(self))
		print ("other: " + str(other))
		if self == other:
			return True

		# type identifier[]; *identifier = literal;
		# if not self.isArray and self.indirections == 0 and not other.isArray and (other.indirections == 1 or other.indirections == 0):
			# return self.basetype == other.basetype

		# type *identifier; identifier = literal;
		# if not self.isArray and self.indirections == 1 and other.isArray:
			# return self.basetype == other.basetype

		if self.indirections == 1 and other.indirections == 1 and not self.isArray and other.isArray:
			return self.basetype == other.basetype

		return False

		# 	return other.__eq__(self)
		# if other.isArray:
		# 	other = copy.deepcopy(other)
		# 	other.indirections += 1
		# 	other.isArray = False

	def __eq__(self, other):
		if self.basetype == other.basetype \
			and self.indirections == other.indirections \
			and self.const == other.const \
			and self.isArray == other.isArray:
			return True
		
	def __str__(self):
		out = self.basetype
		for i in range(self.indirections if not self.isArray else self.indirections - 1):
			out += " *"
			if self.const[i]:
				out += " const"
		if self.isArray:
			out += "[]"
		if self.rvalue is not None:
			out += " " + ("r" if self.rvalue else "l") + "value"

		return out