# Question C: Cache

From the characteristic of the question, the requirements translate to a system that will store significant amounts of data; it will have more than 50 K queries per second, It should have the smallest latency possible, it will use LRU eviction policy, it needs 100% availability and be scalable.

The first thing to consider is the chache access pattern policy, as "Writes need to be in real time" the best choice here is to use  a write back pattern on which the data will be written directly on the cache, and the will be an assincronus  task that will synchronize the date with the database (DB). 
For the cache itself what is needed are two data structures a hash table to store data and a linked list to address the LRU policy. By updating the head and tail of the linked list, it is possible to remove the least used element and implement the LRU eviction, as head access is O(1) and hasta table access is also O(1). 

Also, the is a need for a service to handle put, get, delete data from the cache.  The service will be working as follows: there will be a queue that received al requests and stores them, that queue will interact with an event pool that is a thread that will be reading events and past it to a thread pool;  the loop also retrieves the answer asynchronously from that thread pool.  The thread pool will work as a balancer and send the request to the right ram location. 

There is also a need to handle craches from a server, from that it is possible to implement two variants the first is to take a temporal snapshot from the DB and restores from it, but it can lead to data loss. The second variant is to implement a request log system that could help to restore data on the DB from an asynchronous thread, in my opinion, that is the right chose here. 

It is vital to handle availability to get a 100% system availability. The best way to do that is to implement for each server a master-slave system, so the data is written simultaneously on both server, but only requests will be made to the master, is the master down the requests will be made to the slave.  

Making a resume the systems need a client that will send requests to the queue from the service itself, a Database to store and restore the cache,  and a cluster-distributed system that will add and disconnect nodes and the service thread pool will have to handle it. 

Due to the complex of the system, the dependence of the implementation of the thread pool about the underlying clustering and the fact that the requirements for the library are already cover in other great solutions, battle-tested in real-world problems for years. That's why I believe is not worth it to implement from scratch such a library, but instead, focus on using an existing one, showcasing how to fulfill the requirements. As a particular case, I'll focus on using [Memcached](https://memcached.org/) and the python client [pymemcache](https://github.com/pinterest/pymemcache), letting the implementations only to the situation in which and specifics clustering support is needed and not cover but the actual application or any of the elements listed before is required to be adjusted for any reason. 


## Integration

The integration process is really simple, just install `pymemcache` using `pip`

> pip install pymemcache


