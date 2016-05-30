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

	def isConst(self):
		if len(self.const):
			return self.const[-1]
		return False
		# raise Exception("Type {0} has empty const list".format(self))

	def isCompatible(self, other, ignoreRvalue=True, ignoreConst=False):
		if self is None or other is None:
			return False
		if self.equals(other, ignoreRvalue = ignoreRvalue, ignoreConst = ignoreConst):
			return True

		'''
		// char* = char []
        char *a = "please help me this is so hard";

        a[] = {1, 2};
		// int * = int []
		int *b = a;

		int *c;
		// int * = int []
		c = a;
		more examples: tests/testfiles/binary-operators/strings-and-arrays.c
		'''

		if self.indirections == 1 and other.indirections == 1 and (not self.isArray and other.isArray or self.isArray and not other.isArray):
			return self.basetype == other.basetype

		if not ignoreConst and not self.isConstCompatible(other):
			return False

		return False


	def isConstCompatible(self, other):
		if len(self.const) != len(other.const):
			# if throw:
			# 	raise Exception("isConstCompatible expects const lists of the same length; got {0} for {1} and {2} for {3}".format(\
			# 	self.const, str(self), other.const, str(other)))
			# else:
				return False

		# print("--- isConstCompatible: comparing {0} to {1}: {2} and {3}".format(self, other, self.const, other.const))

		for i in range(len(self.const) - 1):
			# last one is always OK because that's the one we're actually assigning (sorry bad explanation ask me)
			cself = self.const[i]
			cother = other.const[i]
			if cother and not cself:

				return False

		return True

	def equals(self, other, ignoreRvalue=True, ignoreConst=False):
		if self is None or other is None:
			return False
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
		# print("CONST ELEMENTS for basetype {0}, indirections {1}: {2}".format(self.basetype, self.indirections, self.const))
		if len(self.const) and self.const[0]:
			out += "const "

		out += self.basetype

		for i in range(0, (self.indirections if not self.isArray else self.indirections - 1)):
			out += " *"
			if i+1 < len(self.const) and self.const[i+1]:
				out += " const"

		if self.isArray:
			out += " []"

		if withRvalue and self.rvalue is not None:
			out += " " + ("r" if self.rvalue else "l") + "value"

		# out += " ind: " + str(self.indirections) + " const: " + str(self.const)
		return out

	def __str__(self):
		return self.out()
