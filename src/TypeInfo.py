import copy

class TypeInfo:
	def __init__(self, rvalue, basetype, indirections=0, const=[False], isArray=False):
		self.rvalue = rvalue
		self.basetype = basetype
		self.indirections = indirections
		self.const = const
		self.isArray = isArray

	def toRvalue(self):
		if self.rvalue:
			return self
		cpy = copy.deepcopy(self)
		cpy.rvalue = True
		return cpy

	def isCompatible(self, other, ignoreRvalue=True, ignoreConst=False):
		if self.equals(other, ignoreRvalue = ignoreRvalue, ignoreConst = ignoreConst):
			return True

		return False

	def equals(self, other, ignoreRvalue=True, ignoreConst=False):
		# print ("ignoreConst = " + str(ignoreConst), "ignoreRvalue = ", str(ignoreRvalue))
		# print ("self: " + str(self))
		# print ("other: " + str(other) + "\n")

		if not ignoreConst and self.const != other.const:
			return False

		if not ignoreRvalue and self.rvalue != other.rvalue:
			return False

		return  self.basetype     == other.basetype \
			and self.indirections == other.indirections \
			and self.isArray      == other.isArray

	def __eq__(self, other):
		return self.equals(other)

	def out(self, withRvalue=False):
		out = ""
		if self.const[0]:
			out += "const "

		out += self.basetype

		for i in range(0, (self.indirections if not self.isArray else self.indirections - 1)):
			out += " *"
			if i+1 < len(self.const) and self.const[i+1]:
				out += " const"

		if self.isArray:
			out += "[]"

		if withRvalue and self.rvalue is not None:
			out += " " + ("r" if self.rvalue else "l") + "value"

		# out += " ind: " + str(self.indirections) + " const: " + str(self.const)
		return out

	def __str__(self):
		return self.out()
