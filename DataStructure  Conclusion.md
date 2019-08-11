# 对常见数据结构的个人总结：

## Array/List :
1. 线性结构，内存地址连续
2. 可以通过下标访问或者修改元素，均为O(1)     
3. 缺点：插入或者删除元素开销大，为O(n)  

## Linked_List:
1. 非线性结构，内存地址不连续
2. 插入操作比较方便 为O(1)
3. 访问、修改、删除值操作开销大，为O(n)
4. 翻转LL操作思路：法(1)三个指针，将每个节点的node.next指向原来的上一个节点
                 法(2)利用Stack，FILO的模式进行翻转

## DoubleCircalLinkedList:
1. 同LL相比更灵活，双端均可插入、遍历
2. 删除node操作为O(1)

## Queue(LL/Array achieve):
1. 因为队列主要操作为pop和push，对LL来说均为O(1)复杂度，开销小易于实现
2. Array实现时用python取模的方法确定元素下标

## Deque:
1. 双链表实现，可pop  popleft  append  appendleft操作

## HashTable:
1. 冲突因子， Hash函数， rehash操作
2. add， get， remove等操作均为O(1)
3. python内部dict实现采用HashTable，为键值对结构

## Stack
1. 采用deque实现，Stack为FILO模式
2. 根据1，定义stack对于deque的操作映射为：pop->pop, push->append

## Recursion
1. 递归要注意递归出口
2. 尾递归可以节约开销
3. Hannota问题，利用中介进行递归

## Sort
1. bubble
2. select
3. insertion
>1,2,3均为O(n^2)
4. 分治 -- merge sort 
>O(nlgn)

                            