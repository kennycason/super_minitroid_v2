#!/usr/bin/env python3
"""
Create IPS patch to set horizontal momentum to 45 in Super Minitroid
Ultra-fast horizontal movement patch!
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
    print("Creating IPS patch for ULTRA-FAST horizontal momentum (45)...")
    
    # Set all horizontal movement values to 45 (0x2D in hex)
    # This will make Samus move extremely fast horizontally!
    changes = [
        (0x81F71, bytes([0x2D])),  # Non-spinning jump horizontal speed: 00 → 45
        (0x81F7D, bytes([0x2D])),  # Spinning jump horizontal speed: 00 → 45  
        (0x81F65, bytes([0x2D])),  # Running max speed: 01 → 45
        (0x81FA1, bytes([0x2D])),  # Horizontal speed after running off ledge: 00 → 45
    ]
    
    print("Applying these LIGHTNING-FAST changes:")
    print("- Address 0x81F71: Non-spinning jump horizontal speed 00 → 45")
    print("- Address 0x81F7D: Spinning jump horizontal speed 00 → 45") 
    print("- Address 0x81F65: Running max speed 01 → 45")
    print("- Address 0x81FA1: Horizontal speed after ledge 00 → 45")
    print("\n⚡ WARNING: This will make horizontal movement EXTREMELY fast! ⚡")
    
    # Create the IPS patch
    create_ips_patch(changes, 'horizontal_momentum_45.ips')
    
    print(f"\nIPS patch created: horizontal_momentum_45.ips")
    print("🚀 Get ready for SONIC SPEED horizontal movement!")
    print("To apply: Use multipatch tool to apply this patch to Super Minitroid.smc")

if __name__ == "__main__":
    main() 