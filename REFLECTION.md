# Part B: Reflection

### 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?
9 tests in `test_kitchen.py` (42 lines with imports and comments). Production code in `kitchen.py` is 40 lines covering `Quantity`, `Sum`, `Converter`, and the `grams`/`ounces` helpers.

So the ratio is about 1:1 in terms of lines. Roughly 1 test per 4-5 lines of production code, which makes sense because each test is targeting one specific behavior.

---

### 2. When was your bar red for the longest time, and what made it last so long?
Step A7, when I was adding mixed-unit conversion rates. I had to touch three classes at the same time — adding the rates dict to `Converter`, changing the `reduce` signature on both `Quantity` and `Sum` to accept a converter, and then getting `Sum.reduce` to actually convert both sides before adding them up. Kept hitting TypeErrors and AttributeErrors until I got all the pieces to line up.

---

### 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?
- **Fake It**: Step A1 — I just hardcoded `self.amount = 600` to make the test pass. Felt weird but it was useful because it confirmed that pytest could find and run the test file before I wrote any real logic.
- **Triangulate**: Step A2 — added a second test doing `times(2)` expecting 400, which broke the hardcoded 600 and forced me to write the actual formula `self.amount * multiplier`.
- **Obvious Implementation**: Step A8 — adding `times` to `Sum` was just `Sum(self.left.times(multiplier), self.right.times(multiplier))`. By that point the pattern was obvious from the earlier steps so I just wrote it directly.

All three felt like the right call for their situations.

---

### 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?
All the items from the handout are checked off. One thing I noticed is that `__hash__` should probably be added alongside `__eq__` if we ever want to put `Quantity` objects in sets or use them as dict keys.

**Next**: error handling when someone calls `converter.reduce` with a unit pair that hasn't been added — right now it just throws a raw `KeyError` which isn't very helpful.

**Delete**: stuff like division, subtraction, or supporting alternate unit names like 'gram' vs 'g'. No actual need for those right now.

---

### 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?
Probably not. My first instinct would have been to put all the conversion logic inside `Converter` and use `isinstance` checks to handle `Quantity` vs `Sum` differently.

The way it turned out — where `Quantity` and `Sum` each have their own `reduce` — came from the tests pushing me in that direction. It works better because `Converter` doesn't have to know about the different types of expressions.

---

### 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?
Part 0 felt more like verifying something that already existed. Since the code was already there, I was mostly just confirming it worked rather than thinking about what it *should* do. The shipping fee bug hunt (Step 0.8) showed the downside of that — the code looked fine until I actually tested the boundary cases at 0 kg, 1.0 kg, and 5.2 kg.

Part A was different because writing the test first made me decide the API before writing the implementation. Two tests that really shaped the design:
- `test_multiplication_returns_a_new_quantity` — this is what made me return a new object from `times()` instead of modifying the original.
- `test_simple_addition` — this is why I created the `Sum` class instead of trying to add amounts directly (which wouldn't work with mixed units).
