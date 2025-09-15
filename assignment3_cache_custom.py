import m5
from m5.objects import *
import sys

# System
system = System()
system.clk_domain = SrcClockDomain(clock='1GHz', voltage_domain=VoltageDomain())
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

# CPU and Interrupt Controller
system.cpu = X86TimingSimpleCPU()
system.cpu.createInterruptController()

# Add L1 D-TLB and I-TLB
system.cpu.dtb = X86TLB(size = 64, entry_type='data')
system.cpu.itb = X86TLB(size = 64, entry_type='instruction')

# L1 Caches
system.cpu.icache = Cache(size='16kB', assoc=2, tag_latency=2, data_latency=2, response_latency=2, mshrs=4, tgts_per_mshr=20)
system.cpu.dcache = Cache(size='16kB', assoc=4, tag_latency=2, data_latency=2, response_latency=2, mshrs=4, tgts_per_mshr=20)

# Memory Bus
system.membus = SystemXBar()

# Connect L1 caches
system.cpu.icache_port = system.cpu.icache.cpu_side
system.cpu.dcache_port = system.cpu.dcache.cpu_side
system.cpu.icache.mem_side = system.membus.cpu_side_ports
system.cpu.dcache.mem_side = system.membus.cpu_side_ports

# Connect the interrupt ports
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

# Memory Controller
system.mem_ctrl = MemCtrl(dram=DDR3_1600_8x8(range=system.mem_ranges[0]))
system.mem_ctrl.port = system.membus.mem_side_ports

# Workload - Get the binary from command line arguments
binary_name = 'hello'  # Default binary name
if len(sys.argv) > 1:
    # Look for --cmd argument
    for i, arg in enumerate(sys.argv):
        if arg == '--cmd' and i + 1 < len(sys.argv):
            binary_name = sys.argv[i + 1]
            break

# Proper workload setup
process = Process()
process.cmd = [binary_name]
process.cwd = '.'  # Set working directory
process.executable = binary_name  # Set executable

# Set up the workload properly
system.workload = SEWorkload.init_compatible(binary_name)
system.cpu.workload = process
system.cpu.createThreads()

# Instantiate and Simulate
root = Root(full_system=False, system=system)
m5.instantiate()

print("**** Starting simulation... ****")
exit_event = m5.simulate()
print("Exiting @ tick %i because %s" % (m5.curTick(), exit_event.getCause()))
