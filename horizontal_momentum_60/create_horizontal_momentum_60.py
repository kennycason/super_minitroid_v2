#!/usr/bin/env python3
"""
Create IPS patch to set horizontal momentum to 60 in Super Minitroid
Very fast horizontal movement patch!
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
    print("Creating IPS patch for VERY FAST horizontal momentum (60)...")
    
    # Set all horizontal movement values to 60 (0x3C in hex)
    # This will make Samus move very fast horizontally!
    changes = [
        (0x81F71, bytes([0x3C])),  # Non-spinning jump horizontal speed: 00 → 60
        (0x81F7D, bytes([0x3C])),  # Spinning jump horizontal speed: 00 → 60  
        (0x81F65, bytes([0x3C])),  # Running max speed: 01 → 60
        (0x81FA1, bytes([0x3C])),  # Horizontal speed after running off ledge: 00 → 60
    ]
    
    print("Applying these VERY FAST changes:")
    print("- Address 0x81F71: Non-spinning jump horizontal speed 00 → 60")
    print("- Address 0x81F7D: Spinning jump horizontal speed 00 → 60") 
    print("- Address 0x81F65: Running max speed 01 → 60")
    print("- Address 0x81FA1: Horizontal speed after ledge 00 → 60")
    print("\n🚀 This will make horizontal movement VERY FAST! 🚀")
    print("Speed 60 is faster than 45 but slower than 120!")
    
    # Create the IPS patch
    create_ips_patch(changes, 'horizontal_momentum_60.ips')
    
    print(f"\nIPS patch created: horizontal_momentum_60.ips")
    print("⚡ Get ready for VERY FAST horizontal movement! ⚡")
    print("To apply: Use multipatch tool to apply this patch to Super Minitroid.smc")

if __name__ == "__main__":
    main() 