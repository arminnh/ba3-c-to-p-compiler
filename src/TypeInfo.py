import copy

class TypeInfo:
	def __init__(self, rvalue, basetype, indirections=0, const=[False], isArray=False):
		self.rvalue = rvalue
		self.basetype = basetype
		self.indirections = indirections
		self.const = const
		self.isArray = isArray

	def isCompatible(self, other, ignoreRvalue=True, ignoreConst=False):
		if self.equals(other, ignoreRvalue = ignoreRvalue, ignoreConst = ignoreConst):
			return True

		if self.indirections == 1 and other.indirections == 1 and not self.isArray and other.isArray:
			return self.basetype == other.basetype

		return False

	def equals(self, other, ignoreRvalue=True, ignoreConst=False):
		print ("ignoreConst = " + str(ignoreConst), "ignoreRvalue = ", str(ignoreRvalue))
		print ("self: " + str(self))
		print ("other: " + str(other) + "\n")

		if not ignoreConst and self.const != other.const:
			return False

		if not ignoreRvalue and self.rvalue != other.rvalue:
			return False

		return  self.basetype     == other.basetype \
			and self.indirections == other.indirections \
			and self.isArray      == other.isArray

	def __eq__(self, other):
		return self.equals(other)
		
	def __str__(self):
		out = self.basetype
		for i in range(self.indirections if not self.isArray else self.indirections - 1):
			out += " *"
			if i < len(self.const) and self.const[i]:
				out += " const"
		if self.isArray:
			out += "[]"
		if self.rvalue is not None:
			out += " " + ("r" if self.rvalue else "l") + "value"

		return out