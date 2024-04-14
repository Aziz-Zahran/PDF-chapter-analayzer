import PyPDF2
# Define the chapters and their corresponding keywords
chapters = {
    "1.1 Data Representation": ["data representation", "number systems","binary","BCD", "binary coded decimal", "denary", "overflow" "convert" "kibi", "kilo", "mebi", "mega", "gibi" "giga", "tebi", "tera"],
    "1.2 Multimedia - Graphics": ["Multimedia", "Graphics", "bitmapped image", "pixel", "file header", "image resolution", "screen resolution", "colour depth", "bit depth", "file size", "bitmap image", "vector graphic", "drawing object", "property", "drawing list", "sampling"],
    "1.3 Compression": ["compression", "RLE", "run-length encoding"],
    "2.1 Networks including the internet": ["networks", "internet", "networking devices", "LAN", "local area network", "WAN", "wide area network", "client-server", "peer-to-peer", "thin-client", "thick-client", "topologies", "bus", "star", "mesh", "hybrid", "cloud computing", "public clouds", "private clouds", "wireless networks", "wired networks", "copper cable", "fibre-optic cable", "radio waves", "WiFi", "microwaves", "satellites", "LAN hardware", "switch", "server", "Network Interface Card", "NIC", "Wireless Network Interface Card", "WNIC", "Wireless Access Points", "WAP", "cables", "bridge", "repeater", "router", "Ethernet", "collisions", "Carrier Sense Multiple Access / Collision Detection", "CSMA/CD", "bit streaming", "bit rates", "broadband speed", "World Wide Web", "WWW", "modems", "PSTN", "Public Switched Telephone Network", "dedicated lines", "cell phone network", "IP addresses", "IPv4", "IPv6", "subnetting", "public IP address", "private IP address", "security", "static IP address", "dynamic IP address", "Uniform Resource Locator", "URL", "Domain Name Service", "DNS"],
    "3.1 Computers and their components": ["input", "output", "primary memory", "secondary storage", "removable storage", "embedded systems", "Laser printer", "3D printer", "microphone", "speakers", "magnetic hard disk", "solid state memory", "flash memory", "optical disc reader", "optical disc writer", "touchscreen", "virtual reality headset", "buffers", "Random Access Memory", "RAM", "Read Only Memory", "ROM", "Static RAM", "SRAM", "Dynamic RAM", "DRAM", "Programmable ROM", "PROM", "Erasable Programmable ROM", "EPROM", "Electrically Erasable Programmable ROM", "EEPROM", "monitoring systems", "control systems", "sensors", "temperature", "pressure", "infra-red", "sound", "actuators", "feedback"],
    "3.2 Logic Gates and Logic Circuits": ["logic gates", "NOT", "AND", "OR", "NAND", "NOR", "XOR", "EOR", "functions", "truth table", "logic circuit", "problem statement", "logic expression"],
    "4.1 Central Processing Unit (CPU) Architecture": ["Von Neumann model", "stored program concept", "registers", "general purpose registers", "special purpose registers", "Program Counter", "PC", "Memory Data Register", "MDR", "Memory Address Register", "MAR", "Accumulator", "ACC", "Index Register", "IX", "Current Instruction Register", "CIR", "Status Register", "Arithmetic and Logic Unit", "ALU", "Control Unit", "CU", "system clock", "Immediate Access Store", "IAS", "address bus", "data bus", "control bus", "processor type", "number of cores", "bus width", "clock speed", "cache memory", "ports", "peripheral devices", "Universal Serial Bus", "USB", "High Definition Multimedia Interface", "HDMI", "Video Graphics Array", "VGA", "Fetch-Execute cycle", "register transfer notation", "interrupts", "Interrupt Service handling Routine", "ISR"],
    "4.2 Assembly Language": ["assembly language", "machine code", "assembly process", "two-pass assembler", "simple assembly language program", "instruction groups", "Data movement", "Input and output of data", "Arithmetic operations", "Unconditional instructions", "conditional instructions", "Compare instructions", "modes of addressing", "immediate addressing", "direct addressing", "indirect addressing", "indexed addressing", "relative addressing", "instruction set", "Opcode", "Operand", "LDM", "LDD", "LDI", "LDX", "LDR", "MOV", "STO", "ADD", "SUB", "INC", "DEC", "JMP", "CMP", "CMI", "JPE", "JPN", "IN", "OUT", "END", "Accumulator", "Index Register", "<address>"],
    "4.3 Bit manipulation": ["bit manipulation", "binary shifts", "logical shift", "arithmetic shift", "cyclic shift", "left shift", "right shift", "monitor", "control", "device", "bitwise AND", "bitwise XOR", "bitwise OR", "bit masking", "LSL", "LSR", "label", "opcode", "operand"],
    "5.1 Operating Systems": ["Operating System", "OS", "key management tasks", "memory management", "file management", "security management", "hardware management", "input", "output", "peripherals", "process management", "utility software", "disk formatter", "virus checker", "defragmentation software", "disk contents analysis", "disk repair software", "file compression", "back-up software", "program libraries", "software development", "existing code", "Dynamic Link Library", "DLL"],
    "5.2 Language Translators": ["Language Translators", "assembler software", "assembly language program", "compiler", "high-level language program", "interpreter", "translation", "execution", "benefits", "drawbacks", "Integrated Development Environment", "IDE", "coding", "context-sensitive prompts", "initial error detection", "dynamic syntax checks", "presentation", "prettyprint", "expand", "collapse code blocks", "debugging", "single stepping", "breakpoints", "variables", "expressions", "report window"],
    "6.1 Data Security": ["Data Security", "security", "privacy", "integrity", "computer system security", "security measures", "stand-alone PC", "network of computers", "user accounts", "passwords", "authentication techniques", "digital signatures", "biometrics", "firewall", "anti-virus software", "antispyware", "encryption", "threats", "networks", "internet", "malware", "virus", "spyware", "hackers", "phishing", "pharming", "risk management", "restricting risks", "data security methods", "access rights"],
    "6.2 Data Integrity": ["Data Integrity", "data validation", "data verification", "integrity of data", "methods", "range check", "format check", "length check", "presence check", "existence check", "limit check", "check digit", "data entry", "data transfer", "visual check", "double entry", "parity check", "byte", "block", "checksum"],
    "7.1 Ethics and Ownership": ["Ethics", "Ownership", "computing professional", "professional ethical body", "BCS", "British Computer Society", "IEEE", "Institute of Electrical and Electronic Engineers", "ethics", "impact", "copyright legislation", "software licensing", "licence", "Free Software Foundation", "Open Source Initiative", "shareware", "commercial software", "Artificial Intelligence", "AI", "social issues", "economic issues", "environmental issues", "applications"],
    "8.1 Database Concepts": ["Database Concepts", "limitations", "file-based approach", "storage", "retrieval", "relational database", "features", "entity", "table", "record", "field", "tuple", "attribute", "primary key", "candidate key", "secondary key", "foreign key", "relationship", "referential integrity", "indexing", "entity-relationship diagram", "E-R diagram", "normalisation process", "First Normal Form", "1NF", "Second Normal Form", "2NF", "Third Normal Form", "3NF", "normalised database design"],
    "8.2 Database Management Systems (DBMS)": ["Database Management Systems", "DBMS", "features", "file-based approach", "data management", "data dictionary", "data modelling", "logical schema", "data integrity", "data security", "backup procedures", "access rights", "software tools", "developer interface", "query processor"],
    "8.3 Data Definition Language (DDL) and Data Manipulation Language (DML)": ["Data Definition Language", "DDL", "Data Manipulation Language", "DML", "Structured Query Language", "SQL", "SQL statement", "CREATE DATABASE", "CREATE TABLE", "ALTER TABLE", "PRIMARY KEY", "FOREIGN KEY", "REFERENCES", "SQL script", "query", "modify data", "database tables", "SELECT", "FROM", "WHERE", "ORDER BY", "GROUP BY", "INNER JOIN", "SUM", "COUNT", "AVG", "INSERT INTO", "DELETE FROM", "UPDATE"]
}

with open("pastpapers.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

# Split the text by newline characters ("\n") instead of "\n\n"
lines = text.split("\n")

# Analyze each line and determine if it's a question
chapter_counts = {chapter: 0 for chapter in chapters}
current_chapter = None
for line in lines:
    print(f"Line: {line}")
    # If the line is empty or contains only whitespace, skip it
    if not line.strip():
        continue
    # If the line starts with a word that is not in the current chapter's keywords,
    # assign the line to the next chapter
    if current_chapter is not None and not any(keyword in line.lower() for keyword in chapters[current_chapter]):
        current_chapter = None
    # If the line contains a keyword from any chapter, assign the line to that chapter
    if any(keyword in line.lower() for chapter in chapters for keyword in chapters[chapter]):
        current_chapter = max((chapter for chapter in chapters if any(keyword in line.lower() for keyword in chapters[chapter])), key=len)
        chapter_counts[current_chapter] += 1
        print(f"Assigned to chapter: {current_chapter}")
    # If the line is not assigned to any chapter, print a message
    else:
        print(f"Unassigned line: {line}")

# Print the chapter counts
for chapter, count in chapter_counts.items():
    print(f"{chapter}: {count}")
