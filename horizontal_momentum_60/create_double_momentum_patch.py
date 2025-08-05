#!/usr/bin/env python3
"""
Create IPS patch to double horizontal momentum in Super Minitroid
Based on analysis of original Super Metroid vs Super Minitroid physics values
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
    print("Creating IPS patch to double horizontal momentum in Super Minitroid...")
    
    # Define the changes based on our analysis
    # Original Super Metroid values were: 01, 01, 02, 01
    # We want to double them to: 02, 02, 04, 02
    changes = [
        (0x81F71, bytes([0x02])),  # Non-spinning jump horizontal speed: 00 → 02
        (0x81F7D, bytes([0x02])),  # Spinning jump horizontal speed: 00 → 02  
        (0x81F65, bytes([0x04])),  # Running max speed: 01 → 04 (byte after acceleration)
        (0x81FA1, bytes([0x02])),  # Horizontal speed after running off ledge: 00 → 02
    ]
    
    print("Applying these changes:")
    print("- Address 0x81F71: Non-spinning jump horizontal speed 00 → 02")
    print("- Address 0x81F7D: Spinning jump horizontal speed 00 → 02") 
    print("- Address 0x81F65: Running max speed 01 → 04")
    print("- Address 0x81FA1: Horizontal speed after ledge 00 → 02")
    
    # Create the IPS patch
    create_ips_patch(changes, 'double_horizontal_momentum.ips')
    
    print(f"\nIPS patch created: double_horizontal_momentum.ips")
    print("To apply: Use multipatch tool to apply this patch to Super Minitroid.smc")
    print("This will create a version with doubled horizontal momentum!")

if __name__ == "__main__":
    main() 