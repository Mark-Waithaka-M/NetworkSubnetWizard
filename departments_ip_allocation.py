# Part 1: Calculate the number of borrowed bits
def calculate_borrowed_bits(subnets):
    # Calculate the number of borrowed bits using the formula (2^n = number of subnets)
    borrowed_bits = 0
    while 2 ** borrowed_bits < subnets:
        borrowed_bits += 1

    return borrowed_bits

# Prompt the user to enter the number of subnets
try:
    subnets = int(input("Enter the number of subnets: "))
    if subnets <= 0:
        raise ValueError("Number of subnets must be a positive integer.")
except ValueError as e:
    print("Invalid input. Please enter a positive integer for the number of subnets.")
else:
    borrowed_bits = calculate_borrowed_bits(subnets)
    print(f"Number of borrowed bits: {borrowed_bits}")


# Part 2: Calculate the new subnet mask
def calculate_new_subnet_mask(default_subnet_mask, borrowed_bits):
    # Convert the default subnet mask to binary
    default_binary_subnet_mask = ''.join(format(int(x), '08b') for x in default_subnet_mask.split('.'))
    
    # Split the binary subnet mask into Network ID and Host ID sections
    network_id_section = default_binary_subnet_mask[:24]
    host_id_section = default_binary_subnet_mask[24:]

    # Replace zeros with ones in the Host ID section from left to right
    new_host_id_section = ''.join('1' if i < borrowed_bits else bit for i, bit in enumerate(host_id_section))

    # Combine both sections to get the new binary subnet mask
    new_binary_subnet_mask = network_id_section + new_host_id_section

    # Convert the binary subnet mask to decimal format
    new_subnet_mask = '.'.join(str(int(new_binary_subnet_mask[i:i+8], 2)) for i in range(0, 32, 8))

    return new_subnet_mask

# Assume the default subnet mask is 255.255.255.0
default_subnet_mask = "255.255.255.0"

# Use the value obtained in Part 1 (borrowed_bits)
new_subnet_mask = calculate_new_subnet_mask(default_subnet_mask, borrowed_bits)
print(f"New subnet mask: {new_subnet_mask}")


# Part 3: Calculate the Block size
def calculate_block_size(new_subnet_mask):
    # Calculate the value in the Host ID section
    host_id_value = int(new_subnet_mask.split('.')[-1])

    # Calculate the Block size by subtracting the host ID value from 256
    block_size = 256 - host_id_value

    return block_size

# Use the new_subnet_mask obtained in Part 2
block_size = calculate_block_size(new_subnet_mask)
print(f"Block size: {block_size}")

# Part 4: Calculate the number after slash

def calculate_number_after_slash(new_subnet_mask):
    # Convert the new subnet mask to binary
    new_binary_subnet_mask = ''.join(format(int(x), '08b') for x in new_subnet_mask.split('.'))
    
    # Count the number of ones in the new binary subnet mask
    ones_count = new_binary_subnet_mask.count('1')

    return ones_count

# Use the new_subnet_mask obtained in Part 2
number_after_slash = calculate_number_after_slash(new_subnet_mask)
print(f"Number after slash: /{number_after_slash}")


# part 5: IP Application for each department
def calculate_network_details(base_network, borrowed_bits, block_size, department_index):
    # Split the base network into Network ID section and Host ID section
    base_network_parts = base_network.split('.')
    network_id_section = '.'.join(base_network_parts[:3])
    host_id_section = base_network_parts[3]

    # Calculate the Network ID of the current department
    if department_index == 0:
        current_network_id = base_network
    else:
        host_id_value = int(host_id_section) + (block_size * department_index)
        current_network_id = f"{network_id_section}.{host_id_value}"

    # Calculate the Broadcast ID of the current department
    broadcast_id_value = int(host_id_section) + (block_size * (department_index + 1)) - 1
    current_broadcast_id = f"{network_id_section}.{broadcast_id_value}"

    # Calculate the Host range of the current department
    host_range_start = int(host_id_section) + (block_size * department_index) + 1
    host_range_end = int(host_id_section) + (block_size * (department_index + 1)) - 2
    current_host_range = f"{network_id_section}.{host_range_start} - {network_id_section}.{host_range_end}"

    return current_network_id, current_broadcast_id, current_host_range


# Part 1: Calculate the number of borrowed bits
# ... (Code from Part 1)

# Part 2: Calculate the new subnet mask
# ... (Code from Part 2)

# Part 3: Calculate the Block size
# ... (Code from Part 3)

# Part 4: Calculate the number after slash
# ... (Code from Part 4)

# Part 5: Automate IP Allocation for each department
# Prompt the user to enter the base network
try:
    base_network = input("Enter the base network (e.g., 192.168.1.0): ")
    base_subnet_mask = new_subnet_mask
except ValueError as e:
    print("Invalid input. Please enter a valid base network.")
else:
    # Loop through the number of departments (equal to the number of subnets)
    for department_index in range(subnets):
        current_network_id, current_broadcast_id, current_host_range = calculate_network_details(
            base_network, borrowed_bits, block_size, department_index)

        # Display the details for each department
        print(f"Department {department_index + 1}:")
        print(f"Network ID: {current_network_id}")
        print(f"Broadcast ID: {current_broadcast_id}")
        print(f"Host Range: {current_host_range}")
        print()
