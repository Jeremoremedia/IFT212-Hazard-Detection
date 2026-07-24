# This class represents the instruction I want to check
class Instruction:
    def __init__(self, src1=None, src2=None):
        self.src1 = src1
        self.src2 = src2


# This class represents a register in the pipeline
class PipelineRegister:
    def __init__(self, valid, dest_reg):
        self.valid = valid
        self.dest_reg = dest_reg


# These are the destination registers currently in the pipeline stages
ID_EX = PipelineRegister(True, "R4")
EX_MEM = PipelineRegister(True, "R1")
MEM_WB = PipelineRegister(True, "R2")


# This function checks if there is a RAW data hazard
def detect_raw_hazard(decoded_instr):

    # Store the source registers of the current instruction
    src_regs = []

    if decoded_instr.src1 is not None:
        src_regs.append(decoded_instr.src1)

    if decoded_instr.src2 is not None:
        src_regs.append(decoded_instr.src2)

    # Check the source registers against the EX stage
    if ID_EX.valid and ID_EX.dest_reg in src_regs:
        return True

    # Check the source registers against the MEM stage
    if EX_MEM.valid and EX_MEM.dest_reg in src_regs:
        return True

    # Check the source registers against the WB stage
    if MEM_WB.valid and MEM_WB.dest_reg in src_regs:
        return True

    # If there is no matching register, there is no hazard
    return False


# The instruction I am checking is ADD R5, R1, R2
decoded_instr = Instruction("R1", "R2")

# Call the function and save the result
result = detect_raw_hazard(decoded_instr)

# Display the result
print("Instruction: ADD R5, R1, R2")
print("Source Registers: R1, R2")
print("Hazard Detected:", result)
