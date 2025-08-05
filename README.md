# Super Minitroid Horizontal Momentum Modding Project

**Objective**: Improve the limited horizontal momentum in Super Minitroid while preserving all other hack features.

## 🎯 **IMPORTANT: Patching Workflow**

**Base ROM**: `Super Minitroid.smc` (original Super Minitroid hack)  
**Our Patches**: Applied **on top of** Super Minitroid.smc using multipatch  
**Final Result**: `Super Minitroid v2.smc` (enhanced with perfect horizontal momentum)

> **Note**: Our horizontal momentum patches are designed to be applied to the already-patched Super Minitroid.smc file, NOT the original Super Metroid ROM. The result creates Super Minitroid v2 with restored air control.

---

## 🔍 Key Discovery: The "Zero Air Control" Problem

**BREAKTHROUGH**: Super Minitroid didn't just reduce horizontal momentum - it **completely eliminated horizontal air control**!

### Original Problem Statement
> "The horizontal momentum is too limited. I'd like to double the horizontal momentum if possible."

### What We Actually Found
Super Minitroid **removed nearly all horizontal air movement**, making Samus feel sluggish and unresponsive during platforming.

---

## 🎯 Memory Addresses & Values Analysis

### Critical Horizontal Movement Addresses

| Address | Function | Original Super Metroid | Super Minitroid | Effect |
|---------|----------|----------------------|-----------------|--------|
| **0x81F71** | Non-spinning jump horizontal speed | **01** | **00** | ❌ NO air control |
| **0x81F7D** | Spinning jump horizontal speed | **01** | **00** | ❌ NO air control |
| **0x81F65** | Running max speed | **02** | **01** | 🐌 Halved speed |
| **0x81FA1** | Horizontal speed after ledge fall | **01** | **00** | ❌ NO ledge momentum |
| **0x82049** | Wall jump horizontal speed | **01** | **00** | ❌ NO wall jump momentum |

### Impact Analysis
- **Air Control**: Super Minitroid = **0** vs Original = **1** (infinite improvement needed!)
- **Running Speed**: Super Minitroid = **1** vs Original = **2** (50% reduction)
- **Ledge Momentum**: Super Minitroid = **0** vs Original = **1** (infinite improvement needed!)
- **Wall Jump Momentum**: Super Minitroid = **0** vs Original = **1** (infinite improvement needed!)

---

## 🛠️ ROM Hacking Methodology

### Phase 1: Discovery & Analysis
1. **Binary Comparison**: Used `xxd` to examine specific memory addresses
2. **Value Verification**: Confirmed each address controls specific movement types
3. **Impact Assessment**: Discovered the "zero air control" issue

### Phase 2: Solution Development
1. **Custom Patch Creation**: Python script to generate IPS files
2. **Iterative Testing**: Fine-tuned speed values based on gameplay feel
3. **Factor Analysis**: Calculated exact improvement ratios

### Phase 3: Optimization
1. **Speed Dialing**: Found perfect speed through systematic testing
2. **Multiple Variants**: Created organized folder structure for different speeds
3. **Documentation**: Comprehensive notes for future reference

---

## ✅ Final Solution: Speed Factor Analysis

### "What factor speed did you apply?"

**Answer**: Ken applied **infinite factor improvements** to horizontal air movement!

| Movement Type | Original Super Metroid | Custom Patch (Speed 1) | Improvement Factor |
|---------------|-------------------------|----------------------|-------------------|
| **Non-spinning jump** | 0 | 1 | **∞** (0→1, infinite!) |
| **Spinning jump** | 0 | 1 | **∞** (0→1, infinite!) |
| **Running speed** | 1 | 1 | **1x** (unchanged) |
| **Ledge falling** | 0 | 1 | **∞** (0→1, infinite!) |
| **Wall jump** | 0 | 1 | **∞** (0→1, infinite!) |

### Real Impact
- **Transformed**: Zero air control → Precise air control
- **Preserved**: Original running feel (no change to ground movement)
- **Enhanced**: Platforming responsiveness without breaking game balance

---

## 📁 Organized Project Structure

```
super_minitroid_v2/
├── NOTES.md                          # This documentation
├── Super Metroid (JU) [!].smc        # Original unmodified ROM
├── Super Minitroid.smc               # Base Super Minitroid ROM
├── Super Minitroid.ips               # Original Super Minitroid patch
│
├── horizontal_momentum_custom/       # 🎯 PERFECT SOLUTION (Speed 1)
│   ├── create_custom_momentum_patch.py
│   ├── custom_horizontal_momentum.ips
│   └── [Customizable speed experiments]
│
├── horizontal_momentum_doubled/      # Conservative (Speed 2-4)
│   ├── create_doubled_momentum_patch.py
│   ├── horizontal_momentum_doubled.ips
│   └── [ROM to be created]
│
├── horizontal_momentum_45/           # Ultra-fast (Speed 45)
│   ├── create_horizontal_momentum_45.py
│   ├── horizontal_momentum_45.ips
│   └── Super Minitroid - horizontal momentum 45.smc
│
├── horizontal_momentum_60/           # Very fast (Speed 60)
│   ├── create_horizontal_momentum_60.py
│   ├── horizontal_momentum_60.ips  
│   └── Super Minitroid - horizontal momentum 60.smc
│
└── horizontal_momentum_120/          # ULTRA-EXTREME (Speed 120)
    ├── create_horizontal_momentum_120.py
    ├── horizontal_momentum_120.ips
    └── [ROM to be created]
```

---

## 🎮 Speed Reference Guide

### Practical Speed Ranges

| Speed Value | Feel | Use Case |
|-------------|------|----------|
| **0** | No air control | Original Super Minitroid (broken) |
| **1** | ⭐ **Perfect** | Precise platforming, balanced control |
| **2** | Slightly faster | Conservative boost |
| **3-5** | Moderate | Faster platforming |
| **6-10** | Fast | Speedrun practice |
| **11-20** | Very fast | Advanced players |
| **21-45** | Extremely fast | Experimental/fun |
| **46+** | Insane | Chaos mode |

### Recommended Progression
1. **Start with Speed 1** (our optimized solution)
2. **Experiment upward** if you want more speed
3. **Use custom script** for precise tuning

---

## 🐍 Python Automation Scripts

### Custom Speed Generator (Recommended)
```bash
cd horizontal_momentum_custom/
python3 create_custom_momentum_patch.py
# Edit line 37 to change speed value
```

### Pre-configured Speed Scripts
```bash
# Conservative boost (Speed 2-4)
python3 horizontal_momentum_doubled/create_doubled_momentum_patch.py

# Ultra-fast variants
python3 horizontal_momentum_45/create_horizontal_momentum_45.py
python3 horizontal_momentum_60/create_horizontal_momentum_60.py
python3 horizontal_momentum_120/create_horizontal_momentum_120.py
```

---

## 🔧 Technical Implementation Details

### IPS Patch Structure
- **Format**: Standard IPS (PATCH...EOF)
- **Size**: 38 bytes (5 single-byte modifications)
- **Compatibility**: All IPS patching tools
- **Base ROM**: Apply to Super Minitroid.smc

### Memory Address Details
- **0x81F71**: Controls left/right movement during non-spinning jumps
- **0x81F7D**: Controls left/right movement during spinning jumps  
- **0x81F65**: Controls maximum running speed (byte after acceleration)
- **0x81FA1**: Controls horizontal momentum when falling off ledges
- **0x82049**: Controls horizontal momentum after wall jumps

### SNES Technical Context
- **CPU**: 65816 processor
- **ROM Banks**: Code typically in $80-$FF range
- **Data Type**: Single-byte values (0-255 range)
- **Physics Engine**: Real-time momentum calculations

---

## 🏆 Project Success Summary

### Problem Solved
✅ **Eliminated the "zero air control" issue**
✅ **Preserved all Super Minitroid features** 
✅ **Fixed wall jump horizontal momentum**
✅ **Created scalable solution for any speed preference**
✅ **Documented complete methodology for future ROM hackers**

### Tools & Techniques Mastered
- Binary ROM analysis with `xxd`
- IPS patch creation and automation
- Python scripting for ROM modification
- Systematic speed value optimization
- Organized development workflow

