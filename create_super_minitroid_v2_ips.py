#!/usr/bin/env python3
"""
Custom Horizontal Momentum Experiment Script
Find your perfect speed around the 2-6 range!
"""

def create_ips_patch(changes, output_filename):
    """
    Create an IPS patch file
    changes: list of (address, new_bytes) tuples
    """
    with open(output_filename, 'wb') as f:
        # Write IPS header
        f.write(b'PATCH')
        
        # Write each change record
        for address, data in changes:
            # Write 3-byte address (big-endian)
            f.write(address.to_bytes(3, 'big'))
            # Write 2-byte size (big-endian)  
            f.write(len(data).to_bytes(2, 'big'))
            # Write data bytes
            f.write(data)
        
        # Write IPS footer
        f.write(b'EOF')

def main():
    print("🎮 Custom Super Minitroid Horizontal Momentum Tuner 🎮")
    print("=" * 55)
    
    # CORRECTED! Your perfect speed is around 2-6, not 40-60!
    # Your "working perfectly" ROM actually uses speed 2!
    
    # 🎯 RECOMMENDED STARTING POINTS (corrected range):
    speed = 1  # ⭐ ULTRA-CONSERVATIVE: Even slower than your "perfect" ROM!
    # speed = 2  # Your known "perfect" speed
    # speed = 3  # Conservative boost from 2
    # speed = 4  # Moderate boost 
    # speed = 6  # More aggressive but still reasonable
    # speed = 8  # Getting faster
    
    print(f"🚀 Setting horizontal momentum to: {speed}")
    print(f"   (Hex: 0x{speed:02X})")
    
    print(f"\n📊 CORRECTED Speed Reference:")
    print(f"   2 - Your 'perfect' speed (from working ROM)")
    print(f"   3 - Slightly faster")
    print(f"   4 - Moderate boost")
    print(f"   5 - ⭐ RECOMMENDED starting point")
    print(f"   6 - Bit more aggressive")
    print(f"   8 - Getting fast")
    print(f"   10+ - Will feel 'super fast'")
    
    # Apply the speed to all movement types
    changes = [
        (0x81F71, bytes([speed])),  # Non-spinning jump horizontal speed
        (0x81F7D, bytes([speed])),  # Spinning jump horizontal speed  
        (0x81F65, bytes([speed])),  # Running max speed
        (0x81FA1, bytes([speed])),  # Horizontal speed after running off ledge
        (0x82049, bytes([speed])),  # Wall jump horizontal speed
    ]
    
    print(f"\n⚙️  Applying speed {speed} to all addresses:")
    print(f"   - 0x81F71: Non-spinning jump → {speed}")
    print(f"   - 0x81F7D: Spinning jump → {speed}") 
    print(f"   - 0x81F65: Running max speed → {speed}")
    print(f"   - 0x81FA1: Horizontal ledge speed → {speed}")
    print(f"   - 0x82049: Wall jump speed → {speed}")
    
    # Create the IPS patch
    create_ips_patch(changes, 'Super Minitroid V2.ips')
    
    print(f"\n✅ IPS patch created: Super Minitroid V2.ips")
    print(f"🎯 Speed: {speed} (perfect range 2-8)")
    print(f"📱 Apply with multipatch to Super Minitroid.smc")
    print(f"🚀 Now includes wall jump horizontal momentum!")
    
    print(f"\n💡 TO EXPERIMENT:")
    print(f"   Edit line 37: speed = {speed}  # Change this number!")
    print(f"   Try: 3, 4, 5, 6, 7, 8 and see what feels best!")
    print(f"   (Stay under 10 unless you want 'super fast')")

if __name__ == "__main__":
    main() 