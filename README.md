
```markdown
# Network Diagnostic and Tool Package Project

This project is a comprehensive network diagnostic tool built using Python 3. It includes multiple modules for socket programming, network diagnostics, time synchronization, error management, and chat functionality. The project allows students to gain hands-on experience with real-world networking and troubleshooting techniques.

## Project Features

1. **Machine Information Module**  
   Retrieve and display the local machine's hostname, IP address, and network interfaces.

2. **Echo Test Module**  
   Perform basic connection tests between a client and a server using sockets. This module checks if the data sent by the client is received back correctly by the server.

3. **SNTP Time Synchronization Module**  
   Retrieve the current time from an SNTP server (e.g., pool.ntp.org) and compare it with the system time.

4. **Chat Module**  
   A simple chat application where users can send messages between a client and a server. All chat messages are logged in a JSON file.

5. **Error Management and Settings Module**  
   Allows you to modify socket settings such as timeouts, buffer sizes, and switching between blocking and non-blocking modes. Errors are caught and handled gracefully.

## Prerequisites

- Python 3.x
- The following Python libraries:
  - `socket`
  - `time` (or `ntplib` for SNTP)
  - `argparse` (for command-line parameters)
  - `json`
  - `sys`

### Installation

1. **Clone the Repository**
   
   Clone the repository to your local machine using the following command:

   ```bash
   git clone https://github.com/yourusername/network-diagnostic-tool.git
   ```

2. **Install Dependencies**

   It's recommended to use a virtual environment for Python to manage dependencies:

   ```bash
   cd network-diagnostic-tool
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

   Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, you can manually install the dependencies:

   ```bash
   pip install socket ntplib
   ```

### Usage

1. **Run the Main Program**

   After setting up the environment, run the main program using the following command:

   ```bash
   python network_diagnostic_tool.py
   ```

   This will display the main menu where you can choose which module to run.

2. **Main Menu Options**

   - **1. Machine Information**  
     Displays the local machine’s hostname, IP address, and network interfaces.
   
   - **2. Echo Test**  
     Allows you to test the server-client connection by sending data and receiving it back.

   - **3. SNTP Time Check**  
     Retrieves the current time from an SNTP server and compares it with the local system time.

   - **4. Chat**  
     Allows you to run a simple chat server and client. Messages will be logged to `chat_history.json`.

   - **5. Error Management**  
     Allows you to experiment with socket timeouts, buffer sizes, and non-blocking modes. Displays any errors encountered during the test.

   - **6. Exit**  
     Exits the program.

3. **Echo Test Example:**

   - Choose **Echo Test** from the main menu.
   - Select **Server** mode to start the server.
   - Enter the IP and port to listen for connections.
   - In a separate terminal, run the program again and select **Client** mode to connect to the server.

   **Server Example:**
   ```
   Enter mode (client/server): server
   Enter server IP: localhost
   Enter port: 12345
   ```

   **Client Example:**
   ```
   Enter mode (client/server): client
   Enter server IP: localhost
   Enter port: 12345
   Enter message: "Hello, Server"
   ```

4. **Chat Example:**

   - Choose **Chat** from the main menu.
   - Select **Server** mode to start the chat server.
   - Enter the IP and port to listen for connections.
   - In a separate terminal, run the program again and select **Client** mode to connect to the chat server.
   
   **Chat History** will be saved in a file called `chat_history.json`.

5. **SNTP Time Check Example:**

   - Choose **SNTP Time Check** from the main menu.
   - The current time from an NTP server will be displayed along with the comparison to the local system time.

6. **Error Management Example:**

   - Choose **Error Management** from the main menu.
   - You can test socket timeouts, buffer sizes, and switch between blocking and non-blocking modes.

## Example Output

**Echo Test Client:**
```
Enter mode (client/server): client
Enter server IP: localhost
Enter port: 12345
Sent message: "Hello, Server"
Received from server: "Hello, Server"
Connection successful, data matches.
```

**Chat History JSON:**
```json
[
    "Hello, Server!",
    "Hello, Client!"
]
```

**SNTP Time Check Output:**
```
Current time from NTP server pool.ntp.org: 2025-03-21 12:34:56
```

## Error Management Example

**Socket Timeout:**
```
Socket timeout after 5 seconds.
```

---

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. If you have any issues or suggestions, please open an issue in the repository.

---

## License

This project is open source and available under the [MIT License](LICENSE).
```
