# Circular Relationship

Great — this version introduces **many-to-many relationships** (`Product` ↔ `Promotion`) and also a **self-reference risk** (Collection featuring a Product). Your question about _circular relationships_ is spot-on here, because Django prevents issues that could arise if models refer to each other in a circular way.

---

## **1. What is a Circular Relationship?**

A **circular relationship** happens when:

- **Model A depends on Model B**, and
- **Model B also depends on Model A**,
  directly or indirectly.

In database terms, this means that:

- To create a record in table A, you first need a record in table B,
- but to create a record in table B, you also need a record in table A.

### **Example of circular reference**

```python
class A(models.Model):
    b = models.ForeignKey('B', on_delete=models.CASCADE)

class B(models.Model):
    a = models.ForeignKey(A, on_delete=models.CASCADE)
```

This creates a loop:

- A references B, and
- B references A.

When Django tries to create tables, it has to figure out which comes first — but **both need the other one first**.

---

## **2. Why does this matter in your code?**

Look at:

```python
class Collection(models.Model):
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name="+")
```

- **Collection → Product** through `featured_product`
- **Product → Collection** through `product = models.ForeignKey(Collection, ...)`

This is _not a strict circular relationship at the database level_, because:

- `featured_product` can be `null` (so Collection can be created without a Product yet).
- `on_delete=models.SET_NULL` breaks the hard dependency — if the Product is deleted, Collection just clears its reference.

**If you didn’t allow null:**

- You couldn’t create a Collection without first creating a Product,
- but you can’t create a Product without first assigning a Collection.
- Boom: circular dependency → neither table can be populated initially.

---

## **3. What happens if you ignore it?**

- At **migration time**: Django can still build tables, because the foreign keys are just integer columns with constraints — but you may get warnings if both sides are non-nullable and required.
- At **runtime**: you may have logic errors where you literally can't insert initial data (e.g., you must insert a Product but need a Collection first, which itself requires a Product).

---

## **4. How do we solve circular relationships?**

### **(A) Use `null=True` or `blank=True` on one side**

- Makes the field optional so you can create one model without immediately providing the other.

```python
featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
```

### **(B) Use a string reference `'ModelName'` instead of importing directly**

- This is exactly what Mosh did:

```python
featured_product = models.ForeignKey('Product', ...)
```

- Django resolves the model by name after all models are loaded — preventing circular **import errors**.

### **(C) Use `related_name="+"` to prevent reverse accessor**

- In your code:

```python
related_name="+"
```

- This tells Django **not to create a reverse relation** (so `Product` won’t try to add a confusing `.collection_set` or `.featured_product_set`).
- This avoids name clashes and complexity.

### **(D) Break dependency at DB level using `SET_NULL` or `SET_DEFAULT`**

- Using `on_delete=SET_NULL` lets you delete a Product even if a Collection points to it.
- If you used `CASCADE`, deleting the product could wipe out the collection — dangerous.

### **(E) Reconsider design**

- Sometimes circular relationships are a **smell** — maybe "featured product" should live outside the main Collection table in a separate model.

---

## **5. What if you do nothing at all?**

- If fields are **required (null=False)** → You won’t be able to create records easily.
- If you use **direct imports in both models** → you could hit **circular import errors** in Python (not just database problems).
- If you allow both fields optional → You’ll avoid crashes, but logically your app could end up with incomplete data (e.g., a Collection without a featured product).

---

## **6. Summary: Why Mosh used this approach**

- `'Product'` as a string reference avoids Python circular import errors.
- `null=True` breaks the hard circular dependency — you can insert collections before products.
- `related_name='+'` prevents reverse relation noise (no `.collection_set` created).
- `on_delete=SET_NULL` ensures deleting a product won’t destroy the collection.

---

## **Quick Visual of Your Relationships**

```
Promotion  <----->  Product  ---->  Collection
   ^                       \
   |                        ----> CartItem
   |                        ----> OrderItem
   |
Customer ----> Order ----> OrderItem
      \
       ----> Address (1-to-1)
```

- **Many-to-many**: Product ↔ Promotion
- **One-to-many**: Collection → Product, Order → OrderItem, Cart → CartItem
- **One-to-one**: Customer → Address

---

Do you want me to **(1) draw a full ERD diagram (tables + keys)** and **(2) give example Django queries showing forward and reverse lookups for all three relationships (One-to-One, One-to-Many, Many-to-Many)**?
This will make the whole schema crystal clear.
