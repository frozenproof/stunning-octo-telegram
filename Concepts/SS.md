# Slide 3-13
## 3
### Programming language
- Either compile or inteprete based on languages
- Compile create machine codes or give manual instructions to the operating system/virtual machine
- Bytecodes are set of instructions to run on VM, this also mean to decompile the bytecodes -> need a specific decompiler like dnspy

## 4
### Caching strategies
- Not all information are accessed from disk or database, rather through a third party aka caches
- Stragies include:
    - C_Aside : Update both cache and db, which guarantee a **very bad desync rate**
    - R_Through : Cache manage the Database which guarantee **one point of entry, easier to penetrate**
    - W_Around : If caches dont have data, get from server then update the cache, basic structure
    - W_Back : Cache is used as a source of truth, then update the DB after a period of time. While **safe and convenient** for using, chances are the caches might get **corrupted/abused and lose all transactions data**, which happens a lot, in a case such as toram online during the first year of operating which had to reset the whole database due to a fraud.
    - W_through : Similar to W_back but directly operate like R_Through, which negates the effect of losing data but increased traffic means increased cost


## 5
### 5 Unique **ID** Generators
- Unique ID provides a layer of accessibility(read speed and write indexing) as well as security to information stored in the database.
- UUID: Random number based UUID might have conflict, but timestamp based UUID and namespace based UUID are safe for using. Due to the nature of hashing, such ID are **not sequential and inefficient for database indexing**.
- Snowflake: We create an internal indexing system which then guarantee the uniqueness of each ID within their domain, for example:
    ```9099091239``` might mean data warehouse `9`, any ID after it is guaranteed to be unique within data warehouse 9. This system is **fast and indexed, scalability** come with the risks of **getting penetrated** due to <b>known rules of indexings</b>.
- Database auto-increment: This ID system scream "WE DONT HAVE ENOUGH CUSTOMERS" to anyone who know the current indexes of the database, and **DOES NOT GUARANTEE UNIQUENESS ON THE WHOLE DATABASE**
- DB Segment: It's a part of snowflake system, or very similar, which each database server holds a certain number of ID, allows the system to get efficient I/O access.
- Redis : Got tired of waiting for database query? We keep **everything in the RAM** now apparently.
  
## 6
### How Redis persist data
Data persistence is not performed on the critical path and doesn't block the write process in Redis.

● AOF: Write-after log, serve as CDC (Change Data Capture) for Redis

● RDB: If the server ever go down, all data will be gone. In case of such failures, RDB serve as a backup similar to how Github operate.

## 7
### Google Sheets as backend
- Pros: 
    - Cheaper to implement
    - All data are **online and presist** since it's google
- Cons:
  - God saves us if the serverless computing doesn't create issue with **bots and unauthorized access**

## 8
### CRUD ( Create Read Update Delete) vs Event Sourcing
- If CRUD is the base of all operations, Event Sourcing is the logbook that records everything CRUD does, which allows for **an alternative path of recovering database**

<div style="page-break-after: always;"></div>

## 9
### Firewall
- As a rule of thumb, one must remember. **Firewall protect against outside attacks, not inside attacks.**
![alt text](image.png)
- Firewall can be both hardware or software
- Packet filtering basically prevent unsourced machines from sending packets to the machines by **blocking packets from ports or IP address**
- Circuit level gateway: Check for TCP handshakes for legitmacy, can be used to prevent DDos attacks before they have a chance of sending an attack
- Application level gateway ( aka proxy firewall) : Create your own rules of filtering packets or implementation of connections regulations.
- Stateful inspection : Track all packets to see if they are acceptable within their domain of data stream given their context.
- NGFW : Next Generation Firewall that serve as the baseline of how everything is monitored, like **intrusion prevention, deep packets analysis, application awareness.** Such an example would be <span style="color:blue">IBM QRadar SOAR</span>. Built in intrusion prevention, with AI monitored systems to guarantee an application is doing exactly what the policy entails.

## 10 
### Linux Performance Observability Tool
![alt text](image-1.png)

Since there are too many, we focus on most important tools.

‘**vmstat**’ - reports information about processes, memory, paging, block IO, traps, and CPU activity.

- ‘**iostat**’ - reports CPU and input/output statistics of the system.
- ‘**netstat**’ - displays statistical data related to IP, TCP, UDP, and ICMP protocols.
- ‘**lsof**’ - lists open files of the current system.
- ‘**pidstat**’ - monitors the utilization of system resources by all or specified processes, including CPU, memory, device IO, task switching, threads, etc.

## 11
### Message queue
- Since the system must deal with desynchronization , such as messages brokers, the queue system is used to guarantee the safety of data as well as the order of which data are procssed
- Queues have three design principles
    - at-most-once: <span style="color:red">will lose data but have exceptional speed</span>
    - at-least-once: guaranteed to have duplicates of data, doomed if you use, doomed if you don't.
    - exactly-once: require another system of managing the queue, but the cost can be alleviated using hashes to guarantee at-least-once is used to confirm the transactions then overwrite the data with same hashes to store them

## 12
### Where do we cache data
Not all data are needed to get cached, only data that are required to transfer.
Thus the tools that keep data cache should be either get access frequently or convieniently placed near users.

These include, but not limited to:
- Client apps (Duh) 
- CDN (Content Delivery Network)
- Load Balancer (Can be used if the system load is too heavy)
- Services (Cache strategies)
- Distributed Cache (**Use key-value pairs**, which make the database run smoother because operations can be sharded between machines)
- Database (Of course, a database of caches for databases)
Transaction log (Operating log, unconventional method)
Replication Log (Used frequently since it's a replica of the database at it's stable form)

## 13
### Session, Cookie, JWT, OAuth2 and the birth of SSO

Long ago, when websites don't persist too many functions, a simple login form (today also known as WWW-A) was sufficient. 

Then everyone realized that every operation would need a login since **<span style="color:red">the authorization doesn't persist</span>**. Session and Cookie were created in response as a way for the server to retrieve the user data without relogging

But cookie **<span style="color:red">wasn't designed for mobile apps</span>**. So tokens were created as an universal way for all application to apply. JWT is created, **contains signing keys which can be trusted**.

Now we have too many applications, thus **<span style="color:red">signing in become a hassle</span>**. SSO solve this issue by sharing the user profile from a central authorization server.

OAuth serve as the policy which **All OPERATIONS MUST OBLIGE TO.**

# Slide 14-24

## 14
### Types of software engineers
![alt text](image-2.png)

Front end is user sided, including **User Interfaces and User Experience**.

Back end is where **businesses logics are implemented and handled**.

Where the two sides meet are "Full Stack", the one where operations are performed at the most atomic form and delays are rarer, however, should the developers elope with another company, it spells **the end of the product without a manual**.

## 15
### Webhook vs Polling
- Since operations don't always complete instantly, we needed a method for **desynchronization and data consistency.**
![alt text](image-3.png)
- Webhook serve as open port of the server, when the operations are run, **the client respond at this webhook address to notify the server of the completion, failure, delay, requirement.**
- Polling serve as a hotline between server and client and is the **fallback for the interact protocols** when Webhook is unavailable.

## 16
### Inter-process communications
There are 5 types total, and we should only need these 5 unless something really bizarre happens.

- Pipe : Literally connecting one end of a process of another process. Similar to how apis work, it share the same weaknesses apis have 
- Message queue : Everything is recorded into a single queue
- Signal : Works similar to how machines ask for remote host ports, if a process is holding the connection, other processes will wait. <span style="color:red">May lead to race conditions</span>.
- Semaphore : Processes waits until the value is set to a certain value, in this way there is **no race condition or desyncrhonization**, but will look very weird.
- Virtual memory : Programs handle the communication by themselves, which is the most frequently used by large companies, but also the worst solution possible, prone to errors and should the virtual machine is hacked, there is no stopping it since the evil process already detached from the server.

## 17 
### Upload large files
- **Just cut the file, file cutter**, said the Multi-part upload.
- We reassemble the files back to their original state at the peers. This guarantee an integrity check is confirmed upon inspection.

## 18
### Redis vs Memcached
![alt text](image-4.png)
Redis is just superior to memcached, except for the architecture, because memcached relies on multiple processes which allows it for having multiple load balancers.

## 19
### Eight data structure
They are known as the big 8 of data.

- Skiplist : Instead of an array, **each item know where the next and the previous item is**.
- Hash index : Used in map structure since anything with an unique index use map.
- SS Table : A data tree that **allows fast read and write access but need to re sort** every time new data are inserted into the database. Immutable.
- LSM Tree : Log structured merge tree, an abomination created by joining Skiplist and SS Table with are both known for their **high write throughput** since the pointer only contain a single unit of data.
- B Tree : Self balancing tree, the **most consistant performance** since it works well on disks.
- Inverted index : Instead of storing the data, we store a list of known data then store the new data in form of a tree made of known indexes from the list, **replacing the data with indexes**.
- Suffix tree : Hoffman tree. 
- R Tree : The more data overlaps, the better this database perform.

## 20
### Where are data structures used
- list: Singular **array of information** that users can rely on
- stack: The evolution of any data are kept safe here
- queue: User actions in-game, since users know what they did and expect the game to **respect that order**
- heap: Task scheduling, anything with a tree structure is functional for a task schedule, or anything with order
- tree: Keep the HTML document structure, or for AI decision. Not viable as a tool of high performance data storage but **extremely efficient as the roadmap generators**. 
- suffix tree: Searching string in a document, a specific case of trees
- graph: **Tracking and visualize the data**
- r-tree: Finding the nearest neighbor, useful for clustering 
- vertex buffer: Sending data to GPU for rendering, very specific.

## 21
### Design patterns

♦ Builder: Lego Master - Builds objects step by step, keeping creation and appearance separate. Similar to Factory but only produce evolutions of a class, completed in the last part. 

♦ Prototype: Clone Maker - Creates copies of fully prepared examples.

♦ Singleton: One and Only - A special class with just one instance. Useful for managing a single service.

♦ Adapter: Universal Plug - Connects things with different interfaces. Useful when the new interface is required for an old system, or when data types don't match.

♦ Bridge: Function Connector - Links how an object works to what it does. Connecting abstraction to implementer, this way interfaces can be reused for different similar classes and each class still hold their own implementations.

♦ Composite: Tree Builder - Forms tree-like structures of simple and complex parts. One components can contain sub components.

♦ Decorator: Customizer - Adds features to objects without changing their core. Like customizing a pizza, you can add cheese but the bread is always guaranteed. 

♦ Facade: One-Stop-Shop - Represents a whole system with a single, simplified interface. Batched commands are considered a part of facade system.

♦ Flyweight: Space Saver - Shares small, reusable items efficiently. Used in vm ware where processes share same hardwares, or users sharing the compiler in the same vm.

♦ Proxy: Stand-In Actor - Represents another object, controlling access or actions. Serve as an empty blanket that only call real data when needed.

♦ Chain of Responsibility: Request Relay - Passes a request through a chain of objects until handled. For example, an auto parsers will try every single compiler, each step is a part of the chain.

♦ Command: Task Wrapper - Turns a request into an object, ready for action. Basically an interface for interactions.

♦ Iterator: Collection Explorer - Accesses elements in a collection one by one. The most important part of any operation is accessing the data, and iterator provides the solution for all to use.

♦ Mediator: Communication Hub - Simplifies interactions between different classes. Like a coffee making machine, the users select options and the machine know which components to call, and in which order thanks to the meditator.

♦ Memento: Time Capsule - Captures and restores an object's state. A back up system for the class instances.

♦ Observer: News Broadcaster - Notifies classes about changes in other objects. Always listening to all changes to report to other components.

♦ Visitor: Skillful Guest - Adds new operations to a class without altering it. Visitor essentially add operations to classes without changing the classes, making it essential for hot fixes.

## 22
### Code Review Pyramid
![alt text](image-5.png)
- If anything go wrong, ask the reviews.

## 23
### HTTP Responses
- Informational (100-199)
- Success (200-299)
- Redirection (300-399)
- Client Error (400-499)
- Server Error (500-599)
  ![alt text](image-6.png)

## 24 
### Writing codes that run on all platforms 
There are many options

- Cross platform intepreter : Constraint and extra works
- Using universal platform : Constraint on overhead since optimization is not possible
- Isolate platform support into code modules : Like adding more metal on a metal bar, it just get heavier and resistant to change
- Emulator : Compatibility is a guaranteed issue since the instruction sets may not be emulated efficiently.
- Adaptable code plans : Since universal codes are unreal, we create codes for the same functionalities accross languages and platforms.
- Engage in code sharing platform : How is this a solution ? It reduces the amount of works, but make the codes become complex since the codes are not designed to works with system requirements.

# Slide 25-35
## 25
### Latency number we should know
![alt text](image-7.png)

## 26
### Proxy vs Reverse Proxy
Proxy protect users, reverse proxy protect the servers.

## 27
### Symmetric vs Asymmetric Encryption
Both peers use the same system of keys which can always be used to access or encrypt the data, and since the data are encrypted in batches, **symmetric's fast.**

However, if bad actor grab a key, it's game over for security. When traffics happens, things are bound to be **lost in traffic**. And there can **only be so many keys** since the algorithms have a length standard.

Asymmetric keys don't need to transfer the secret key, which allows for **secured transfers between peers** as long as the secret key isn't lost.

The backside is that the algorithm is too complicated to run efficiently, which make encoding and decoding ultra **slower compared to the symmetric algorithms.**

## 28
### Load balancing algorithm
Since a system can't always rely on a single unit to process all data.

#### Static:
- Round Robin : A queue system which run based on whichever request came first, then whichever request surpass a certain degree of heavy duty will be partitioned into smaller parts. This also mean this balance only maintains **if the processing rate is assumed to be uniform across all instances of services, thus should only be available for stateless services.**
- Sticky R2 : Basically same as Round Robin but we assume each pair of query is from the same host, prone to errors.
- Weighted R2 : Now we specify a host is stronger than other host and allowed to handle more requests than others.
- Hash : Random BS goes here, why bother with balance when you can just send requests based on a rule that completely remove all optimizations.
#### Dynamic:
- Least connections : Whichever peer has the least concurrent connections will be chosen for the next requests.
- Fastest response time : This is **the best solution but the most prone to error** due to the fact that a request might be too light to confirm how fast the system can respond.

## 29
### What's the deal with Program and Process and even Thread ( get it ?)

- Programs are **sets of instructions.**
- Processes are the **loaded instances of a program in RAM**, hence there can be multiple processes of a same program.
- Threads are the **representations of the calculations being made by the program**, hence they have address of the virtual thread aka process.

With that established, no threads can run by themselves to produce meaningful actions, they need to notify other threads of their actions, which is why **inter-thread communication is required and must run fast since threads are inherently, I/O blocking operations.**

## 30
### Cookie vs Session

Cookie was created as a solution for authorization, but that also means it **can get stolen.**

The solution was managing **a new entity that can effectively encapsulate the cookie, and server can control it directly** without interfering with legimate operations.

## 31
### What make URL an URL?
![alt text](image-8.png)
URL are , universal resource locator. URL innit?

But in all honesty, URL are important.

Query using URL are unsafe, but we can tolerate it for public API.

Parameters tell the host what the requests need. Fragments of all things are frequently used when dynamic loading wasn't a thing in older internet protocols. 

I'm not satisfied with this conclusion but URL are very ancient so we can't say more.

## 32
### Internet Traffic Routing Policy

Just like a city, the internet has roads of traffic. Routing are just traffic laws that packets must follow in order to get to an end point. A server can have many mirrors to support a single service, each of these services are considered to be a single end point of the server.

There are total of 6 universal ways of doing it, but just like traffic laws, it only get to the point where congestions are impossible to avoid.

- Simple : Can't reach then just fail. Very common and the most frequently used by new devs since they don't have the fund to deal with back ups or fall back.
- Fall back : Fall back. It's just back up of the service. What more can you possibly squeeze from this other than the fact it's redundancy and expensive.
- Geolocation : Our houses have been next to each other since birth.
- Latency : Wrap me in plastic and let me shine. You basically never gonna meet me live.
- Multivalue answer : I have a coin, meet me on the flip side.
- Weighted routing policy : Democracy is eternal.

## 33
### JWT
All technical details are important 
![alt text](image-9.png)

JWT is a token used for authentication.

## 34
### Linux Operating System Commands
![alt text](image-10.png)

There is not a better description than this chart, if one need to use a more complicated command, command /help would guide the user.

## 35
### Linux Boot Process
![alt text](image-11.png)

Power go into the circuit -> BIOS Awaken -> Request and detect devices -> Choose a boot device like disks -> Boot load using grub, execute kernel commands and load supported libraries -> execute systemd thus manage all processes and check all hardwares -> run target files which are default files -> execute startup scripts which are just shell commands and scripts that users customize.

<h1> This is the point </h1>
Well that's one-fifth of this 

# Slide 36-46

## 36 
### Payment system
![alt text](image-12.png)

FedNow is automatic and FedWire which use ACH ( Automatic Clearing House aka only clearing the cached transactions ).

The difference is that ACH needs human operators since there are confirmation made by humans.

## 37
### OSI Models

Please Do Not Touch Sausage PizzA

![alt text](image-13.png)

## 38
### Fullstack operations

![alt text](image-14.png)

Everything a fullstack dev need is basically whatever you can imagine needed for a server operation.

## 39
### Web protocols

![alt text](image-15.png)

I don't think there is a remark to be made here, except i'm burned out.

## 40
### ACID 

Our favorite rules, among ACIT

- Atomicity : Everything is chained together in batch, either the whole batch get accepted into the system or get rejected.
- Consistency : Github
- Isolation : Each query acts like the only running operation. We just throw the lost one out.
- Durability : Data is backed up

## 41
### OAuth 2.0

![alt text](image-16.png)

The land of promises, essentially just slap SSO on all services. Big companies hate this because they can't access user information.

## 42
### 9 http request types

![alt text](image-17.png)

I remember all of them by heart.

## 43
### SSO

![alt text](image-18.png)

User make a single profile and share the same profile across all services and memes.

## 44
### IaaS / PaaS / SaaS

Infrastructure is the hardware, Platform is the software foundation, Software is the implementation completed.

## 45
### Data Storage structure

![alt text](image-19.png)

Block storage is just physical disk storage. File Storage are just a way of abstraction to manage the block storage.

Object storage are essentially raw bits data, thus cold. Therefore they don't need write access but frequently need to be retrieved from the service.

## 46
### Performance chart

![alt text](image-20.png)

#
