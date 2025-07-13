### **Module 1: What is the Internet, Really?**

#### **Item 1: A World of Connected Computers**

- **Type:** `lesson`
- **Core Question Answered:** "What is the internet at its most basic level?"
- **Concept:** The internet is not a magical cloud; it's a physical network of billions of computers connected by wires and wireless signals.
- **Analogy:** A giant city where every house is a computer and the roads are the cables connecting them.
- **Interactive Idea:** A `quiz` step asking "Which of these best describes the internet? A) A satellite system, B) A global network of connected computers, C) A single giant computer owned by Google."

#### **Item 2: The Physical Wires**

- **Type:** `lesson`
- **Core Question Answered:** "If it's connected by wires, where are they?"
- **Concept:** Introducing the physical infrastructure: undersea fiber optic cables, local ISP lines, and massive data centers.
- **Analogy:** The global highway system. Undersea cables are the massive intercontinental highways, and your home internet connection is the local street leading to your house.
- **Interactive Idea:** A `markdown` step with an image of the world submarine cable map to show the physical reality of the internet.

#### **Item 3: What is "The Cloud"?**

- **Type:** `lesson`
- **Core Question Answered:** "So when I save something to the cloud, where does it go?"
- **Concept:** "The Cloud" is just a friendly term for someone else's computer (a server) that you are renting space on.
- **Analogy:** It's like renting a storage unit. You don't keep the files in your own house (computer), you store them in a secure facility (a data center) that you can access anytime.
- **Interactive Idea:** A `quiz` asking "The 'Cloud' is best described as: A) A wireless network in the sky, B) Servers in a data center you can access online, C) A new type of hard drive."

---

### **Module 2: Your Digital Address (IP & Domains)**

#### **Item 1: The Computer's Address (IP Address)**

- **Type:** `lesson`
- **Core Question Answered:** "How does one computer find another specific computer on the internet?"
- **Concept:** Every device connected to the internet needs a unique address to be found, called an IP (Internet Protocol) address.
- **Analogy:** An IP address is like a postal address for a house. It's a unique set of numbers that tells data exactly where to go.
- **Interactive Idea:** A `fill` step: "Write a valid IP address: @@INPUT@@" (Answer: use regex for valid ip).

#### **Item 2: The Human-Friendly Address (Domain Name)**

- **Type:** `lesson`
- **Core Question Answered:** "Why do I type `akood.com` instead of a bunch of numbers?"
- **Concept:** Domain names are easy-to-remember labels that stand in for hard-to-remember IP addresses.
- **Analogy:** You don't remember your friend's phone number; you just remember their name in your contacts list. The domain name is the "Name," and the IP address is the "Number."
- **Interactive Idea:** A `quiz` asking "What is the primary purpose of a domain name? A) To secure a website, B) To make IP addresses easier for humans to remember, C) To make websites faster."

---

### **Module 3: The Two Sides of the Coin (Clients & Servers)**

#### **Item 1: The Customer (The Client)**

- **Type:** `lesson`
- **Core Question Answered:** "What is my computer's role when I browse the web?"
- **Concept:** A "client" is a piece of software (like your web browser) that requests information from a server.
- **Analogy:** You are a customer in a restaurant. You (the client) are the one asking for something (a meal).
- **Interactive Idea:** A `quiz`: "When you watch a YouTube video, your web browser is acting as a: A) Client, B) Server, C) Network."

#### **Item 2: The Store (The Server)**

- **Type:** `lesson`
- **Core Question Answered:** "What is a 'server' that I always hear about?"
- **Concept:** A "server" is a powerful computer that is always on, waiting to receive requests and "serve" data (like webpages, videos, or files).
- **Analogy:** The server is the restaurant's kitchen. It has all the ingredients (data) and is ready to prepare and send out your order (the webpage).
- **Interactive Idea:** A `quiz` step showing a multiple sentence and user have to choose wrong one: "A server is a computer that requests information from your browser." The user must identify this statement as incorrect.

---

### **Module 4: The Language of the Web (HTTP/HTTPS/Others)**

#### **Item 1: The Rules of Communication (HTTP)**

- **Type:** `lesson`
- **Core Question Answered:** "How do the client and server know how to talk to each other?"
- **Concept:** HTTP (HyperText Transfer Protocol) is the set of rules or the language that clients and servers use to communicate.
- **Analogy:** HTTP is the language the customer and the waiter use to communicate. The customer knows how to order, and the waiter knows how to take the order.
- **Interactive Idea:** A `fill` step: "The protocol that defines the rules for web communication is called `____`." (Answer: HTTP).

#### **Item 2: The Secure Handshake (HTTPS)**

- **Type:** `lesson`
- **Core Question Answered:** "What does the 'S' in `https://` mean and why is it important?"
- **Concept:** HTTPS is the secure version of HTTP. It encrypts the data sent between the client and server, making it unreadable to anyone trying to eavesdrop.
- **Analogy:** HTTPS is like putting your order in a sealed, secret envelope. Only the waiter (server) can open it. With regular HTTP, you're shouting your order across the restaurant for anyone to hear.
- **Interactive Idea:** A `quiz`: "You should always look for HTTPS when: A) Watching videos, B) Reading news, C) Entering a password or credit card number."

#### **Item 3: The Internet's Toolbox (Other Protocols)**

- **Type:** `lesson`
- **Core Question Answered:** "Is the internet only for browsing websites?"
- **Concept:** While HTTP is the main protocol for websites, the internet is like a giant toolbox with different tools (protocols) for different jobs. We won't dive deep, but it's good to know they exist.
- **Analogy:** Think of a construction worker. They use a hammer for nails (like HTTP for websites), but they also have a screwdriver for screws (like **SMTP** for sending email) and a wrench for bolts (like **FTP** for transferring files). Different jobs require different tools.
- **Interactive Idea:** A `quiz` step for choosing the wrong statement: "statement match the protocol to its main job."

---

### **Module 5: The Internet's Phonebook (DNS)**

#### **Item 1: The Translation Problem**

- **Type:** `lesson`
- **Core Question Answered:** "If my browser needs an IP address, but I only give it a domain name, how does it find the website?"
- **Concept:** There needs to be a system that translates human-friendly domain names into computer-friendly IP addresses.
- **Analogy:** You want to call your friend "Ibrahim," but your phone can only dial numbers. You need to look up "Ibrahim" in your contacts to find his number first.

#### **Item 2: The Phonebook Solution (DNS)**

- **Type:** `lesson`
- **Core Question Answered:** "What is the DNS?"
- **Concept:** The DNS (Domain Name System) is the internet's directory. It's a network of servers whose job is to look up a domain name and return the corresponding IP address.
- **Analogy:** DNS is the internet's giant, public phonebook. Your browser asks it for the number associated with a name.
- **Interactive Idea:** A `quiz`: "The primary job of a DNS server is to: A) Store website files, B) Translate domain names to IP addresses, C) Secure your connection."
- **Interactive Idea:** A `markdown` showing a visual"

---

### **Module 6: Building Blocks of a Webpage (HTML, CSS, JS)**

#### **Item 1: The Skeleton (HTML)**

- **Type:** `lesson`
- **Core Question Answered:** "What is the basic structure of every webpage made of?"
- **Concept:** HTML (HyperText Markup Language) provides the fundamental structure and content of a webpage—the headings, paragraphs, images, and links.
- **Analogy:** HTML is the skeleton of a house. It defines the rooms, doors, and windows, but doesn't include any paint or furniture.
- **Interactive Idea:** A `markdown` step showing a very simple HTML snippet and the raw, unstyled browser output.

#### **Item 2: The Style (CSS)**

- **Type:** `lesson`
- **Core Question Answered:** "How are websites made to look good with colors, fonts, and layouts?"
- **Concept:** CSS (Cascading Style Sheets) is the language used to describe the presentation and styling of a webpage.
- **Analogy:** CSS is the interior design of the house. It's the paint color, the type of furniture, and the pictures on the wall.
- **Interactive Idea:** A `markdown` step showing the same HTML as before, but now with CSS applied, demonstrating the visual transformation.

#### **Item 3: The Interactivity (JavaScript)**

- **Type:** `lesson`
- **Core Question Answered:** "What makes websites interactive, with things like pop-ups, animations, and forms that work?"
- **Concept:** JavaScript is the programming language that brings a webpage to life, allowing it to respond to user actions.
- **Analogy:** JavaScript is the electricity and plumbing in the house. It makes the lights turn on when you flip a switch and the water run when you turn the faucet.
- **Interactive Idea:** A `markdown` step showing the same HTML as before, but now with JS applied, demonstrating the interactive transformation, like the page content changing on button click.
- **Interactive Idea:** A `quiz`: "Which technology would be responsible for showing a pop-up message after you click a button? A) HTML, B) CSS, C) JavaScript."

---

### **Module 7: Putting It All Together**

#### **Item 1: The Complete Journey**

- **Type:** `lesson`
- **Core Question Answered:** "Can we walk through the entire process from start to finish?"
- **Concept:** A step-by-step recap of the entire request-response cycle, reinforcing every concept from the track.
- **Analogy:** A story: "You decide you want to visit the akood.com website. You type its name into your Browser. The browser asks the DNS for the IP. Once you have the ip, you drive there and tell the HTTP request which page you want. The HTTP gets it (Server processing) and gives it to you (HTTP Response). You can now read the page (Browser renders HTML, CSS, JS)."
- **Interactive Idea:** A `markdown` step with a numbered list clearly outlining the 6-7 key steps.

#### **Item 2: Order the Steps**

- **Type:** `lesson`
- **Core Question Answered:** "Can I correctly identify the sequence of events?"
- **Concept:** Testing the user's understanding of the entire process flow.
- **Analogy:** Assembling a piece of furniture; the steps must be done in the correct order for it to work.
- **Interactive Idea:** An `order` (Parson's Problem) step. The user must drag and drop the following events into the correct sequence: `Browser sends request to Server`, `User types domain name`, `Browser renders the page`, `Browser asks DNS for IP address`, `Server sends response to Browser`.
