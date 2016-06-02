import copy

class TypeInfo:
	def __init__(self, rvalue, basetype, indirections=[(False, False)]):
		self.rvalue = rvalue
		self.basetype = basetype
		self.indirections = indirections # list of tuples: (is array, is constant)

	def array(self):
		return [indirect[0] for indirect in self.indirections]

	def const(self):
		return [indirect[1] for indirect in self.indirections]

	def nrIndirections(self):
		return len(self.indirections) - 1

	def toRvalue(self):
		if self.rvalue:
			return self
		cpy = copy.deepcopy(self)
		cpy.rvalue = True
		cpy.indirections = [(False, isConst) for (isArray, isConst) in cpy.indirections]
		return cpy

	def isArray(self):
		return self.array()[-1]

	def isConst(self):
		return self.const()[-1]

	def isCompatible(self, other, ignoreRvalue=True):
		if self is None or other is None:
			return False

		# print(str(self.indirections), ", ", str(other.indirections))

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
		# assigning an array to a pointer is ok, like in the examples above
		if self.nrIndirections() == 1 and other.nrIndirections() == 1 and (not self.isArray() and other.isArray()):
			return self.basetype == other.basetype

		return  self.basetype         == other.basetype \
			and self.nrIndirections() == other.nrIndirections() \
			and self.isArray()        == other.isArray()


	def isConstCompatible(self, other):
		cself = self.const()
		cother = other.const()
		if len(cself) != len(cother):
			raise Exception("isConstCompatible expects const lists of the same length; got {0} for {1} and {2} for {3}".format(\
			cself, str(self), cother, str(other)))

		# print("--- isConstCompatible: comparing {0} to {1}: {2} and {3}".format(self, other, self.const, other.const))

		for i in range(len(cself) - 1):
			# last one is always OK because that's the one we're actually assigning (sorry bad explanation ask me)
			if cother[i] and not cself[i]:
				return False

		return True

	def equals(self, other, ignoreRvalue=True):
		if self is None or other is None:
			return False
		# print ("ignoreRvalue = ", str(ignoreRvalue))
		# print ("self: " + str(self))
		# print ("other: " + str(other) + "\n")

		if not ignoreRvalue and self.rvalue != other.rvalue:
			return False

		return  self.basetype         == other.basetype \
			and self.nrIndirections() == other.nrIndirections() \
			and self.isArray()        == other.isArray()

	def __eq__(self, other):
		return self.equals(other)

	def out(self, withRvalue=False):
		out = ""
		# print("CONST ELEMENTS for basetype {0}, indirections {1}: {2}".format(self.basetype, self.indirections, self.const))
		if len(self.const()) and self.const()[0]:
			out += "const "

		out += self.basetype

		for i in range(self.nrIndirections()):
			out += " *" if not self.array()[i+1] else " []"
			if i+1 < len(self.const()) and self.const()[i+1]:
				out += " const"

		if withRvalue and self.rvalue is not None:
			out += " " + ("r" if self.rvalue else "l") + "value"
		# out += str(self.indirections)
		# out += " ind: " + str(self.indirections) + " const: " + str(self.const)
		return out

	def __str__(self):
		return self.out()
