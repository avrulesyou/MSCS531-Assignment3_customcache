# Gem5 Cache Simulation - Assignment 3

**Author:** Abhishek Vishwakarma  
**Course:** Computer Architecture and Design  
**Assignment:** 3 - Exploring Memory Hierarchy Design in gem5

## Overview

This repository contains a custom gem5 simulation script that implements a system with L1 instruction and data caches, along with TLB (Translation Lookaside Buffer) components. The simulation demonstrates cache performance analysis using the gem5 computer architecture simulator.

## System Configuration

### CPU Architecture
- **CPU Type:** X86 Timing Simple CPU
- **Clock Frequency:** 1 GHz
- **Memory Mode:** Timing
- **Memory Range:** 512 MB

### Cache Hierarchy
- **L1 Instruction Cache (I-Cache):**
  - Size: 16 kB
  - Associativity: 2-way set associative
  - Tag Latency: 2 cycles
  - Data Latency: 2 cycles
  - Response Latency: 2 cycles
  - MSHRs: 4
  - Targets per MSHR: 20

- **L1 Data Cache (D-Cache):**
  - Size: 16 kB
  - Associativity: 4-way set associative
  - Tag Latency: 2 cycles
  - Data Latency: 2 cycles
  - Response Latency: 2 cycles
  - MSHRs: 4
  - Targets per MSHR: 20

### TLB Configuration
- **Data TLB (D-TLB):**
  - Size: 64 entries
  - Type: Data TLB

- **Instruction TLB (I-TLB):**
  - Size: 64 entries
  - Type: Instruction TLB

### Memory System
- **Memory Controller:** DDR3-1600-8x8
- **Memory Bus:** SystemXBar

## Requirements

- gem5 simulator (version 23.0.0.1 or compatible)
- X86 architecture support
- Python 3.x

## Usage

### Basic Usage
```bash
build/X86/gem5.opt assignment3_cache_custom.py --cmd=hello
```

### Running with Custom Binary
```bash
build/X86/gem5.opt assignment3_cache_custom.py --cmd=./your_program
```

### Command Line Arguments
- `--cmd`: Specifies the binary to execute (default: 'hello')

## Features

- **Custom Cache Configuration:** Configurable L1 instruction and data caches with different associativities
- **TLB Support:** Separate instruction and data TLBs for address translation
- **Flexible Workload:** Supports execution of custom binaries
- **Comprehensive Statistics:** Detailed cache performance metrics
- **Modern Architecture:** Uses gem5's latest simulation framework

## Cache Performance Analysis

The simulation provides detailed statistics including:

- Cache hit/miss rates
- Access latencies
- Memory access patterns
- TLB performance metrics
- Instruction and data cache behavior comparison

### Key Performance Metrics
- **I-Cache Miss Rate:** ~3.8%
- **D-Cache Miss Rate:** ~7.0%
- **Average Miss Latency:** ~59,000 ticks

## File Structure

```
├── assignment3_cache_custom.py    # Main simulation script
└── README.md                      # This file
```

## Simulation Output

The simulation generates comprehensive statistics including:
- Cache access patterns
- Hit/miss ratios
- Latency measurements
- Memory traffic analysis
- TLB performance data

## Technical Details

### Cache Parameters
- **MSHR (Miss Status Holding Register):** Handles outstanding cache misses
- **Targets per MSHR:** Maximum number of requests per MSHR entry
- **Associativity:** 2-way for I-cache, 4-way for D-cache

### Memory Hierarchy
1. CPU → L1 Caches (I-cache, D-cache)
2. L1 Caches → Memory Bus
3. Memory Bus → DDR3 Memory Controller

## Contributing

This is an academic assignment project. For questions or issues, please contact me.

## License

This project is created for educational purposes as part of Computer Architecture and Design coursework.


---

*Last Updated: Fall 2025*
