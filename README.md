# NetworkSubnetWizard
Subnetting automation scripts in Python: Calculate subnet details, automate IP allocation for departments, and run via an interactive interface. Simplify network management with efficient solutions.


Subnetting Scripts Repository
This repository contains a collection of Python scripts to assist with various subnetting tasks, including subnet calculation, IP allocation for multiple departments, and an interactive interface to run these scripts. These scripts are designed to simplify network administration tasks and provide useful information about IP address allocation within a network.

Contents
1. departments_ip_allocation.py
This script automates the IP allocation process for multiple departments within an organization. It calculates network details, such as Network ID, Broadcast ID, and Host Range, for each department based on the provided base network and subnet mask. The allocation is performed using the concepts of subnetting and network segmentation.

2. subnet_calculation.py
This script calculates various subnet details for a given IP address in CIDR notation. It provides information about the total number of IPs, usable IPs, subnet mask, and IP range for the specified subnet. This is particularly useful for understanding the characteristics of a specific subnet.

3. subnetting_interface.py
An interactive interface to run the subnetting scripts conveniently. This script provides a user-friendly menu where you can choose between subnet calculation and IP allocation scripts. It allows you to input data and view results in a seamless manner.

How to Use
Clone the repository to your local machine.
Navigate to the desired script's directory.
Run the script using Python 3: python script_name.py.
For the interactive interface, run subnetting_interface.py and follow the on-screen prompts to choose a script to run.

Contributions
Contributions to this repository are welcome! If you have suggestions for improvements, bug fixes, or additional features, feel free to open a pull request. Please make sure to adhere to the repository's coding style and standards.

License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code as per the terms of the license.

Feel free to customize this description according to your preferences and any additional information you want to provide about the scripts or their functionalities.
