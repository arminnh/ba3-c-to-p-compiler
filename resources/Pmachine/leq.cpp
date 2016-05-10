//leq.cpp

#include "leq.h"


/** 
*	Constructor
*	@param type		specifies on which type to perform the leq operation (StackElementType)
*/
Leq::Leq(StackElementType type): fType(type) {}


/** 
*	Destructor
*/
Leq::~Leq() {}


/** 
*	Checks whether the 2 uppermost stackpositions are of the right type and then performs the leq-operation.
*	@return			none
*	@param stack	the machine on which the operation is performed (StackMachine*)
*	@exception		ExecutionError
*/
void Leq::execute(StackMachine *stack) 
{
	// check if the stack contains at least two entries
	if(stack->fSP < 1)
		throw ExecutionError("instruction leq: requires 2 stackelements to be present.");

	switch(fType)
	{
		case integer:
		{
			StackInteger p1;

			// check if the two uppermost stackentries are of type integer
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP])))
				throw ExecutionError("instruction leq: SP does not point to element of type integer.");
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP - 1])))
				throw ExecutionError("instruction leq: SP - 1 does not point to element of type integer.");

			break;
		}	
		case real:
		{
			StackReal p1;
			// check if the two uppermost stackentries are of type real
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP])))
				throw ExecutionError("instruction leq: SP does not point to element of type real.");
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP - 1])))
				throw ExecutionError("instruction leq: SP - 1 does not point to element of type real.");
			break;
		}
		case boolean:
		{
			StackBoolean p1;
			// check if the two uppermost stackentries are of type real
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP])))
				throw ExecutionError("instruction leq: SP does not point to element of type boolean.");
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP - 1])))
				throw ExecutionError("instruction leq: SP - 1 does not point to element of type boolean.");
			break;
		}

		case character:
		{
			StackCharacter p1;
			// check if the two uppermost stackentries are of type real
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP])))
				throw ExecutionError("instruction leq: SP does not point to element of type character.");
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP - 1])))
				throw ExecutionError("instruction leq: SP - 1 does not point to element of type character.");
			break;
		}
		case address:
		{
			StackAddress p1;
			// check if the two uppermost stackentries are of type real
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP])))
				throw ExecutionError("instruction leq: SP does not point to element of type address.");
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP - 1])))
				throw ExecutionError("instruction leq: SP - 1 does not point to element of type address.");
			break;
		}

	}
		
	// compare
	StackBoolean *result;
	if(*(stack->fStore[stack->fSP - 1]) <= *(stack->fStore[stack->fSP]))
		result = new StackBoolean(true);
	else
		result = new StackBoolean(false);
		
	// remove operands
	delete stack->fStore[stack->fSP];
	stack->fStore[stack->fSP] = 0;
	delete stack->fStore[stack->fSP - 1];
	stack->fStore[stack->fSP - 1] = 0;
	stack->fStore.pop_back();
	stack->fStore.pop_back();
	--stack->fSP;

	// put result on top of stack
	stack->fStore.push_back(result);
	
	// adding cost of this instruction
	stack->fTime.count("leq");

}


/** 
*	Prints the instuction into an outputstream
*	@return			reference to ostream filled with the printed instruction
*	@param os		reference to ostream (ostream&)	
*	@exception		none
*/
ostream& Leq::print(ostream &os) const
{
	os << "leq " << printStackElementType(fType);
	return os;
}

