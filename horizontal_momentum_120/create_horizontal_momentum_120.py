#!/usr/bin/env python3
"""
Create IPS patch to set horizontal momentum to 120 in Super Minitroid
ULTRA-EXTREME horizontal movement patch!
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
    print("Creating IPS patch for ULTRA-EXTREME horizontal momentum (120)...")
    
    # Set all horizontal movement values to 120 (0x78 in hex)
    # This will make Samus move INCREDIBLY fast horizontally!
    changes = [
        (0x81F71, bytes([0x78])),  # Non-spinning jump horizontal speed: 00 → 120
        (0x81F7D, bytes([0x78])),  # Spinning jump horizontal speed: 00 → 120  
        (0x81F65, bytes([0x78])),  # Running max speed: 01 → 120
        (0x81FA1, bytes([0x78])),  # Horizontal speed after running off ledge: 00 → 120
    ]
    
    print("Applying these ULTRA-EXTREME changes:")
    print("- Address 0x81F71: Non-spinning jump horizontal speed 00 → 120")
    print("- Address 0x81F7D: Spinning jump horizontal speed 00 → 120") 
    print("- Address 0x81F65: Running max speed 01 → 120")
    print("- Address 0x81FA1: Horizontal speed after ledge 00 → 120")
    print("\n🚀 WARNING: This will make horizontal movement ULTRA-EXTREME! 🚀")
    print("Speed 120 is nearly 3x faster than our previous 'insane' 45 speed!")
    
    # Create the IPS patch
    create_ips_patch(changes, 'horizontal_momentum_120.ips')
    
    print(f"\nIPS patch created: horizontal_momentum_120.ips")
    print("⚡ Get ready for WARP SPEED horizontal movement! ⚡")
    print("To apply: Use multipatch tool to apply this patch to Super Minitroid.smc")

if __name__ == "__main__":
    main() 