def parse_netlist(file_path):
    # Initialize the circuit structure
    circuit = []
    sub_circuit = {
        "transistor": [],
        "resistor": []
    }

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            # Remove comments from the line
            line = line.split("*")[0].strip()

            if line.startswith("M"):
                segments = line.split()
                name = segments[0]
                parameters = " ".join(segments[1:])
                sub_circuit["transistor"].append({
                    "parameter": name,
                    "value": parameters
                })

            elif line.startswith("R"):
                segments = line.split()
                name = segments[0]
                parameters = " ".join(segments[1:])
                sub_circuit["resistor"].append({
                    "parameter": name,
                    "value": parameters
                })

    circuit.append({"sub_circuit": sub_circuit})
    return circuit

def write_netlist(circuit, file_path):
    # Write the circuit structure to a netlist file
    with open(file_path, 'w') as file:
        for sub in circuit:
            sub_circuit = sub["sub_circuit"]

            # Write transistors
            for transistor in sub_circuit["transistor"]:
                line = f"{transistor['parameter']} {transistor['value']}\n"
                file.write(line)

            # Write resistors
            for resistor in sub_circuit["resistor"]:
                line = f"{resistor['parameter']} {resistor['value']}\n"
                file.write(line)


circuit = parse_netlist("netlist.txt")
print("Parsed Circuit Structure:", circuit)
write_netlist(circuit, "output.txt")