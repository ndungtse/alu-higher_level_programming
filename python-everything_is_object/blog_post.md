---
title: "Python: Mutable, Immutable... Everything is an Object!"
published: false
description: "A deep dive into how Python handles objects in memory — id, type, mutability, aliasing, integer caching, and how arguments are really passed to functions."
tags: python, programming, beginners, memory
cover_image: https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/assets/everything-is-object.png
---

> **Cover image tip:** dev.to shows the `cover_image` above the title. Replace the
> `cover_image` URL above with any image you like (e.g. a Python-memory diagram).
> If you don't have one, drop a picture into the article body with the dev.to
> image uploader so the post still has "at least one picture at the top."

## Introduction

In most programming languages you learn early on to separate *values* from
*variables*: a variable is a labelled box, and you drop a value inside it. Python
quietly breaks that mental model. In Python, **everything is an object** — integers,
strings, lists, functions, even classes themselves — and a variable is never the box.
It is a *name* that points at an object living somewhere in memory.

That single idea explains a surprising number of "wait, what?" moments: why changing
one list seems to change another, why `a is b` is sometimes `True` and sometimes
`False` for equal values, and why a function can modify your list but not your integer.
Let's unpack it.

## `id` and `type`

Every object in Python carries two things we can always ask about: **what it is** and
**where it is**.

- `type(obj)` tells you the object's type (its class).
- `id(obj)` returns a unique identifier for the object. In CPython (the reference
  implementation) this identifier is the object's memory address.

```python
>>> a = 89
>>> type(a)
<class 'int'>
>>> id(a)
140234981234567
>>> type("Best School")
<class 'str'>
>>> type([1, 2, 3])
<class 'list'>
```

Two names refer to the **same** object if and only if they share the same `id`. That
is exactly what the `is` operator checks, while `==` only checks whether the *values*
are equal:

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b      # same value?
True
>>> a is b      # same object?
False
>>> id(a) == id(b)
False
```

## Mutable objects

A **mutable** object can be changed *in place* after it is created — its `id` stays
the same while its contents change.

The mutable built-in types are:

- `list`
- `dict`
- `set`
- `bytearray`

```python
>>> my_list = [1, 2, 3]
>>> id(my_list)
140234981000000
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]
>>> id(my_list)
140234981000000   # SAME id — we mutated the very same object
```

## Immutable objects

An **immutable** object can never be changed after creation. Any operation that looks
like a change actually builds a *brand-new* object.

The immutable built-in types are:

- Numbers: `int`, `float`, `complex`
- `str` (string)
- `tuple`
- `frozenset`
- `bytes`

```python
>>> n = 10
>>> id(n)
140234980000100
>>> n += 5          # looks like a mutation...
>>> n
15
>>> id(n)
140234980000260   # ...but it's a DIFFERENT object
```

The name `n` was simply re-pointed at a new integer object `15`. The original `10`
was never touched.

### Assignment vs. referencing

This is the distinction that trips everyone up.

- **Referencing (aliasing):** `b = a` does *not* copy anything. It makes `b` a second
  name for the *same* object `a` points to.
- **Assignment to a name:** `a = something` re-binds the *name* `a` to a new object. It
  never changes the object `a` previously referred to.

```python
>>> a = [1, 2, 3]
>>> b = a          # b is an ALIAS of a — same object
>>> b is a
True
>>> a = a + [4]    # re-binds the NAME a to a new list
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3]          # b still points at the original object
>>> a is b
False
```

### How an immutable object is stored in memory

Because immutable objects can never change, CPython is free to **reuse** them. When
you write the literal `89` in two places, the interpreter can safely hand back the
*same* object both times — there is no risk that someone mutates it and surprises
everyone else. This is why identity results can look strange for immutables.

## Memory schemas (the pictures)

### Schema 1 — aliasing a mutable object

```
a = [1, 2, 3]
b = a
b.append(4)

   Names            Objects in memory
   -----            -----------------
   a ---------\
               >---> [ 1, 2, 3, 4 ]   (id: 0x1000)
   b ---------/

Both names point to ONE list. Mutating through b is visible through a.
print(a)  ->  [1, 2, 3, 4]
```

### Schema 2 — rebinding vs. mutating

```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]        # rebinding: builds a NEW list

   Names            Objects in memory
   -----            -----------------
   l2 --------> [ 1, 2, 3 ]        (id: 0x2000)
   l1 --------> [ 1, 2, 3, 4 ]     (id: 0x2500)  <- new object

print(l2)  ->  [1, 2, 3]     (unchanged)


Compare with in-place mutation:
l1 = [1, 2, 3]
l2 = l1
l1 += [4]            # in-place extend: SAME object

   l1 -------\
              >---> [ 1, 2, 3, 4 ]   (id: 0x2000, unchanged id)
   l2 -------/

print(l2)  ->  [1, 2, 3, 4]
```

That `+` vs `+=` difference is real and worth internalizing:

```python
>>> a = [1, 2, 3, 4]
>>> before = id(a)
>>> a = a + [5]        # new object
>>> id(a) == before
False
>>> a = [1, 2, 3]
>>> before = id(a)
>>> a += [4]           # in-place, same object
>>> id(a) == before
True
```

## Why it matters: how Python treats mutable and immutable objects differently

- **Immutable objects are safe to share.** Since nobody can change them, CPython
  reuses and caches them freely. Equality and identity often coincide for small,
  common immutables.
- **Mutable objects are dangerous to share accidentally.** Two names pointing at the
  same list means a change through one name is seen through the other. This is a
  feature when you want it and a bug when you don't — which is why you copy lists
  (`new = old[:]` or `list(old)`) when you need independence.

## How arguments are passed to functions

Python passes arguments by **assignment** (often called "pass by object reference").
The parameter name inside the function becomes a new name bound to the *same* object
the caller passed in. What happens next depends entirely on whether that object is
mutable and on what you do with it.

**Immutable argument — the caller is unaffected:**

```python
def increment(n):
    n += 1          # rebinds the LOCAL name to a new int
                    # the caller's object is untouched

a = 1
increment(a)
print(a)            # 1
```

**Mutable argument, mutated in place — the caller sees the change:**

```python
def increment(n):
    n.append(4)     # mutates the SAME list object

l = [1, 2, 3]
increment(l)
print(l)            # [1, 2, 3, 4]
```

**Mutable argument, but rebinding inside — the caller is unaffected:**

```python
def assign_value(n, v):
    n = v           # rebinds the LOCAL name only

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)           # [1, 2, 3]   (unchanged — we only moved a local name)
```

The rule of thumb: **mutating** an object (calling a method like `.append`, or index
assignment) affects everyone who shares it; **rebinding a name** (`n = ...`) affects
only that name.

## Integer pre-allocation and the small-integer cache

Here is where identity gets genuinely surprising:

```python
>>> a = 89
>>> b = 89
>>> a is b
True                # same object!

>>> a = 1000
>>> b = 1000
>>> a is b
False               # different objects
```

When CPython starts up, it **pre-allocates** a pool of small integer objects and keeps
them around for the entire lifetime of the program. Any time you use one of these
values, you get the *same* cached object instead of a freshly created one. That's why
`89 is 89` is `True` but `1000 is 1000` is not.

### NSMALLPOSINTS and NSMALLNEGINTS

The size of that cache is defined in CPython's source (`Objects/longobject.c`) by two
constants:

- `NSMALLPOSINTS = 257` → the positive integers `0` through `256`
- `NSMALLNEGINTS = 5` → the negative integers `-5` through `-1`

Together they cache the integers in the range **-5 to 256**, which is
`5 + 257 = 262` pre-allocated integer objects.

```python
>>> a = 256
>>> b = 256
>>> a is b
True                # 256 is cached

>>> a = 257
>>> b = 257
>>> a is b
False               # 257 is outside the cache
```

### Why those particular values?

The range `-5` to `256` was chosen because these are the **most frequently used**
integers in real programs: loop counters, small indices, byte values (`0`–`255`),
flags, and the like. Caching them avoids constantly allocating and freeing the same
tiny objects, which is a real performance and memory win. Values outside that range
are rare enough that caching them wouldn't pay off.

> ⚠️ **Never rely on this in your code.** The small-integer cache is an implementation
> detail of CPython. Use `==` to compare values and reserve `is` for identity checks
> like `x is None`.

## The special case of tuples and frozensets

Tuples and frozensets are **immutable containers** — you cannot add, remove, or replace
their elements. But there's a subtle catch: *immutability of the container does not
make its contents immutable.* A tuple can hold a mutable object, and that object can
still change:

```python
>>> t = (1, 2, [3, 4])
>>> t[2].append(5)
>>> t
(1, 2, [3, 4, 5])       # the tuple's list element changed!
>>> t[2] = [9]          # but you can't rebind a slot
Traceback (most recent call last):
  ...
TypeError: 'tuple' object does not support item assignment
```

So the tuple itself never changed *which* objects it references — that binding is
frozen — but a mutable object it references can still be mutated internally. This is
also why a tuple containing a list is **not hashable** (and therefore can't be a dict
key or set member), while a tuple of only immutables is.

Also note the empty-tuple singleton and single-element quirks:

```python
>>> a = ()
>>> b = ()
>>> a is b
True                # CPython uses a single shared empty tuple

>>> a = (1)         # NOT a tuple — just the int 1 in parentheses
>>> type(a)
<class 'int'>
>>> a = (1,)        # the trailing comma makes it a tuple
>>> type(a)
<class 'tuple'>
```

## Conclusion

Once you internalize that **variables are names, not boxes**, and that every value is
an object with an identity (`id`), a type (`type`), and a mutability, Python's behavior
stops being mysterious:

- Assignment binds a name; it never copies an object.
- Aliasing lets two names share one object — harmless for immutables, powerful (and
  occasionally dangerous) for mutables.
- Functions receive references by assignment, so mutation leaks out but rebinding
  doesn't.
- CPython caches small integers (-5 to 256) and the empty tuple for performance.
- Immutable containers freeze their bindings, not necessarily their contents.

Keep `==` for values, `is` for identity, and you'll write code that behaves exactly
the way you expect.

---

*Thanks for reading! If this helped clarify Python's object model, drop a ❤️ and a
comment — and connect with me on LinkedIn.*
