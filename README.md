# AlgosPA2

Kalim Qazi (85459364) 
Anvit Dhamnekar (15965003)


To run this project you simply have to call the example.in, file1.in, file2.in, file3.in file with the main.py file with this following command in the terminal: 

python3 src/main.py test/example.in test/example.out 

You have to make sure that you update the input file and the name for the output file to have the correct test ran.


Solutions to the Written component: 
1) 
<img width="1218" height="294" alt="image" src="https://github.com/user-attachments/assets/35576f4a-8d7a-4b68-8bea-baf05a649f1f" />

Yes, OPTFF achieves the fewest misses in every test. This is expected as OPTFF is provably optimal so no algorithm, online or offline, can incur fewer cache misses on a fixed sequence.

LRU is never worse than FIFO in these three tests. In File1 they are equal, while in File2 and File3 LRU has fewer misses than FIFO. This shows that LRU usually makes better eviction choices because it keeps recently used items in the cache.


2 ) For a cache size of (k = 3), the sequence ((1, 2, 3, 4, 1)) shows that OPTFF can have fewer misses than FIFO and LRU. FIFO has 5 misses, LRU has 5 misses, and OPTFF has 4 misses. After the cache fills with (1, 2, 3), the request for 4 forces an eviction. FIFO evicts 1 because it was inserted first, and LRU also evicts 1 because it was used least recently. The next request is 1, so both FIFO and LRU miss again. OPTFF looks ahead, sees that 1 will be used again soon, and evicts 2 or 3 instead, since neither is used again. Therefore OPTFF has fewer misses.

3) Consider any offline algorithm A that knows the full request sequence. We show that OPTFF has no more misses than A. Look at the first step where A and OPTFF make different eviction choices. Suppose OPTFF evicts page f, and A evicts page a. Since OPTFF chooses the page whose next use is farthest in the future, page f is needed no earlier than page a. Now change A so that it evicts f instead of a. This change does not increase the number of misses, because a will be needed before f, or f may never be needed again. Repeating this argument at every step transforms A into OPTFF without increasing misses. Therefore OPTFF has at most as many misses as any offline algorithm, so OPTFF is optimal.



