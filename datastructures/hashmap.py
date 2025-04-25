from __future__ import annotations
from typing import Callable, Iterator, Optional, Tuple, Hashable
from datastructures.ihashmap import KT, VT, IHashMap
import pickle
import hashlib

from datastructures.linkedlist import LinkedList
from datastructures.array import Array

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self.__capacity:int = number_of_buckets
        self.__buckets:Array[LinkedList[tuple[KT, VT]]] = Array([LinkedList(data_type=tuple) for _ in range(self.__capacity)], data_type=LinkedList)
        self.__load_factor:float = load_factor
        self.__hash = HashMap._default_hash_function if not custom_hash_function else custom_hash_function
        self.__length = 0

    def __getitem__(self, key: KT) -> VT:
        for tup in self.__buckets[self.__hash(key) % self.__capacity]:
            if tup[0] == key:
                return tup[1]
        raise KeyError("Key not found")

    def __setitem__(self, key: KT, value: VT) -> None:
        if not isinstance(key, Hashable):
           raise TypeError("Key must be hashable")
        else:
            if self.__length > self.__capacity * self.__load_factor:
                self.__resize()
            bucket = self.__buckets[self.__hash(key) % self.__capacity]
            for item in bucket:
                if item[0] == key:
                    bucket.remove(item)
                    bucket.append((key, value))
                    return
            bucket.append((key, value))
            self.__length += 1

    def keys(self) -> Iterator[KT]:
        return iter(self)
    
    def values(self) -> Iterator[VT]:
        return iter([j[1] for i in self.__buckets for j in i])

    def items(self) -> Iterator[Tuple[KT, VT]]:
        return iter([j for i in self.__buckets for j in i])
            
    def __delitem__(self, key: KT) -> None:
        bucket = self.__buckets[self.__hash(key) % self.__capacity]
        for tup in bucket:
            if tup[0] == key:
                bucket.remove(tup)
                self.__length -= 1
                return
        raise KeyError("Key not present")
    
    def __contains__(self, key: KT) -> bool:
        for tup in self.__buckets[self.__hash(key) % self.__capacity]:
            if tup[0] == key:
                return True
        return False
    
    def __len__(self) -> int:
        return self.__length
    
    def __iter__(self) -> Iterator[KT]:
        return iter([j[0] for i in self.__buckets for j in i])
    
    def __eq__(self, other: HashMap) -> bool:
        if len(self) != len(other):
            return False
        else:
            for i in self:
                if i not in other:
                    return False
            return True

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self.items()) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    def __resize(self) ->None:
        def isprime(n):
            d = 3
            while d * d <= n:
                if n % d == 0:
                    return False
                d = d + 2
            return True
        new_size = self.__capacity * 2
        while not isprime(new_size):
            new_size += 1
        new_buckets = Array([LinkedList() for _ in range(new_size)])
        for k,v in self.items():
            new_buckets[self.__hash(k) % new_size].append((k,v))
        self.__capacity = new_size
        self.__buckets = new_buckets

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)