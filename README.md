# Super Minitroid v2

Fixed horizontal momentum in Super Minitroid - now with proper air control and wall jump momentum.

## Quick Start

1. **Apply patch**: Use multipatch to apply `Super Minitroid v2.ips` to `Super Minitroid.smc`
2. **Result**: `Super Minitroid v2.smc` with restored air control
3. **Customize**: Edit line 36 in `create_super_minitroid_v2_ips.py` and run to generate custom speeds

## The Problem

Super Minitroid didn't just reduce horizontal momentum - it **completely eliminated air control** in multiple movement scenarios, making platforming feel unresponsive.

---

## Memory Addresses Fixed

| Address | Function | Original | Super Minitroid | Fixed |
|---------|----------|----------|-----------------|-------|
| **0x81F71** | Non-spinning jump horizontal speed | 01 | 00 | ✅ |
| **0x81F7D** | Spinning jump horizontal speed | 01 | 00 | ✅ |
| **0x81F65** | Running max speed | 02 | 01 | ✅ |
| **0x81FA1** | Horizontal speed after ledge fall | 01 | 00 | ✅ |
| **0x82049** | Wall jump horizontal speed | 01 | 00 | ✅ |

**Result**: All movement types now have proper horizontal momentum (0→1+ = infinite improvement)

## Speed Guide

| Speed | Feel | Notes |
|-------|------|-------|
| **1** | ⭐ **Balanced** | Recommended starting point |
| **2-3** | Slightly faster | Conservative boost |
| **4-6** | Moderate | Good for speedruns |
| **7+** | Fast | Experimental territory |

## Usage

```bash
python3 create_super_minitroid_v2_ips.py
```

Edit line 36 to change speed value, then run to generate a new patch.

## Technical Details

### IPS Patch Structure
- **Format**: Standard IPS (PATCH...EOF)
- **Size**: 38 bytes (5 single-byte modifications)
- **Base ROM**: Apply to Super Minitroid.smc

### Memory Address Functions
- **0x81F71**: Non-spinning jump horizontal speed
- **0x81F7D**: Spinning jump horizontal speed  
- **0x81F65**: Running max speed
- **0x81FA1**: Horizontal momentum when falling off ledges
- **0x82049**: Horizontal momentum after wall jumps

### Files
- `Super Minitroid v2.ips` - The patch file (38 bytes, 5 modifications)
- `create_super_minitroid_v2_ips.py` - Script to generate custom patches
- `Super Minitroid v2.smc` - Patched ROM with fixed momentum