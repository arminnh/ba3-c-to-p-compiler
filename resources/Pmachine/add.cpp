//add.cpp

#include "add.h"

/** 
*	Constructor
*	@param type		specifies on which type (integer or real) to perform the subtraction (StackElementType)
*/
Add::Add(StackElementType type) : fType(type) {}


/** 
*	Destructor
*/
Add::~Add() {}


/** 
*	Checks the contents of the stack and then performs the addition.
*	@return			none
*	@param stack	the machine on which the addition is performed (StackMachine*)
*	@exception		ExecutionError
*/
void Add::execute(StackMachine *stack) 
{
	// check if the stack contains at least two entries
	if(stack->fSP < 1)
		throw ExecutionError("instruction add: requires 2 stackelements to be present.");
		
	switch(fType)
	{
		case integer:
		{
			StackInteger p1;

			// check if the two uppermost stackentries are of type integer
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP])))
				throw ExecutionError("instruction add: SP does not point to element of type integer.");
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP - 1])))
				throw ExecutionError("instruction add: SP - 1 does not point to element of type integer.");

			break;
		}	
		case real:
		{
			StackReal p1;
			// check if the two uppermost stackentries are of type real
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP])))
				throw ExecutionError("instruction add: SP does not point to element of type real.");
			if(typeid(p1) != typeid(*(stack->fStore[stack->fSP - 1])))
				throw ExecutionError("instruction add: SP - 1 does not point to element of type real.");
			break;
		}
		default:
			cerr << "operation not supported for this type" << endl;
	}
	
	// actual addition
	stack->fStore[stack->fSP - 1]->add(stack->fStore[stack->fSP]);
	
	// SP := SP - 1
	delete stack->fStore[stack->fSP];
	stack->fStore[stack->fSP] = 0;
	stack->fStore.pop_back();
	--stack->fSP;
	
	// adding cost of this instruction
	stack->fTime.count("add");
}


/** 
*	Prints the instuction into an outputstream
*	@return			reference to ostream filled with the printed instruction
*	@param os		reference to ostream (ostream&)	
*	@exception		none
*/
ostream& Add::print(ostream &os) const
{
	os << "add " << printStackElementType(fType);
	return os;
}


